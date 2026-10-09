"""Offline x86 oracle using a user's version-locked PM executable.

No executable entry point, OS process, imported game DLL, or game save is
opened. Unicorn executes only two lookup initializers and audited leaf pixel
decoders. Native memset is the sole emulated external operation. This tool is
research infrastructure, not a component required in the player patch.
"""
from __future__ import annotations

import hashlib
from pathlib import Path
import struct

from rUGP.formats.video.crsi import Frame

PM_EXE_SHA256 = '8e442f263feed7b79e5ccb83c3f26b12cc12e1953fb4a262b4bb74017d6e26b8'


class NativeCrsiDecoder:
    def __init__(self, executable: Path):
        # Optional dependencies remain outside the normal format-test suite.
        import pefile
        import unicorn as uc
        from unicorn import x86_const as x86

        data = executable.read_bytes()
        if hashlib.sha256(data).hexdigest() != PM_EXE_SHA256:
            raise ValueError('unsupported PM executable identity')
        pe = pefile.PE(data=data)
        if pe.OPTIONAL_HEADER.ImageBase != 0x400000:
            raise ValueError('unexpected PM image base')
        self.x86 = x86
        self.u = u = uc.Uc(uc.UC_ARCH_X86, uc.UC_MODE_32)
        u.mem_map(0x400000, 0x400000)
        u.mem_write(0x400000, pe.get_memory_mapped_image())
        u.mem_map(0x1000000, 0x2000000)
        self.dimensions = None

        def memset(machine, _address, _size, _context):
            sp = machine.reg_read(x86.UC_X86_REG_ESP)
            ret, dest, value, count = struct.unpack('<4I', machine.mem_read(sp, 16))
            if not (0x1000000 <= dest <= dest + count <= 0x3000000 and count <= 16_777_216):
                raise ValueError('native memset exceeds emulated work memory')
            machine.mem_write(dest, bytes([value & 255]) * count)
            machine.reg_write(x86.UC_X86_REG_EAX, dest)
            machine.reg_write(x86.UC_X86_REG_ESP, sp + 4)
            machine.reg_write(x86.UC_X86_REG_EIP, ret)

        u.hook_add(uc.UC_HOOK_CODE, memset, begin=0x5fc508, end=0x5fc508)
        self._call(0x403600, [])
        self._call(0x403a20, [])

    def _call(self, entry: int, arguments: list[int]) -> None:
        self.u.mem_write(0x2f00000, struct.pack('<' + 'I'*(len(arguments)+1), 0x2ff0000, *arguments))
        self.u.reg_write(self.x86.UC_X86_REG_ESP, 0x2f00000)
        self.u.emu_start(entry, 0x2ff0000, timeout=20_000_000, count=100_000_000)
        if self.u.reg_read(self.x86.UC_X86_REG_EIP) != 0x2ff0000:
            raise ValueError('native decoder did not return within its execution limit')

    def decode(self, frame: Frame, width: int, height: int) -> bytes:
        """Return top-down RGB; decode dependent frames in original order.

        The fourth native byte is discarded, not interpreted as PNG alpha.
        The original mode's high bytes are not a uniform transparency plane.
        """
        if not (0 < width <= 4096 and 0 < height <= 4096 and width*height <= 2_097_152):
            raise ValueError('dimensions exceed this oracle memory layout')
        if not 0 < len(frame.payload) < 0x400000 - 32:
            raise ValueError('payload exceeds this oracle memory layout')
        if not frame.independent and self.dimensions != (width, height):
            raise ValueError('dependent frame requires a preceding decoded surface')
        self.u.mem_write(0x1000000, frame.payload + bytes(32))
        args = [0x1800000+(height-1)*width*4, width*4, 0, width | (height << 16)]
        if frame.mode == 0x575 and frame.parameter == 8:
            if width % 2 or height % 2:
                raise ValueError('observed codec-1 requires even dimensions')
            self.u.mem_write(0x1400000, bytes.fromhex('0001000106070600010008000000'))
            self._call(0x5b8ad0 if frame.independent else 0x5b9450, [0x1000000, 0x1400000, *args])
        elif frame.mode == 0x16d and frame.parameter is None and frame.independent:
            self.u.mem_write(0x1400000, bytes.fromhex('0001000106060600010000000000'))
            self.u.reg_write(self.x86.UC_X86_REG_ECX, 0x1000000)
            self.u.reg_write(self.x86.UC_X86_REG_EDX, 0x1400000)
            self._call(0x579b30, args)
        else:
            raise ValueError('frame is outside the verified native decoder profiles')
        self.dimensions = (width, height)
        from PIL import Image
        raw = bytes(self.u.mem_read(0x1800000, width*height*4))
        return Image.frombytes('RGB', (width, height), raw, 'raw', 'BGRX', 0, -1).tobytes()
