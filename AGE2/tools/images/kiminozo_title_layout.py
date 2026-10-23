"""Render complete title-menu rows with a shared type scale and baseline.

The layout contains only UI copy, geometry and sampled effect parameters.
No original game images or font binaries are required in the repository.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess

from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont


def placement(group, units_per_reference_height):
    """The same group always supplies scale/origin/baseline, independent of text."""
    return (group['origin_x'], group['baseline_y'],
            group['reference_ink_height'] / units_per_reference_height)


def svg_row(font, row, group):
    glyphs, cmap = font.getGlyphSet(), font.getBestCmap()
    reference = BoundsPen(glyphs)
    glyphs[cmap[ord('国')]].draw(reference)
    x, baseline, scale = placement(group, reference.bounds[3] - reference.bounds[1])
    path, bounds, advance = SVGPathPen(glyphs), BoundsPen(glyphs), 0
    for char in row['text']:
        if ord(char) not in cmap:
            raise ValueError('Font does not cover UI copy: ' + char)
        name = cmap[ord(char)]
        transform = (1, 0, 0, 1, advance, 0)
        glyphs[name].draw(TransformPen(path, transform))
        glyphs[name].draw(TransformPen(bounds, transform))
        advance += font['hmtx'][name][0]
    width, height = row['size']
    left, bottom, right, top = bounds.bounds
    if min(x + left * scale - 2, baseline - top * scale - 2) < 0 or \
            x + right * scale + 2 >= width or baseline - bottom * scale + 2 >= height:
        raise ValueError('UI copy does not fit fixed group geometry: ' + row['key'])
    glyph = (f'<path d="{path.getCommands()}" transform="translate({x} {baseline}) '
             f'scale({scale} {-scale})" stroke="white" stroke-width="{.5 / scale}" '
             'fill="white" stroke-linejoin="round"/>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">'
            f'<g transform="translate(-.75 0)">{glyph}</g>'
            f'<g transform="translate(.75 0)">{glyph}</g>{glyph}</svg>')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--layout', type=Path, required=True)
    parser.add_argument('--font', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--node', type=Path, help='Also rasterize with this Node executable')
    parser.add_argument('--sharp-module', default='sharp', help='Sharp package name or absolute package path')
    args = parser.parse_args()
    config = json.loads(args.layout.read_text('utf-8'))
    if hashlib.sha256(args.font.read_bytes()).hexdigest() != config['font_sha256']:
        raise ValueError('Font differs from the reviewed typography input')
    args.output.mkdir(parents=True, exist_ok=False)
    with TTFont(args.font) as font:
        seen = set()
        for row in config['records']:
            key = row['key']
            if not key or any(c not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-' for c in key) or key in seen:
                raise ValueError('Unsafe or duplicate UI resource key')
            seen.add(key)
            (args.output / (key + '.svg')).write_text(svg_row(font, row, config['groups'][row['group']]), 'utf-8')
    render_config = args.output / 'render-config.json'
    render_config.write_text(json.dumps(config['records'], ensure_ascii=False, indent=2), 'utf-8')
    if args.node:
        renderer = Path(__file__).with_suffix('.cjs')
        subprocess.run([str(args.node), str(renderer), str(render_config), str(args.output), args.sharp_module], check=True)


if __name__ == '__main__':
    main()
