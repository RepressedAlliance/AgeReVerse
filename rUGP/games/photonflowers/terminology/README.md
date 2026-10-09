# 光子之花术语与基线

[返回本作](../README.md) · [术语维护规则](../../../../localization/text/04-terminology.md)

- [本作术语表](../../../../localization/glossaries/photonflowers.ja-zh-Hans.csv)：313条，查当前采用译法及`context`使用限制。
- [本作基线](baseline.ja-zh-Hans.csv)：1889条来源记录、1193种去重后的日文写法，查语境、旧译、候选和处理依据。
- [系列通用表](../../../../localization/glossaries/muv-luv.ja-zh-Hans.csv)：与本作表共同使用，不加载其他作品专表。

数量按2026-10-09当前CSV统计。基线保留同一词的不同来源，记录数和不同词形数都不是已确认术语数。

## 如何使用

先在本作术语表查采用译法，再按`context`确认人物、篇章、呼号或说话人范围。基线的`cn`可能是旧译、历史候选或空值，不能仅凭`status`或命中词形覆盖现行译文。同一日文可以随语境采用不同译法；表内没有做全局替换的授权。

基线的字段、状态、来源记录编号和出现次数口径见[字段说明](../../../../localization/text/04-terminology.md#公开基线字段与状态)。`source_row`定位的是来源表中的记录，不是游戏台词编号。

## 来源与覆盖范围

本作基线承接已找到的旧术语表和详细基线，并保存后续修订记录。旧表以合集保存的篇章范围仍按原合集记录。它记录已找到的资料，不代表已经穷举本作全部专名或逐项审定所有候选。

| 来源标识 | 本作含义 |
| --- | --- |
| `selected-photonflowers` | 先前暂定专表及精确说话人映射 |
| `pf-ex-table`、`pf-ex-baseline` | EX旧术语表与详细基线，分别为88条和945条来源记录 |
| `pf-al-table` | AL五篇合并旧表，共98条来源记录 |
| `mixed`、`legacy`、`legacy-tsv` | 旧词库在本作日文中的命中记录 |
| `photon-native` | 适用于本作的CRsa联合术语记录 |
| `glossary-20261009-photonflowers` | 本次补录的15条现行术语；来源是现行表已有译法与使用限制 |
| `current-glossary-20261009-photonflowers` | 截至本轮整理的313条现行采用记录，完整保留术语表使用限制；与旧来源分开读取 |

来源的历史路径、提交与原始规模见[恢复说明](../../../../docs/research/localization/terminology-history/recovery-20260908.md)和[恢复清单](../../../../docs/research/localization/terminology-history/recovery-20260908.json)。其中旧路径描述当时的位置；当前术语和基线路径以本作`project.toml`为准。2026-09-20修订见[逐条记录](../../../../docs/research/localization/terminology-history/revision-20260920.json)。

2026-10-09新增的15条只补齐已采用术语的基线记录，译法和使用限制均沿用现行表。没有注明具体篇章的条目如实保留这个限制，不补造出现次数或原文证据。对应词条、现行表记录编号及来源版本见[补录记录](../../../../docs/research/localization/terminology-history/baseline-additions-20261009.json)。

后续正文校对另见[BETA 0.1.2校对更新](../../../../docs/project/photon-beta012-proofreading.md)，包含柚子コショウ的贡献署名。正文反馈不会自动成为新术语；历史空中文候选也不因这次整理而补成定稿。

## 本轮基线整理

本次在原有1576条记录后追加313条现行采用记录；原有译法、状态和来源全部保留。记录数增加是为了把当前决定与历史证据分开，不是新增了313个术语。译法沿用现行术语表，没有修改游戏正文。

[整理明细](review-20261009.md)列出原基线未同步的18项中文、说明修正及仍缺的定位。现行记录的`source_row`对应本版术语表记录编号（含表头）；`basis`先保留完整使用限制，再列出旧来源编号。

```powershell
python localization/tools/terminology.py photonflowers --baseline
python localization/tools/terminology.py photonflowers --baseline --group current
python localization/tools/terminology.py photonflowers --check-baseline
```

`current`查现行决定；`reference`查历史／语境参考；`candidate`、`question`、`excluded`分别查候选、疑问和排除记录。`noise`只筛出旧依据已明确记为普通片假名／拟声或正则误命中的记录，不改旧状态。
