"""Scoped, reproducible PM recap and PF countdown lettering.

Only prepares pixels; CRsi coding is provided by the existing C codec.
The countdown cleanplate estimates the smooth panel lighting, not the hidden original pixels.
"""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def glyph(text, size, weight, canvas, xy, font_path):
    """Render variable-font lettering at fourfold sampling, then downsample."""
    s = 4
    im = Image.new('L', (canvas[0] * s, canvas[1] * s))
    f = ImageFont.truetype(str(font_path), round(size * s))
    f.set_variation_by_axes([weight])
    b = f.getbbox(text)
    ImageDraw.Draw(im).text((xy[0] * s - b[0], xy[1] * s - b[1]), text, font=f, fill=255)
    return np.asarray(im.resize(canvas, Image.Resampling.LANCZOS)).astype('float32') / 255

def surface(a, valid, sample, region):
    """Fit smooth panel lighting using known, visible background samples."""
    y, x = np.indices(a.shape[:2])
    xx = x / 1200
    yy = y / 600
    X = np.stack([np.ones_like(xx), xx, yy, xx * yy, xx ** 2, yy ** 2], axis=-1)
    pick = valid & sample & region
    co = np.linalg.lstsq(X[pick][::3], a[pick][::3], rcond=None)[0]
    return np.clip(X @ co, 0, 255).astype('float32')

def counter(a, font_path):
    """Reletter a padded, rectified panel; retain the original numeric band.

    Padding includes clipped source lettering left of the plane origin. Continuous
    header feathering avoids old glyph-shaped glow. Fit from visible pixels, but
    extrapolate the cleanplate across canvas edges so inverse sampling has no gaps.
    """
    h, w = a.shape[:2]
    size = (1856, 1056)
    H = cv2.getPerspectiveTransform(np.float32([[77, -33], [995, 45], [800, 831], [36, 259]]), np.float32([[128, 128], [1328, 128], [1328, 448], [128, 448]]))
    inv = np.linalg.inv(H)
    rect = cv2.warpPerspective(a, H, size).astype('float32')
    valid = cv2.warpPerspective(np.ones((h, w), np.uint8), H, size) > 0
    y, x = np.indices(rect.shape[:2])
    y = y - 128
    x = x - 128
    top = (y < 104) & (x < 720) & (x > 8)
    bottom = (y > 372) & (y < 601) & (x < 1200)
    clean = rect.copy()
    bg = surface(rect, valid, rect[:, :, 0] < 45, (y < 112) & (x < 900))
    header_bottom = np.where(x > 605, 92, 104)
    oldtop = top * np.clip((x - 8) / 15, 0, 1) * np.clip((720 - x) / 35, 0, 1) * np.clip((header_bottom - y) / 4, 0, 1)
    clean[oldtop > 0] = bg[oldtop > 0]
    red = surface(rect, valid, rect[:, :, 0] > 235, bottom)
    clean[bottom] = red[bottom]
    topmask = glyph('主机临界剩余时间', 80, 900, size, (168, 138), font_path)
    topmask *= top
    bottommask = glyph('乘员撤离', 190, 900, size, (136, 516), font_path)
    bottommask *= bottom
    mask = np.maximum(oldtop, ((topmask > 0) | bottom).astype('float32'))
    originalclean = cv2.warpPerspective(clean, inv, (w, h))
    scope = cv2.warpPerspective(mask, inv, (w, h))
    alpha1 = cv2.warpPerspective(topmask, inv, (w, h))
    alpha2 = cv2.warpPerspective(bottommask, inv, (w, h))
    scope = np.clip(scope, 0, 1)
    out = a.astype('float32') * (1 - scope[:, :, None]) + originalclean * scope[:, :, None]
    cleanview = out.copy()
    bloom = cv2.GaussianBlur(alpha1, (0, 0), 1.5)
    out = np.clip(out + bloom[:, :, None] * np.array([110, 0, 18]), 0, 255)
    out = out * (1 - alpha1[:, :, None]) + np.array([255, 3, 57]) * alpha1[:, :, None]
    dark = surface(rect, valid, rect[:, :, 0] < 125, bottom)
    dark = cv2.warpPerspective(dark, inv, (w, h))
    out = out * (1 - alpha2[:, :, None]) + dark * alpha2[:, :, None]
    protected = cv2.warpPerspective((((y >= 105) | (y >= 92) & (x > 605)) & (y <= 325)).astype('uint8'), inv, (w, h), flags=cv2.INTER_NEAREST) > 0
    out[protected] = a[protected]
    cleanview[protected] = a[protected]
    return (np.clip(np.round(out), 0, 255).astype('uint8'), np.clip(np.round(cleanview), 0, 255).astype('uint8'), H, scope)

