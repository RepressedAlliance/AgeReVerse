# 字体排版｜别让字体出卖你的补丁

**Fonts & Typography: Don't Let Fonts Give Your Patch Away**

[返回本地化](../README.md) · **[游戏字体对应表](runtime.md)** · **[图片用字与样式](images.md)** · [精确版本目录](catalog.json)

<details>
<summary><strong>English · Don't Let Fonts Give Your Patch Away — expand here</strong></summary>

The catalog covers the seven released games, original AGE2 roles, every bundled AGE2 font, the distinct PF/PM PhotonR2 binaries, and known image-authoring inputs. Runtime selection, bundled-but-unused fonts, image production and historical trials are separate. Source hashes identify files; they do not establish visual acceptance or grant redistribution rights. For another locale, check its own coverage, shaping, metrics and engine selection.

</details>

译文进入游戏以后，还要放得下、看得清，并贴合作品原有的气质。这里集中维护七作的字体选择与来源，游戏文本和图片烘焙用字分别登记。替换运行时字体不会改变已画进图片的文字，重画图片也不会修复正文的选字、字宽或换行。

运行时对应表按下列发布版本列出实际配置；图片用字表区分采用方案、历史试样和在制素材。当前图片表尚未覆盖所有成品，未登记的用字不能仅凭外观推定。

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

AGE2 中文实际配置是：系统 **AGE2 UI Sans SC Dash**、正文 **白无常可可体粗**、姓名 **美呗嘿嘿体**、HUD **Noto Sans SC 500**、语言选择 **IBM Plex Sans SC Regular**、备用 **AGE2 Fallback SC Dash**。各角色分别选型，配置与文件身份见[游戏字体对应表](runtime.md)。

PF／PM 都请求 `PhotonR2` 家族，但两作字体字集和修正不同，**文件同名不代表内容相同，不能互换**。旧 `PhotonCN`、早期 PhotonR2 与当前发布包分别记录；详见[运行时对应表](runtime.md)。

## 来源与复用

感谢以下字体项目与作者，为本项目的文本显示与图片制作提供字形基础。

| 字体家族 | 来源 |
| --- | --- |
| Noto Sans／Serif CJK | [Noto CJK](https://github.com/notofonts/noto-cjk)，OFL 1.1 |
| 思源黑体、PhotonR2 派生基础 | [Source Han Sans](https://github.com/adobe-fonts/source-han-sans)，OFL 1.1 |
| IBM Plex Sans SC、AGE2 UI Sans 派生基础 | [IBM Plex](https://github.com/IBM/plex)，OFL 1.1 |
| 源石黑体、AGE2 GenSeki 派生基础 | [GenSeki](https://github.com/ButTaiwan/genseki-font)，OFL 1.1 |
| 狮尾加糖宋体 | [Swei Sugar](https://github.com/max32002/swei-sugar)，OFL 1.1 |
| 白无常可可体 | [作者发布页](https://www.zcool.com.cn/work/ZNTk4NTI2ODA%3D.html)，作者使用声明；不属于 OFL |
| 美呗嘿嘿体 | [作者发布页](https://www.zcool.com.cn/work/ZNTY3OTI5ODg%3D.html)，作者使用声明；不属于 OFL |

白无常可可体和美呗嘿嘿体的项目版本包含缺字补充，按作者使用声明处理；使用与再分发须核对声明对修改版本的适用要求。各字体的版本与修改说明见[字体目录](catalog.json)，实际用途分别见[游戏文本字体](runtime.md)与[图片用字](images.md)。随包附带但当前未使用的字体，在对应表中单独标注。

制作或更换字体时，同步登记实际文件版本、来源、许可及补字、子集化等修改。复用与分发遵循对应字体的许可，保留所需版权与许可文件；派生字体的命名按其上游要求处理。二进制通过适当的发布包提供，仓库维护目录与配方。

## 覆盖与实机

```powershell
python -m Localization-MakeGamesSpeak.Tools-LetToolsHandleRepetition.font_coverage work/TargetFont.ttf AGE2/games/tda01/translations/ja-zh-Hans.csv --column cn_text
```

这只检查字符是否在字体 cmap 中。AGE2 还要核对配置、语言槽、松散覆盖和实际显示；rUGP 还要核对字体加载、家族替换和版本绑定；图片另查排版、笔画和视觉融合。需要补字时才用[子集扩展工具](../Tools-LetToolsHandleRepetition/extend_font_subset.py)，PM 度量专项见 [rUGP 字体工具](../../rUGP/tools/fonts/README.md)。新语言重新做其字符覆盖和排版检查。
