"""Export a draft Chinese technical/notice track from measured video glyph signals.

Reveal and opacity use candidate measurements, not approved final animation keys.
The corresponding English glyphs must be removed from the source video first.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def build_ass(layout: dict, analysis: dict, arrays, rows, font: str) -> str:
    if layout.get('schema') != 'photon-crsi-technical-layout/1':
        raise ValueError('unsupported layout schema')
    if analysis.get('schema') != 'photon-crsi-technical-analysis/1':
        raise ValueError('unsupported analysis schema')
    if layout['source_global_offset'] != analysis['source_global_offset']:
        raise ValueError('layout and analysis describe different sources')
    if not font.strip() or any(c in font for c in ',\r\n{}\\'):
        raise ValueError('invalid ASS font name')
    texts = {}
    for row in rows:
        if row['variant'] not in ('both', layout['text_variant']) or row['layer'] == 'subtitle':
            continue
        if row['id'] in texts:
            raise ValueError(f'duplicate text: {row["id"]}')
        value = row['target_text']
        if not value or any(c in value for c in '{}\\\r\n'):
            raise ValueError(f'unsupported ASS markup: {row["id"]}')
        texts[row['id']] = value
    detected = {entry['occurrence']: entry for entry in analysis['overlays']}
    occurrences = {spec['occurrence'] for spec in layout['overlays']}
    if len(detected) != len(analysis['overlays']) or len(occurrences) != len(layout['overlays']) or detected.keys() != occurrences:
        raise ValueError('analysis occurrence coverage mismatch')

    def timestamp(frame):
        centiseconds = frame * 100 // 30
        return f'{centiseconds//360000}:{centiseconds//6000%60:02}:{centiseconds//100%60:02}.{centiseconds%100:02}'

    lines = ['[Script Info]', 'Title: Rebirth Chinese technical text draft',
             'ScriptType: v4.00+', 'PlayResX: 1024', 'PlayResY: 600',
             'WrapStyle: 2', 'ScaledBorderAndShadow: yes', '', '[V4+ Styles]',
             'Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding',
             f'Style: Label,{font},30,&H00FFFFFF,&H00FFFFFF,&H00FFFFFF,&H00000000,0,0,0,0,100,100,0,0,1,0,0,7,0,0,0,1',
             '', '[Events]', 'Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text']
    covered = set()
    for spec in layout['overlays']:
        key = spec['text_id']
        if key not in texts:
            raise ValueError(f'missing Chinese text: {key}')
        covered.add(key)
        text = texts[key]
        if 'text_part' in spec:
            parts = text.split(spec['text_separator'])
            if not 0 <= spec['text_part'] < len(parts):
                raise ValueError(f'missing text part: {key}')
            text = parts[spec['text_part']]
        entry = detected[spec['occurrence']]
        signal = arrays[f'signal_{entry["mask_index"]}']
        if f'coverage_{entry["mask_index"]}' not in arrays:
            raise ValueError('glyph analysis lacks reveal coverage; rerun overlay_masks')
        coverage = arrays[f'coverage_{entry["mask_index"]}']
        start, end = spec['detection_span']
        if len(signal) != end - start or len(coverage) != len(signal) or entry['signal_start_frame'] != start or entry['peak'] <= 0:
            raise ValueError(f'invalid signal: {key}')
        target = spec['target']
        most_visible = 0
        for frame in range(start, end):
            ratio = max(0.0, min(1.0, float(signal[frame-start]) / entry['peak']))
            fraction = max(0.0, min(1.0, float(coverage[frame-start])))
            visible = max(most_visible, round(len(text) * fraction))
            most_visible = visible
            # Coverage drives typewriter progression; intensity drives opacity.
            # Normalize partial-line intensity by coverage so text does not fade
            # merely because only its first few glyphs have appeared.
            intensity = ratio if visible == len(text) else ratio/max(fraction, .01)
            alpha = round((1-min(1.0, intensity)) * 255)
            if not visible or alpha == 255:
                continue
            # Transparent suffix preserves the width and the fixed left origin
            # of a right-aligned typewriter line as more characters appear.
            content = text[:visible]
            if visible < len(text):
                content += '{\\alpha&HFF&}' + text[visible:]
            tags = (f'{{\\an{target["alignment"]}\\pos({target["x"]},{target["y"]})'
                    f'\\fs{target["font_size"]}\\c&H{target["ass_color"]}&'
                    f'\\alpha&H{alpha:02X}&}}')
            lines.append(f'Dialogue: 0,{timestamp(frame)},{timestamp(frame+1)},Label,,0,0,0,,{tags}{content}')
    if covered != texts.keys():
        raise ValueError('layout omits an applicable technical/notice text')
    return '\n'.join(lines) + '\n'


def main() -> None:
    import numpy as np

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--layout', required=True, type=Path)
    parser.add_argument('--analysis-directory', required=True, type=Path)
    parser.add_argument('--text', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--font', default='Microsoft YaHei')
    args = parser.parse_args()
    layout = json.loads(args.layout.read_text(encoding='utf-8'))
    analysis = json.loads((args.analysis_directory / 'analysis.json').read_text(encoding='utf-8'))
    with args.text.open(encoding='utf-8-sig', newline='') as stream:
        rows = list(csv.DictReader(stream))
    with np.load(args.analysis_directory / 'glyphs-and-signals.npz') as arrays:
        track = build_ass(layout, analysis, arrays, rows, args.font)
    with args.output.open('x', encoding='utf-8-sig', newline='\n') as stream:
        stream.write(track)
    print(f'Wrote all {len(layout["overlays"])} Chinese overlay occurrences')


if __name__ == '__main__':
    main()
