"""Observed schema-1 Photon CRsi records, including variable-width frame rows.

This is deliberately not a generic video container reader. The 26-byte parent
profile is locked to the four investigated PM Rebirth sequences. A codec-1
row carries a two-byte parameter; codec-0 rows do not. Payloads remain opaque.
"""
from __future__ import annotations

from dataclasses import dataclass
import struct


@dataclass(frozen=True)
class Frame:
    flags: int
    offset: int
    reserved: int
    mode: int
    parameter: int | None
    payload: bytes

    @property
    def independent(self) -> bool:
        return bool(self.flags & 1)


@dataclass(frozen=True)
class Sequence:
    header: bytes
    width: int
    height: int
    rate: int
    frames: tuple[Frame, ...]


def parse(data: bytes) -> Sequence:
    if len(data) < 26:
        raise ValueError('truncated CRsi header')
    if data[:10] != bytes.fromhex('00010100000000000000'):
        raise ValueError('unrecognized scoped CRsi header')
    width, height = struct.unpack_from('<HH', data, 10)
    rate = struct.unpack_from('<H', data, 18)[0]
    count = struct.unpack_from('<H', data, 24)[0]
    if data[14:18] != bytes(4) or data[20:24] != bytes(4):
        raise ValueError('unsupported CRsi parent flags or timing extension')
    if not (0 < width <= 4096 and 0 < height <= 4096 and width * height <= 16777216):
        raise ValueError('invalid CRsi dimensions')
    if not rate or not 0 < count < 0xffff:
        raise ValueError('unsupported CRsi rate or frame count')
    pos = 26
    rows = []
    for _ in range(count):
        if pos + 9 > len(data):
            raise ValueError('truncated CRsi frame row')
        flags, offset, reserved, mode = struct.unpack_from('<BIHH', data, pos)
        pos += 9
        codec = (mode >> 10) & 7
        if flags not in (0, 1) or reserved or mode & ~0x05ff or codec not in (0, 1):
            raise ValueError('unsupported CRsi frame flags, address extension or codec')
        parameter = None
        if codec == 1:
            if pos + 2 > len(data):
                raise ValueError('truncated CRsi codec parameter')
            parameter = struct.unpack_from('<H', data, pos)[0]
            pos += 2
        if pos + 4 > len(data):
            raise ValueError('truncated CRsi payload length')
        size = struct.unpack_from('<I', data, pos)[0]
        pos += 4
        if not size or size > 16_777_216:
            raise ValueError('invalid CRsi frame payload length')
        rows.append((flags, offset, reserved, mode, parameter, size))
    end = 0
    frames = []
    for flags, offset, reserved, mode, parameter, size in rows:
        if offset != end or pos + offset + size > len(data):
            raise ValueError('CRsi frame payloads are not contiguous and bounded')
        frames.append(Frame(flags, offset, reserved, mode, parameter, data[pos+offset:pos+offset+size]))
        end = offset + size
    if pos + end != len(data):
        raise ValueError('unaccounted CRsi trailing bytes')
    if not frames[0].independent:
        raise ValueError('CRsi sequence starts with a dependent frame')
    return Sequence(data[:26], width, height, rate, tuple(frames))


def rebuild(sequence: Sequence, replacements: dict[int, Frame]) -> bytes:
    """Replace frames without changing count/timing; require dependency closure.

    After a replaced frame, original dependent frames cannot be reused until
    the next original independent frame. Their predictor would be different.
    """
    if any(not 0 <= i < len(sequence.frames) for i in replacements):
        raise ValueError('replacement index outside CRsi sequence')
    dirty = False
    frames = []
    for i, original in enumerate(sequence.frames):
        if original.independent:
            dirty = False
        if i in replacements:
            candidate = replacements[i]
            if not candidate.independent:
                raise ValueError('replacement must be an independently coded frame')
            dirty = True
            frames.append(candidate)
        else:
            if dirty:
                raise ValueError(f'replacement leaves original dependent frame {i}')
            frames.append(original)
    table = bytearray()
    payload = bytearray()
    for frame in frames:
        table.extend(struct.pack('<BIHH', frame.flags, len(payload), frame.reserved, frame.mode))
        if ((frame.mode >> 10) & 7) == 1:
            if frame.parameter is None:
                raise ValueError('codec-1 row needs a parameter')
            table.extend(struct.pack('<H', frame.parameter))
        elif frame.parameter is not None:
            raise ValueError('codec-0 row cannot carry a parameter')
        table.extend(struct.pack('<I', len(frame.payload)))
        payload.extend(frame.payload)
    result = sequence.header + table + payload
    parse(result)
    return result
