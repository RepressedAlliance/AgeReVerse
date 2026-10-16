"""Offline, version-locked oracle for PM's RUO address resolver.

Executes audited address/hash functions and the stream caller's range-argument
preparation in Unicorn. Archive objects and hash buckets are synthetic;
redirect values come from the supplied RUO. Full caller lifecycle and file IO
are outside this oracle.
"""
from __future__ import annotations

import hashlib
from pathlib import Path
import struct

from rUGP.formats.rio.crypto import EXTENT_OFFSET_BIAS, EXTENT_SIZE_BIAS, encode_extent_size
from rUGP.formats.rio.ruo import Redirect
from rUGP.tools.video.native_crsi import PM_EXE_SHA256


class NativeRuoResolver:
    ARCHIVE = 0x1000000
    NODE = 0x1001000
    OUTPUT = 0x1002000
    VOLUMES = 0x1003000
    VOLUME = 0x1004000
    FILE_VIEW = 0x1005000
    BUCKETS = 0x1010000
    ENTRIES = 0x1020000
    STACK = 0x12f0000
    RETURN = 0x12ff000

    def __init__(self, executable: Path, redirects: list[Redirect]):
        import pefile
        import unicorn as uc
        from unicorn import x86_const as x86

        data = executable.read_bytes()
        if hashlib.sha256(data).hexdigest() != PM_EXE_SHA256:
            raise ValueError('unsupported PM executable identity')
        if len(redirects) > 4096:
            raise ValueError('redirect table exceeds oracle work memory')
        if len({r.source_raw_offset for r in redirects}) != len(redirects):
            raise ValueError('duplicate redirect source')
        self.x86 = x86
        self.u = u = uc.Uc(uc.UC_ARCH_X86, uc.UC_MODE_32)
        u.mem_map(0, 0x1000)  # Local SEH chain; no OS exception machinery.
        u.mem_map(0x400000, 0x400000)
        u.mem_write(0x400000, pefile.PE(data=data).get_memory_mapped_image())
        u.mem_map(0x1000000, 0x300000)
        self._words(0x6c3e40, EXTENT_OFFSET_BIAS, EXTENT_SIZE_BIAS)
        self._words(self.ARCHIVE + 0xe4, 0x6c3de4)
        self._words(self.ARCHIVE + 0x54, self.VOLUMES, 2)
        self._words(self.VOLUMES, 0, self.VOLUME)
        bucket_count = 17
        self._words(self.ARCHIVE + 0xec, self.BUCKETS, bucket_count)
        buckets = [0] * bucket_count
        for index, redirect in enumerate(redirects):
            entry = self.ENTRIES + index * 24
            key = redirect.source_raw_offset
            bucket = (key >> 4) % bucket_count
            # CMap node: separate lookup key, 12-byte value, next, hash.
            self._words(entry, key, key, redirect.ruo_raw_offset,
                        redirect.replacement_raw_size, buckets[bucket], key >> 4)
            buckets[bucket] = entry
        self._words(self.BUCKETS, *buckets)

        def restrict_execution(_machine, address, _size, _context):
            allowed = ((0x5d9de0, 0x5d9f57), (0x5df070, 0x5df0ca),
                       (0x5de2f3, 0x5de30b), (0x5fc7f0, 0x5fc811),
                       (0x5f4040, 0x5f40c3), (0x5dea1c, 0x5deb05),
                       (0x430dd0, 0x430dee), (0x5d6060, 0x5d6102),
                       (0x1100300, 0x1100308))
            if not any(start <= address < end for start, end in allowed):
                raise ValueError(f'unexpected native control flow: {address:#x}')

        u.hook_add(uc.UC_HOOK_CODE, restrict_execution)

    def _words(self, address: int, *values: int) -> None:
        self.u.mem_write(address, struct.pack('<' + 'I' * len(values), *values))

    def _run(self, start: int, end: int) -> None:
        self.u.emu_start(start, end, timeout=1_000_000, count=100_000)
        if self.u.reg_read(self.x86.UC_X86_REG_EIP) != end:
            raise ValueError('native resolver did not return within limit')

    def volume_base_units(self, *, patched: bool) -> int:
        """Run the original/patched loader's base calculation with unit size 4."""
        self.u.mem_write(0x5de302, b'\xff' if patched else b'\x7f')
        self._words(self.ARCHIVE + 0x1c, 2)
        self.u.reg_write(self.x86.UC_X86_REG_EBX, self.ARCHIVE)
        self.u.reg_write(self.x86.UC_X86_REG_ESP, self.STACK)
        self._run(0x5de2f3, 0x5de30b)
        return (self.u.reg_read(self.x86.UC_X86_REG_EDX) << 32 |
                self.u.reg_read(self.x86.UC_X86_REG_EAX))

    def resolve(self, source_key: int, original_units: int, original_size: int,
                volume_base_units: int, *, enabled: bool = True,
                volume_index: int = 1) -> tuple[bool, int, int]:
        if not (0 <= source_key <= 0xffffffff and 0 <= original_size <= 0xffffffff
                and 0 <= original_units <= 0xffffffffffffffff
                and 0 <= volume_base_units <= 0xffffffffffffffff
                and 0 <= volume_index <= 0xffffffff):
            raise ValueError('argument outside native integer bounds')
        self.u.mem_write(self.ARCHIVE + 0xc8, bytes([enabled]))
        self._words(self.ARCHIVE + 0xcc, volume_index)
        self.u.mem_write(self.VOLUME + 0x60, struct.pack('<Q', volume_base_units))
        self._words(self.NODE + 0x20, source_key)
        self.u.mem_write(self.OUTPUT, struct.pack('<QI', original_units, original_size))
        self._words(self.STACK, self.RETURN, self.NODE, self.OUTPUT, self.OUTPUT + 8)
        self.u.reg_write(self.x86.UC_X86_REG_ESP, self.STACK)
        self.u.reg_write(self.x86.UC_X86_REG_ECX, self.ARCHIVE)
        self._run(0x5d9de0, self.RETURN)
        offset, size = struct.unpack('<QI', self.u.mem_read(self.OUTPUT, 12))
        return bool(self.u.reg_read(self.x86.UC_X86_REG_EAX)), offset, size

    def relative_position(self, start: int, size: int, relative: int) -> int:
        """Native bounded-file GetPosition, using its unbuffered branch."""
        if not (0 <= start <= start + size <= 0x7fffffffffffffff
                and 0 <= relative <= size):
            raise ValueError('invalid file-view range')
        self.u.mem_write(self.FILE_VIEW, bytes(0x50))
        self.u.mem_write(self.FILE_VIEW + 0x14, b'\x01')
        self.u.mem_write(self.FILE_VIEW + 0x18, struct.pack('<QQ', start, start + size))
        self.u.mem_write(self.FILE_VIEW + 0x40, struct.pack('<Q', start + relative))
        self._words(self.STACK, self.RETURN)
        self.u.reg_write(self.x86.UC_X86_REG_ESP, self.STACK)
        self.u.reg_write(self.x86.UC_X86_REG_ECX, self.FILE_VIEW)
        self._run(0x5f4040, self.RETURN)
        return (self.u.reg_read(self.x86.UC_X86_REG_EDX) << 32 |
                self.u.reg_read(self.x86.UC_X86_REG_EAX))

    def caller_extent(self, source_key: int, original_size: int,
                      volume_base_units: int) -> tuple[int, int]:
        """Run the native stream caller through its bounded-file arguments.

        Starts at 0x5dea1c, after file creation. An already-loaded archive
        handle and a positive CFile runtime-type check are explicit stubs.
        Stops at 0x5deb00 before SetRange/Seek: no file IO is executed.
        """
        if not (0 <= source_key <= 0xffffffff and 0 < original_size <= 0xffffffff
                and 0 <= volume_base_units <= 0xffffffffffffffff):
            raise ValueError('argument outside native integer bounds')
        handle, type_check = 0x1100000, 0x1100300
        frame_base = self.STACK - 0x200
        self.u.mem_write(handle, bytes(0x40))
        self._words(handle, self.ARCHIVE)
        self.u.mem_write(handle + 0x1c, b'\x04')  # already loaded handle
        self._words(self.ARCHIVE + 0x1c, 2)  # 4-byte allocation units
        self.u.mem_write(self.ARCHIVE + 0xc8, b'\x01')
        self._words(self.ARCHIVE + 0xcc, 1)
        self.u.mem_write(self.VOLUME + 0x60, struct.pack('<Q', volume_base_units))
        self._words(self.NODE + 0x20, source_key, encode_extent_size(original_size))
        self.u.mem_write(type_check, b'\xb8\x01\x00\x00\x00\xc2\x04\x00')
        self._words(0x618d58, type_check)
        self.u.mem_write(frame_base - 0x100, bytes(0x200))
        self._words(frame_base + 0xc, handle, 0, 0, self.FILE_VIEW)
        self.u.reg_write(self.x86.UC_X86_REG_EBP, frame_base)
        self.u.reg_write(self.x86.UC_X86_REG_ESP, frame_base - 0x80)
        self.u.reg_write(self.x86.UC_X86_REG_EBX, self.NODE)
        self._run(0x5dea1c, 0x5deb00)
        if self.u.reg_read(self.x86.UC_X86_REG_ECX) != self.FILE_VIEW:
            raise ValueError('native caller selected an unexpected bounded file')
        stack = self.u.reg_read(self.x86.UC_X86_REG_ESP)
        return struct.unpack('<QQ', self.u.mem_read(stack, 16))


