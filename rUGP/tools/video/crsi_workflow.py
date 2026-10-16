"""Extract a bounded CRsi object or stream every C-decoded frame to FFV1.

Run from the repository root. No game code, native fallback or audio is used.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
from rUGP.formats.video.crsi import parse
from .portable_codec import Codec, native_to_rgb


def extract(source: Path, offset: int, size: int, output: Path) -> dict:
    if offset < 0 or not 0 < size <= 1_073_741_824:
        raise ValueError('invalid range (maximum object size: 1 GiB)')
    with source.open('rb') as stream:
        if offset + size > source.stat().st_size:
            raise ValueError('source range exceeds file')
        stream.seek(offset)
        data = stream.read(size)
    if len(data) != size:
        raise ValueError('truncated source range')
    sequence = parse(data)
    with output.open('xb') as stream:
        stream.write(data)
    return dict(bytes=size, sha256=hashlib.sha256(data).hexdigest(),
                frames=len(sequence.frames), width=sequence.width, height=sequence.height,
                rate=sequence.rate)


def export(library: Path, source: Path, output: Path, report_path: Path,
           ffmpeg: str = 'ffmpeg') -> dict:
    if output.suffix.lower() != '.mkv':
        raise ValueError('FFV1 output must use .mkv')
    if output.resolve() == report_path.resolve() or output.exists() or report_path.exists():
        raise FileExistsError('output and report must be distinct new paths')
    data = source.read_bytes()
    sequence = parse(data)
    codec = Codec(library)
    report = dict(schema='photon-crsi-export/1', status='incomplete',
                  source_sha256=hashlib.sha256(data).hexdigest(),
                  width=sequence.width, height=sequence.height, rate=sequence.rate,
                  frame_count=len(sequence.frames), decoded_frames=0,
                  rgb_sha256=[], native_bgrx_sha256=[],
                  limitation='C decode only; no native comparison, audio or playback validation')
    # Reserve the report before starting; a failed export keeps an explicit incomplete record.
    with report_path.open('x', encoding='utf-8') as report_stream:
        process = None
        try:
            process = subprocess.Popen([ffmpeg, '-hide_banner', '-loglevel', 'error', '-n',
                '-f', 'rawvideo', '-pixel_format', 'rgb24', '-video_size',
                f'{sequence.width}x{sequence.height}', '-framerate', f'{sequence.rate}/100',
                '-i', 'pipe:0', '-an', '-c:v', 'ffv1', '-level', '3', '-pix_fmt', 'bgr0',
                str(output)], stdin=subprocess.PIPE)
            previous = None
            for index, frame in enumerate(sequence.frames):
                try:
                    previous, _ = codec.decode(frame, sequence.width, sequence.height, previous)
                except ValueError as error:
                    raise ValueError(f'C decode failed at frame {index}: {error}') from error
                rgb = native_to_rgb(previous)
                process.stdin.write(rgb)
                report['native_bgrx_sha256'].append(hashlib.sha256(previous).hexdigest())
                report['rgb_sha256'].append(hashlib.sha256(rgb).hexdigest())
                report['decoded_frames'] += 1
            process.stdin.close()
            if process.wait() != 0:
                raise RuntimeError('FFmpeg export failed')
            report['status'] = 'complete C decode; FFV1 proxy exported'
        except BaseException as error:
            report['error'] = str(error)
            if process is not None:
                if process.stdin and not process.stdin.closed:
                    try:
                        process.stdin.close()
                    except BrokenPipeError:
                        pass
                if process.poll() is None:
                    process.terminate()
                process.wait()
            raise
        finally:
            json.dump(report, report_stream, indent=2)
            report_stream.write('\n')
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    ex = commands.add_parser('extract', help='extract a known volume-local offset and exact extent')
    ex.add_argument('source', type=Path)
    ex.add_argument('offset', type=lambda value: int(value, 0))
    ex.add_argument('size', type=lambda value: int(value, 0))
    ex.add_argument('output', type=Path)
    out = commands.add_parser('export', help='full sequential C decode to lossless silent FFV1')
    for name in ('library', 'source', 'output', 'report'):
        out.add_argument(name, type=Path)
    out.add_argument('--ffmpeg', default='ffmpeg')
    args = parser.parse_args()
    if args.command == 'extract':
        result = extract(args.source, args.offset, args.size, args.output)
    else:
        result = export(args.library, args.source, args.output, args.report, args.ffmpeg)
        result = {key: result[key] for key in ('status', 'frame_count', 'decoded_frames')}
    print(json.dumps(result))


if __name__ == '__main__':
    main()
