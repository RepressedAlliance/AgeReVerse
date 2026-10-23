using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Web.Script.Serialization;

// Used by the per-game Windows installer. All game data is version checked
// before mutation; previous loose resources remain in a recoverable archive.
public sealed class Age2PackageFile { public string path; public long size; public string sha256; }
public sealed class Age2Native { public string original_sha256; public string patched_sha256; }
public sealed class Age2Manifest {
    public string format, game, title, version, exe, display_channel;
    public Age2Native native;
    public Age2PackageFile[] files;
    public string[] foundation;
    public string[] incompatible_paths;
    public string variant;
    public Age2PackageFile[] dependencies;
}
public sealed class Age2Edit { public int offset; public string data; }
public sealed class Age2Delta {
    public string format, original_sha256, patched_sha256;
    public int output_size;
    public Age2Edit[] edits;
}
public static class Age2InstallEngine {
    static readonly JavaScriptSerializer Json = new JavaScriptSerializer { MaxJsonLength = 64 * 1024 * 1024 };
    static readonly string[] Games = { "tm", "tda00", "tda01", "tda02", "tda03", "kiminozs", "kiminoaz" };
    static readonly string[] RuntimeFiles = { "FridaGadget.dll", "FridaGadget.config", "COPYING-frida.txt", "age2-cn.js" };
    static readonly string[] Foundation = { "readme.txt", "resident.list", "data/hiscore.conf" };
    static readonly string[] EerBins = { "obb/patch00d.bin", "obb/patch00m.bin", "obb/patch01m.bin" };
    public static string Hash(byte[] data) {
        using (var sha = SHA256.Create()) return BitConverter.ToString(sha.ComputeHash(data)).Replace("-", "").ToLowerInvariant();
    }
    static T ReadJson<T>(string path) { return Json.Deserialize<T>(File.ReadAllText(path, Encoding.UTF8)); }
    static void WriteJson(string path, object value) { File.WriteAllText(path, Json.Serialize(value), new UTF8Encoding(false)); }
    public static string Child(string root, string relative) {
        if (String.IsNullOrWhiteSpace(relative) || Path.IsPathRooted(relative) || relative.Contains(":")) throw new IOException("补丁含无效路径。");
        var parts = relative.Replace('\\', '/').Split('/');
        if (parts.Any(p => p.Length == 0 || p == "." || p == ".." || p.EndsWith(".") || p.EndsWith(" "))) throw new IOException("补丁含无效路径。");
        string prefix = Path.GetFullPath(root).TrimEnd(Path.DirectorySeparatorChar) + Path.DirectorySeparatorChar;
        string path = Path.GetFullPath(Path.Combine(prefix, relative.Replace('/', Path.DirectorySeparatorChar)));
        if (!path.StartsWith(prefix, StringComparison.OrdinalIgnoreCase)) throw new IOException("补丁路径超出安装目录。");
        return path;
    }
    public static void NoLinks(string path, bool tree) {
        string current = Path.GetFullPath(path);
        while (current != null) {
            if ((File.Exists(current) || Directory.Exists(current)) && (File.GetAttributes(current) & FileAttributes.ReparsePoint) != 0)
                throw new IOException("目录包含链接，请选择实际目录：" + current);
            current = Path.GetDirectoryName(current);
        }
        if (!tree || !Directory.Exists(path)) return;
        foreach (var item in Directory.EnumerateFileSystemEntries(path)) {
            if ((File.GetAttributes(item) & FileAttributes.ReparsePoint) != 0) throw new IOException("资源目录包含链接：" + item);
            if (Directory.Exists(item)) NoLinks(item, true);
        }
    }
    public static Age2Manifest Verify(string package) {
        NoLinks(package, true);
        var manifest = ReadJson<Age2Manifest>(Child(package, "manifest.json"));
        if (manifest.format != "age2-cn-package-1" || !Games.Contains(manifest.game) || manifest.exe != manifest.game + "-win64vc14-release.exe")
            throw new IOException("补丁作品信息无效。");
        if (manifest.files == null || manifest.files.Length == 0 || manifest.native == null || manifest.foundation == null ||
            !new HashSet<string>(manifest.foundation).SetEquals(Foundation)) throw new IOException("补丁清单不完整。");
        if (manifest.incompatible_paths != null &&
            (manifest.game != "kiminozs" || manifest.incompatible_paths.Length != EerBins.Length ||
             !new HashSet<string>(manifest.incompatible_paths, StringComparer.Ordinal).SetEquals(EerBins)))
            throw new IOException("普通 EE 基底互斥清单无效。");
        if (manifest.dependencies != null || manifest.variant == "EER-1.0") {
            if (manifest.game != "kiminozs" || manifest.variant != "EER-1.0" || manifest.incompatible_paths != null ||
                manifest.dependencies == null || manifest.dependencies.Length != EerBins.Length ||
                manifest.dependencies.Any(d => d == null || d.size <= 0 || d.sha256 == null || d.sha256.Length != 64 || d.sha256.Any(c => !"0123456789abcdef".Contains(c))) ||
                !new HashSet<string>(manifest.dependencies.Select(d => d.path), StringComparer.Ordinal).SetEquals(EerBins))
                throw new IOException("EER 1.0 基底依赖清单无效。");
        }
        var names = new HashSet<string>(StringComparer.OrdinalIgnoreCase);
        foreach (var entry in manifest.files) {
            if (entry == null || entry.path == null || !names.Add(entry.path)) throw new IOException("补丁含重复资源。");
            if (!entry.path.StartsWith("root/", StringComparison.Ordinal) && !RuntimeFiles.Select(f => "game/" + f).Contains(entry.path))
                throw new IOException("补丁含未知安装目标。");
            string file = Child(package, entry.path);
            if (!File.Exists(file) || new FileInfo(file).Length != entry.size || Hash(File.ReadAllBytes(file)) != entry.sha256)
                throw new IOException("补丁文件损坏：" + entry.path);
        }
        bool nativeChannel = (manifest.game == "kiminozs" || manifest.game == "kiminoaz") && manifest.display_channel == "jp";
        if (nativeChannel && (manifest.native.original_sha256 != manifest.native.patched_sha256 || manifest.files.Any(f => !f.path.StartsWith("root/", StringComparison.Ordinal))))
            throw new IOException("原生显示通道补丁不能包含程序或运行组件改动。");
        if (Foundation.Any(f => !names.Contains("root/" + f)) || (!nativeChannel && RuntimeFiles.Any(f => !names.Contains("game/" + f)))) throw new IOException("补丁基础文件缺失。");
        var delta = ReadJson<Age2Delta>(Child(package, "exe.delta.json"));
        if (delta.original_sha256 != manifest.native.original_sha256 || delta.patched_sha256 != manifest.native.patched_sha256)
            throw new IOException("程序差分与补丁清单不一致。");
        return manifest;
    }
    public static byte[] ApplyDelta(byte[] original, Age2Delta delta) {
        if (delta.format != "age2-exe-delta-1" || Hash(original) != delta.original_sha256 || delta.output_size < 1 || delta.output_size > 256 * 1024 * 1024 || delta.edits == null)
            throw new IOException("游戏版本不符合补丁要求。");
        byte[] result = new byte[delta.output_size];
        Buffer.BlockCopy(original, 0, result, 0, Math.Min(original.Length, result.Length));
        long previousEnd = 0;
        foreach (var edit in delta.edits) {
            byte[] bytes = Convert.FromBase64String(edit.data);
            if (edit.offset < previousEnd || (long)edit.offset + bytes.Length > result.Length) throw new IOException("程序差分范围无效。");
            Buffer.BlockCopy(bytes, 0, result, edit.offset, bytes.Length); previousEnd = (long)edit.offset + bytes.Length;
        }
        if (Hash(result) != delta.patched_sha256) throw new IOException("程序差分校验失败。");
        return result;
    }
    static void CopyFile(string source, string target) {
        Directory.CreateDirectory(Path.GetDirectoryName(target)); File.Copy(source, target, false);
    }
    static void RequireStopped(string exe) {
        if (Process.GetProcessesByName(Path.GetFileNameWithoutExtension(exe)).Length != 0) throw new IOException("请先退出游戏，再安装补丁。");
        using (var stream = new FileStream(exe, FileMode.Open, FileAccess.Read, FileShare.None)) { }
    }
    // A bundle checks every installed component before it commits the first.
    public static void ValidateCompatibleBase(Age2Manifest manifest, string gameRoot) {
        if (manifest.dependencies != null) foreach (var dependency in manifest.dependencies) {
            string file=Child(gameRoot,dependency.path); NoLinks(file,false);
            if (!File.Exists(file) || new FileInfo(file).Length != dependency.size)
                throw new IOException("EER 1.0 基底文件缺失或版本不符："+dependency.path);
            using (var stream=File.OpenRead(file)) using (var sha=SHA256.Create()) {
                if (BitConverter.ToString(sha.ComputeHash(stream)).Replace("-", "").ToLowerInvariant() != dependency.sha256)
                    throw new IOException("EER 1.0 基底文件校验失败："+dependency.path);
            }
        }
        if (manifest.incompatible_paths == null) return;
        foreach (string relative in manifest.incompatible_paths) {
            string path=Child(gameRoot,relative); NoLinks(path,false);
            if (File.Exists(path) || Directory.Exists(path))
                throw new IOException("检测到 EER 资源。本包用于普通 EE，请先恢复普通 EE 基底后安装："+relative);
        }
    }
    public static void Preflight(string package, string gameRoot, string localAppData) {
        var m=Verify(package);
        ValidateCompatibleBase(m,gameRoot);
        string exe=Child(gameRoot,m.exe), storage=Child(gameRoot,".age2-cn"), saved=Child(storage,"original.exe");
        string data=Child(localAppData,"ancr/"+m.game+"/data"), root=Child(data,"root");
        NoLinks(gameRoot,false);NoLinks(storage,true);NoLinks(data,false);NoLinks(root,true);
        if(!File.Exists(exe))throw new IOException("所选目录没有对应游戏程序："+m.game);
        RequireStopped(exe);
        byte[] current=File.ReadAllBytes(exe), original=current;
        if(Hash(current)!=m.native.original_sha256) {
            if(Hash(current)!=m.native.patched_sha256 || !File.Exists(saved))throw new IOException("游戏程序版本不匹配："+m.game);
            original=File.ReadAllBytes(saved);
        }
        if(File.Exists(saved) && Hash(File.ReadAllBytes(saved))!=m.native.original_sha256)throw new IOException("保存的原版程序校验失败："+m.game);
        ApplyDelta(original,ReadJson<Age2Delta>(Child(package,"exe.delta.json")));
        foreach(string name in RuntimeFiles) {
            string file=Child(gameRoot,name);NoLinks(file,false);
            if(File.Exists(file) && !File.Exists(saved))throw new IOException("游戏目录已有同名运行组件："+name);
            if(File.Exists(file))using(var stream=new FileStream(file,FileMode.Open,FileAccess.Read,FileShare.None)) { }
        }
        foreach(var entry in m.files.Where(f=>f.path.StartsWith("root/"))) {
            if(Child(root,entry.path.Substring(5)).Length>=256)throw new IOException("本机用户数据路径过长："+m.game);
            if(Child(data,".age2-cn-work/00000000000000-00000000/"+entry.path).Length>=256)throw new IOException("安装准备目录路径过长："+m.game);
        }
    }
    public static void RollbackBundleComponent(string package, string receiptPath) {
        var m=Verify(package);var receipt=ReadJson<Dictionary<string,object>>(receiptPath);
        string gameRoot=(string)receipt["gameRoot"],root=(string)receipt["dataRoot"],oldRoot=(string)receipt["previousRoot"],work=Path.GetDirectoryName(receiptPath);
        if((string)receipt["status"]!="installed" || (string)receipt["game"]!=m.game)throw new IOException("安装记录不匹配。");
        RequireStopped(Child(gameRoot,m.exe));NoLinks(root,true);NoLinks(work,true);
        if(Hash(File.ReadAllBytes(Child(gameRoot,m.exe)))!=m.native.patched_sha256)throw new IOException("安装后程序已变化，停止自动恢复。");
        foreach(var entry in m.files) {
            string target=entry.path.StartsWith("root/") ? Child(root,entry.path.Substring(5)) : Child(gameRoot,entry.path.Substring(5));
            if(!File.Exists(target)||Hash(File.ReadAllBytes(target))!=entry.sha256)throw new IOException("安装后资源已变化，停止自动恢复："+entry.path);
        }
        string failedRoot=Child(Path.GetDirectoryName(root),".age2-cn-work/"+Path.GetFileName(work)+"/bundle-failed-root");
        NoLinks(Path.GetDirectoryName(failedRoot),false);
        Directory.CreateDirectory(Path.GetDirectoryName(failedRoot));Directory.Move(root,failedRoot);
        if(oldRoot!=null)Directory.Move(oldRoot,root);
        foreach(string name in RuntimeFiles.Concat(new[]{m.exe}).Reverse()) {
            string failed=Child(work,"bundle-failed/"+name),previous=Child(work,"old/"+name);
            Directory.CreateDirectory(Path.GetDirectoryName(failed));File.Move(Child(gameRoot,name),failed);
            if(File.Exists(previous))File.Move(previous,Child(gameRoot,name));
        }
        receipt["status"]="bundle-rolled-back";WriteJson(receiptPath,receipt);
    }
    // localAppData is supplied by the UI from the Windows known folder, not
    // inferred from a Steam path. Tests use an explicitly isolated directory.
    public static string Install(string package, string gameRoot, string localAppData, Action<string> report) {
        if (report == null) report = delegate { };
        report("正在检查补丁与游戏版本…");
        var m = Verify(package);
        var runtimeFiles = ((m.game == "kiminozs" || m.game == "kiminoaz") && m.display_channel == "jp") ? new string[0] : RuntimeFiles;
        gameRoot = Path.GetFullPath(gameRoot); localAppData = Path.GetFullPath(localAppData);
        ValidateCompatibleBase(m,gameRoot);
        string exe = Child(gameRoot, m.exe), storage = Child(gameRoot, ".age2-cn"), savedExe = Child(storage, "original.exe");
        string data = Child(localAppData, "ancr/" + m.game + "/data"), root = Child(data, "root");
        NoLinks(gameRoot, false); NoLinks(storage, true); NoLinks(data, false); NoLinks(root, true);
        if (!File.Exists(exe)) throw new IOException("所选目录没有对应游戏程序。");
        RequireStopped(exe);
        byte[] current = File.ReadAllBytes(exe), original;
        if (Hash(current) == m.native.original_sha256) original = current;
        else if (Hash(current) == m.native.patched_sha256 && File.Exists(savedExe) && Hash(File.ReadAllBytes(savedExe)) == m.native.original_sha256) original = File.ReadAllBytes(savedExe);
        else throw new IOException("游戏程序版本不匹配。请通过 Steam 验证游戏文件后重试。");
        if (File.Exists(savedExe) && Hash(File.ReadAllBytes(savedExe)) != m.native.original_sha256) throw new IOException("保存的原版程序校验失败，已停止安装。");
        foreach (string name in runtimeFiles) {
            string path = Child(gameRoot, name); NoLinks(path, false);
            if (File.Exists(path) && !File.Exists(savedExe)) throw new IOException("游戏目录已有同名运行组件，请先确认来源：" + name);
        }
        foreach (var entry in m.files.Where(f => f.path.StartsWith("root/")))
            if (Child(root, entry.path.Substring(5)).Length >= 256) throw new IOException("本机用户数据路径过长，游戏无法读取部分资源。");
        byte[] patched = ApplyDelta(original, ReadJson<Age2Delta>(Child(package, "exe.delta.json")));
        string id = DateTime.UtcNow.ToString("yyyyMMddHHmmss") + "-" + Guid.NewGuid().ToString("N").Substring(0, 8);
        string work = Child(storage, "transactions/" + id), dataWork = Child(data, ".age2-cn-work/" + id);
        string newRoot = Child(dataWork, "root"), oldRoot = Child(data, ".age2-cn-backups/" + id + "/root");
        NoLinks(Path.GetDirectoryName(oldRoot), false); NoLinks(dataWork, false);
        Directory.CreateDirectory(work); Directory.CreateDirectory(newRoot);
        Directory.CreateDirectory(Child(work, "new"));
        report("正在准备独立中文资源…");
        foreach (var entry in m.files.Where(f => f.path.StartsWith("root/"))) CopyFile(Child(package, entry.path), Child(newRoot, entry.path.Substring(5)));
        var targets = runtimeFiles.Concat(new[] { m.exe }).ToArray();
        foreach (string name in runtimeFiles) CopyFile(Child(package, "game/" + name), Child(work, "new/" + name));
        File.WriteAllBytes(Child(work, "new/" + m.exe), patched);
        if (!File.Exists(savedExe)) CopyFile(exe, savedExe);
        // Finish every check and copy before removing anything from active use.
        RequireStopped(exe); NoLinks(root, true); ValidateCompatibleBase(m,gameRoot);
        var movedOld = new List<string>(); var installed = new List<string>();
        bool archivedRoot = false, activatedRoot = false;
        try {
            report("正在安装，并保留旧资源副本…");
            if (Directory.Exists(root)) { Directory.CreateDirectory(Path.GetDirectoryName(oldRoot)); Directory.Move(root, oldRoot); archivedRoot = true; }
            Directory.Move(newRoot, root); activatedRoot = true;
            foreach (string name in targets) {
                string dest = Child(gameRoot, name), previous = Child(work, "old/" + name);
                if (File.Exists(dest)) { Directory.CreateDirectory(Path.GetDirectoryName(previous)); File.Move(dest, previous); movedOld.Add(name); }
                File.Move(Child(work, "new/" + name), dest); installed.Add(name);
            }
            WriteJson(Child(work, "receipt.json"), new { game = m.game, variant = m.variant, version = m.version, gameRoot, dataRoot = root, previousRoot = archivedRoot ? oldRoot : null, originalExe = savedExe, installed = targets, status = "installed" });
            report("安装完成。旧资源已保留，存档目录未改动。");
            return Child(work, "receipt.json");
        } catch (Exception error) {
            // Move only this transaction's files; keep failed outputs for
            // diagnosis rather than deleting an unknown or newly changed file.
            try {
                foreach (string name in installed.AsEnumerable().Reverse()) { string dest = Child(work, "failed/" + name); Directory.CreateDirectory(Path.GetDirectoryName(dest)); File.Move(Child(gameRoot, name), dest); }
                foreach (string name in movedOld.AsEnumerable().Reverse()) File.Move(Child(work, "old/" + name), Child(gameRoot, name));
                if (activatedRoot) Directory.Move(root, Child(dataWork, "failed-root"));
                if (archivedRoot) Directory.Move(oldRoot, root);
                WriteJson(Child(work, "receipt.json"), new { status = "rolled-back", error = error.Message });
            } catch (Exception rollback) { throw new IOException("安装中断且自动恢复未完成。请保留此目录以便恢复：" + work + "\n" + rollback.Message, error); }
            throw new IOException("安装未完成，已恢复安装前状态。" + error.Message, error);
        }
    }
}
