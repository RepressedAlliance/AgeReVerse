"""Compile one automatic EE/EER/AEC installer from frozen, verified payloads."""
from pathlib import Path
import argparse
import hashlib
import json
import os
import re
import subprocess
import zipfile


def digest(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--staging', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--version', help='Stable semantic version; leave unset to preserve the staged channel')
    parser.add_argument('--release-name', help='Optional player-facing name for a stable release')
    args = parser.parse_args()
    if args.version and not re.fullmatch(r'(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)', args.version):
        parser.error('--version must be a stable major.minor.patch version')
    if args.release_name and not args.version:
        parser.error('--release-name requires --version')
    manifest = json.loads((args.staging / 'manifest.json').read_text(encoding='utf-8'))
    if manifest['format'] != 'age2-cn-variants-1' or manifest['game'] != 'kiminozo':
        raise ValueError('Expected the automatic KimiNozo variant manifest')
    staged_version = manifest['version']
    if args.version:
        manifest.update(version=args.version, release_channel='stable', status='release')
        if args.release_name:
            manifest['release_name'] = args.release_name
    args.output.mkdir(parents=True, exist_ok=False)
    payload = args.output / 'kiminozo-payload.zip'
    counts = {}
    with zipfile.ZipFile(payload, 'x', zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        archive.writestr('manifest.json', json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
        for relative, game in [('variants/ee', 'kiminozs'), ('variants/eer', 'kiminozs'), ('kiminoaz', 'kiminoaz')]:
            package = args.staging / relative
            part = json.loads((package / 'manifest.json').read_text(encoding='utf-8'))
            if part['game'] != game or part['display_channel'] != 'zh_hans' or part['version'] != staged_version:
                raise ValueError('Mismatched component or release version')
            if args.version:
                part.update(version=args.version, release_channel='stable')
            archive.writestr(relative + '/manifest.json', json.dumps(part, ensure_ascii=False, indent=2) + '\n')
            archive.write(package / 'exe.delta.json', relative + '/exe.delta.json')
            for entry in part['files']:
                path = package / entry['path']
                if path.stat().st_size != entry['size'] or digest(path) != entry['sha256']:
                    raise ValueError('Changed staged resource: ' + entry['path'])
                archive.write(path, relative + '/' + entry['path'])
            counts[relative] = len(part['files'])
    output = args.output / ('KimiNozo-CN-' + manifest['version'].replace(' ', '-') + '-Setup.exe')
    source = Path(__file__).resolve().parents[2] / 'packaging/windows'
    compiler = Path(os.environ['WINDIR']) / 'Microsoft.NET/Framework64/v4.0.30319/csc.exe'
    sources = [source / n for n in ['Age2Installer.cs', 'Age2InstallEngine.cs', 'Age2BundleInstallEngine.cs', 'Age2KimiUnifiedInstallEngine.cs']]
    subprocess.run([str(compiler), '/nologo', '/target:winexe', '/platform:x64', '/out:' + str(output.resolve()),
                    '/resource:' + str(payload.resolve()) + ',payload.zip', '/reference:System.Windows.Forms.dll',
                    '/reference:System.Drawing.dll', '/reference:System.Web.Extensions.dll',
                    '/reference:System.IO.Compression.dll', '/reference:System.IO.Compression.FileSystem.dll',
                    *map(str, sources)], check=True)
    report = {'installer': str(output.resolve()), 'bytes': output.stat().st_size, 'sha256': digest(output),
              'manifest_sha256': digest(args.staging / 'manifest.json'), 'payload_counts': counts,
              'compiled_sources': {str(p): digest(p) for p in sources}}
    (args.output / 'build-report.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(json.dumps(report), flush=True)


if __name__ == '__main__':
    main()
