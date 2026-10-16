# 03 · 翻译与图片表字段约定

[规则顺序](README.md) · 上一步：[02 源数据](02-source-data.md) · 下一步：[04 术语](04-terminology.md)

[返回本地化工作区](../README.md) · [源数据规范](02-source-data.md) · [单个游戏项目清单](01-game-project.md)

本仓库有多代已经由 manifest 和 SHA-256 锁定的表。为了“看起来统一”直接重命名历史
表头，会改变整份 CSV 字节、破坏公开证据并让旧工具失配。因此采用两层规则：

1. 已封存表保留现有 schema，由工具显式声明字段映射；
2. 新建的跨引擎工作表使用下面的规范核心字段，按文字、语音或图片输入关联实际源证据。

## 新表的规范核心字段

| 字段 | 含义 |
| --- | --- |
| `stable_id` | 不依赖当前排序的资源/文本身份 |
| `source_locale` | 已声明源内容的 BCP 47 语源，例如 `ja`；不从底稿语言或写回槽位猜测 |
| `target_locale` | BCP 47 目标语言，例如 `zh-Hans`、`ko`、`ru` |
| `source_text_sha256` | 有实际源文本字段时，其 UTF-8 内容的准确 SHA-256；没有文本字段时不伪造 |
| `localized_text` | 面向人的已翻译候选或定稿文本 |
| `review_status` | `translated`、`keep`、`revise`、`question`、`blocked` 等受控状态 |
| `notes` | 必要且可长期维护的说明；临时聊天过程不放入正式表 |

引擎可以追加 `egpack`、`rio_file`、偏移、容量、控制符或 runtime binding 等字段，但不
应改变核心字段含义。

语音／纯图片输入用实际资源身份、摘要及必要片段／区域关联原意依据，工作转写与 OCR 结果另列。经确认的真正新增内容声明实际语源。原意依据、呈现／制作底稿与交付目标通过现有备注或旁表分别关联，不要求塞进同一个 `source` 字段。历史源哈希若锁定的是用于连接的资源字段，保持其原义并明确对应关系，不能把英文连接字段误认作日语原文。

`review_status` 表示翻译或审核阶段的结论，不同时表示修改已采用、关联位置已同步或资源已写回。
采用决定和反查结果可以保存在按稳定身份关联的工作记录中，不要求为此修改现有表头。
相关记录遵守 02 的公开边界，内容要求见 [07 修改反查](07-change-impact.md)。

## 现有封存表的兼容映射

| 范围 | 身份 | 源哈希 | 人类译文 | 特殊说明 |
| --- | --- | --- | --- | --- |
| AGE2 TDA/帝都正文 | `id` | `source_text_sha256` | `cn_text` | 已由快照哈希绑定，暂不改表头 |
| rUGP 已审校正文 | `stable_id` | `source_text_sha256` | `translated_text` | 面向完整审校与其他语言移植 |
| rUGP 精确运行时表 | `stable_id` | `source_field_sha256` | `translation_text` | `runtime_text` 是写入值，不一定等同展示用译文 |
| 帝都图片文案 | `asset_id` | `source_text_sha256` | `zh_cn` | 还要结合源图锁、排版和资源路径 |
| 系列总术语 | `jp` | 当前无逐行哈希 | `cn` | 小型人工维护表；新增语言应建立独立文件 |

## 新语言模板

[`create_locale_template.py`](../Tools-LetToolsHandleRepetition/create_locale_template.py) 不猜测这些历史字段。调用者
必须显式提供身份列、源哈希列和旧目标文本列；工具删除旧目标文本并创建空的
`target_locale,target_text`。这能在不修改已封存中文权威的情况下，为韩语、俄语等目标
生成统一工作入口。

该工具适用于已有受支持身份／源哈希列的文本表；它不生成语音对应、识读结果或图片制作清单。不适用的输入保留本作源记录并另行关联，不能为通过模板检查填入虚构文本哈希。

## 文件命名

- 同时包含源与目标文本/身份时优先：`<scope>.ja-zh-Hans.csv`；
- 只包含目标权威、源文本仅以哈希表示的历史文件可保留 `<scope>.zh-Hans.csv`；
- 新语言使用含义准确的 BCP 47 标识：`cn` 不是语言代码，`kr` 表示卡努里语而不是韩语；
  `ru-RU` 是合法的“俄罗斯地区俄语”标签，但项目没有地区差异时应使用较简洁的 `ru`；
- 版本号写入 schema、manifest 与 Git tag，活动目录名保持稳定。

## English summary

New cross-engine tables use stable identity, declared source/target locales,
localized text and explicit review state. Preserve an exact
`source_text_sha256` when an actual source text field exists; audio/image inputs
link real resource hashes and segments/regions separately from transcripts/OCR.
Distinguish meaning evidence, authoring bases and targets through existing notes
or sidecars. Historical join hashes retain their declared meaning and do not
prove translation authority. Existing tables keep their headers and mappings.
The locale-template tool handles supported text tables, not audio correspondence
or image inventories; never fabricate a text hash to fit its interface.
