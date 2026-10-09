"""Reconstruct only Rebirth's smooth blue opening field from same-frame borders.

The scoped interval is frames 0..189 of the no-caption long ending proxy. This
method is unsuitable for the later model/mesh scenes. Outputs contain game
pixels and must remain in a private working directory.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def coons_fill(rgb, box):
    import numpy as np

    height, width, channels = rgb.shape
    x0, y0, x1, y1 = box
    if channels != 3 or not (0 < x0 < x1 < width and 0 < y0 < y1 < height):
        raise ValueError('fill region needs one clean border pixel on every side')
    source = rgb.astype(np.float32)
    u = ((np.arange(x1-x0, dtype=np.float32)+1)/(x1-x0+1))[None, :, None]
    v = ((np.arange(y1-y0, dtype=np.float32)+1)/(y1-y0+1))[:, None, None]
    left, right = source[y0:y1, x0-1:x0], source[y0:y1, x1:x1+1]
    top, bottom = source[y0-1:y0, x0:x1], source[y1:y1+1, x0:x1]
    tl, tr, bl, br = source[y0-1, x0-1], source[y0-1, x1], source[y1, x0-1], source[y1, x1]
    patch = (left*(1-u) + right*u + top*(1-v) + bottom*v
             - ((1-u)*(1-v)*tl + u*(1-v)*tr + (1-u)*v*bl + u*v*br))
    result = rgb.copy()
    result[y0:y1, x0:x1] = np.rint(np.clip(patch, 0, 255)).astype(np.uint8)
    return result


def prepare(video: Path, output: Path) -> None:
    import cv2
    import numpy as np
    from PIL import Image

    output.mkdir(parents=True, exist_ok=False)
    for name in ('frames', 'masks', 'repaired'):
        (output / name).mkdir()
    crop = (200, 104, 824, 464)
    region = (224, 136, 800, 432)
    x0, y0, x1, y1 = crop
    box = (region[0]-x0, region[1]-y0, region[2]-x0, region[3]-y0)
    mask = np.zeros((y1-y0, x1-x0), np.uint8)
    mask[box[1]:box[3], box[0]:box[2]] = 255
    rows = []
    capture = cv2.VideoCapture(str(video))
    try:
        for number in range(190):
            ok, frame = capture.read()
            if not ok or frame.shape != (600, 1024, 3):
                raise ValueError(f'missing native source frame {number}')
            rgb = cv2.cvtColor(frame[y0:y1, x0:x1], cv2.COLOR_BGR2RGB)
            repaired = coons_fill(rgb, box)
            name = f'{number:04}.png'
            Image.fromarray(rgb).save(output / 'frames' / name)
            Image.fromarray(mask).save(output / 'masks' / name)
            Image.fromarray(repaired).save(output / 'repaired' / name)
            rows.append(dict(frame=number, file=name, mask_pixels=int(np.count_nonzero(mask))))
    finally:
        capture.release()
    manifest = dict(source=1715679260, range=[0, 190], crop_xyxy=crop, resize=False,
                    mask_region_xyxy=region, method='same-frame Coons boundary interpolation',
                    status='scoped opening background draft; visual acceptance and game integration pending', frames=rows)
    with (output / 'manifest.json').open('x', encoding='utf-8') as stream:
        json.dump(manifest, stream, indent=2)
        stream.write('\n')


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--video', required=True, type=Path)
    parser.add_argument('--output-directory', required=True, type=Path)
    args = parser.parse_args()
    prepare(args.video, args.output_directory)
    print('Prepared 190 opening backgrounds; later scenes are outside this method')


if __name__ == '__main__':
    main()
