"""Check variant selection and preflight on retained synthetic directories only."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys
import uuid

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from AGE2.tools.runtime.exe_delta import make_delta

BINS = ['obb/patch00d.bin', 'obb/patch00m.bin', 'obb/patch01m.bin']
FOUNDATION = ['readme.txt', 'resident.list', 'data/hiscore.conf']
RUNTIME = ['FridaGadget.dll', 'FridaGadget.config', 'COPYING-frida.txt', 'age2-cn.js']
ORIGINAL = b'MZ' + bytes(range(256)) * 64
PATCHED = ORIGINAL[:1024] + b'CN-HOOK' + ORIGINAL[1031:] + b'IMPORT-SECTION'

HARNESS = r'''
using System;
using System.IO;
public static class KimiHarness {
  public static int Main(string[] args) {
    try {
      if(args[0]=="verify") Age2KimiUnifiedInstallEngine.Verify(args[1]);
      else if(args[0]=="detect") Console.WriteLine(Age2KimiUnifiedInstallEngine.Detect(args[1],args[2]));
      else if(args[0]=="install") Console.WriteLine(Age2KimiUnifiedInstallEngine.Install(args[1],args[2],args[3],null));
      else if(args[0]=="rollback") {
        FileStream locked=null; bool recovered=false;
        try {
          Age2KimiUnifiedInstallEngine.Install(args[1],args[2],args[3],line=>{
            if(line.StartsWith("AEC+ 追加篇：正在安装"))
              locked=new FileStream(Path.Combine(args[2],"kiminoaz","kiminoaz-win64vc14-release.exe"),FileMode.Open,FileAccess.Read,FileShare.None);
          });
        }catch(IOException error){recovered=error.Message.Contains("已恢复已安装篇章");}
        finally {if(locked!=null)locked.Dispose();}
        if(!recovered)throw new Exception("Bundle did not recover main component after AEC commit failure");
      }
      else throw new Exception("Unknown test action");
      return 0;
    }catch(Exception error){Console.Error.WriteLine(error.Message);return 1;}
  }
}
'''

def sha(data):
    return hashlib.sha256(data).hexdigest()

def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)

def put_json(path, value):
    write(path, json.dumps(value, ensure_ascii=False).encode('utf-8'))

def component(package, game, variant=None):
    entries = []
    files = {**{'root/' + n: b'FOUNDATION-' + n.encode() for n in FOUNDATION},
             **{'game/' + n: b'RUNTIME-' + n.encode() for n in RUNTIME},
             'root/assets/probe.txt': ('PAYLOAD-' + (variant or 'AEC')).encode()}
    for name, data in files.items():
        write(package / name, data)
        entries.append({'path': name, 'size': len(data), 'sha256': sha(data)})
    delta = make_delta(ORIGINAL, PATCHED)
    manifest = {'format': 'age2-cn-package-1', 'game': game, 'title': 'Synthetic fixture',
                'version': 'test', 'exe': game + '-win64vc14-release.exe', 'display_channel': 'zh_hans',
                'native': {key: delta[key] for key in ['original_sha256', 'patched_sha256']},
                'files': entries, 'foundation': FOUNDATION}
    if variant:
        manifest['variant'] = variant
    if variant == 'EE':
        manifest['incompatible_paths'] = BINS
    if variant == 'EER-1.0':
        manifest['dependencies'] = [{'path': n, 'size': len(n.encode()), 'sha256': sha(n.encode())} for n in BINS]
    put_json(package / 'manifest.json', manifest)
    put_json(package / 'exe.delta.json', delta)

def fixture(work, name, bins=0, aec=False):
    case = work / name
    package, game, profile = case / 'package', case / 'game', case / 'profile'
    component(package / 'variants/ee', 'kiminozs', 'EE')
    component(package / 'variants/eer', 'kiminozs', 'EER-1.0')
    component(package / 'kiminoaz', 'kiminoaz')
    put_json(package / 'manifest.json', {'format': 'age2-cn-variants-1', 'game': 'kiminozo',
             'exe': 'kiminozs-win64vc14-release.exe', 'version': 'test'})
    write(game / 'kiminozs/kiminozs-win64vc14-release.exe', ORIGINAL)
    for relative in BINS[:bins]:
        write(game / 'kiminozs' / relative, relative.encode())
    for part in ['kiminozs', 'kiminoaz']:
        write(profile / 'ancr' / part / 'data/user/savedata.bin', b'PLAYER-SAVE')
    if aec:
        write(game / 'kiminoaz/kiminoaz-win64vc14-release.exe', ORIGINAL)
    return package, game, profile

def snapshot(*roots):
    return {str(p): sha(p.read_bytes()) for root in roots for p in root.rglob('*') if p.is_file()}

def main():
    work = ROOT / 'local-internal/age2-installer-tests' / ('kimi-' + uuid.uuid4().hex[:8])
    work.mkdir(parents=True, exist_ok=False)
    compiler = Path(os.environ['WINDIR']) / 'Microsoft.NET/Framework64/v4.0.30319/csc.exe'
    source = work / 'KimiHarness.cs'
    source.write_text(HARNESS, 'utf-8')
    harness = work / 'KimiHarness.exe'
    subprocess.run([str(compiler), '/nologo', '/target:exe', '/platform:x64',
                    '/out:' + str(harness), '/reference:System.Web.Extensions.dll',
                    *[str(ROOT / 'AGE2/packaging/windows' / n) for n in
                      ['Age2InstallEngine.cs', 'Age2BundleInstallEngine.cs', 'Age2KimiUnifiedInstallEngine.cs']],
                    str(source)], check=True)
    results = []
    def run(name, args, expected=0, contains=None):
        result = subprocess.run([str(harness), *map(str, args)], capture_output=True)
        assert result.returncode == expected, (name, result.stdout, result.stderr)
        if contains:
            assert contains.encode() in result.stdout, (name, result.stdout)
        results.append(name)

    for name, bins, expected, selected in [('plain-ee', 0, 0, 'variants/ee'),
                                         ('partial-eer', 1, 1, None),
                                         ('complete-eer', 3, 0, 'variants/eer')]:
        package, game, profile = fixture(work, name, bins)
        before = snapshot(game, profile)
        run(name, ['detect', package, game / 'kiminozs'], expected, selected)
        assert snapshot(game, profile) == before, name + ' mutated detection inputs'

    package, game, profile = fixture(work, 'unknown-eer', 3)
    write(game / 'kiminozs' / BINS[1], b'UNKNOWN')
    before = snapshot(game, profile)
    run('unknown-eer-rejected', ['install', package, game, profile], 1)
    assert snapshot(game, profile) == before

    package, game, profile = fixture(work, 'aec-preflight', 0, True)
    write(game / 'kiminoaz/kiminoaz-win64vc14-release.exe', b'WRONG')
    before = snapshot(game, profile)
    run('aec-rejection-before-main-write', ['install', package, game, profile], 1)
    assert snapshot(game, profile) == before

    for name, bins, aec, selected in [('install-ee', 0, False, 'EE'), ('install-eer-and-aec', 3, True, 'EER-1.0')]:
        package, game, profile = fixture(work, name, bins, aec)
        run(name, ['install', package, game / 'kiminozs', profile])
        assert (profile / 'ancr/kiminozs/data/root/assets/probe.txt').read_bytes() == ('PAYLOAD-' + selected).encode()
        assert (game / 'kiminozs/kiminozs-win64vc14-release.exe').read_bytes() == PATCHED
        assert (game / 'kiminozs/.age2-cn/original.exe').read_bytes() == ORIGINAL
        for part in ['kiminozs', 'kiminoaz']:
            assert (profile / 'ancr' / part / 'data/user/savedata.bin').read_bytes() == b'PLAYER-SAVE'
        if aec:
            assert (profile / 'ancr/kiminoaz/data/root/assets/probe.txt').read_bytes() == b'PAYLOAD-AEC'
        else:
            assert not (profile / 'ancr/kiminoaz/data/root').exists()

    package, game, profile = fixture(work, 'aec-commit-rollback', 0, True)
    run('aec-commit-failure-restores-main', ['rollback', package, game, profile])
    for part in ['kiminozs', 'kiminoaz']:
        assert (game / part / (part + '-win64vc14-release.exe')).read_bytes() == ORIGINAL
        assert not (profile / 'ancr' / part / 'data/root').exists()
        assert (profile / 'ancr' / part / 'data/user/savedata.bin').read_bytes() == b'PLAYER-SAVE'
        assert all(not (game / part / name).exists() for name in RUNTIME)

    package, game, profile = fixture(work, 'version-mismatch')
    metadata = package / 'kiminoaz/manifest.json'
    value = json.loads(metadata.read_text('utf-8'))
    value['version'] = 'wrong'
    put_json(metadata, value)
    run('component-version-mismatch', ['verify', package], 1)
    report = {'status': 'passed', 'cases': results, 'fixture': str(work), 'real_game_or_profile_used': False}
    put_json(work / 'result.json', report)
    print(json.dumps(report, ensure_ascii=False))

if __name__ == '__main__':
    main()
