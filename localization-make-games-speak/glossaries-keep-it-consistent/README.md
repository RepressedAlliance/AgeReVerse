# 现行术语表

[返回本地化工作区](../README.md) · [术语维护规则](../text-ai-translation-worth-reading/04-terminology.md)

这里集中存放Muv-Luv系列通用表和八作现行术语表。点击文件即可在GitHub查看日文、中文和使用语境。
Muv-Luv七作使用 **系列通用表 + 本作表**；君望独立使用本作表。

| 范围 | 术语表 | 条目数 |
| --- | --- | ---: |
| 系列通用 | [muv-luv.ja-zh-Hans.csv](muv-luv.ja-zh-Hans.csv) | 146 |
| TDA00 | [tda00.ja-zh-Hans.csv](tda00.ja-zh-Hans.csv) | 135 |
| TDA01 | [tda01.ja-zh-Hans.csv](tda01.ja-zh-Hans.csv) | 89 |
| TDA02 | [tda02.ja-zh-Hans.csv](tda02.ja-zh-Hans.csv) | 98 |
| TDA03 | [tda03.ja-zh-Hans.csv](tda03.ja-zh-Hans.csv) | 115 |
| 帝都燃烧篇 | [imperial-capital-burns.ja-zh-Hans.csv](imperial-capital-burns.ja-zh-Hans.csv) | 306 |
| 光子之花 | [photonflowers.ja-zh-Hans.csv](photonflowers.ja-zh-Hans.csv) | 313 |
| 光子旋律 | [photonmelodies.ja-zh-Hans.csv](photonmelodies.ja-zh-Hans.csv) | 750 |
| 君望（本篇及番外） | [kiminozo.ja-zh-Hans.csv](kiminozo.ja-zh-Hans.csv) | 167 |

每张表使用 `jp`（日文）、`cn`（中文）、`context`（适用语境）三列。
同一词在不同作品中的人物、称谓或场景可能不同，请连同语境阅读；各作专表不互相继承。
表中条目数按各表分别统计，不代表去重后的系列总数或全篇人工校对进度。

## 君望术语与基线

君望公开167条术语与360条基线记录：基线包含全部167条确认术语的依据，以及193条语境、候选和待核记录，涵盖本篇及番外已有整理结果，后续随审核更新。
[本作说明](../../AGE2/games/kiminozo/terminology/README.md)列出来源与待核状态。
基线放在`AGE2/games/kiminozo/terminology/`，是本作术语的父集，但不作为自动替换字典加载；君望也不继承Muv-Luv通用表。

## 维护与查词

直接编辑这里对应的现行表；各游戏的 `project.toml` 已指向这些文件，无须维护第二份副本。
新增或修改译法时，先在本作基线记录出处和判断依据，审定后更新现行表；有跨作依据才提升到通用表。

```powershell
python localization-make-games-speak/tools-let-tools-handle-repetition/terminology.py tda00 --term ウィル
python localization-make-games-speak/tools-let-tools-handle-repetition/terminology.py photonflowers --term ミキ
python localization-make-games-speak/tools-let-tools-handle-repetition/terminology.py kiminozo --term タケス
```

工具只读取本作明确登记的表；Muv-Luv通用与本作同词异译会报错。君望只读本作表，工具不会自动改写正文。

## 查证与历史资料

基线CSV仍放在各作品的`terminology/`中，本目录只集中维护现行术语表。各作品首页的“术语与基线”入口说明本作来源、适用范围和当前数量。

旧版本、恢复清单、审计记录及各作基线入口统一放在[术语查证与历史记录](../../docs/research/localization/terminology-history/README.md)。
候选、争议与历史译法不作为现行术语加载。

八作主基线都包含各自现行术语的中文和完整使用限制，每条现行术语只列一次；相同译法合并来源，不同语境、候选和待核状态保留区别。主表六列用于阅读及程序处理，原始九列来源表另存于本作`terminology/history/`。可用`--baseline --term 日文`同时取得条目和关联来源，或用`--baseline --group candidate`只看候选；加`--history`读取原始来源。逐作改动、数量及尚缺具体篇章定位的资料见上述整理明细。

## English

This folder contains the Muv-Luv shared glossary and eight game-specific glossaries.
Use shared + own for the seven Muv-Luv games; Kiminozo uses only its own table.
Respect each entry's `context`; contextual baselines remain under each game's directory.
These are the maintained source files, not duplicate exports. Historical evidence is kept
in the [terminology records](../../docs/research/localization/terminology-history/README.md).