def recap(a, index, reference, font_path):
    """Follow source title position, scale and brightness; retain the 2.4 lead-in."""
    if index < 251:
        return a.copy()
    q = a[260:365, 80:945].max(axis=2)
    peak = q.max()
    if peak < 12:
        return a.copy()

    def box(im):
        yy, xx = np.where(im > max(12, float(im.max()) * 0.72))
        return (xx.min(), yy.min(), xx.max(), yy.max())
    x0, y0, x1, y1 = box(q)
    r0, s0, r1, s1 = box(reference[260:365, 80:945].max(axis=2))
    sx = (x1 - x0 + 1) / (r1 - r0 + 1)
    sy = (y1 - y0 + 1) / (s1 - s0 + 1)
    text = '《时空的欠片》前情回顾'
    f = ImageFont.truetype(str(font_path), 120)
    f.set_variation_by_axes([600])
    im = Image.new('L', (1800, 360))
    d = ImageDraw.Draw(im)
    x = 40
    for ch in text:
        b = f.getbbox(ch)
        d.text((x, 80 - b[1]), ch, font=f, fill=255)
        x += f.getlength(ch) + 10
    bb = im.getbbox()
    im = im.crop((bb[0] - 24, bb[1] - 24, bb[2] + 24, bb[3] + 24))
    im = im.resize((max(1, round(im.width / 4 * sx)), max(1, round(im.height / 4 * sy))), Image.Resampling.LANCZOS)
    mask = np.zeros(a.shape[:2], np.float32)
    mx = round((x0 + x1) / 2 + 80 - im.width / 2)
    my = round((y0 + y1) / 2 + 260 - im.height / 2)
    mask[my:my + im.height, mx:mx + im.width] = np.asarray(im) / 255
    out = a.astype('float32')
    out[260:365, 80:945] = 0
    ly, lx = np.where(q > max(2, float(peak) * 0.16))
    rq = reference[260:365, 80:945].max(axis=2)
    ry, rx = np.where(rq > float(rq.max()) * 0.16)
    halo = max(0.35, (ly.max() - ly.min() - (y1 - y0)) / max(1, ry.max() - ry.min() - (s1 - s0)))
    echo_ratio = (lx.max() - lx.min() + 1) / (x1 - x0 + 1)
    luminous = mask.copy()
    if index >= 265 and echo_ratio > 1.06:
        center = ((x0 + x1) / 2 + 80, (y0 + y1) / 2 + 260)
        echo = cv2.warpAffine(mask, cv2.getRotationMatrix2D(center, 0, echo_ratio), (a.shape[1], a.shape[0]))
        luminous += echo * 0.28
        out += echo[:, :, None] * np.array([71, 64, 57])
    outer = cv2.GaussianBlur(luminous, (0, 0), max(0.6, 2.8 * halo))
    inner = cv2.GaussianBlur(luminous, (0, 0), max(0.4, 1.1 * sy))
    out += outer[:, :, None] * np.array([260, 60, 12]) * halo + inner[:, :, None] * np.array([125, 51, 19])
    color = np.array([255, 247, 233]) * min(1, float(peak) / 245)
    out = out * (1 - mask[:, :, None]) + color * mask[:, :, None]
    return np.clip(np.round(out), 0, 255).astype('uint8')

