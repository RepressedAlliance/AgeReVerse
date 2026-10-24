# 君望／你所期望的永远 Steam 简体中文补丁

[返回首页](../../../README.md) · [玩家安装指南](../../../docs/player/README.md#君望-steam-版) · [项目清单](project.toml)

**君望中文补丁 1.0.0「再会」**适用于 Steam 本篇 [Kimi ga Nozomu Eien: Enhanced Edition](https://store.steampowered.com/app/1777440/)（EE）及 [Kimi ga Nozomu Eien Enhanced Edition another episode collection+](https://store.steampowered.com/app/3112140/)（AEC+）。正文、菜单、设置及图片文字一并中文化，新增／调整文本已完成人工校对。

**[下载统一安装包](https://github.com/RepressedAlliance/AgeReVerse/releases/download/kiminozo-1.0.0/KimiNozo-CN-1.0.0.zip)** · [发布说明、校验值及适用版本](https://github.com/RepressedAlliance/AgeReVerse/releases/tag/kiminozo-1.0.0)。解压运行 `KimiNozo-CN-1.0.0-Setup.exe`；GitHub 的 Source code ZIP 不能安装汉化。

## EE、可选 EER 与 AEC+

| 部分 | 适用版本 | 安装方式 |
| --- | --- | --- |
| 本篇 EE | Steam App 1777440，build 18634794 | 直接运行中文安装器 |
| 本篇 + 社区 EER 1.0 | 上述 Steam EE，另装匹配的上游 EER 1.0 | 先装上游 EER，再运行同一中文安装器 |
| 附加篇 AEC+ | Steam DLC App 3112140，资源目录 `kiminoaz` | 同一安装器检测已安装的附加篇并处理 |

**EER 是可选步骤，不是汉化的前置要求。**社区 EER Patch 来自 **Muv-Luv Verse**，作用是补全 EE 删减的内容。希望使用这部分内容的玩家，可从 **[上游主页 kiminozo.life](https://kiminozo.life/)** 获取，亦可[下载上游 Steam EER 1.0 ZIP](https://files.kiminozo.life/Patches/Kiminozo_EER_Patch_EN_Steam_1.0.zip)。按上游说明，将 ZIP 中的 `obb` 合并至本篇 `kiminozs` 目录，然后安装中文补丁。我们提供中文适配，不在本仓库镜像上游补丁。

安装器以三个 EER BIN 的大小与 SHA-256 自动区分普通 EE 与完整 EER 1.0；缺少部分文件或遇到其他版本会停止，避免装错资源。支持范围不包含 LE、旧光盘版、其他来源 EER 或 Steam Deck／Proton。

## 翻译与制作

**已获木之许可复用 LE 旧译，并获准进行 Muv-Luv Verse 社区 EER 的中文适配。**这是相关译文与社区补丁适配的许可，不是原作 IP 的官方授权。

有 LE 对应旧译的内容先承接木之译文，由 AI 协助复查错字、错译与表达，再由木之人工审核修订。没有对应旧译的新增／调整文本，使用 [GPT-6 Sol × GPT-6 Astra 工作流](../../../Localization-MakeGamesSpeak/Text-AITranslationWorthReading/README.md)：梳理人物、上下文及专名，整场翻译，独立回读日文二审并提出 `revise` 与 `question`；压抑同盟与木之讨论处理，最后由木之全文校对这批新增／调整文本并修改。

三版合计有 **4,886 处新增／调整文本**经过 AI 工作流翻译及人工校对；另核实 **874 条旧译误译／表达修正**及 **128 条错别字修正**。三版相同的日中句对只计一次，排除纯符号；修正类别可交叠，不能相加作为新译总数。

图片汉化覆盖菜单、系统界面及场景内文字，包含多块招牌、透视、遮挡与原有材质的处理；标题菜单采用共同字号、基线与左缘配置，见[标题菜单排版](images/title-menu-layout.md)。文本人工校对完成不代表已经人工走遍全部路线或所有图像出现位置；运行限制及反馈入口见发布说明。

## 署名

- **木之**：LE 原译、译文校对。
- **压抑同盟**：译文修订、移植、图片制作与统筹。
- **Muv-Luv Verse Team · Lemonov · TotSamiyMisha**：社区 EER Patch。
- 原作：© KimiNozo / Developed by aNCHOR, fuzz, Inc.，以游戏原有版权标识为准。

## 公开资料与构建

本仓库保留[术语表](../../../Localization-MakeGamesSpeak/Glossaries-KeepItConsistent/kiminozo.ja-zh-Hans.csv)、[语境基线与来源](terminology/README.md)、通用格式及运行工具、[统一安装器源码和构建说明](../../packaging/windows/README.md)。正式版的输入摘要、输出文件清单、构建源码提交和验证范围随 Release 交付。

完整旧译、完整调整后译文表、私人邮件／聊天及内部审校附件不放入公开 Git；`translation_authorities` 留空表示公开范围限制，不表示正文未完成。补丁仅分发运行所需中文覆盖资源与程序差分，不包含完整游戏原始容器或原版 EXE。用户须自行持有合法游戏。

反馈请注明 EE／EER／AEC+、补丁版本、前后台词或显示截图。[提交问题](https://github.com/RepressedAlliance/AgeReVerse/issues/new?template=bug-report.yml) · QQ 交流群 **273626767**。
