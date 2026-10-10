# 字体排版｜别让字体出卖你的补丁

**Fonts & Typography: Don't Let Fonts Give Your Patch Away**

[返回本地化](../README.md) · **[游戏字体对应表](runtime.md)** · **[图片用字与样式](images.md)** · [字体致谢与许可](attribution.md) · [新图片登记](registration.md) · [精确版本目录](catalog.json)

<details>
<summary><strong>English · Don't Let Fonts Give Your Patch Away — expand here</strong></summary>

The catalog covers the seven released games, original AGE2 roles, every bundled AGE2 font, the distinct PF/PM PhotonR2 binaries, and known image-authoring inputs. Runtime selection, bundled-but-unused fonts, image production and historical trials are separate. Source hashes identify files; they do not establish visual acceptance or grant redistribution rights. For another locale, check its own coverage, shaping, metrics and engine selection.

The October 11 audit traces 3,720 current release image files to their font or original/generated lettering sources, and records 365 selected local candidates separately. It also identifies missing authoring inputs, including Swei SemiBold, an unpatched MEB image font and a static Noto Sans 700 instance. Read the [image usage table](images.md), [credits](attribution.md) and [registration policy](registration.md). This is provenance within the listed file scope, not new visual/runtime approval. Historical font-byte and rendering limitations remain explicit.

</details>

译文进入游戏以后，还要放得下、看得清，并贴合作品原有的气质。这里集中维护七作的字体选择与来源，游戏文本和图片烘焙用字分别登记。替换运行时字体不会改变已画进图片的文字，重画图片也不会修复正文的选字、字宽或换行。

**核对范围：运行时按 2026-10-05 的七作发布包核对；图片追溯更新于 2026-10-11。** 五作 AGE2 的 859 个独立图片文件和 PF／PM 的 2,861 个 PNG 文件，均对应到实际字体或原版／生成字样来源；另列 365 项本地在制成品。目录共登记 24 项具体图片字体输入／试样，区分当前采用、历史替换与在制方案。详情与历史字体版本、HTML 加载和旧计时排版的限制见[图片用字表](images.md)，不以来源核对代替人工视觉审核和实机验证。

## 当前发布版使用什么

| 游戏 | 核对版本 | 中文运行时方案 |
| --- | --- | --- |
| TDA00 | BETA 0.2.1 | 下列 AGE2 六个角色 |
| TDA01 | BETA 0.3.3 | 同上 |
| TDA02 | BETA 0.2.1 | 同上 |
| TDA03 | BETA 0.2.7 | 同上 |
| 帝都燃烧 | BETA 0.2.1 | 同上 |
| PF | BETA 0.1.2 | PF 专用 `PhotonR2-Regular.ttf` |
| PM | BETA 0.1.2 | PM 专用 `PhotonR2-Regular.ttf` |

AGE2 中文实际配置是：系统 **AGE2 UI Sans SC Dash**、正文 **白无常可可体粗**、姓名 **美呗嘿嘿体**、HUD **Noto Sans SC 500**、语言选择 **IBM Plex Sans SC Regular**、备用 **AGE2 Fallback SC Dash**。旧介绍中的“统一思源黑体候选”已经不能描述当前包。

PF／PM 都请求 `PhotonR2` 家族，但两作字体字集和修正不同，**文件同名不代表内容相同，不能互换**。旧 `PhotonCN`、早期 PhotonR2 与当前发布包分别记录；详见[运行时对应表](runtime.md)。

## 怎么核对的

2026-10-05 逐作核对：AGE2 包内字体和三个实际配置的摘要与对应公开 release manifest 一致；PF／PM 从下载 ZIP 内安装器的嵌入包读取字体，ZIP 摘要与公开 manifest 一致。结果、版本、文件摘要、原版配置和全部随包字体见 [catalog.json](catalog.json)，对应发布入口以[玩家版本索引](../../docs/player/release-index.json)为准。

“随包附带”与“被当前配置使用”分开：TDA 每包附带 11 个字体文件，帝都 13 个，其中中文配置直接选用 6 个角色；原版日／英配置及图片制作也需独立核对。查明附带的旧候选不等于建议继续打包它们。

## 来源与复用

| 字体家族 | 来源 |
| --- | --- |
| Noto Sans／Serif CJK | [Noto CJK](https://github.com/notofonts/noto-cjk)，OFL 1.1 |
| 思源黑体、PhotonR2 派生基础 | [Source Han Sans](https://github.com/adobe-fonts/source-han-sans)，OFL 1.1 |
| IBM Plex Sans SC、AGE2 UI Sans 派生基础 | [IBM Plex](https://github.com/IBM/plex)，OFL 1.1 |
| 源石黑体、AGE2 GenSeki 派生基础 | [GenSeki](https://github.com/ButTaiwan/genseki-font)，OFL 1.1 |
| 狮尾加糖宋体 Medium／SemiBold | [Swei Sugar](https://github.com/max32002/swei-sugar)，OFL 1.1；分别用于发布卡片和在制纸箱括注 |
| 思源宋体、霞鹜文楷 GB、得意黑、小赖、马善政、站酷快乐体 | [图片字体致谢与许可](attribution.md)，逐项列作者、上游和实际用途；均为 OFL 1.1 |
| 白无常可可体 | [作者发布页](https://www.zcool.com.cn/work/ZNTk4NTI2ODA%3D.html)，作者使用声明；不属于 OFL |
| 美呗嘿嘿体 | [作者发布页](https://www.zcool.com.cn/work/ZNTY3OTI5ODg%3D.html)，作者使用声明；不属于 OFL |

白无常／美呗的来源说明来自已发布包和维护者提供的作者说明，本次站酷页面未能读到正文，不宣称重新完整核验了授权。两款有已记录的缺字补充；旧来源文字中的“未修改字集”不能替代补充后的构建记录。此目录不重新授予字体许可，也不复制官方商业字体。

制作时保存实际字体文件版本、来源、许可、修改／子集化方式与输出摘要；衍生字体的改名和许可证跟随实际来源。二进制继续随适当的发布包提供，Git 维护目录与配方，不重复提交整套大字体。

图片制作还用过楷体、宋体、MS Mincho 和微软雅黑等 Windows 字体，试样与对照中另有 SimHei／MS Gothic；它们不归入开源字体。新图片和返修必须按[登记规范](registration.md)补齐实际用字与来源；只制作图片和随包分发字体文件的许可要求分别处理。

## 覆盖与实机

```powershell
python -m Localization-MakeGamesSpeak.Tools-LetToolsHandleRepetition.font_coverage work/TargetFont.ttf AGE2/games/tda01/translations/ja-zh-Hans.csv --column cn_text
```

这只检查字符是否在字体 cmap 中。AGE2 还要核对配置、语言槽、松散覆盖和实际显示；rUGP 还要核对字体加载、家族替换和版本绑定；图片另查排版、笔画和视觉融合。需要补字时才用[子集扩展工具](../Tools-LetToolsHandleRepetition/extend_font_subset.py)，PM 度量专项见 [rUGP 字体工具](../../rUGP/tools/fonts/README.md)。新语言重新做其字符覆盖和排版检查。
