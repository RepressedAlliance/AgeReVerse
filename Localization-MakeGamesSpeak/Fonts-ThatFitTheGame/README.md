# 字体排版｜别让字体出卖你的补丁

**Fonts & Typography: Don't Let Fonts Give Your Patch Away**

[返回本地化](../README.md) · **[七作图片用字总表](audit.md)** · [游戏文本字体](runtime.md) · [图片用字与样式](images.md) · [作者与许可](attribution.md) · [新图片登记](registration.md)

译文进入游戏以后，还要放得下、看得清，并贴合作品原有的气质。这里集中维护 TDA00–03、帝都燃烧、PF 和 PM 的字体选择、使用位置与来源。运行时正文与图片里的字分别登记：替换正文的字体不会改变图片中已经画好的文字。

图片逐图表覆盖下列版本补丁携带的 **3,720 个独立图片文件**，包括五作 AGE2 的 859 个 WebP／AVIF 文件和 PF／PM 的 2,861 个 PNG 文件。每项关联实际字体、继承字层、原图沿用或生成方式；历史试样与 365 项本地候选另列，不混入当前发布版。

<details>
<summary><strong>English · Don't Let Fonts Give Your Patch Away — expand here</strong></summary>

This guide separates runtime text fonts from lettering baked into images. The release registers cover 3,720 image files carried by the seven listed patch versions; historical trials and local candidates are separate. The catalog contains 37 specific font inputs, faces or versions: 36 have material or typography-prototype uses, and one is comparison-only. Untouched original lettering is not assigned a guessed font. Start with the [game/image usage tables](audit.md), [credits and licenses](attribution.md), [registration guide](registration.md) and [typography methods](typography.md). Some exact historical font binaries and production inputs remain unavailable; the [limitations](font-evidence.md) identify the affected materials.

</details>

## 当前发布版使用什么

| 游戏 | 对应版本 | 中文运行时方案 |
| --- | --- | --- |
| TDA00 | BETA 0.2.1 | 下列 AGE2 六个角色 |
| TDA01 | BETA 0.3.3 | 同上 |
| TDA02 | BETA 0.2.1 | 同上 |
| TDA03 | BETA 0.2.7 | 同上 |
| 帝都燃烧 | BETA 0.2.1 | 同上 |
| PF | BETA 0.1.2 | PF 专用 `PhotonR2-Regular.ttf` |
| PM | BETA 0.1.2 | PM 专用 `PhotonR2-Regular.ttf` |

AGE2 中文实际配置是：系统 **AGE2 UI Sans SC Dash**、正文 **白无常可可体粗**、姓名 **美呗嘿嘿体**、HUD **Noto Sans SC 500**、语言选择 **IBM Plex Sans SC Regular**、备用 **AGE2 Fallback SC Dash**。具体配置、随包附带但未被当前中文配置选用的文件，见[运行时对应表](runtime.md)。

PF／PM 都请求 `PhotonR2` 家族，但两作的字集和修正不同，**同名文件不能互换**。图片制作使用过的旧 PhotonCN、旧 PhotonR2 与当前运行时版本也分别登记。

## 图片字体、来源与复用

[七作用字总表](audit.md)按游戏和字体查询；[图片说明](images.md)列素材组和样式；[版本目录](catalog.json)维护精确字体文件、字重、TTC 索引及许可身份；[逐图表索引](image-font-index.json)说明各清单的范围与计数单位。

感谢这些字体项目与作者为正文显示和图片制作提供字形基础：

| 字体家族／派生基础 | 来源与许可 |
| --- | --- |
| Noto Sans／Serif CJK | [Noto CJK](https://github.com/notofonts/noto-cjk)，OFL 1.1 |
| 思源黑体、PhotonCN／PhotonR2 派生基础 | [Source Han Sans](https://github.com/adobe-fonts/source-han-sans)，OFL 1.1 |
| IBM Plex Sans SC、AGE2 UI Sans 派生基础 | [IBM Plex](https://github.com/IBM/plex)，OFL 1.1 |
| 源石黑体、AGE2 GenSeki 派生基础 | [GenSeki](https://github.com/ButTaiwan/genseki-font)，OFL 1.1 |
| 狮尾加糖宋体 Medium／SemiBold | [Swei Sugar](https://github.com/max32002/swei-sugar)，OFL 1.1 |
| 思源宋体、霞鹜文楷 GB、得意黑、小赖、马善政等图片用字 | [完整作者与许可表](attribution.md)，按实际用途区分发布、试样和在制输入 |
| 白无常可可体 | [作者发布页](https://www.zcool.com.cn/work/ZNTk4NTI2ODA%3D.html)，作者使用声明，不属于 OFL |
| 美呗嘿嘿体 | [作者发布页](https://www.zcool.com.cn/work/ZNTY3OTI5ODg%3D.html)，作者使用声明，不属于 OFL |

白无常可可体和美呗嘿嘿体的项目版本包含缺字补充。现有来源资料尚不足以重新确认作者声明对修改版本的全部适用条件；使用和再分发须核对相应要求，不能以旧说明中的“未修改字集”代替修改后的构建记录。

部分图片也用过楷体、宋体、MS Mincho、微软雅黑、黑体、BIZ 和等线等 Windows 字体，它们不属于本项目的开源字体清单。图片致谢与分发字体软件的要求分别见[许可说明](attribution.md)。字体二进制通过适当的发布包提供，仓库维护目录与配方。

## 做新图或换字体

按[登记规范](registration.md)留下实际用字、作者来源、许可、配方与采用版本。同图混用和继承字层也要记录；字体文件缺失、旧版本不明及未发布素材的具体范围见[版本与资料限制](font-evidence.md)。浏览器后备字体、TTC 索引和字层继承的处理方法见[排字技术说明](typography.md)。

```powershell
python -m Localization-MakeGamesSpeak.Tools-LetToolsHandleRepetition.font_coverage work/TargetFont.ttf AGE2/games/tda01/translations/ja-zh-Hans.csv --column cn_text
```

这个命令只检查 cmap 字符覆盖。正文还需检查配置、语言槽、字体加载、字宽和换行；图片另查笔画、排版和视觉融合。需要补字时使用[子集扩展工具](../Tools-LetToolsHandleRepetition/extend_font_subset.py)，PM 度量专项见 [rUGP 字体工具](../../rUGP/tools/fonts/README.md)。
