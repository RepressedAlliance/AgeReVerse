# 十分钟入门：查术语，并看懂结果

**First ten minutes: look up a term and understand the result**

[研究入口](README.md) · [本地化方法](../../Localization-MakeGamesSpeak/README.md) · [工具目录](../../Localization-MakeGamesSpeak/Tools-LetToolsHandleRepetition/README.md) · [提问或建议](https://github.com/RepressedAlliance/AgeReVerse/issues/new?template=question.yml)

先做一件小事：查询 TDA00 里“戦術機”现在怎样译。这个例子只读取仓库公开的术语数据，**不需要游戏文件、字体、AI 账号或额外 Python 库**，也不会修改译文。

## 1. 准备代码

需要 Python 3.12 或更新版本，以及 Git。在终端运行：

```powershell
git clone https://github.com/RepressedAlliance/AgeReVerse.git
cd AgeReVerse
```

如果已经有仓库，进入现有仓库根目录即可。

## 2. 查询一个词

```powershell
python -X utf8 -m Localization-MakeGamesSpeak.Tools-LetToolsHandleRepetition.terminology tda00 --term 戦術機 | python -X utf8 -m json.tool --no-ensure-ascii
```

结果包含：

```json
{
    "jp": "戦術機",
    "cn": "战术机",
    "context": "仅作翻译审校参考；确认对应专名/军事称谓后使用，不自动替换正文",
    "scope": "common"
}
```

不用熟悉 JSON，也可以这样理解：

| 字段 | 它告诉你什么 |
| --- | --- |
| `jp` | 查询的日文词是“戦術機” |
| `cn` | 现行术语表给出的中文是“战术机” |
| `context` | 使用前仍需确认专名、称谓及具体语境；工具不会替你改正文 |
| `scope` | `common` 表示这个词来自明确适用于本作的系列共用术语表；其他词也可能来自本作专用表 |

`--term` 按**完整日文词条**查询。返回 `null` 表示有效术语表中没有这个精确词条，不等于正文漏译，也不能据此自动新增译法。

## 3. 下一步按目的选

| 你想继续做什么 | 去哪里 |
| --- | --- |
| 看基线怎样成为术语、怎样保持全文一致 | [术语与全文一致性](../../Localization-MakeGamesSpeak/Glossaries-KeepItConsistent/README.md)；候选和历史依据不会自动覆盖现行译法 |
| 学习 AI 辅助翻译和独立复核 | [文本翻译五阶段](../../Localization-MakeGamesSpeak/Text-AITranslationWorthReading/workflow.md) |
| 提取、分类和制作中文图片 | [图片汉化五阶段](../../Localization-MakeGamesSpeak/Images-MakeItLookNative/README.md)；真实提取需要合法且版本匹配的游戏输入 |
| 深入 FPD／EGPACK 或 RIO／CRsa 等格式 | [AGE2](../../AGE2/README.md) · [rUGP](../../rUGP/README.md)，按具体工具准备输入 |
| 遇到问题，或想补充说明 | [问题咨询与建议](https://github.com/RepressedAlliance/AgeReVerse/issues/new?template=question.yml) |

这个例子展示的是公开术语的查询与解释。构建玩家补丁仍需相应游戏的合法输入、制作资产、引擎适配及人工审核，详见各作工具与发布说明。

<details>
<summary><strong>English · Try the first tool and understand its output — expand here</strong></summary>

Start by looking up one adopted term for TDA00. This example reads public terminology only, requires Python 3.12 or newer and Git, and needs no game files, fonts, AI account or extra Python packages. It does not edit dialogue.

```powershell
git clone https://github.com/RepressedAlliance/AgeReVerse.git
cd AgeReVerse
python -X utf8 -m Localization-MakeGamesSpeak.Tools-LetToolsHandleRepetition.terminology tda00 --term 戦術機 | python -X utf8 -m json.tool --no-ensure-ascii
```

Use your existing repository root if you already have a checkout. The output shown above contains four fields:

| Field | Meaning |
| --- | --- |
| `jp` | The exact Japanese term queried: 戦術機 |
| `cn` | Its current Chinese glossary rendering: 战术机 |
| `context` | A reminder to confirm the proper-name or military usage in context; no automatic dialogue replacement occurs |
| `scope` | `common` means an explicitly applicable shared series glossary; other entries can come from the selected game's own glossary |

`--term` requires an exact Japanese key. `null` means no exact entry in the effective glossary, not missing dialogue or permission to invent a translation. Historical and candidate baseline records do not automatically override adopted terminology.

Continue with the [consistency guide](../../Localization-MakeGamesSpeak/Glossaries-KeepItConsistent/README.md), [English text workflow](../../Localization-MakeGamesSpeak/Text-AITranslationWorthReading/workflow.en.md), [image workflow](../../Localization-MakeGamesSpeak/Images-MakeItLookNative/README.md), or the [AGE2](../../AGE2/README.md) / [rUGP](../../rUGP/README.md) tool guides. Real extraction and patch production need legally held, matching game inputs and the documented authoring and review steps. Ask through the [general question form](https://github.com/RepressedAlliance/AgeReVerse/issues/new?template=question.yml).

</details>
