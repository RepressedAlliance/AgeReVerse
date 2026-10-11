"""Render reusable native-size text layers from a shared Rebirth style profile.

Uses the repository's existing baseline-aware, variable-font image typography.
Outputs are static full-text layers; video reveal/fade timing is a separate step.
"""
from __future__ import annotations

from pathlib import Path
from importlib import import_module


def role_for(spec: dict, profile: dict) -> dict:
    key = spec['text_id'] if spec['group'] == 'notice' else ('price' if spec['color'] == 'magenta' else 'technical')
    role = dict(profile['roles'][key])
    if 'anchor' not in role:
        role['anchor'] = [spec['target']['x'], spec['box_xyxy'][1] + role['baseline_from_source_box_top']]
        role['alignment'] = 'right' if spec['target']['alignment'] == 9 else 'left'
    return role


def render_layer(text: str, role: dict, profile: dict, font_path: Path):
    from PIL import Image, ImageFilter
    typography = import_module(
        'Localization-MakeGamesSpeak.Tools-LetToolsHandleRepetition.images.render_deterministic_localized_text'
    )
    load_variable_font = typography.load_variable_font
    render_tracking_mask = typography.render_tracking_mask
    tint = typography.tint

    if profile.get('schema') != 'photon-crsi-style-study/1' or profile.get('supersample') != 8 or profile.get('scale_x') != 1:
        raise ValueError('unsupported video style profile')
    if not text or '\n' in text or '\r' in text:
        raise ValueError('one nonempty text line is required')
    ss = profile['supersample']
    font, lock = load_variable_font(font_path, role['size'], role['weight'], ss, profile['font']['sha256'])
    raw = render_tracking_mask(text, font, role['tracking'], ss)
    glow, outline = role.get('glow', 0), role.get('outline', 0)
    pad = round(max(8, glow*4, outline+3)*ss)
    mask = Image.new('L', (raw.width+pad*2, raw.height+pad*2))
    mask.paste(raw.image, (pad, pad))
    layer = Image.new('RGBA', mask.size)
    if outline:
        border = mask.filter(ImageFilter.MaxFilter(round(outline*ss)*2+1))
        layer = Image.alpha_composite(layer, tint(border, (0, 0, 0, 220)))
    if glow:
        halo = mask.filter(ImageFilter.GaussianBlur(glow*ss))
        layer = Image.alpha_composite(layer, tint(halo, (*role['color'], 140)))
    layer = Image.alpha_composite(layer, tint(mask, (*role['color'], 255)))
    layer = layer.resize((round(layer.width/ss), round(layer.height/ss)), Image.Resampling.LANCZOS)
    x, baseline = role['anchor']
    alignment = role['alignment']
    if alignment not in ('left', 'center', 'right'):
        raise ValueError('unsupported text alignment')
    width = raw.width/ss
    left = x-(width if alignment == 'right' else width/2 if alignment == 'center' else 0)
    top = baseline-raw.baseline_from_top_hi/ss
    position = (round(left-pad/ss), round(top-pad/ss))
    metrics = dict(ink_box=[left, top, left+width, top+raw.height/ss],
                   position=position, layer_size=list(layer.size), font=lock)
    if not (0 <= position[0] and 0 <= position[1] and position[0]+layer.width <= 1024 and position[1]+layer.height <= 600):
        raise ValueError(f'text/effect layer extends beyond the native frame: {text}')
    return layer, position, metrics
