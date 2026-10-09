# TDA01术语与基线

[返回本作](../README.md) · [术语维护规则](../../../../localization/text/04-terminology.md)

- [本作术语表](../../../../localization/glossaries/tda01.ja-zh-Hans.csv)：89条，查当前采用译法及`context`使用限制。
- [本作基线](baseline.ja-zh-Hans.csv)：484条来源记录、191个不同日文词形，查语境、旧译、候选和处理依据。
- [系列通用表](../../../../localization/glossaries/muv-luv.ja-zh-Hans.csv)：与本作表共同使用，不加载其他作品专表。

数量按2026-10-09当前CSV统计。基线保留同一词的不同来源，记录数和不同词形数都不是已确认术语数。

## 如何使用

先在本作术语表查采用译法，再按`context`确认人物、篇章、呼号或说话人范围。基线的`cn`可能是旧译、历史候选或空值，不能仅凭`status`或命中词形覆盖现行译文。同一日文可以随语境采用不同译法；表内没有做全局替换的授权。

基线的字段、状态、来源记录编号和出现次数口径见[字段说明](../../../../localization/text/04-terminology.md#公开基线字段与状态)。`source_row`定位的是来源表中的记录，不是游戏台词编号。

## 来源与覆盖范围

本作基线由旧词库与本作日文记录的哈希对齐结果重建；本次历史查证没有找到与Photon同格式的旧独立详细基线。它记录已找到的资料，不代表已经穷举本作全部专名或逐项审定所有候选。

| 来源标识 | 本作含义 |
| --- | --- |
| `selected-tda01` | 先前暂定专表，使用限制保留在basis中 |
| `mixed`、`legacy`、`legacy-tsv` | 旧词库在本作日文中的命中记录；命中本身不等于译法已确认 |
| `tda-shared-decisions` | 旧TDA交接记录中适用于本作的决定 |
| `maintainer-20260920` | 2026-09-20审定后新增的条目；此前已有来源的修订仍保留原来源标识 |

来源的历史路径、提交与原始规模见[恢复说明](../../../../docs/research/localization/terminology-history/recovery-20260908.md)和[恢复清单](../../../../docs/research/localization/terminology-history/recovery-20260908.json)。其中旧路径描述当时的位置；当前术语和基线路径以本作`project.toml`为准。2026-09-20修订见[逐条记录](../../../../docs/research/localization/terminology-history/revision-20260920.json)。
