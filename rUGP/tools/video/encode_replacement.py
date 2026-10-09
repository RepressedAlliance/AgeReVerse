"""Build scoped CRsi replacements from source and edited lossless RGB videos.

Run as ``python -m rUGP.tools.video.encode_replacement --help``. A complete
native replay against ``target_rgb_sha256`` is required before installation;
successful construction alone establishes neither decoding nor visual quality.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import time

import cv2
import numpy as np

from rUGP.formats.video.crsi import parse, rebuild
from .compact_encoder import encode_rgb


def build(original: Path, source_video: Path, edited_video: Path,
          output: Path, report_path: Path) -> dict:
    for path in (output, report_path):
        if path.exists():
            raise FileExistsError(path)
    if output.resolve() == report_path.resolve():
        raise ValueError('resource and report need distinct output paths')
    data = original.read_bytes()
    sequence = parse(data)
    source = cv2.VideoCapture(str(source_video))
    edited = cv2.VideoCapture(str(edited_video))
    started = time.perf_counter()
    replacements = {}
    changed, closure, hashes = [], [], []
    dirty = False
    counts = dict(above_pixels=0, repeat_pixels=0, literal_pixels=0)
    try:
        for capture in (source, edited):
            if not capture.isOpened():
                raise ValueError('cannot open input video')
            if abs(capture.get(cv2.CAP_PROP_FPS) - sequence.rate / 100) > 0.001:
                raise ValueError('input video frame rate differs from CRsi')
        for index, frame in enumerate(sequence.frames):
            ok_a, a = source.read()
            ok_b, b = edited.read()
            shape = (sequence.height, sequence.width, 3)
            if not ok_a or not ok_b or a.shape != shape or b.shape != shape:
                raise ValueError(f'missing or wrong-size input frame {index}')
            rgb = cv2.cvtColor(b, cv2.COLOR_BGR2RGB).tobytes()
            hashes.append(hashlib.sha256(rgb).hexdigest())
            different = not np.array_equal(a, b)
            if frame.independent:
                dirty = False
            if different or dirty:
                replacement, statistics = encode_rgb(rgb, sequence.width, sequence.height)
                replacements[index] = replacement
                for key, value in statistics.items():
                    counts[key] += value
                (changed if different else closure).append(index)
                dirty = True
            if (index + 1) % 300 == 0:
                print(f'Encoded {index + 1}/{len(sequence.frames)} frames', flush=True)
        if source.read()[0] or edited.read()[0]:
            raise ValueError('input video has extra frames')
    finally:
        source.release()
        edited.release()
    result = rebuild(sequence, replacements)
    report = dict(
        schema='photon-crsi-replacement/1',
        status='encoded candidate; native replay and visual acceptance pending',
        original_sha256=hashlib.sha256(data).hexdigest(),
        output_sha256=hashlib.sha256(result).hexdigest(),
        original_bytes=len(data), output_bytes=len(result),
        width=sequence.width, height=sequence.height, rate=sequence.rate,
        frame_count=len(sequence.frames),
        changed_frames=changed, dependency_closure_frames=closure,
        replaced_frames=len(replacements),
        retained_original_frames=len(sequence.frames)-len(replacements),
        replacement_mode='0x03ff', statistics=counts,
        target_rgb_sha256=hashes, seconds=time.perf_counter()-started,
        limitation='Videos are decoded by frame index; audio and in-game streaming are not exercised.')
    with output.open('xb') as stream:
        stream.write(result)
    with report_path.open('x', encoding='utf-8') as stream:
        json.dump(report, stream, indent=2)
        stream.write('\n')
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('original', 'source_video', 'edited_video', 'output', 'report'):
        parser.add_argument(name, type=Path)
    args = parser.parse_args()
    report = build(args.original, args.source_video, args.edited_video, args.output, args.report)
    print(json.dumps({key: report[key] for key in
                      ('frame_count', 'replaced_frames', 'retained_original_frames', 'output_bytes', 'seconds')}))


if __name__ == '__main__':
    main()
