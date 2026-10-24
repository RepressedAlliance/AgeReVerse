# 玩家下载、安装、卸载与排错指南

[返回首页](../../README.md) · [English](../en/player-guide.md) · [研究与制作入口](../research/README.md) · [提交 Bug](https://github.com/RepressedAlliance/AgeReVerse/issues/new?template=bug-report.yml)

## 汉化范围与实机预览

我们以游戏内可见内容的完整中文化为目标，已发布补丁接近完整覆盖剧情正文、菜单与设置、字幕和各类图片文字；
可编辑文本与嵌在图片中的文字一并汉化，仍会继续修正遗漏、原文残留和显示问题。
各作已知限制见下文与对应发布说明；“接近完整汉化”不代表已完成全路线人工遍历或全文人工校对。

**[查看 TDA00、TDA03、光子之花与光子旋律的中文实机截图](screenshots.md)**：正文、主界面、设置、操作菜单、字幕、振假名、地图与战术标注、地点提示、年表、手写道具及演出画面文字。

下载表上方为中文圈常用名或简称，下方为完整 Steam 名称，可点击前往商店核对。更多别名与版本区别见[作品名称对照](game-names.md)。

## 君望 Steam 版

**君望中文补丁 1.0.0「再会」**：本篇 EE、可选社区 EER 1.0 与 AEC+ 使用同一个安装器。

| 游戏 | 版本 | 下载 |
| --- | --- | --- |
| **君望／你所期望的永远 + AEC+**<br><sub>[Kimi ga Nozomu Eien: Enhanced Edition](https://store.steampowered.com/app/1777440/)<br>[Kimi ga Nozomu Eien Enhanced Edition another episode collection+](https://store.steampowered.com/app/3112140/)</sub> | **1.0.0** | [下载汉化补丁](https://github.com/RepressedAlliance/AgeReVerse/releases/download/kiminozo-1.0.0/KimiNozo-CN-1.0.0.zip) · [发布说明](https://github.com/RepressedAlliance/AgeReVerse/releases/tag/kiminozo-1.0.0) |

1. 在 Steam 安装本篇及你拥有的 AEC+，等待更新完成并退出游戏。
2. **普通 EE 跳过此步。**想补全 EE 删减内容时，从 [Muv-Luv Verse 上游主页](https://kiminozo.life/) 或[上游 Steam EER 1.0 ZIP](https://files.kiminozo.life/Patches/Kiminozo_EER_Patch_EN_Steam_1.0.zip) 获取可选 EER。按上游说明，将 ZIP 中的 `obb` 合并至本篇 `kiminozs` 目录。
3. 解压 `KimiNozo-CN-1.0.0.zip`，运行 `KimiNozo-CN-1.0.0-Setup.exe`。安装器自动查找游戏根目录；未找到时，可选择含 `kiminozs` 的游戏根目录，或含 `kiminozs-win64vc14-release.exe` 的本篇目录。不要选择 `obb` 或整个 Steam 安装目录。
4. 点击“安装汉化”。安装器自动识别 EE／完整 EER 1.0，并检测相邻的已安装 AEC+；部分或未知版本的 EER 会被拒绝。安装完成后，从 Steam 启动，在游戏设置中选择中文。

适用于 Windows x64、Steam build 18634794 及匹配的 AEC+。程序与 EER 文件均按摘要检查；其他商业版 EER、LE、旧光盘版及 Proton 未验证。新增／调整文本已完成人工校对，但不声称全路线人工实机遍历。

恢复原版时先切回英语／日语并退出游戏。保留两篇 `%LOCALAPPDATA%\ancr\<kiminozs或kiminoaz>\data\user`，只移走中文 `data\root` 及各自游戏目录的 `FridaGadget.dll`、`FridaGadget.config`、`age2-cn.js`、`COPYING-frida.txt`，以各自 `.age2-cn/original.exe` 恢复程序。EER 是另一层可选补丁：想回到普通 EE 时，另按上游说明移走其三个 `obb/patch*.bin`，不要动 Steam 原有 `pack*.bin`。Steam 验证不会清除 AppData 覆盖或额外 EER 文件。旧安装器保留的备份不要一并删除。

LE 原译及校对：**木之**；修订、移植、图片制作与统筹：**压抑同盟**；社区 EER：**Muv-Luv Verse Team · Lemonov · TotSamiyMisha**。旧译复用及社区 EER 中文适配均已获得相应许可。详细[制作说明与公开范围](../../AGE2/games/kiminozo/README.md)。

## AGE2 BETA · 安装方式更新 2026-09-21

| 游戏 | 版本 | 下载 |
| --- | --- | --- |
| **TDA00**<br><sub>[\[TDA00\] Muv-Luv Unlimited: THE DAY AFTER - Episode 00 REMASTERED](https://store.steampowered.com/app/1407100/)</sub> | **BETA 0.2.1** | [下载汉化补丁](https://github.com/RepressedAlliance/AgeReVerse/releases/download/tda00-BETA-0.2.1/TDA00-CN-BETA-0.2.1-Complete.zip) · [发布说明](https://github.com/RepressedAlliance/AgeReVerse/releases/tag/tda00-BETA-0.2.1) |
| **TDA01**<br><sub>[\[TDA01\] Muv-Luv Unlimited: THE DAY AFTER - Episode 01 REMASTERED](https://store.steampowered.com/app/1407090/)</sub> | **BETA 0.3.3** | [下载汉化补丁](https://github.com/RepressedAlliance/AgeReVerse/releases/download/tda01-BETA-0.3.3/TDA01-CN-BETA-0.3.3-Patch.zip) · [发布说明](https://github.com/RepressedAlliance/AgeReVerse/releases/tag/tda01-BETA-0.3.3) |
| **TDA02**<br><sub>[\[TDA02\] Muv-Luv Unlimited: THE DAY AFTER - Episode 02 REMASTERED](https://store.steampowered.com/app/1342410/)</sub> | **BETA 0.2.1** | [下载汉化补丁](https://github.com/RepressedAlliance/AgeReVerse/releases/download/tda02-BETA-0.2.1/TDA02-CN-BETA-0.2.1-Patch.zip) · [发布说明](https://github.com/RepressedAlliance/AgeReVerse/releases/tag/tda02-BETA-0.2.1) |
| **TDA03**<br><sub>[\[TDA03\] Muv-Luv Unlimited: THE DAY AFTER - Episode 03 REMASTERED](https://store.steampowered.com/app/789830/)</sub> | **BETA 0.2.7** | [下载汉化补丁](https://github.com/RepressedAlliance/AgeReVerse/releases/download/tda03-BETA-0.2.7/TDA03-CN-BETA-0.2.7-Patch.zip) · [发布说明](https://github.com/RepressedAlliance/AgeReVerse/releases/tag/tda03-BETA-0.2.7) |
| **帝都燃烧篇**<br><sub>[The Imperial Capital Burns - Muv-Luv Alternative Total Eclipse](https://store.steampowered.com/app/2630300/)</sub> | **BETA 0.2.1** | [下载汉化补丁](https://github.com/RepressedAlliance/AgeReVerse/releases/download/imperial-capital-burns-BETA-0.2.1/TM-CN-BETA-0.2.1-Patch.zip) · [发布说明](https://github.com/RepressedAlliance/AgeReVerse/releases/tag/imperial-capital-burns-BETA-0.2.1) |

五部作品都提供一键安装和手动复制。解压后只有四项：`安装说明.txt`、`root`、`game` 和安装器。

**一键安装：**退出游戏 → 运行安装器 → 选择本作目录 → 安装。

**手动安装：**退出游戏并备份原 EXE，将 `game` 里的五个文件复制到本作游戏目录，同名覆盖；将整个 `root` 复制到下表位置。已有 `root` 先改名保留，**不要动 `user`**。无需运行生成工具。

| 游戏 | root 放到这里 |
| --- | --- |
| TDA00 | `%LOCALAPPDATA%\ancr\tda00\data` |
| TDA01 | `%LOCALAPPDATA%\ancr\tda01\data` |
| TDA02 | `%LOCALAPPDATA%\ancr\tda02\data` |
| TDA03 | `%LOCALAPPDATA%\ancr\tda03\data` |
| 帝都燃烧 | `%LOCALAPPDATA%\ancr\tm\data` |

安装后从 Steam 启动游戏，在设置里选择中文。2026-09-21 的安装方式更新保留上一版汉化内容，已正常安装上一版无需重装。

恢复原版：先切回英文或日文，再退出游戏。保留 `data/user`，将 `data/root` 和游戏目录中的 `FridaGadget.dll`、`FridaGadget.config`、`age2-cn.js`、`COPYING-frida.txt` 移到备份位置；恢复自行备份的原 EXE（安装器备份为 `.age2-cn/original.exe`），或用 Steam 验证恢复程序。Steam 验证不会移走 AppData 的补丁资源。

旧 ZIP 的安装与恢复说明见[历史版本说明](historical-age2.md)，不适用于新版安装器。

## 玩家下载

### 光子之花 / 光子旋律

光子之花、光子旋律已正式公开发布，各自下载、安装，不混用。以下是 Windows / Steam 的简体中文汉化补丁，涵盖正文、界面和图片文字，仍有下述待修正内容：

| 游戏 | 版本 | 下载 |
| --- | --- | --- |
| **光子之花（PF）**<br><sub>[Muv-Luv photonflowers\*](https://store.steampowered.com/app/889700/)</sub> | **BETA 0.1.2** | [下载汉化补丁](https://github.com/RepressedAlliance/AgeReVerse/releases/download/pf-BETA-0.1.2/MuvLuv_PF_CN_Patch_BETA_0.1.2.zip) · [发布页](https://github.com/RepressedAlliance/AgeReVerse/releases/tag/pf-BETA-0.1.2) |
| **光子旋律（PM）**<br><sub>[Muv-Luv photonmelodies♮](https://store.steampowered.com/app/889710/)</sub> | **BETA 0.1.2** | [下载汉化补丁](https://github.com/RepressedAlliance/AgeReVerse/releases/download/pm-BETA-0.1.2/MuvLuv_PM_CN_Patch_BETA_0.1.2.zip) · [发布页](https://github.com/RepressedAlliance/AgeReVerse/releases/tag/pm-BETA-0.1.2) |

Steam 语言设为 **English（英语）**，等待下载完成并退出游戏；解压 ZIP，双击 EXE，点击“安装汉化”。无需安装旧版，也无需手动运行校验脚本。安装器自动定位游戏目录，未找到时选择对应文件夹。

**BETA 0.1.2** 同步最新校对：光子之花 24 条、光子旋律 23 条。校对及反馈致谢：**柚子コショウ**。两款均保留 BETA 0.1.1 修复，可从旧版直接覆盖升级。光子之花偶发英文及光子旋律《再诞》片尾动画英文尚未解决；详见[更新范围与署名](../project/photon-beta012-proofreading.md)。

采用 R2 内容，并修复回看“返回游戏”按钮。**完全不备份，不附卸载器或回滚程序。** 安装失败、中断或恢复原版时，保留存档，通过 Steam 卸载对应游戏，清除该游戏安装目录中的汉化残留，再重新下载。只处理对应游戏文件夹，不要清空 Steam 根目录、steamapps/common、userdata 或个人存档目录。仅验证完整性不能保证清除额外汉化文件。

## 排错与反馈

请提供游戏名称、补丁版本、Windows 环境、报错截图及前后台词，并说明是否安装其他补丁。
已发布的 TDA00—03 与帝都燃烧补丁在游戏设置中选择中文；光子之花／光子旋律在安装前将 Steam 语言设为 English。
不要混用不同作品的补丁。Steam Deck／Proton 不应视为已经验证的支持平台。

[提交运行问题](https://github.com/RepressedAlliance/AgeReVerse/issues/new?template=bug-report.yml)
· [提交翻译修正](https://github.com/RepressedAlliance/AgeReVerse/issues/new?template=translation-review.yml)
· QQ 交流群：273626767。

## 历史版本

[AGE2 旧 ZIP 安装、恢复与已知问题](historical-age2.md)。历史 Release、tag 和附件保留；新玩家使用本页当前版本。
