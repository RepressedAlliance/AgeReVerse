using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Web.Script.Serialization;

public static class Age2BundleInstallEngine {
    static readonly string[] Games={"kiminozs","kiminoaz"};
    public static void Verify(string package) {
        Age2InstallEngine.NoLinks(package,true);
        var doc=new JavaScriptSerializer().Deserialize<Dictionary<string,object>>(File.ReadAllText(Age2InstallEngine.Child(package,"manifest.json"),Encoding.UTF8));
        if((string)doc["format"]!="age2-cn-bundle-1" || (string)doc["game"]!="kiminozo")throw new IOException("合并补丁信息无效。");
        var games=((System.Collections.IEnumerable)doc["games"]).Cast<object>().Select(v=>(string)v).ToArray();
        if(!games.SequenceEqual(Games))throw new IOException("合并补丁篇章清单无效。");
        foreach(string game in Games) {
            var m=Age2InstallEngine.Verify(Age2InstallEngine.Child(package,game));
            if(m.game!=game || m.display_channel!="zh_hans")throw new IOException("合并补丁需要独立中文资源。");
        }
    }
    public static string NormalizeRoot(string root) {
        root=Path.GetFullPath(root).TrimEnd(Path.DirectorySeparatorChar);
        if(Games.Contains(Path.GetFileName(root),StringComparer.OrdinalIgnoreCase))root=Path.GetDirectoryName(root);
        return root;
    }
    public static string Install(string package,string root,string localAppData,Action<string> report) {
        if(report==null)report=delegate{};
        Verify(package);root=NormalizeRoot(root);Age2InstallEngine.NoLinks(root,false);
        if(!File.Exists(Age2InstallEngine.Child(root,"kiminozs/kiminozs-win64vc14-release.exe")))throw new IOException("请选择同时包含 kiminozs 和 kiminoaz 的 Steam 游戏目录。");
        var installed=new List<string>();
        foreach(string game in Games) {
            string dir=Age2InstallEngine.Child(root,game);
            if(game=="kiminoaz" && !Directory.Exists(dir)) {report("未安装 AEC+，本次仅安装 EE 本篇。");continue;}
            report("正在检查 "+(game=="kiminozs"?"EE 本篇":"AEC+ 追加篇")+"…");
            Age2InstallEngine.Preflight(Age2InstallEngine.Child(package,game),dir,localAppData);installed.Add(game);
        }
        var completed=new List<KeyValuePair<string,string>>();
        try {
            foreach(string game in installed) {
                string part=Age2InstallEngine.Child(package,game);
                string receipt=Age2InstallEngine.Install(part,Age2InstallEngine.Child(root,game),localAppData,line=>report((game=="kiminozs"?"EE 本篇：":"AEC+ 追加篇：")+line));
                completed.Add(new KeyValuePair<string,string>(part,receipt));
            }
        }catch(Exception error) {
            try {foreach(var item in completed.AsEnumerable().Reverse())Age2InstallEngine.RollbackBundleComponent(item.Key,item.Value);}
            catch(Exception rollback) {throw new IOException("合并安装中断，自动恢复未完成；请保留安装记录。\n"+rollback.Message,error);}
            throw new IOException("合并安装未完成，已恢复已安装篇章。\n"+error.Message,error);
        }
        return "已安装："+String.Join("、",installed.Select(g=>g=="kiminozs"?"EE 本篇":"AEC+ 追加篇"))+"。请在游戏设置中选择中文。";
    }
}
