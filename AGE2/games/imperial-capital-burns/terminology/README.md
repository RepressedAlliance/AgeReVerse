# 帝都燃烧篇术语与基线

[返回本作](../README.md) · [术语维护规则](../../../../localization/text/04-terminology.md)

- [本作术语表](../../../../localization/glossaries/imperial-capital-burns.ja-zh-Hans.csv)：183条，查当前采用译法及`context`使用限制。
- [本作基线](baseline.ja-zh-Hans.csv)：264条来源记录、185个不同日文词形，查语境、旧译、候选和处理依据。
- [系列通用表](../../../../localization/glossaries/muv-luv.ja-zh-Hans.csv)：与本作表共同使用，不加载其他作品专表。

数量按2026-10-09当前CSV统计。基线保留同一词的不同来源，记录数和不同词形数都不是已确认术语数。

## 如何使用

先在本作术语表查采用译法，再按`context`确认人物、篇章、呼号或说话人范围。基线的`cn`可能是旧译、历史候选或空值，不能仅凭`status`或命中词形覆盖现行译文。同一日文可以随语境采用不同译法；表内没有做全局替换的授权。

基线的字段、状态、来源记录编号和出现次数口径见[字段说明](../../../../localization/text/04-terminology.md#公开基线字段与状态)。`source_row`定位的是来源表中的记录，不是游戏台词编号。

## 来源与覆盖范围

本作基线承接已找到的旧术语表和详细基线，并保存后续修订记录。旧表以合集保存的篇章范围仍按原合集记录。它记录已找到的资料，不代表已经穷举本作全部专名或逐项审定所有候选。

| 来源标识 | 本作含义 |
| --- | --- |
| `selected-imperial-capital-burns` | 先前暂定专表 |
| `imperial-old` | 旧独立表，共185条来源记录 |

来源的历史路径、提交与原始规模见[恢复说明](../../../../docs/research/localization/terminology-history/recovery-20260908.md)和[恢复清单](../../../../docs/research/localization/terminology-history/recovery-20260908.json)。其中旧路径描述当时的位置；当前术语和基线路径以本作`project.toml`为准。2026-09-20修订见[逐条记录](../../../../docs/research/localization/terminology-history/revision-20260920.json)。
