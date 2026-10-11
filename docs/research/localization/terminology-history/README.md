# 术语维护与回归资料

[现行术语与基线](../../../../Localization-MakeGamesSpeak/Glossaries-KeepItConsistent/README.md) · [术语取舍实例](../../../../Localization-MakeGamesSpeak/Glossaries-KeepItConsistent/decisions.md)

日常查词和维护请使用各作 `project.toml` 登记的现行表、主基线及来源 CSV。主基线保留语境、候选和问题，来源表保留原译与出处；历史译法不自动作为当前采用译法加载。

本目录的机器数据用于术语回归：检查跨作污染、来源记录丢失、不同译法误合并，以及已排除映射重新进入使用表。旧混合表、恢复快照和后续修订数据属于这些检查的输入，不是翻译进度、现行总表或通用替换字典。

| 数据 | 回归用途 |
| --- | --- |
| `mixed-20260908.csv`、`imperial-20260908.csv`、`scope-audit-20260908.json` | 识别旧混合来源与已知错误映射 |
| `recovery-20260908.json` | 检查分作来源内容与身份未丢失 |
| `revision-20260920.json`、`baseline-additions-20261009.json` | 核对审定修改与后续补入的依据 |
| `imperial-review-20261009.json` | 帝都词项分类、具体场景和记录 ID；支持来源关联与回归 |

来源记录数、日文词形数与确认术语数各有不同含义，不直接相加；旧数据中的计数仅对应其记录版本。候选与未定位语境不能因为进入基线就视为已审定。

字段、查询命令与维护规则见[术语流程](../../../../Localization-MakeGamesSpeak/Text-AITranslationWorthReading/04-terminology.md)。修改上述数据契约时运行对应的[研究测试](../tests)。

## English

These files are regression inputs for preventing scope contamination, loss of historical source entries and incorrect merging of different decisions. Use the maintained game glossary and contextual baseline for translation. Historical counts and wording describe their recorded versions, not the current translation or proofreading progress.
