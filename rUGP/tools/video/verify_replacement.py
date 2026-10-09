"""Verify an encoded CRsi candidate through PM's native leaves.

This is an offline codec/table check, not a streaming or in-game playback test.
An explicitly supplied, fully replayed baseline can cover identical frames;
changed frames must be independent and leave no dependent frame to reuse.
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


def reusable_indices(previous, current, old_hashes, new_hashes) -> set[int]:
    """Prove which baseline surfaces can be reused, ignoring relocated offsets.

    Native table verification separately checks every new payload offset.
    Reject changes that would require carrying an altered predictor into a
    reused frame; full replay remains available for those changes.
    """
    if previous.header != current.header or len(previous.frames) != len(current.frames):
        raise ValueError('baseline header or frame count differs')
    if len(old_hashes) != len(previous.frames) or len(new_hashes) != len(current.frames):
        raise ValueError('baseline or candidate hash count differs')
    reusable, dirty = set(), False
    for index, (old, new) in enumerate(zip(previous.frames, current.frames)):
        if new.independent:
            dirty = False
        same = (old.flags, old.reserved, old.mode, old.parameter, old.payload) == (
            new.flags, new.reserved, new.mode, new.parameter, new.payload)
        if same:
            if dirty:
                raise ValueError(f'baseline reuse leaves altered dependency at frame {index}')
            if old_hashes[index] != new_hashes[index]:
                raise ValueError(f'identical frame has different target RGB at frame {index}')
            reusable.add(index)
        else:
            if not new.independent:
                raise ValueError(f'changed dependent frame {index} requires full replay')
            dirty = True
    return reusable


def verify(executable: Path, candidate: Path, build_report: Path, output: Path,
           *, baseline: Path | None = None, baseline_build: Path | None = None,
           baseline_native: Path | None = None) -> dict:
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
    reusable, reuse_evidence = set(), None
    if any(path is not None for path in (baseline, baseline_build, baseline_native)):
        if any(path is None for path in (baseline, baseline_build, baseline_native)):
            raise ValueError('baseline resource, build report and full native report are all required')
        old_data, old_build_bytes, old_native_bytes = (
            path.read_bytes() for path in (baseline, baseline_build, baseline_native))
        old_build, old_native = json.loads(old_build_bytes), json.loads(old_native_bytes)
        old_digest = hashlib.sha256(old_data).hexdigest()
        if (old_build.get('schema') != 'photon-crsi-replacement/1'
                or old_native.get('schema') != 'photon-crsi-replacement-native/1'
                or old_native.get('validation') != 'all native RGB frames and frame-table rows match; offline only'
                or old_digest != old_build.get('output_sha256')
                or old_digest != old_native.get('candidate_sha256')
                or hashlib.sha256(old_build_bytes).hexdigest() != old_native.get('build_report_sha256')
                or old_native.get('executable_sha256') != PM_EXE_SHA256
                or old_native.get('frame_count') != len(sequence.frames)
                or old_build.get('frame_count') != len(sequence.frames)):
            raise ValueError('baseline is not bound to a full native verification')
        reusable = reusable_indices(parse(old_data), sequence,
                                    old_build['target_rgb_sha256'], hashes)
        reuse_evidence = dict(candidate_sha256=old_digest,
                             build_report_sha256=hashlib.sha256(old_build_bytes).hexdigest(),
                             native_report_sha256=hashlib.sha256(old_native_bytes).hexdigest(),
                             identical_frames=len(reusable))
        del old_data
    started = time.perf_counter()
    tables = verify_tables(executable, [candidate])
    oracle = NativeCrsiDecoder(executable)
    modes = {}
    decoded = 0
    for index, frame in enumerate(sequence.frames):
        if index not in reusable:
            actual = oracle.decode(frame, sequence.width, sequence.height)
            if hashlib.sha256(actual).hexdigest() != hashes[index]:
                raise ValueError(f'native RGB differs from edited video at frame {index}')
            decoded += 1
            if decoded % 50 == 0:
                print(f'Native RGB exact: {decoded}/{len(sequence.frames)-len(reusable)} decoded', flush=True)
        mode = f'0x{frame.mode:04x}'
        modes[mode] = modes.get(mode, 0) + 1
    result = dict(
        schema='photon-crsi-replacement-native/1',
        validation='all native RGB frames and frame-table rows match; offline only',
        candidate_sha256=digest, build_report_sha256=hashlib.sha256(report_bytes).hexdigest(),
        executable_sha256=PM_EXE_SHA256, frame_count=len(sequence.frames),
        modes=modes, tables=tables, seconds=time.perf_counter()-started,
        limitations=['No game process or streaming IO exercised',
                     'Pixel equality does not establish translation or visual acceptance'])
    if reuse_evidence is not None:
        result.update(schema='photon-crsi-replacement-native-reuse/1',
                      validation='changed native RGB frames and all new table rows match; identical baseline frames reused',
                      native_decoded_frames=decoded, baseline=reuse_evidence)
    with output.open('x', encoding='utf-8') as stream:
        json.dump(result, stream, indent=2)
        stream.write('\n')
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('executable', 'candidate', 'build_report', 'output'):
        parser.add_argument(name, type=Path)
    for name in ('baseline', 'baseline-build', 'baseline-native'):
        parser.add_argument('--'+name, type=Path)
    args = parser.parse_args()
    print(json.dumps(verify(args.executable, args.candidate, args.build_report, args.output,
                           baseline=args.baseline, baseline_build=args.baseline_build,
                           baseline_native=args.baseline_native), indent=2))


if __name__ == '__main__':
    main()
