"""Replay every frame of an encoded CRsi candidate through PM's native leaves.

This is an offline codec/table check, not a streaming or in-game playback test.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import time

from rUGP.formats.video.crsi import parse
from .native_crsi import NativeCrsiDecoder, PM_EXE_SHA256
from .native_crsi_table import verify_tables


def verify(executable: Path, candidate: Path, build_report: Path, output: Path) -> dict:
    if output.exists():
        raise FileExistsError(output)
    report_bytes = build_report.read_bytes()
    expected = json.loads(report_bytes)
    if expected.get('schema') != 'photon-crsi-replacement/1':
        raise ValueError('unsupported build report')
    data = candidate.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    if digest != expected['output_sha256']:
        raise ValueError('candidate differs from build report')
    sequence = parse(data)
    del data
    hashes = expected['target_rgb_sha256']
    if len(sequence.frames) != expected['frame_count'] or len(hashes) != len(sequence.frames):
        raise ValueError('candidate and report frame counts differ')
    started = time.perf_counter()
    tables = verify_tables(executable, [candidate])
    oracle = NativeCrsiDecoder(executable)
    modes = {}
    for index, frame in enumerate(sequence.frames):
        actual = oracle.decode(frame, sequence.width, sequence.height)
        if hashlib.sha256(actual).hexdigest() != hashes[index]:
            raise ValueError(f'native RGB differs from edited video at frame {index}')
        mode = f'0x{frame.mode:04x}'
        modes[mode] = modes.get(mode, 0) + 1
        if (index + 1) % 100 == 0:
            print(f'Native RGB exact: {index + 1}/{len(sequence.frames)}', flush=True)
    result = dict(
        schema='photon-crsi-replacement-native/1',
        validation='all native RGB frames and frame-table rows match; offline only',
        candidate_sha256=digest, build_report_sha256=hashlib.sha256(report_bytes).hexdigest(),
        executable_sha256=PM_EXE_SHA256, frame_count=len(sequence.frames),
        modes=modes, tables=tables, seconds=time.perf_counter()-started,
        limitations=['No game process or streaming IO exercised',
                     'Pixel equality does not establish translation or visual acceptance'])
    with output.open('x', encoding='utf-8') as stream:
        json.dump(result, stream, indent=2)
        stream.write('\n')
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('executable', 'candidate', 'build_report', 'output'):
        parser.add_argument(name, type=Path)
    args = parser.parse_args()
    print(json.dumps(verify(args.executable, args.candidate, args.build_report, args.output), indent=2))


if __name__ == '__main__':
    main()
