# 译文修订数据与回归输入

[本地化参考](../README.md) · [术语取舍实例](../../../../Localization-MakeGamesSpeak/Glossaries-KeepItConsistent/decisions.md) · [现行译文位置](../../asset-map.md)

这里保留可维护表的修订数据和测试所需的上下文。阅读处理方法从上方实例进入；编辑新译文使用各作现行 CSV、术语与基线，不把历史 `after` 值当作永久批准名单。

| 数据 | 维护用途 |
| --- | --- |
| `main-al-alignment-20260909.json`、`tda-fragment-repairs-20260909.json` | 源身份、参考译法与片段修复回归 |
| `age2-native-clear-records-20260914.json` | 结构性空槽和 ParaTranz 同步回归 |
| `age2-text-loss-20260914.json`、`age2-auxiliary-context-20260914.json`、`age2-content-corrections-20260914.json` | 正文或字幕的缺漏、语境与说话人修订 |
| `age2-name-consistency-20260915.json`、`age2-norad-consistency-20260915.json`、`age2-terminology-20260920.json` | 现行表来源关联，含姓名、机构名、ruby 与术语修改 |
| `age2-dialogue-frames-20260916.json`、`age2-tda02-01986-line-break-20260919.json` | 对白括号及场景断行修复 |
| `main-al-image-impact-20260909.json` | 2026-09-09 的图片文案修改建议，按资源 ID 关联；该快照不说明后续玩家包的采用状态 |

记录使用游戏、资源 ID、源摘要和修改理由连接具体位置。源摘要用于防止错配；前后文本及范围说明用于理解修订。某个历史记录写着未安装或未重建发布包，仅描述那次修改的交付范围，不能据此判断后续包仍未更新。

图片建议涉及“轨道降下兵团／轨道空降兵团”与“伊尔玛／伊露玛”等用法。继续处理时先查现行术语、较新的图片文案与相应 Release，不能直接把这些旧候选覆盖到现在的资源上。

## English

These records support source association, translation maintenance and selected regressions. Use the current game tables for new edits. Historical before/after text is not an immutable approval list; dated image suggestions do not establish their adoption status in later player releases.
