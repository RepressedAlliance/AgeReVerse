using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Web.Script.Serialization;

// One entry point; the installed base selects the frozen EE or EER payload.
public static class Age2KimiUnifiedInstallEngine {
    static readonly string[] Bins={"obb/patch00d.bin","obb/patch00m.bin","obb/patch01m.bin"};
    public static void Verify(string package) {
        Age2InstallEngine.NoLinks(package,true);
        var doc=new JavaScriptSerializer().Deserialize<Dictionary<string,object>>(File.ReadAllText(Age2InstallEngine.Child(package,"manifest.json"),Encoding.UTF8));
        if((string)doc["format"]!="age2-cn-variants-1" || (string)doc["game"]!="kiminozo" ||
            (string)doc["exe"]!="kiminozs-win64vc14-release.exe")throw new IOException("统一补丁信息无效。");
        var ee=Age2InstallEngine.Verify(Age2InstallEngine.Child(package,"variants/ee"));
        var eer=Age2InstallEngine.Verify(Age2InstallEngine.Child(package,"variants/eer"));
        var aec=Age2InstallEngine.Verify(Age2InstallEngine.Child(package,"kiminoaz"));
        if(ee.game!="kiminozs" || ee.variant!="EE" || ee.incompatible_paths==null || ee.dependencies!=null ||
            eer.game!="kiminozs" || eer.variant!="EER-1.0" || eer.dependencies==null || eer.incompatible_paths!=null ||
            aec.game!="kiminoaz" || aec.dependencies!=null || aec.incompatible_paths!=null || aec.variant!=null ||
            ee.native.original_sha256!=eer.native.original_sha256 || ee.native.patched_sha256!=eer.native.patched_sha256 ||
            new[]{ee,eer,aec}.Any(m=>m.display_channel!="zh_hans" || m.version!=(string)doc["version"]))
            throw new IOException("统一补丁的篇章或版本清单不一致。");
    }
    // No writes, and no fallback from an incomplete or unknown EER base to EE.
    public static string Detect(string package,string mainRoot) {
        int count=0;
        foreach(string name in Bins) {
            string file=Age2InstallEngine.Child(mainRoot,name);Age2InstallEngine.NoLinks(file,false);
            if(File.Exists(file)||Directory.Exists(file))count++;
        }
        if(count==0)return "variants/ee";
        if(count!=Bins.Length)throw new IOException("检测到不完整的 EER 基底。请先完整安装受支持的 EER 1.0，或恢复普通 EE 基底；尚未写入补丁。");
        var eer=Age2InstallEngine.Verify(Age2InstallEngine.Child(package,"variants/eer"));
        Age2InstallEngine.ValidateCompatibleBase(eer,mainRoot);
        return "variants/eer";
    }
    public static string Install(string package,string root,string localAppData,Action<string> report) {
        if(report==null)report=delegate{};
        Verify(package);root=Age2BundleInstallEngine.NormalizeRoot(root);Age2InstallEngine.NoLinks(root,false);
        string main=Age2InstallEngine.Child(root,"kiminozs");
        if(!File.Exists(Age2InstallEngine.Child(main,"kiminozs-win64vc14-release.exe")))throw new IOException("请选择含 kiminozs 的 Steam 游戏目录。");
        string selected=Detect(package,main),label=selected=="variants/eer"?"EER 1.0 本篇":"EE 本篇";
        report("已自动识别："+label+"；正在检查本篇和追加篇…");
        var parts=new List<KeyValuePair<string,string>>{new KeyValuePair<string,string>(selected,"kiminozs")};
        if(Directory.Exists(Age2InstallEngine.Child(root,"kiminoaz")))parts.Add(new KeyValuePair<string,string>("kiminoaz","kiminoaz"));
        else report("未安装 AEC+，本次仅安装本篇。");
        foreach(var part in parts)Age2InstallEngine.Preflight(Age2InstallEngine.Child(package,part.Key),Age2InstallEngine.Child(root,part.Value),localAppData);
        var completed=new List<KeyValuePair<string,string>>();
        try {
            foreach(var part in parts) {
                string source=Age2InstallEngine.Child(package,part.Key);
                string receipt=Age2InstallEngine.Install(source,Age2InstallEngine.Child(root,part.Value),localAppData,line=>report((part.Value=="kiminozs"?label:"AEC+ 追加篇")+"："+line));
                completed.Add(new KeyValuePair<string,string>(source,receipt));
            }
        }catch(Exception error) {
            try {foreach(var item in completed.AsEnumerable().Reverse())Age2InstallEngine.RollbackBundleComponent(item.Key,item.Value);}
            catch(Exception rollback){throw new IOException("统一安装中断，自动恢复未完成；请保留安装记录。\n"+rollback.Message,error);}
            throw new IOException("统一安装未完成，已恢复已安装篇章。\n"+error.Message,error);
        }
        return "已安装："+label+(parts.Count==2?"、AEC+ 追加篇":"")+"。请在游戏设置中选择中文。";
    }
}
