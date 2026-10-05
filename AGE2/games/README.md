# AGE2 游戏项目

[返回 AGE2](../README.md) · [玩家指南](../../docs/player/README.md) · [完整资产地图](../../docs/research/asset-map.md) · [通用本地化工作流](../../localization/text/workflow.md)

每个目录是一部独立游戏。`project.toml` 记录 Steam App ID、开发状态以及文本、图片和
字体权威入口；`translations/` 保存可维护译文；`images/` 保存图片文案或历史 Release
图片清单。补丁里的字体和 WebP 二进制继续留在 Release，不在 Git 中重复保存。当前字体逐作配置见[字体目录](../../localization/fonts/README.md)。

| 游戏 | App ID | 主要文本 | 历史 Release 中的 WebP | 玩家状态 |
| --- | ---: | ---: | ---: | --- |
| [TDA00](tda00/) | 1407100 | 3,713 行 | [70 项](tda00/images/) | [BETA 0.2.1](https://github.com/RepressedAlliance/AgeReVerse/releases/tag/tda00-BETA-0.2.1) |
| [TDA01](tda01/) | 1407090 | 8,565 行 | [93 项](tda01/images/) | [BETA 0.3.3](https://github.com/RepressedAlliance/AgeReVerse/releases/tag/tda01-BETA-0.3.3) |
| [TDA02](tda02/) | 1342410 | 6,589 行 | [100 项](tda02/images/) | [BETA 0.2.1](https://github.com/RepressedAlliance/AgeReVerse/releases/tag/tda02-BETA-0.2.1) |
| [TDA03](tda03/) | 789830 | 6,913 行 | [152 项](tda03/images/) | [BETA 0.2.7](https://github.com/RepressedAlliance/AgeReVerse/releases/tag/tda03-BETA-0.2.7) |
| [帝都燃烧篇](imperial-capital-burns/) | 2630300 | 5,564 行正文及辅助表 | [315 项](imperial-capital-burns/images/) | [BETA 0.2.1](https://github.com/RepressedAlliance/AgeReVerse/releases/tag/imperial-capital-burns-BETA-0.2.1) |
| [君望 Enhanced Edition](kiminozo/) | 1777440 | 文本审核中，正文尚未公开 | [UI、图片与字体制作中](kiminozo/images/) | 在制，尚未发布补丁 |

君望项目同时整理 Another Episode Collection+（App ID 3112140）；本篇与附加篇分别管理。
详见[项目范围及当前进度](kiminozo/README.md)。在制项目的清单可以暂不登记正文和图片权威文件，
但必须说明状态；文档入口不充当已完成的数据表或发布清单。

WebP 数量是对应历史 ZIP 中实际存在的图片成员数，不等于“独立翻译图片数”。同一内容
可能同时覆盖 `_ja`、`_zh` 或无语言后缀路径，也可能是为保证 UI 完整而复制的官方
fallback。每部游戏的 `release-inventory.json` 保存逐项路径、尺寸、模式和 SHA-256，
供后续权利审计、去重和重新构建使用。

## 新增游戏的最小要求

1. 建立 `project.toml`，不要复制另一作的 App ID、语言槽或资源路径。
2. 把可维护文本放入 `translations/`，以稳定 ID 和源哈希绑定合法提取。
3. 图片存在时建立 `images/` 清单；没有图片时在项目状态中明确写“未建立”，不建空目录。
4. 字体按照[统一字体政策](../../localization/fonts/README.md)处理。
5. 写回工具、测试和实机结果必须属于该作，不能用另一作成功来代替。
