"""Compose local repaired video crops into a lossless proxy with pixel checks.

The input crop must equal the source frame. Every unmasked pixel in a repaired
crop must equal its input. No game assets or repair models are distributed here.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess


def compose(video: Path, repairs: list[tuple[Path, Path]], output: Path) -> dict:
    import cv2
    import numpy as np

    if output.exists():
        raise FileExistsError(output)
    prepared = []
    for input_dir, result_dir in repairs:
        manifest = json.loads((input_dir / 'manifest.json').read_text(encoding='utf-8'))
        start, end = manifest['range']
        box = manifest['crop_xyxy']
        if not (0 <= start < end and len(manifest['frames']) == end-start):
            raise ValueError('invalid repair frame coverage')
        if [row['frame'] for row in manifest['frames']] != list(range(start, end)):
            raise ValueError('repair manifest frame order mismatch')
        if manifest.get('resize') is not False:
            raise ValueError('only native-resolution crops are supported')
        names = [row['file'] for row in manifest['frames']]
        if any(Path(name).name != name for name in names) or len(set(names)) != len(names):
            raise ValueError('invalid crop filenames')
        if {path.name for path in result_dir.glob('*.png')} != set(names):
            raise ValueError('repair output coverage mismatch')
        prepared.append((start, end, box, input_dir, result_dir, names))
    prepared.sort(key=lambda item: item[0])
    if any(a[1] > b[0] for a, b in zip(prepared, prepared[1:])):
        raise ValueError('overlapping repair time ranges are not supported')

    def read_png(path):
        pixels = cv2.imdecode(np.frombuffer(path.read_bytes(), dtype=np.uint8), cv2.IMREAD_UNCHANGED)
        if pixels is None:
            raise ValueError(f'cannot decode crop: {path}')
        return pixels

    capture = cv2.VideoCapture(str(video))
    pipe = None
    count = 0
    changed_frames = 0
    checked_crops = 0
    try:
        while True:
            ok, frame = capture.read()
            if not ok:
                break
            if frame.shape != (600, 1024, 3):
                raise ValueError('expected a native 1024x600 Rebirth proxy')
            if pipe is None:
                pipe = subprocess.Popen(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-nostdin', '-n',
                                         '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', '1024x600', '-r', '30',
                                         '-i', 'pipe:0', '-an', '-c:v', 'ffv1', str(output)], stdin=subprocess.PIPE)
            for start, end, box, input_dir, result_dir, names in prepared:
                if not start <= count < end:
                    continue
                x0, y0, x1, y1 = box
                if not (0 <= x0 < x1 <= 1024 and 0 <= y0 < y1 <= 600):
                    raise ValueError('crop exceeds source dimensions')
                name = names[count-start]
                original = read_png(input_dir / 'frames' / name)
                repaired = read_png(result_dir / name)
                mask = read_png(input_dir / 'masks' / name)
                if original.shape != (y1-y0, x1-x0, 3) or repaired.shape != original.shape or mask.shape != original.shape[:2]:
                    raise ValueError(f'crop dimensions differ at frame {count}')
                if not np.array_equal(original, frame[y0:y1, x0:x1]):
                    raise ValueError(f'input crop does not match source frame {count}')
                if not np.array_equal(repaired[mask == 0], original[mask == 0]):
                    raise ValueError(f'unmasked pixels changed at frame {count}')
                changed_frames += int(np.any(original != repaired))
                checked_crops += 1
                frame[y0:y1, x0:x1] = repaired
            pipe.stdin.write(frame.tobytes())
            count += 1
        if not count or any(end > count for _, end, *_ in prepared):
            raise ValueError('source does not cover all repair ranges')
        pipe.stdin.close()
        if pipe.wait() != 0:
            raise RuntimeError('FFmpeg lossless composition failed')
    finally:
        capture.release()
        if pipe is not None and pipe.poll() is None:
            pipe.stdin.close()
            pipe.terminate()
            pipe.wait()
    return dict(frames=count, dimensions=[1024, 600], nominal_fps='30/1',
                checked_crops=checked_crops, changed_frames=changed_frames,
                unmasked_pixels_identical=True,
                repair_ranges=[dict(frames=[start, end], crop=box) for start, end, box, *_ in prepared],
                limitation='pixel preservation and composition checks only; repair quality and game timing are not approved')


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--video', required=True, type=Path)
    parser.add_argument('--repair', required=True, action='append', nargs=2, type=Path,
                        metavar=('INPUT_DIRECTORY', 'REPAIRED_FRAMES_DIRECTORY'))
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--report', required=True, type=Path)
    args = parser.parse_args()
    if args.report.exists():
        raise FileExistsError(args.report)
    report = compose(args.video, args.repair, args.output)
    with args.report.open('x', encoding='utf-8') as stream:
        json.dump(report, stream, indent=2)
        stream.write('\n')
    print(f'Composed {report["frames"]} frames; checked {report["checked_crops"]} repaired crops')


if __name__ == '__main__':
    main()
