"""Scoped Rebirth caption composition from both original language videos.

Preserves original English artwork. Only narration glyph masks and new Chinese
layers are changed. Background recovery is an approximate temporal blend, so
motion/edge review is still required. Inputs are decoded lossless 1024x600 video.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path
import subprocess

import cv2
import numpy as np

from .style_layers import render_layer


def caption_mask(witness):
    crop = witness[505:589]
    small = cv2.resize(crop, (512, 42), interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)
    near_dark = cv2.dilate((gray < 90).astype(np.uint8), np.ones((5, 5), np.uint8)).astype(bool)
    template = (small.min(axis=2) > 170) & ((small.max(axis=2)-small.min(axis=2)) < 24) & near_dark
    core = cv2.resize(template.astype(np.uint8), (1024, 84), interpolation=cv2.INTER_NEAREST)*255
    core = cv2.dilate(core, np.ones((13, 13), np.uint8))
    # Native-size components retain thin strokes and isolated punctuation that
    # the half-size template can lose. No minimum component area is imposed.
    gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    near_dark = cv2.dilate((gray < 90).astype(np.uint8), np.ones((7, 7), np.uint8)).astype(bool)
    fine = ((crop.min(axis=2) > 160) & ((crop.max(axis=2)-crop.min(axis=2)) < 35) & near_dark).astype(np.uint8)
    count, labels, stats, _ = cv2.connectedComponentsWithStats(fine)
    glyphs = np.zeros_like(fine)
    for index in range(1, count):
        if stats[index, cv2.CC_STAT_WIDTH] <= 30 and stats[index, cv2.CC_STAT_HEIGHT] <= 32:
            glyphs[labels == index] = 255
    core = np.maximum(core, cv2.dilate(glyphs, np.ones((9, 9), np.uint8)))
    soft = cv2.GaussianBlur(cv2.dilate(core, np.ones((7, 7), np.uint8)), (7, 7), 1.2)
    return np.maximum(soft, core).astype(np.float32)/255


def feature(frame):
    return cv2.resize(frame[:505], (128, 64), interpolation=cv2.INTER_AREA).astype(np.float32)


def open_video(path):
    capture = cv2.VideoCapture(str(path))
    if not capture.isOpened():
        capture.release()
        raise ValueError(f'cannot open {path}')
    if (capture.get(cv2.CAP_PROP_FRAME_WIDTH), capture.get(cv2.CAP_PROP_FRAME_HEIGHT)) != (1024, 600) or abs(capture.get(cv2.CAP_PROP_FPS)-30) > .001:
        capture.release()
        raise ValueError('this compositor requires 1024x600 at nominal 30fps')
    return capture


def compose(source_video: Path, background_video: Path, timeline_path: Path,
            text_path: Path, profile_path: Path, font: Path, output: Path,
            report_path: Path, ffmpeg: str = 'ffmpeg') -> dict:
    for path in (output, report_path):
        if path.exists():
            raise FileExistsError(path)
    if output.resolve() == report_path.resolve():
        raise ValueError('video and report need distinct output paths')
    timeline = json.loads(timeline_path.read_text(encoding='utf-8'))
    profile = json.loads(profile_path.read_text(encoding='utf-8'))
    if (timeline.get('schema'), timeline.get('source_global_offset'), timeline.get('frame_count')) != ('photon-crsi-caption-frames/1', 27493704, 1905):
        raise ValueError('unsupported source timeline')
    cues = timeline['captions']
    if len(cues) != 22 or len({cue['id'] for cue in cues}) != 22:
        raise ValueError('expected 22 unique ending captions')
    previous_end = 0
    for cue in cues:
        start, end = cue['start_frame'], cue['end_frame']
        if not previous_end <= start <= cue['witness_frame'] < end <= 1905:
            raise ValueError('overlapping or out-of-range caption')
        previous_end = end
    with text_path.open(encoding='utf-8-sig', newline='') as stream:
        rows = [row for row in csv.DictReader(stream)
                if row['layer'] == 'subtitle' and row['variant'] in ('long', 'both')]
    text = {row['id']: row['target_text'] for row in rows}
    if len(text) != len(rows) or set(text) != {cue['id'] for cue in cues}:
        raise ValueError('caption text IDs do not match timeline')
    from fontTools.ttLib import TTFont
    with TTFont(font) as face:
        cmap = face.getBestCmap()
        missing = {char for line in text.values() for char in line if ord(char) not in cmap}
    if missing:
        raise ValueError(f'font lacks caption characters: {sorted(missing)}')
    layers, masks, metrics = {}, [], []
    capture = open_video(source_video)
    try:
        for cue in cues:
            layer, position, measure = render_layer(text[cue['id']], profile['roles']['narration'], profile, font)
            layers[cue['id']] = (np.asarray(layer), position)
            metrics.append(dict(id=cue['id'], **measure))
            capture.set(cv2.CAP_PROP_POS_FRAMES, cue['witness_frame'])
            ok, witness = capture.read()
            if not ok:
                raise ValueError('missing caption witness')
            masks.append(caption_mask(witness))
    finally:
        capture.release()
    features, bands = [], []
    capture = open_video(background_video)
    try:
        while True:
            ok, frame = capture.read()
            if not ok:
                break
            features.append(feature(frame))
            bands.append(frame[505:589].copy())
    finally:
        capture.release()
    if len(bands) != 1904:
        raise ValueError('expected 1904 background reference frames')
    features, bands = np.stack(features), np.stack(bands)
    capture = open_video(source_video)
    try:
        encoder = subprocess.Popen([ffmpeg, '-hide_banner', '-loglevel', 'error', '-n',
            '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', '1024x600', '-r', '30',
            '-i', 'pipe:0', '-an', '-c:v', 'ffv1', '-level', '3', '-pix_fmt', 'bgr0', str(output)], stdin=subprocess.PIPE)
    except BaseException:
        capture.release()
        raise
    records, hashes = [], []
    number = changed = outside = 0
    try:
        while True:
            ok, source = capture.read()
            if not ok:
                break
            frame = source.copy()
            active = [i for i, cue in enumerate(cues) if cue['start_frame']-2 <= number < cue['end_frame']+3]
            allowed = np.zeros((600, 1024), dtype=bool)
            if active:
                target, best = feature(source), None
                for j in range(max(0, number-4), min(len(bands)-1, number+2)):
                    a, delta = features[j], features[j+1]-features[j]
                    alpha = float(np.clip(np.sum((target-a)*delta)/max(float(np.sum(delta*delta)), 1), 0, 1))
                    error = float(np.mean(np.abs(target-(a+alpha*delta))))
                    if best is None or error < best[0]:
                        best = (error, j, alpha)
                error, j, alpha = best
                background = bands[j].astype(np.float32)*(1-alpha)+bands[j+1].astype(np.float32)*alpha
                mask = np.maximum.reduce([masks[i] for i in active])
                frame[505:589] = np.rint(source[505:589]*(1-mask[:, :, None])+background*mask[:, :, None]).astype(np.uint8)
                allowed[505:589] = mask > 0
                records.append(dict(frame=number, japanese_pair=[j, j+1], blend=alpha, top_feature_mae=error))
            for cue in cues:
                if cue['start_frame'] <= number < cue['end_frame']:
                    layer, (x, y) = layers[cue['id']]
                    h, w = layer.shape[:2]
                    alpha = layer[:, :, 3:4].astype(np.float32)/255
                    frame[y:y+h, x:x+w] = np.rint(frame[y:y+h, x:x+w]*(1-alpha)+layer[:, :, :3][:, :, ::-1]*alpha).astype(np.uint8)
                    allowed[y:y+h, x:x+w] |= layer[:, :, 3] > 0
            diff = np.any(frame != source, axis=2)
            outside += int(np.count_nonzero(diff & ~allowed))
            changed += bool(np.any(diff))
            hashes.append(hashlib.sha256(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB).tobytes()).hexdigest())
            encoder.stdin.write(frame.tobytes())
            number += 1
            if number % 300 == 0:
                print(f'Composed {number}/1905 frames', flush=True)
    finally:
        capture.release()
        try:
            encoder.stdin.close()
        finally:
            result = encoder.wait()
    if result or number != 1905 or outside:
        raise ValueError(f'composition failed: ffmpeg={result}, frames={number}, outside-mask pixels={outside}')
    report = dict(status='caption composition candidate; language and motion acceptance pending',
        frame_count=number, changed_frames=changed, outside_allowed_changed_pixels=outside,
        typography=metrics, frame_alignment=records, target_rgb_sha256=hashes,
        source_global_offset=27493704, background_global_offset=1715679260,
        input_sha256={label: hashlib.sha256(path.read_bytes()).hexdigest() for label, path in
                      [('timeline', timeline_path), ('text', text_path), ('profile', profile_path)]},
        limitation='Adjacent Japanese frames approximate the caption background; no game playback verified')
    with report_path.open('x', encoding='utf-8') as stream:
        json.dump(report, stream, indent=2)
        stream.write('\n')
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('source_video', 'background_video', 'timeline', 'text', 'profile', 'font', 'output', 'report'):
        parser.add_argument(name, type=Path)
    parser.add_argument('--ffmpeg', default='ffmpeg')
    args = parser.parse_args()
    report = compose(args.source_video, args.background_video, args.timeline,
                     args.text, args.profile, args.font, args.output, args.report, args.ffmpeg)
    print(json.dumps({key: report[key] for key in ('frame_count', 'changed_frames', 'outside_allowed_changed_pixels')}))


if __name__ == '__main__':
    main()
