# 光子之花术语与基线

[返回本作](../README.md) · [术语维护规则](../../../../Localization-Make-Games-Speak/Text-AI-Translation-Worth-Reading/04-terminology.md)

- [本作术语表](../../../../Localization-Make-Games-Speak/Glossaries-Keep-It-Consistent/photonflowers.ja-zh-Hans.csv)：313条，查当前采用译法及`context`使用限制。
- [主基线](baseline.ja-zh-Hans.csv)：566条，447种日文写法，查现行译法、语境、候选和待核问题。
- [原始来源](history/evidence-20261009.csv)：1576条，保留原状态、译法和出现次数，供追溯。
- [系列通用表](../../../../Localization-Make-Games-Speak/Glossaries-Keep-It-Consistent/muv-luv.ja-zh-Hans.csv)：与本作表共同使用，不加载其他作品专表。

数量按2026-10-09当前CSV统计。主表条目与来源记录分开计数，都不代表全文人工审核进度。

## 如何使用

先在本作术语表查采用译法，再按`context`确认人物、篇章、呼号或说话人范围。主基线用`kind`区分现行术语、参考、候选和问题；其他译法不能仅因日文相同就覆盖现行译文。同一日文可以随语境采用不同译法；表内没有做全局替换的授权。

主表与来源表的字段、状态、编号和出现次数口径见[字段说明](../../../../Localization-Make-Games-Speak/Text-AI-Translation-Worth-Reading/04-terminology.md#公开基线字段与状态)。主表的`evidence_rows`指向本目录来源CSV；来源表的`source_row`回指更早输入文件的原记录编号，二者不能混用，都不是游戏台词编号。

## 原始来源与覆盖范围

以下来源原样保存在[来源表](history/evidence-20261009.csv)，不与日常主表混排。

本作基线承接已找到的旧术语表和详细基线，并保存后续修订记录。旧表以合集保存的篇章范围仍按原合集记录。它记录已找到的资料，不代表已经穷举本作全部专名或逐项审定所有候选。

| 来源标识 | 本作含义 |
| --- | --- |
| `selected-photonflowers` | 先前暂定专表及精确说话人映射 |
| `pf-ex-table`、`pf-ex-baseline` | EX旧术语表与详细基线，分别为88条和945条来源记录 |
| `pf-al-table` | AL五篇合并旧表，共98条来源记录 |
| `mixed`、`legacy`、`legacy-tsv` | 旧词库在本作日文中的命中记录 |
| `photon-native` | 适用于本作的CRsa联合术语记录 |
| `glossary-20261009-photonflowers` | 本次补录的15条现行术语；来源是现行表已有译法与使用限制 |

来源的历史路径、提交与原始规模见[恢复说明](../../../../docs/research/localization/terminology-history/recovery-20260908.md)和[恢复清单](../../../../docs/research/localization/terminology-history/recovery-20260908.json)。其中旧路径描述当时的位置；当前术语和基线路径以本作`project.toml`为准。2026-09-20修订见[逐条记录](../../../../docs/research/localization/terminology-history/revision-20260920.json)。

2026-10-09新增的15条只补齐已采用术语的基线记录，译法和使用限制均沿用现行表。没有注明具体篇章的条目如实保留这个限制，不补造出现次数或原文证据。对应词条、现行表记录编号及来源版本见[补录记录](../../../../docs/research/localization/terminology-history/baseline-additions-20261009.json)。

后续正文校对另见[BETA 0.1.2校对更新](../../../../docs/project/photon-beta012-proofreading.md)，包含柚子コショウ的贡献署名。正文反馈不会自动成为新术语；历史空中文候选也不因这次整理而补成定稿。

## 精简主基线的读法

主表六列为`jp,cn,kind,chapter,basis,evidence_rows`。现行术语313条，语境参考64条，待核问题28条，候选108条，其他来源／语境译法53条。每条现行术语只保留一条；相同日文、中文及类别合并来源，不同中文或候选／待核状态分别保留。

`basis`保留完整使用限制；`chapter`是来源已知的篇章范围，不能代替使用限制。`evidence_rows`是本目录来源CSV的记录编号，以分号分隔，含表头从1计，不是游戏台词编号。旧来源的状态和出现次数原样保留，次数不跨来源相加。原已排除及明确误命中的资料只留在来源表，未审候选不自动确认。

[整理明细](review-20261009.md)列出数量变化和资料限制。默认查主表；`--term`同时返回当前术语与关联来源，程序不必解析说明文字：

```powershell
python Localization-Make-Games-Speak/Tools-Let-Tools-Handle-Repetition/terminology.py photonflowers --baseline
python Localization-Make-Games-Speak/Tools-Let-Tools-Handle-Repetition/terminology.py photonflowers --baseline --term YOKOHAMAスカイウォーカー
python Localization-Make-Games-Speak/Tools-Let-Tools-Handle-Repetition/terminology.py photonflowers --baseline --history
python Localization-Make-Games-Speak/Tools-Let-Tools-Handle-Repetition/terminology.py photonflowers --check-baseline
```