def compose(source: Path, output: Path, report: Path, kind: str, font_path: Path) -> dict:
    """Compose one already decoded, lossless source. Never read or write a game installation."""
    if kind not in ('recap', 'countdown'):
        raise ValueError('unsupported kind')
    outputs = [output, report, output.with_suffix('.png')]
    if kind == 'countdown':
        outputs.append(output.with_name(output.stem + '-cleanplate.png'))
    if len({p.resolve() for p in outputs}) != len(outputs):
        raise ValueError('outputs must be distinct')
    if any((p.exists() for p in outputs)):
        raise FileExistsError('an output or preview already exists')
    expected, rate = (351, 30) if kind == 'recap' else (51, 25)
    cap = cv2.VideoCapture(str(source))
    if not cap.isOpened():
        raise ValueError('Invalid source or composition invariant: cap.isOpened()')
    if not round(cap.get(cv2.CAP_PROP_FRAME_COUNT)) == expected:
        raise ValueError('Invalid source or composition invariant: round(cap.get(cv2.CAP_PROP_FRAME_COUNT)) == expected')
    if not abs(cap.get(cv2.CAP_PROP_FPS) - rate) < 0.001:
        raise ValueError('Invalid source or composition invariant: abs(cap.get(cv2.CAP_PROP_FPS) - rate) < 0.001')
    cap.set(cv2.CAP_PROP_POS_FRAMES, 300 if kind == 'recap' else 0)
    ok, reference = cap.read()
    if not ok:
        raise ValueError('Invalid source or composition invariant: ok')
    reference = cv2.cvtColor(reference, cv2.COLOR_BGR2RGB)
    if not reference.shape == (600, 1024, 3):
        raise ValueError('Invalid source or composition invariant: reference.shape == (600, 1024, 3)')
    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    if kind == 'countdown':
        replacement, clean, _, _ = counter(reference, font_path)
        patch = np.any(replacement != reference, axis=2)
        Image.fromarray(replacement).save(output.with_suffix('.png'))
        Image.fromarray(clean).save(output.with_name(output.stem + '-cleanplate.png'))
    proc = subprocess.Popen(['ffmpeg', '-v', 'error', '-n', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', '1024x600', '-r', str(rate), '-i', 'pipe:0', '-an', '-c:v', 'ffv1', '-level', '3', str(output)], stdin=subprocess.PIPE)
    changed = []
    bounds = []
    pixel_counts = []
    try:
        for i in range(expected):
            ok, bgr = cap.read()
            if not ok:
                raise ValueError('Invalid source or composition invariant: ok')
            a = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
            if kind == 'recap':
                b = recap(a, i, reference, font_path)
                if i < 251:
                    if not np.array_equal(a, b):
                        raise ValueError('Invalid source or composition invariant: np.array_equal(a, b)')
            else:
                drift = a.astype('int16') - reference.astype('int16')
                if not np.abs(drift[patch]).max() <= 8:
                    raise ValueError(f'patch overlaps digit strokes at frame {i}')
                b = a.copy()
                b[patch] = np.clip(replacement[patch].astype('int16') + drift[patch], 0, 255).astype('uint8')
            diff = np.any(a != b, axis=2)
            ys, xs = np.where(diff)
            if len(xs):
                changed.append(i)
                box = [int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())]
                if kind == 'recap':
                    if not (box[0] >= 80 and box[2] < 945 and (box[1] >= 260) and (box[3] < 365)):
                        raise ValueError('Invalid source or composition invariant: box[0] >= 80 and box[2] < 945 and (box[1] >= 260) and (box[3] < 365)')
            else:
                box = None
            bounds.append(box)
            pixel_counts.append(int(diff.sum()))
            proc.stdin.write(b.tobytes())
            if kind == 'recap' and i == 300:
                Image.fromarray(b).save(output.with_suffix('.png'))
        if cap.read()[0]:
            raise ValueError('source has more frames than expected')
    finally:
        cap.release()
        proc.stdin.close()
        exit_code = proc.wait()
    if exit_code:
        raise RuntimeError('FFmpeg lossless output failed')
    result = dict(schema='photon-story-label-composition/1', kind=kind, frames=expected, rate=rate, width=1024, height=600, changed_frames=changed, changed_bounds=bounds, changed_pixel_counts=pixel_counts, font_sha256=hashlib.sha256(font_path.read_bytes()).hexdigest(), font_family='Noto Sans SC', checks=['original frame count/rate/size retained', 'recap frames before 251 unchanged' if kind == 'recap' else 'numeric panel protected; adjacent ambient-light variation retained; no changed digit strokes enter label patch'], limitations=['Offline pixel composition only'] + (['Countdown cleanplate uses smooth lighting estimation; original hidden background is not recovered byte for byte'] if kind == 'countdown' else []))
    report.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return result

def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('source', 'output', 'report'):
        p.add_argument(name, type=Path)
    p.add_argument('--kind', choices=('recap', 'countdown'), required=True)
    p.add_argument('--font', type=Path, required=True)
    a = p.parse_args()
    r = compose(a.source, a.output, a.report, a.kind, a.font)
    print(json.dumps(dict(kind=r['kind'], frames=r['frames'], changed_frames=len(r['changed_frames']))))
if __name__ == '__main__':
    main()
