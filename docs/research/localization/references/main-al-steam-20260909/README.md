# 本篇／Alternative Steam 术语参考

本目录是 2026-09-09 的参考快照，不被各作术语加载器读取。后续独立提取的更大参考集见[独立术语发现](../main-al-independent-20260909/README.md)；两份快照重叠，不能相加当作独立术语数。现行项目译法见[系列及各作术语](../../../../../Localization-MakeGamesSpeak/Glossaries-KeepItConsistent/README.md)。

| 内容 | 本篇 | Alternative |
| --- | ---: | ---: |
| 对齐正文记录 | 60,393 | 54,329 |
| 参考术语对 | [101](ml-reference-terms.json) | [193](al-reference-terms.json) |
| 说话人标签对 | [167](ml-speaker-terms.json) | [296](al-speaker-terms.json) |

[共同参考](common-reference-terms.json)包含两作共有的 84 对。说话人标签含匿名角色、组合与呼号，不能计作人物数量。

## 如何使用

`reference_observed_not_global_replacement` 表示记录原译用法，不允许全局替换；`observed_speaker_label` 只适用于完整说话人标签。普通词、称谓和切分片段不能仅凭命中次数成为强制术语。

- AL 的 `光線級／重光線級` 原译为“激光级／重激光级”；项目已选择的“光线级／重光线级”继续使用。
- `ヴァルキリーズ` 有“女武神／女武神中队”及 `Valkyries` 等写法。带编号的 `ヴァルキリー` 可是呼号，不能一律展开为中队全称。
- AL 登陆作战中的 `エコー／ウィスキー` 出现 `Echo部队／Whiskey部队`；需区分原文“部隊／艦隊”，不把同一词形套到所有场合。

## 来源与字段

本篇中文包的英文语言索引为空，英文需要从日英更新包取得，以日文脚本序列关联并检查日文字段一致；AL 使用原生三语言索引。更新包与基础包的重叠记录只计一次，没有译文索引的控制记录不充作正文。无原生标题的脚本块保留块 ID，不编造章节名。

公开词条的 `evidence` 最多保留两个来源 ID、记录摘要及三语言字段摘要；`occurrences` 是来源中的命中数，含上下文子串，并非人工确认次数。摘要可用于连接本地合法来源，不能证明语义正确。范围是 CRsa 消息与序列化字符串，不穷尽图片、音频及其他对象中的用词。

完整官方例句和未审定候选不随参考集公开。字段与来源规模见[数据概况](summary.json)及[来源身份](source-verification.json)。

## 导出参考集

导出器接收已提取、校验的本地结果，不提供完整原文提取流程。它使用字段白名单，排除完整例句、正文及工作站路径，并拒绝覆盖现有输出。

```powershell
python -m docs.research.localization.tools.export_main_al_reference --local-results <本地结果目录> --output <新的输出目录>
python -m unittest docs.research.localization.tests.test_main_al_reference -v
```
