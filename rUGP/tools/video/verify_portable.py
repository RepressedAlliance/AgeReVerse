"""Verify C-decoded CRsi surfaces against saved native hashes or native leaves.

Saved source decode.json hashes are bottom-up native BGRX. New comparisons
include all four bytes; they do not establish visual quality or playback timing.
"""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import time
from rUGP.formats.video.crsi import parse
from .portable_codec import Codec, native_to_rgb


def native_coverage(sequence, samples: bool) -> set[int]:
    count=len(sequence.frames)
    if not samples or count<400:
        return set(range(count))
    rare=[i for i,f in enumerate(sequence.frames) if (f.mode,f.parameter)!=(0x575,8)]
    targets=set(rare+[min(count-1,i+1) for i in rare]+[round(i*(count-1)/19) for i in range(20)])
    selected=set()
    key=0
    for i,f in enumerate(sequence.frames):
        if f.independent:
            key=i
        if i in targets:
            selected.update(range(key,i+1))
    return selected


def verify(library: Path, source: Path, *, baseline: Path | None = None,
           target_build: Path | None = None,
           executable: Path | None = None, profile_samples: bool = False,
           offset: int = 0, size: int | None = None) -> dict:
    if offset<0 or (size is not None and size<=0):
        raise ValueError('invalid source range')
    with source.open('rb') as stream:
        stream.seek(offset)
        data=stream.read() if size is None else stream.read(size)
    if size is not None and len(data)!=size:
        raise ValueError('truncated source record')
    digest=hashlib.sha256(data).hexdigest()
    sequence=parse(data)
    expected=None
    target=None
    if baseline:
        expected=json.loads(baseline.read_text(encoding='utf-8'))
        if expected['sha256']!=digest or len(expected['frame_sha256'])!=len(sequence.frames):
            raise ValueError('baseline does not identify this complete source')
    if target_build:
        target=json.loads(target_build.read_text(encoding='utf-8'))
        if target.get('schema')!='photon-crsi-replacement/1' or target['output_sha256']!=digest or len(target['target_rgb_sha256'])!=len(sequence.frames):
            raise ValueError('build report does not identify this complete candidate')
    oracle=None
    selected=set()
    if executable:
        from .native_crsi import NativeCrsiDecoder
        oracle=NativeCrsiDecoder(executable)
        selected=native_coverage(sequence,profile_samples)
    if profile_samples and not oracle:
        raise ValueError('profile samples require a native executable')
    codec=Codec(library)
    previous=None
    profiles=Counter()
    tails=Counter()
    native_profiles=Counter()
    started=time.perf_counter()
    stride=sequence.width*4
    for i,frame in enumerate(sequence.frames):
        try:
            previous,bits=codec.decode(frame,sequence.width,sequence.height,previous)
        except ValueError as error:
            raise ValueError(f'C decode failed at frame {i}: {error}') from error
        profiles[f'{frame.mode:04x}/{frame.parameter}/{frame.flags}']+=1
        tails[len(frame.payload)*8-bits]+=1
        if expected:
            h=hashlib.sha256()
            view=memoryview(previous)
            for y in reversed(range(sequence.height)):
                h.update(view[y*stride:(y+1)*stride])
            if h.hexdigest()!=expected['frame_sha256'][i]:
                raise ValueError(f'native baseline mismatch at frame {i}')
        if target and hashlib.sha256(native_to_rgb(previous)).hexdigest()!=target['target_rgb_sha256'][i]:
            raise ValueError(f'target RGB mismatch at frame {i}')
        if i in selected:
            oracle.decode(frame,sequence.width,sequence.height)
            native=bytes(oracle.u.mem_read(0x1800000,len(previous)))
            for y in range(sequence.height):
                row=(sequence.height-1-y)*stride
                if previous[y*stride:(y+1)*stride]!=native[row:row+stride]:
                    raise ValueError(f'native leaf mismatch at frame {i}, row {y}')
            native_profiles[f'{frame.mode:04x}/{frame.parameter}/{frame.flags}']+=1
        if (i+1)%300==0:
            print(f'Decoded {i+1}/{len(sequence.frames)}',flush=True)
    return dict(schema='rugp-crsi-portable-verification/1',source_sha256=digest,
        record_bytes=len(data),offset=offset,width=sequence.width,height=sequence.height,
        frames=len(sequence.frames),profiles=dict(profiles),unused_payload_bits=dict(tails),
        saved_native_hash_matches=len(sequence.frames) if expected else 0,
        target_rgb_matches=len(sequence.frames) if target else 0,
        fresh_native_matches=len(selected),fresh_native_profiles=dict(native_profiles),
        native_sample_indices=sorted(selected) if profile_samples else None,
        seconds=time.perf_counter()-started,
        library_sha256=hashlib.sha256(library.read_bytes()).hexdigest(),
        limitation='Offline decoded bytes only; no game playback, visual quality or audio timing verification.')


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('library',type=Path)
    parser.add_argument('source',type=Path)
    parser.add_argument('output',type=Path)
    parser.add_argument('--baseline',type=Path)
    parser.add_argument('--target-build',type=Path)
    parser.add_argument('--executable',type=Path)
    parser.add_argument('--profile-samples',action='store_true')
    parser.add_argument('--offset',type=lambda v:int(v,0),default=0)
    parser.add_argument('--size',type=lambda v:int(v,0))
    args=parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    result=verify(args.library,args.source,baseline=args.baseline,target_build=args.target_build,executable=args.executable,
                  profile_samples=args.profile_samples,offset=args.offset,size=args.size)
    with args.output.open('x',encoding='utf-8') as stream:
        json.dump(result,stream,indent=2)
        stream.write('\n')


if __name__=='__main__': main()
