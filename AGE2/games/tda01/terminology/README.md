# TDA01术语与基线

[返回本作](../README.md) · [术语维护规则](../../../../Localization-Make-Games-Speak/Text-AI-Translation-Worth-Reading/04-terminology.md)

- [本作术语表](../../../../Localization-Make-Games-Speak/Glossaries-Keep-It-Consistent/tda01.ja-zh-Hans.csv)：89条，查当前采用译法及`context`使用限制。
- [主基线](baseline.ja-zh-Hans.csv)：196条，189种日文写法，查现行译法、语境、候选和待核问题。
- [原始来源](history/evidence-20261009.csv)：484条，保留原状态、译法和出现次数，供追溯。
- [系列通用表](../../../../Localization-Make-Games-Speak/Glossaries-Keep-It-Consistent/muv-luv.ja-zh-Hans.csv)：与本作表共同使用，不加载其他作品专表。

数量按2026-10-09当前CSV统计。主表条目与来源记录分开计数，都不代表全文人工审核进度。

## 如何使用

先在本作术语表查采用译法，再按`context`确认人物、篇章、呼号或说话人范围。主基线用`kind`区分现行术语、参考、候选和问题；其他译法不能仅因日文相同就覆盖现行译文。同一日文可以随语境采用不同译法；表内没有做全局替换的授权。

主表与来源表的字段、状态、编号和出现次数口径见[字段说明](../../../../Localization-Make-Games-Speak/Text-AI-Translation-Worth-Reading/04-terminology.md#公开基线字段与状态)。主表的`evidence_rows`指向本目录来源CSV；来源表的`source_row`回指更早输入文件的原记录编号，二者不能混用，都不是游戏台词编号。

## 原始来源与覆盖范围

以下来源原样保存在[来源表](history/evidence-20261009.csv)，不与日常主表混排。

本作基线由旧词库与本作日文记录的哈希对齐结果重建；本次历史查证没有找到与Photon同格式的旧独立详细基线。它记录已找到的资料，不代表已经穷举本作全部专名或逐项审定所有候选。

| 来源标识 | 本作含义 |
| --- | --- |
| `selected-tda01` | 先前暂定专表，使用限制保留在basis中 |
| `mixed`、`legacy`、`legacy-tsv` | 旧词库在本作日文中的命中记录；命中本身不等于译法已确认 |
| `tda-shared-decisions` | 旧TDA交接记录中适用于本作的决定 |
| `maintainer-20260920` | 2026-09-20审定后新增的条目；此前已有来源的修订仍保留原来源标识 |

来源的历史路径、提交与原始规模见[恢复说明](../../../../docs/research/localization/terminology-history/recovery-20260908.md)和[恢复清单](../../../../docs/research/localization/terminology-history/recovery-20260908.json)。其中旧路径描述当时的位置；当前术语和基线路径以本作`project.toml`为准。2026-09-20修订见[逐条记录](../../../../docs/research/localization/terminology-history/revision-20260920.json)。

## 精简主基线的读法

主表六列为`jp,cn,kind,chapter,basis,evidence_rows`。现行术语89条，候选105条，其他来源／语境译法2条。每条现行术语只保留一条；相同日文、中文及类别合并来源，不同中文或候选／待核状态分别保留。

`basis`保留完整使用限制；`chapter`是来源已知的篇章范围，不能代替使用限制。`evidence_rows`是本目录来源CSV的记录编号，以分号分隔，含表头从1计，不是游戏台词编号。旧来源的状态和出现次数原样保留，次数不跨来源相加。原已排除及明确误命中的资料只留在来源表，未审候选不自动确认。

[整理明细](review-20261009.md)列出数量变化和资料限制。默认查主表；`--term`同时返回当前术语与关联来源，程序不必解析说明文字：

```powershell
python Localization-Make-Games-Speak/Tools-Let-Tools-Handle-Repetition/terminology.py tda01 --baseline
python Localization-Make-Games-Speak/Tools-Let-Tools-Handle-Repetition/terminology.py tda01 --baseline --term インド
python Localization-Make-Games-Speak/Tools-Let-Tools-Handle-Repetition/terminology.py tda01 --baseline --history
python Localization-Make-Games-Speak/Tools-Let-Tools-Handle-Repetition/terminology.py tda01 --check-baseline
```