def verify(executable: Path, ruo: Path, selected_key: int, *, original_size: int = 456) -> dict:
    """Compare all footer entries against native lookup and address arithmetic."""
    from rUGP.formats.rio.crypto import decode_extent_offset, decode_extent_size
    from rUGP.formats.rio.ruo import read_footer

    _, redirects = read_footer(ruo, 4)
    selected = next((r for r in redirects if r.source_raw_offset == selected_key), None)
    if selected is None:
        raise ValueError('selected video key is absent from RUO')
    oracle = NativeRuoResolver(executable, redirects)
    original_base = oracle.volume_base_units(patched=False)
    patched_base = oracle.volume_base_units(patched=True)
    if (original_base * 4, patched_base * 4) != (6 << 30, 8 << 30):
        raise ValueError('native volume base differs from expected PM loader')
    for redirect in redirects:
        offset = decode_extent_offset(redirect.ruo_raw_offset, 4) // 4
        size = decode_extent_size(redirect.replacement_raw_size)
        actual = oracle.resolve(redirect.source_raw_offset, 123, 456, patched_base)
        if actual != (True, patched_base + offset, size):
            raise ValueError(f'native redirect mismatch: {redirect.source_raw_offset:#x}')
    missing = 0
    keys = {r.source_raw_offset for r in redirects}
    while missing in keys:
        missing += 1
    if oracle.resolve(missing, 123, 456, patched_base) != (True, 123, 456):
        raise ValueError('missing-key fallback changed original address')
    if oracle.resolve(selected_key, 123, 456, patched_base, enabled=False) != (True, 123, 456):
        raise ValueError('disabled overlay changed original address')
    for index in (0, 2):
        if oracle.resolve(selected_key, 123, 456, patched_base, volume_index=index)[0]:
            raise ValueError('invalid volume index was accepted')
    local_offset = decode_extent_offset(selected.ruo_raw_offset, 4)
    selected_size = decode_extent_size(selected.replacement_raw_size)
    # An arithmetic boundary case in addition to the actual PM 8 GiB base.
    carry_base = 0xffffffff
    if oracle.resolve(selected_key, 123, 456, carry_base) != (
            True, carry_base + local_offset // 4, selected_size):
        raise ValueError('64-bit carry check failed')
    virtual_start = patched_base * 4 + local_offset
    positions = [0, 26, selected_size // 2, selected_size]
    for relative in positions:
        if oracle.relative_position(virtual_start, selected_size, relative) != relative:
            raise ValueError('native bounded-file relative position mismatch')
    # The real caller decodes the old size, applies the redirect, shifts units
    # to bytes, and passes the replacement's full range to the bounded file.
    caller_range = oracle.caller_extent(selected_key, original_size, patched_base)
    if caller_range != (virtual_start, virtual_start + selected_size):
        raise ValueError('native stream caller produced a wrong bounded-file range')
    return {
        'validation': 'offline native resolver and stream-range arguments; synthetic archive and hash objects',
        'limitations': ['does not execute the complete video caller, file IO, rendering or game process'],
        'executable_sha256': PM_EXE_SHA256,
        'resolver_entry': '0x5d9de0',
        'hash_lookup_entry': '0x5df070',
        'base_calculation_range': ['0x5de2f3', '0x5de30b'],
        'unit_size': 4,
        'original_volume_base_bytes': original_base * 4,
        'patched_volume_base_bytes': patched_base * 4,
        'redirects_checked': len(redirects),
        'all_native_addresses_and_sizes_match': True,
        'missing_key_preserves_original': True,
        'disabled_overlay_preserves_original': True,
        'invalid_volume_indices_rejected': [0, 2],
        '64_bit_addition_carry_verified': True,
        'native_file_position_entry': '0x5f4040',
        'unbuffered_relative_positions_verified': positions,
        'selected_source_key': f'0x{selected_key:08x}',
        'selected_ruo_byte_offset': local_offset,
        'selected_virtual_byte_offset': patched_base * 4 + local_offset,
        'selected_size': selected_size,
        'native_stream_caller_range': {
            'executed': ['0x5dea1c', '0x5deb00'],
            'start': caller_range[0], 'end': caller_range[1],
            'original_size_input': original_size,
            'replacement_size_used': True,
            'stubs': ['already-loaded archive handle', 'positive CFile runtime-type check'],
            'limitation': 'Starts after file creation; stops before bounded-file SetRange/Seek',
        },
    }


def main() -> None:
    import argparse
    import json

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--executable', required=True, type=Path)
    parser.add_argument('--ruo', required=True, type=Path)
    parser.add_argument('--source-key', required=True, type=lambda value: int(value, 0))
    parser.add_argument('--original-size', type=lambda value: int(value, 0), default=456,
                        help='original extent length; default 456 is a synthetic override witness')
    args = parser.parse_args()
    print(json.dumps(verify(args.executable, args.ruo, args.source_key,
                            original_size=args.original_size), indent=2))


if __name__ == '__main__':
    main()
