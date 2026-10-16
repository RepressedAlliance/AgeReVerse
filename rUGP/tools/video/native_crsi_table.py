"""Check complete scoped CRsi frame tables with PM's native deserializer.

The original parent, row reader and row initialization execute in Unicorn.
MFC's short ReadCount, memory allocation and archive-relative GetPosition
are explicit stubs. No streaming IO or game process is executed.
"""
from __future__ import annotations

from pathlib import Path
import hashlib
import struct

from rUGP.formats.video.crsi import parse
from rUGP.tools.video.native_crsi import NativeCrsiDecoder


def verify_tables(executable: Path, records: list[Path]) -> dict:
    import unicorn as uc

    oracle = NativeCrsiDecoder(executable)
    u, x86 = oracle.u, oracle.x86
    archive, obj, buf, rows = 0x1600000, 0x1601000, 0x1610000, 0x1700000
    vtable, count_stub, position_stub = 0x1602000, 0x1603000, 0x1603010

    def words(address, *values):
        u.mem_write(address, struct.pack('<' + 'I' * len(values), *values))

    def uint(address):
        return struct.unpack('<I', u.mem_read(address, 4))[0]

    def require(condition, message):
        if not condition:
            raise ValueError(message)

    def return_value(value, argument_bytes=0):
        sp = u.reg_read(x86.UC_X86_REG_ESP)
        u.reg_write(x86.UC_X86_REG_EAX, value)
        u.reg_write(x86.UC_X86_REG_ESP, sp + 4 + argument_bytes)
        u.reg_write(x86.UC_X86_REG_EIP, uint(sp))

    def read_count(_machine, _address, _size, _context):
        require(u.reg_read(x86.UC_X86_REG_ECX) == archive + 8, 'unexpected count archive')
        cursor = uint(archive + 0x30)
        require(buf <= cursor <= uint(archive + 0x34) - 2, 'count outside table')
        value = struct.unpack('<H', u.mem_read(cursor, 2))[0]
        require(value < 0xffff, 'extended MFC count is outside this probe')
        words(archive + 0x30, cursor + 2)
        return_value(value)

    def position(_machine, _address, _size, _context):
        require(u.reg_read(x86.UC_X86_REG_ECX) == archive, 'unexpected position archive')
        return_value(uint(archive + 0x30) - buf)

    def allocation(_machine, _address, _size, _context):
        require(u.reg_read(x86.UC_X86_REG_ECX) == obj + 0x34, 'unexpected row allocator')
        length = uint(u.reg_read(x86.UC_X86_REG_ESP) + 4)
        require(0 < length < 0x100000, 'row allocation exceeds work memory')
        u.mem_write(rows, bytes(length))
        words(obj + 0x38, rows)
        return_value(1, 4)

    words(0x6189f4, count_stub)
    u.mem_write(count_stub, b'\xc3')
    u.mem_write(position_stub, b'\xc3')
    u.hook_add(uc.UC_HOOK_CODE, read_count, begin=count_stub, end=count_stub)
    u.hook_add(uc.UC_HOOK_CODE, position, begin=position_stub, end=position_stub)
    u.hook_add(uc.UC_HOOK_CODE, allocation, begin=0x5bfe10, end=0x5bfe10)
    reports = []
    for path in records:
        data = path.read_bytes()
        seq = parse(data)
        table_end = len(data) - sum(len(frame.payload) for frame in seq.frames)
        require(table_end < rows - buf, 'frame table exceeds work memory')
        u.mem_write(archive, bytes(256))
        u.mem_write(obj, bytes(256))
        words(archive, vtable)
        words(vtable + 8, position_stub)
        words(archive + 0x20, 1)
        words(archive + 0x30, buf + 2, buf + table_end)
        u.mem_write(buf, data[:table_end])
        u.reg_write(x86.UC_X86_REG_ECX, obj)
        oracle._call(0x5830f0, [archive])
        require(uint(obj + 0x44) == len(seq.frames), 'native frame count differs')
        require(uint(obj + 0x2c) == table_end, 'native payload start differs')
        require(uint(archive + 0x30) == buf + table_end, 'native cursor differs')
        require(struct.unpack('<HH', u.mem_read(obj + 0x24, 4)) == (seq.width, seq.height),
                'native dimensions differ')
        require(struct.unpack('<H', u.mem_read(obj + 0x16, 2))[0] == seq.rate,
                'native rate differs')
        for index, frame in enumerate(seq.frames):
            row = bytes(u.mem_read(rows + index * 36, 36))
            require(row[1] == frame.flags, f'frame {index}: native flags differ')
            require(struct.unpack_from('<II', row, 4) ==
                    (table_end + frame.offset, len(frame.payload)),
                    f'frame {index}: native address or size differs')
            require(struct.unpack_from('<H', row, 14)[0] == frame.mode,
                    f'frame {index}: native mode differs')
            if frame.parameter is not None:
                require(struct.unpack_from('<H', row, 16)[0] == frame.parameter,
                        f'frame {index}: native parameter differs')
        reports.append(dict(record=path.name, sha256=hashlib.sha256(data).hexdigest(),
                            frames=len(seq.frames), table_end=table_end,
                            dimensions=[seq.width, seq.height], rate=seq.rate,
                            all_native_rows_match=True))
    return dict(validation='offline parent and row deserialization; no game process',
                native_entry='0x5830f0', native_row_entry='0x582c70',
                stubs=['MFC ReadCount: observed 16-bit count',
                       'buffer allocation: bounded zero-filled memory',
                       'archive position: cursor relative to record start'], records=reports)


def main() -> None:
    import argparse
    import json

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--executable', required=True, type=Path)
    parser.add_argument('records', nargs='+', type=Path)
    args = parser.parse_args()
    print(json.dumps(verify_tables(args.executable, args.records), indent=2))


if __name__ == '__main__':
    main()
