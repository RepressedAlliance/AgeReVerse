"""Experimental codec-0 independent frame writer for PM's CRsi dispatch.

Reuses the upstream-derived Cr6Ti universal bit writer, not its color model.
Native PM 0x579B30 uses sequential saturated shared, blue and red deltas.
The verified profile is 6/6/6 (mode 0x016D), opaque, with <=3 channel error.
This is a technical probe profile, not approval of production visual quality.
"""
from __future__ import annotations

from rUGP.formats.images.cr6ti_encode import LsbBitWriter
from .crsi import Frame


def encode_rgb(rgb: bytes, width: int, height: int) -> tuple[Frame, bytes]:
    if not (0 < width <= 4096 and 0 < height <= 4096) or len(rgb) != width * height * 3:
        raise ValueError('RGB buffer or CRsi dimensions are invalid')
    writer = LsbBitWriter()
    expected = bytearray()
    for y in range(height):
        writer.unsigned(width - 1)
        red = green = blue = 0
        for x in range(width):
            at = (y * width + x) * 3
            nr, ng, nb = (value & 252 for value in rgb[at:at+3])
            shared = (ng - green) // 4
            predicted_blue = max(0, min(252, blue + shared * 4))
            predicted_red = max(0, min(252, red + shared * 4))
            writer.bit(False)
            for value in (shared, (nb-predicted_blue)//4, (nr-predicted_red)//4):
                if not -63 <= value <= 63:
                    raise ValueError('delta exceeds native short signed table')
                writer.signed(value)
            red, green, blue = nr, ng, nb
            expected.extend((red, green, blue))
    return Frame(1, 0, 0, 0x016d, None, writer.finish()), bytes(expected)
