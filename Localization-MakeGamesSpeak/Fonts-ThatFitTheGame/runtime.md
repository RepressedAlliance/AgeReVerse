# 游戏文本字体对应表

[字体入口](README.md) · [精确版本／摘要](catalog.json) · [图片字体](images.md)

## TDA00–03 与帝都燃烧

五作原版的主要配置相同。英文正文另用 UD 角黑 DB，不能把日文正文的 NewCinema 当作所有语言的正文。

| 角色 | 日文原版 | 英文原版 | 当前中文 `Font_cn.cfg` |
| --- | --- | --- | --- |
| Common／系统 | `beatfont1.otf` | 同左 | `AGE2UISansSC-Dash.otf` |
| Message／正文 | `FOT-NewCinemaAStd-D.otf` | `FOT-UDKakugo_LargePro-DB.otf` | `BWCKKT-Bold.ttf` |
| Speaker／姓名 | `FOT-SkipProN-D.otf` | 同左 | `MEBheiheiti.ttf` |
| Hud | `FOT-UDKakugo_LargePro-DB.otf` | 同左 | `NotoSansSC-500.ttf` |
| LanguageChoice／语言选择 | 原版未单列此角色 | 原版未单列此角色 | `IBMPlexSansSC-Regular.otf` |
| sub／中文备用 | 原版配置未列中文备用 | 原版配置未列中文备用 | `AGE2FallbackSC-Dash.ttf` |

中文系统字体配置的 FamilyName 仍为 `beatfont1`，外部文件名、内部家族名和配置别名不能混为一谈。中文正文 LineBreak 为 1.05；英文原版正文为 1.4。实际值与所有原版／补丁配置列在目录中，修改时使用对应游戏的真实配置，不拿早期 `font_zh_hans` 试验文件替代已发布的 `Font_cn.cfg`。

### 所有随包字体

下表同时列出随包附带但当前中文配置未选用的字体；“附带”与“生效”分别标注。

| 文件 | 当前用途 | 范围 |
| --- | --- | --- |
| AGE2UISansSC-Dash.otf | Common；IBM Plex 派生及横线修正 | 五作 |
| BWCKKT-Bold.ttf | Message；白无常可可体粗，含已记录补字 | 五作 |
| MEBheiheiti.ttf | Speaker；美呗嘿嘿体 3.000，含已记录补字 | 五作 |
| NotoSansSC-500.ttf | Hud；日／英补丁配置的 sub；亦用于图片 | 五作 |
| IBMPlexSansSC-Regular.otf | LanguageChoice | 五作 |
| AGE2FallbackSC-Dash.ttf | 中文 sub；Noto 500 派生横线修正 | 五作 |
| AGE2GenSekiSC-Regular.otf | 随包附带，当前中文配置未选用 | 五作 |
| GenSekiGothic2TW-R.otf | 随包附带，当前中文配置未选用 | 五作 |
| BWCKKT-Regular.ttf | 随包附带，正文实际用 Bold | 五作 |
| SweiSugarCJKsc-Medium.ttf | 随包附带，日期／地点图片制作使用 | 五作 |
| SweiSugarCJKsc-SemiBold.ttf | 随包附带，当前中文配置未选用 | 五作 |
| SourceHanSansSC.otf | 随包附带，当前中文配置未选用 | 仅帝都 |
| SourceHanSansSC-Bold.otf | 随包附带，早期图片方案有使用记录 | 仅帝都 |

原版四个商业字体仅登记配置、家族、版本和文件身份。中文正文与姓名字体包含补字；维护和再分发时应保留实际修改说明及适用的作者许可。

## PF 与 PM

两作走 AGES／GDI 的字体请求与运行时家族替换，不采用 AGE2 的六角色 XML 配置。补丁将请求的字体家族改为 `PhotonR2`，其余字号、粗细、字符集、方向等请求字段保留；参见[运行时策略](../../rUGP/runtime/include/photon_font_policy.h)与[字体复盘](../../rUGP/docs/postmortems/font-runtime.md)。

| 游戏／版本 | 文件 | 内部家族 | 字体记录版本 | 字节数 |
| --- | --- | --- | --- | ---: |
| PF BETA 0.1.2 | PhotonR2-Regular.ttf | PhotonR2 | 2.06，root-fix，U+2060 零 advance | 1,410,172 |
| PM BETA 0.1.2 | PhotonR2-Regular.ttf | PhotonR2 | 2.09，PM choice W550 | 1,460,112 |

精确 SHA-256 分别是 `938a0046…1b0ec64` 与 `3d1cdf9b…4322f3b`，完整值在 [catalog.json](catalog.json)。两者以思源黑体为基础，包含项目改名、度量／字集修正；PF 后续扩字与 PM 排版修正分开维护。不要用同名、同家族或旧版源码中的字体常量判断能否互换。

原生请求使用 Windows 字体路由：Standard／LowSpec 名称对应 **ＭＳ Ｐゴシック（MS PGothic）**，ANSI 为 **Arial**；PM 干净安装的 GB2312 值为空。这些是请求的家族名，实际采用哪个系统字体还取决于系统与字体回退。

它们不是补丁另附的一整套 TTF。实际游戏字号、粗细和选字要观察请求，不能凭 PNG 或菜单外观反推。此目录完整登记发布包所附的字体，不声称已识别每张官方图片的原始排字字体。

## 君望 1.0.0「再会」

EE、可选社区 EER 1.0 与 AEC+ 使用相同中文角色配置，不能沿用上述七作的配置。EER 的姓名字体字节与 EE／AEC+ 不同，同名不可混用；精确文件摘要、家族、版本与许可文件分别记录于[君望发布字体清单](../../AGE2/games/kiminozo/images/release-fonts.json)。

| 用途 | 包内文件 | 来源／处理 |
| --- | --- | --- |
| Common 系统 | `AGE2UISansSC-Dash.otf` | IBM Plex Sans SC 派生，U+2015 字形笔画修正 |
| Message 正文 | `AGE2MessageSC-Bold.ttf` | 狮尾圆体 Swei Curve Sans SC Bold 派生，补 U+00B7 映射 |
| Speaker 姓名 | `AGE2SpeakerSC-Regular.ttf` | GenWa Kocha TC 基础，汉字换为 Swei Spring Sugar SC SemiBold 字形 |
| Hud、sub | `SourceHanSansCN-Medium.otf` | 思源黑体 CN Medium |
| StaffCN 中文署名 | `SourceHanSerifCN-Regular.otf` | 思源宋体 CN Regular |

框架自身的标题／数字／Common 配置使用 `SourceHanSansCN-Medium.otf`。运行时只将中文请求路由至对应配置，日英仍走原配置。补丁亦保留派生基础字体及完整许可；随包存在不等于当前中文角色实际选用。菜单等图片文字独立制作，见[君望图片说明](../../AGE2/games/kiminozo/images/README.md)。
