"""Export reviewed Rebirth caption frame ranges as a Chinese ASS draft.

This is an offline preview track. It does not remove baked technical labels,
encode CRsi, or establish the game's audio/video start-time relationship.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def build_ass(timeline: dict, rows: list[dict[str, str]], font: str) -> str:
    if timeline.get('schema') != 'photon-crsi-caption-frames/1':
        raise ValueError('unsupported caption timeline schema')
    if timeline.get('frame_index_origin') != 0 or timeline.get('end_semantics') != 'exclusive':
        raise ValueError('timeline must use zero-based, end-exclusive frame ranges')
    clock = timeline['native_default_clock']
    numerator, denominator = clock['fps_numerator'], clock['fps_denominator']
    if not (isinstance(numerator, int) and isinstance(denominator, int)
            and 0 < denominator <= numerator <= 100 * denominator):
        raise ValueError('ASS preview supports positive frame rates up to 100 fps')
    if not font.strip() or any(char in font for char in ',\r\n'):
        raise ValueError('invalid ASS font name')
    text = {}
    for row in rows:
        if row['layer'] != 'subtitle' or row['variant'] not in ('both', timeline['text_variant']):
            continue
        if row['id'] in text:
            raise ValueError(f'duplicate applicable caption: {row["id"]}')
        value = row['target_text']
        if not value or any(char in value for char in '{}\\\r\n'):
            raise ValueError(f'caption contains unsupported ASS markup: {row["id"]}')
        text[row['id']] = value

    def timestamp(frame):
        # Floor centiseconds so the ASS event includes exactly the intended
        # 30 fps frame timestamps, including frames at 1/3 centisecond phases.
        centiseconds = frame * 100 * denominator // numerator
        hours, tail = divmod(centiseconds, 360000)
        minutes, tail = divmod(tail, 6000)
        seconds, fraction = divmod(tail, 100)
        return f'{hours}:{minutes:02}:{seconds:02}.{fraction:02}'

    lines = ['[Script Info]', f"Title: Rebirth {timeline['text_variant']} Chinese subtitle draft",
             'ScriptType: v4.00+', 'PlayResX: 1024', 'PlayResY: 600',
             'WrapStyle: 2', 'ScaledBorderAndShadow: yes', '', '[V4+ Styles]',
             'Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding',
             f'Style: Caption,{font},28,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,2,0,2,32,32,28,1',
             '', '[Events]', 'Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text']
    seen = set()
    previous_end = 0
    for cue in timeline['captions']:
        key, start, end = cue['id'], cue['start_frame'], cue['end_frame']
        if not (isinstance(start, int) and isinstance(end, int)
                and previous_end <= start < end <= timeline['frame_count']):
            raise ValueError(f'invalid or overlapping frame range: {key}')
        if key in seen or key not in text:
            raise ValueError(f'duplicate or missing caption text: {key}')
        seen.add(key)
        previous_end = end
        lines.append(f'Dialogue: 0,{timestamp(start)},{timestamp(end)},Caption,,0,0,0,,{text[key]}')
    if seen != text.keys():
        raise ValueError('timeline does not cover every applicable subtitle row')
    return '\n'.join(lines) + '\n'


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--timeline', required=True, type=Path)
    parser.add_argument('--text', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--font', default='Microsoft YaHei')
    args = parser.parse_args()
    timeline = json.loads(args.timeline.read_text(encoding='utf-8'))
    with args.text.open(encoding='utf-8-sig', newline='') as stream:
        rows = list(csv.DictReader(stream))
    track = build_ass(timeline, rows, args.font)
    with args.output.open('x', encoding='utf-8-sig', newline='\n') as stream:
        stream.write(track)
    print(f'Wrote {len(timeline["captions"])} Chinese caption events')


if __name__ == '__main__':
    main()
