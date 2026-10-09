"""Extract fixed technical glyph cores and candidate reveal/fade signals.

Requires a native-resolution decoded proxy, OpenCV and NumPy. Outputs include
derived game pixels and belong in a private task directory, not the repository.
This analyzer does not remove text or certify exact animation timing.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def analyze(video: Path, layout: dict) -> tuple[dict, dict]:
    import cv2
    import numpy as np

    if layout.get('schema') != 'photon-crsi-technical-layout/1':
        raise ValueError('unsupported technical layout schema')
    if layout.get('frame_index_origin') != 0 or layout.get('end_semantics') != 'exclusive':
        raise ValueError('expected zero-based, end-exclusive ranges')
    width, height, count = layout['width'], layout['height'], layout['frame_count']
    needed = set()
    names = set()
    for entry in layout['overlays']:
        name = entry['occurrence']
        if name in names:
            raise ValueError(f'duplicate occurrence: {name}')
        names.add(name)
        x0, y0, x1, y1 = entry['box_xyxy']
        start, end = entry['detection_span']
        references = entry['reference_frames']
        if not (0 <= x0 < x1 <= width and 0 <= y0 < y1 <= height
                and 0 <= start < end <= count and references
                and all(start <= frame < end for frame in references)):
            raise ValueError(f'invalid region or references: {name}')
        if entry['color'] not in ('white', 'magenta', 'cyan'):
            raise ValueError(f'unsupported glyph color: {name}')
        needed.update(range(start, end))
    if not needed:
        raise ValueError('layout has no overlays')

    # Keep only analyzed intervals. Native pixel positions must remain unchanged.
    frames = {}
    capture = cv2.VideoCapture(str(video))
    try:
        for number in range(max(needed) + 1):
            ok, frame = capture.read()
            if not ok:
                raise ValueError(f'video ends before analyzed frame {number}')
            if frame.shape != (height, width, 3):
                raise ValueError('video dimensions differ from glyph layout')
            if number in needed:
                frames[number] = frame
    finally:
        capture.release()

    records, arrays = [], {}
    for index, entry in enumerate(layout['overlays']):
        x0, y0, x1, y1 = entry['box_xyxy']
        refs = np.stack([frames[number][y0:y1, x0:x1].astype(np.float32)
                         for number in entry['reference_frames']])
        if entry['color'] == 'white':
            # Intersection suppresses moving highlights behind fixed white text.
            core = ((refs.min(axis=(0, 3)) > 190)
                    & (np.max(refs.max(axis=3) - refs.min(axis=3), axis=0) < 35))
        elif entry['color'] == 'cyan':
            core = ((refs[:, :, :, 1] - refs[:, :, :, 2]).min(axis=0) > 55)
            core &= ((refs[:, :, :, 0] - refs[:, :, :, 2]).min(axis=0) > 70)
        else:
            # Union is needed because original price text flashes on and off.
            strength = np.minimum(refs[:, :, :, 0], refs[:, :, :, 2]) - refs[:, :, :, 1]
            core = np.max(strength, axis=0) > 60
        if core.sum() < 30:
            raise ValueError(f'no useful glyph core: {entry["occurrence"]}')
        ring = (cv2.dilate(core.astype(np.uint8), np.ones((7, 7), np.uint8)).astype(bool)
                & ~cv2.dilate(core.astype(np.uint8), np.ones((3, 3), np.uint8)).astype(bool))
        if not ring.any():
            raise ValueError(f'no comparison ring: {entry["occurrence"]}')
        signal, coverage = [], []
        start, end = entry['detection_span']
        for number in range(start, end):
            crop = frames[number][y0:y1, x0:x1].astype(np.float32)
            if entry['color'] == 'white':
                plane = crop.min(axis=2)
                visible = (plane > 80) & (crop.max(axis=2)-plane < 60)
            elif entry['color'] == 'cyan':
                plane = crop[:, :, 1] - crop[:, :, 2]
                visible = plane > 25
            else:
                plane = np.minimum(crop[:, :, 0], crop[:, :, 2]) - crop[:, :, 1]
                visible = crop[:, :, 2]-crop[:, :, 1] > 40
            signal.append(float(plane[core].mean() - plane[ring].mean()))
            coverage.append(float(visible[core].mean()))
        signal = np.array(signal)
        coverage = np.array(coverage)
        peak = float(np.percentile(signal, 90))
        active = np.where(signal > max(15, peak * .1))[0]
        full = np.where(signal > peak * .9)[0]
        if not len(active) or not len(full):
            raise ValueError(f'no visible interval: {entry["occurrence"]}')
        records.append(dict(occurrence=entry['occurrence'], mask_index=index,
                            mask_core_pixels=int(core.sum()), signal_start_frame=start,
                            candidate_start=int(active[0] + start),
                            candidate_full_start=int(full[0] + start),
                            candidate_end=int(active[-1] + start + 1), peak=peak))
        arrays[f'mask_{index}'] = core
        arrays[f'signal_{index}'] = signal
        arrays[f'coverage_{index}'] = coverage
    return dict(schema='photon-crsi-technical-analysis/1',
                source_global_offset=layout['source_global_offset'],
                status='candidate thresholds; inspect animation boundaries before production',
                overlays=records), arrays


def main() -> None:
    import numpy as np

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--video', required=True, type=Path)
    parser.add_argument('--layout', required=True, type=Path)
    parser.add_argument('--output-directory', required=True, type=Path)
    args = parser.parse_args()
    if args.output_directory.exists():
        raise FileExistsError('choose a new private analysis output directory')
    layout = json.loads(args.layout.read_text(encoding='utf-8'))
    result, arrays = analyze(args.video, layout)
    args.output_directory.mkdir(parents=True)
    with (args.output_directory / 'analysis.json').open('x', encoding='utf-8') as stream:
        json.dump(result, stream, indent=2)
        stream.write('\n')
    np.savez_compressed(args.output_directory / 'glyphs-and-signals.npz', **arrays)
    print(f'Analyzed {len(result["overlays"])} technical rows; boundaries remain candidates')


if __name__ == '__main__':
    main()
