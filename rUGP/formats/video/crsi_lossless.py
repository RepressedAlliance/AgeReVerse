"""Opaque 8/8/8 CRsi frames using PM's scalar MSB alpha decode path.

Mode 0x03ff selects 8-bit B/G/R and bit 9 selects the scalar alpha decoder
at 0x57b490. This reuses the existing CRip008 kind-3 payload grammar, but
passes B,G,R,0x80 pixels directly: its image-specific RGBA converter uses
a different channel convention and must not be used for CRsi.

The initial writer uses literal rows. It preserves RGB exactly, but does
not yet establish native streaming throughput or patch-size suitability.
"""
from __future__ import annotations

from rUGP.formats.images.crip008_kind3_encode import encode_native_pixels
from .crsi import Frame


def encode_rgb(rgb: bytes, width: int, height: int) -> Frame:
    # The audited scalar leaf has a local row buffer below width 1600. Wider
    # images require an allocation path outside the current native oracle.
    if not (0 < width < 1600 and 0 < height <= 4096 and width*height <= 2_097_152):
        raise ValueError('dimensions exceed the verified scalar CRsi profile')
    if len(rgb) != width * height * 3:
        raise ValueError('RGB buffer does not match CRsi dimensions')
    pixels = width * height
    native = bytearray(pixels * 4)
    native[0::4] = rgb[2::3]
    native[1::4] = rgb[1::3]
    native[2::4] = rgb[0::3]
    native[3::4] = bytes([0x80]) * pixels
    payload, _ = encode_native_pixels(native, width=width, height=height,
                                      x_offset=0, y_offset=0,
                                      draw_width=width, draw_height=height)
    # The native bit reader initially reads four bytes unconditionally.
    payload += bytes(max(0, 4-len(payload)))
    return Frame(1, 0, 0, 0x03ff, None, payload)
