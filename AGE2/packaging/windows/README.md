# AGE2 Windows 安装程序

整合包由 `AGE2/tools/runtime/build_copy_only_package.py --package <本作 staging> --original <合法原版 EXE> --output <新输出目录> --installer <同版安装器>` 生成。ZIP 顶层只有 `安装说明.txt`、`root/`、`game/` 和安装器。`game/` 直接包含预先应用差分的程序与四个运行组件，手动安装无需运行安装器或生成工具。构建端验证原程序、差分结果及全部资源哈希；手动复制时不自动校验目标版本，因此仅适用于发布清单中的对应 Steam 版本。安装器继续保留版本校验。

恢复原版前应先在游戏设置中切回 English 或日本語。仅恢复 EXE、移走覆盖资源而保留中文语言选择，可能暴露原包中文槽自带的红色 `zh` 和错误篇章 logo 占位图。

每部作品生成一个内嵌资源的 Windows x64 EXE。界面沿用 PM/PF 安装程序的目录选择方式，识别 Steam 库中的对应游戏；执行引擎直接使用 .NET，不依赖玩家安装 Python、Frida 命令行或 PowerShell 7。

安装引擎先验证包内文件和原游戏 EXE 版本，生成该版本的程序差分结果，然后准备完整的新 `root`。准备完成后才切换活动目录，安装中文资源、三份基础文件与运行组件。游戏运行时拒绝安装。

原 `root` 移入本作 `data/.age2-cn-backups/<事务号>/root`，原程序保存在游戏目录 `.age2-cn/original.exe`；逐次被替换的程序文件与安装记录保存在 `.age2-cn/transactions/<事务号>`。失败恢复也保留诊断文件。此流程不会删除 `data/user`，也不删除玩家存档；旧覆盖资源仍作为副本保留，不再参与游戏读取。

安装过程中遇到链接目录、版本不符、包文件损坏、过长的资源路径或文件锁定，会停止或恢复安装前状态。事务与文件布局检查使用合成目录，不能代替对应 Steam 版本的完整安装与显示验证。

构建命令：

```powershell
python AGE2/tools/runtime/build_installers.py --staging <五部候选包目录> --output <新的输出目录>
```

输入采用 `age2-cn-package-1` 清单和 `age2-exe-delta-1` 差分。构建需要 Windows 自带的 .NET Framework C# 编译器。`--inspect <报告路径>` 只展开包并检查安装界面／目录识别，不执行安装，保留展开目录供复核。

公开发布使用 `--release`，版本配置见 `../releases/2026-09-20.json`。该模式输出 `*-CN-BETA-<版本>-Setup.exe`，界面不再附加“验收版”。安装程序通过不代表内容翻译、全部场景和语言切换均已验收；内容状态以对应 Release 的验证范围为准。

私有合法资源工作区的整理入口已公开为 `AGE2/tools/runtime/stage_packages.py --workspace <研究资源根目录> --versions AGE2/packaging/releases/2026-09-20.json`。它读取每部现有运行配置、候选资源和合法提取的原程序，在新的 staging 目录创建清单、程序差分及资源副本；公开仓库不包含原游戏资源或研究工作区。

开场单页源模板见 `AGE2/tools/images/boot_notice_template.py`。用 Noto Sans SC 在 Chrome 的 1920×1080 视口渲染后，`package_boot_notice.py` 保持横屏文字像素不变，居中放入原生 1920×1440 画布；竖屏资源保持完整页面和原生画布尺寸。

## 君望 EE／社区 EER／AEC+ 统一安装器

`build_kiminozo_unified_installer.py` 接受已经冻结并核对的完整私有资源目录，顶层为 `age2-cn-variants-1` 清单，包含 `variants/ee`、`variants/eer`、`kiminoaz` 三部分。各部分使用独立的 `zh_hans` 中文资源，版本须一致。这个目录及游戏资源不随维护源码提交。

```powershell
python AGE2/tools/runtime/build_kiminozo_unified_installer.py --staging <完整候选资源目录> --output <新的输出目录>
```

构建器逐项核对大小及 SHA-256，内嵌完整负载，记录四份编译输入的摘要。仅有改图覆盖层的目录不能作为完整输入。

玩家选择 Steam 游戏根目录或本篇／追加篇目录。统一安装器检查本篇的三份指定 EER BIN：全无时选 EE；三份均符合清单时选受支持的社区 EER 1.0；部分存在或内容不符时停止，避免把不完整 EER 当成 EE。此识别不代表支持其他社区补丁或商业日文 EER。

AEC+ 未安装时仅处理本篇；已存在时先核对本篇和追加篇，全部通过才开始写入。合并安装中断时，按各组件记录恢复已经完成的组件，保留事务记录。程序使用实际包内清单校验，不运行游戏，不替玩家进行版本转换。

合成目录测试入口为 `python AGE2/tests/packaging/run_kiminozo_installer_tests.py`。这些测试与通用引擎测试不触及真实 Steam、AppData 或存档，保留新建测试目录；不能代替用户对安装器界面和游戏显示的实际验证。
