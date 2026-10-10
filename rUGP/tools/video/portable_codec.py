"""Explicit bindings to the self-contained C CRsi codec (no game oracle).

Build crsi_codec.c + crsi_lossless.c + crsi_container.c as a shared library,
then pass that file to Codec. No implicit compiler, downloads, or fallback.
"""
from __future__ import annotations
import ctypes as c
from pathlib import Path
from rUGP.formats.video.crsi import Frame


class Codec:
    def __init__(self, library: Path):
        self.library = c.CDLL(str(library.resolve(strict=True)))
        p, s, u, i = c.c_void_p, c.c_size_t, c.c_uint, c.c_int
        signatures = {
            'crsi_decode_codec1': [p,s,u,u,i,u,u,p,s,p],
            'crsi_decode_0575': [p,s,u,u,i,p,s,p],
            'crsi_decode_03ff': [p,s,u,u,p,s,p],
            'crsi_encode_03ff': [p,s,u,u,p,s,p],
            'crsi_encode_0575': [p,s,u,u,i,p,s,p,s,p,p,s],
        }
        for name, args in signatures.items():
            fn = getattr(self.library, name)
            fn.argtypes, fn.restype = args, i
        for suffix in ('03ff', '0575'):
            fn = getattr(self.library, 'crsi_bound_' + suffix)
            fn.argtypes, fn.restype = [u,u], s

    @staticmethod
    def _dimensions(width: int, height: int) -> int:
        if not 0 < width <= 4096 or not 0 < height <= 4096:
            raise ValueError('invalid CRsi dimensions')
        return width * height * 4

    @staticmethod
    def _check(code: int) -> None:
        if code:
            raise ValueError(f'C CRsi codec rejected input ({code})')

    def decode(self, frame: Frame, width: int, height: int,
               previous: bytes | None = None) -> tuple[bytes, int]:
        """Return top-down native BGRX and consumed bits; never treat X as alpha."""
        size = self._dimensions(width, height)
        target = c.create_string_buffer(size)
        bits = c.c_size_t()
        if ((frame.mode == 0x0575 and frame.parameter == 8) or
            (frame.mode in (0x56d,0x52c,0x524) and frame.parameter == 32767)):
            if not frame.independent:
                if previous is None or len(previous) != size:
                    raise ValueError('dependent frame requires the previous native surface')
                target.raw = previous
            code = self.library.crsi_decode_codec1(frame.payload, len(frame.payload),
                width, height, frame.independent, frame.mode, frame.parameter, target, size, c.byref(bits))
        elif frame.mode == 0x03ff and frame.parameter is None and frame.independent:
            code = self.library.crsi_decode_03ff(frame.payload, len(frame.payload),
                width, height, target, size, c.byref(bits))
        else:
            raise ValueError('unsupported scoped CRsi codec profile')
        self._check(code)
        return target.raw, bits.value

    def encode_lossless(self, rgb: bytes, width: int, height: int) -> Frame:
        self._dimensions(width, height)
        if len(rgb) != width * height * 3:
            raise ValueError('RGB size mismatch')
        bound = self.library.crsi_bound_03ff(width, height)
        if not bound:
            raise ValueError('dimensions outside scalar profile')
        target, written = c.create_string_buffer(bound), c.c_size_t()
        self._check(self.library.crsi_encode_03ff(rgb, len(rgb), width, height,
                    target, bound, c.byref(written)))
        return Frame(1,0,0,0x03ff,None,target.raw[:written.value])

    def encode_lossy(self, rgb: bytes, width: int, height: int,
                     previous: bytes | None = None) -> tuple[Frame, bytes]:
        """Research writer; returned reconstruction must drive temporal feedback."""
        size = self._dimensions(width, height)
        if len(rgb) != width * height * 3 or (previous is not None and len(previous) != size):
            raise ValueError('RGB or previous surface size mismatch')
        bound = self.library.crsi_bound_0575(width, height)
        if not bound:
            raise ValueError('dimensions outside codec-1 profile')
        target, surface, written = c.create_string_buffer(bound), c.create_string_buffer(size), c.c_size_t()
        self._check(self.library.crsi_encode_0575(rgb, len(rgb), width, height,
            previous is None, previous, 0 if previous is None else len(previous),
            target, bound, c.byref(written), surface, size))
        return Frame(int(previous is None),0,0,0x0575,8,target.raw[:written.value]), surface.raw


def native_to_rgb(bgrx: bytes) -> bytes:
    if len(bgrx) % 4:
        raise ValueError('unaligned BGRX surface')
    rgb = bytearray(len(bgrx)//4*3)
    rgb[0::3], rgb[1::3], rgb[2::3] = bgrx[2::4], bgrx[1::4], bgrx[0::4]
    return bytes(rgb)
