# 06 · 独立审核规则

[规则顺序](README.md) · 上一步：[05 初译](05-translation.md) · 下一步：[07 修改反查](07-change-impact.md)

本文规定候选 CN 完成后的语义和中文质量审核。审核与初译是两个阶段；初译规则见 [`05-translation.md`](05-translation.md)。

## 1. 审核边界

1. 审核对象包含实际原意依据、候选 CN、适用的场景／说话人与上下文。文字、语音和图片均可输入；不补造不存在的官方 JP 字段。
2. 审核者重新核对声明的来源：文字回读、语音重听、图中文字回看源画面，不能只润色中文或审第一轮转写。确认采用的新增信息按实际语源审核，辅助说明核对功能及其性质。
3. 官方英文可用于比较译法、定位场景和发现疑点；日英不一致先确认关联，再核对原作。裁定日语原作含义时，英文译文和旧中文不能替代原作依据；官方各版本的设计、模板与调用资料可以用于呈现和技术判断，这些结论分别记录。
4. 译者自检不等于独立审核。条件允许时，应由不同对话、不同人员或至少在独立轮次中重新判断。
5. 审核阶段不默认写回资源、打包或安装游戏。

## 2. 审核输入

按输入形态提供适用的定位字段、实际原意依据和上下文：

- `chapter`
- `csv_row`
- `id / stable_id`
- `resource_file`
- `scene`
- `speaker_jp`
- 实际源文本／画面，或语音资源与片段定位、工作转写
- 准确对应的官方英文（若有），用于独立比较，不默认其译法或与日文的配对正确
- 候选 `cn_text`
- 当前章节术语基线版本

听译重新核对实际语音，日语原作内容重听日语，工作转写不是官方原文；语音未确认、关键部分听不清、缺少定位或必要上下文时，不得判定通过。没有同形式日文图不等于缺少原意依据。经确认的新增信息提供来源与采用范围；辅助文案说明用途及实际行为。语言选择遵守[最高原则](../principles.md)，原作已有英文与英文版替换译文分别处理。

原文保留项同时提供用途、范围、理由和维护者确认。审核者按[内容用途、玩家理解和原作表现](../principles.md#如何判断是否需要翻译)核对保留是否合理，检查同一行应译部分；不把曲名、署名等例子当作封闭名单。不能仅因含假名判漏译，也不能仅因标了“保留”就默认 `keep`。

例如 [PM 源槽关联疑点](../../docs/research/localization/source-alignment.md)中，日英内容与说话人不同；二审应保留英文对照，先检查对应关系，而非只让中文更顺。相反，[Photon 的 `Hot Dog` 采用决定](../../rUGP/docs/postmortems/pf-pm-latin-review-20260909.md)保留英文及角色的误解，不能仅因中文里仍有英文就判为 `revise`。前者仍待核，后者是对应语境的采用决定。

## 3. 逐句结论

每行必须给出以下一种结论：

- `keep`：候选 CN 可以保留。
- `revise`：给出修改后的 CN，并说明关键原因。
- `question`：依据不足，列明需要确认的内容。

不能批量默认 `keep`。

`revise` 表示已经给出有依据的修改方案，不表示方案已被采用。`question` 应说明核查后
仍无法解决的具体问题；能够依据现有材料解决的，按结果判为 `keep` 或 `revise`，
不因涉及梗、外语或专名就保留为 `question`。

## 4. `keep` 条件

必须同时满足：

1. 声明来源的原意准确，没有误译、漏译或擅自增译；原作内容核对日文／日语及画面，新增内容的来源与采用范围明确。
2. 应译部分的中文自然，放进上下文不突兀；原文保留符合最高原则且范围准确。
3. 人物语气、称谓和关系正确。
4. 术语符合已冻结基线。
5. 原文中的功能性符号和表达作用没有无故丢失。
6. 英文、拉丁缩写、外语句和カタカナ处理符合最高原则与项目决定，听译已独立核对实际语音。
7. 没有明显日式句壳、翻译腔或错误旧译名。

## 5. `revise` 条件

出现以下任一问题时应修改：

- 误译、漏译、增译或逻辑关系错误。
- 中文不通顺、拗口、过度书面或与原文文体不符。
- 角色语气、身份或称谓不对。
- 术语、专名或固定表达不统一。
- 普通口语被翻成不自然的文绉绉表达。
- 有命名感或设定意义的词被磨掉。
- 原文英文、拉丁缩写或关键符号被错误删除或替换。
- 经确认保留的曲目原题、真实署名或标记被擅自改写，或把本应翻译的岗位、正文、说明误列为保留。

修改回到实际原意依据和上下文，不做只凭个人偏好的同义改写。

给出修改后，应重新对照来源和上下文检查完整新译文，确认修改没有引入新的漏译、
指代错误或前后矛盾。

## 6. `question` 条件

核查现有材料后，仍存在以下问题时使用 `question`：

- 原文或语音可多解，需要后文或更多场景确认。
- 术语、称谓或说话人无法确定。
- 固定梗、设定词或官方写法的依据仍不足，且不同判断会影响译法。
- 外语句是否保留、翻译或加注尚未决定。
- scene 归属、人物关系或文本槽用途不明确。
- 技术显示结果可能影响语义判断。

## 7. 审核检查维度

1. 原意准确性：根据实际语源核对主宾关系、否定、反问、条件、因果、转折和时间关系；日语原作内容仍以日文／日语为准。
2. 信息完整性：人名、称谓、设定、情绪和剧情功能。
3. 中文自然度：口语、旁白、军令、誓词等是否符合文体。
4. 角色一致性：同一角色在相同关系和状态下是否保持稳定语气。
5. 术语一致性：是否符合章节冻结基线和公共总表。
6. 符号功能：`「」`、`『』`、括号等是否被无故删除或改成不同功能的符号。
7. 语言与保留处理：BETA、CP、ID 等缩写是否无故丢失，外语句、曲名和真实署名等是否有明确决定；文本与图片中的同一项是否一致。

控制符、编码、写回位置和打包完整性由对应引擎的 [`AGE2`](../../AGE2/docs/quality.md) 或 [`rUGP`](../../rUGP/docs/quality.md) 技术规则检查，不因为语义审核通过而自动通过。

## 8. 审核输出

每批至少保留：

1. 决策记录：每行 `keep / revise / question`。
2. 修改清单：定位字段、旧 CN、新 CN 和修改理由。
3. 问题清单：所有待确认内容及所需证据。
4. 审核摘要：范围、总行数和三类结论数量。
5. 交接起点：下一批从哪个 `csv_row`、`scene`、`id / stable_id` 继续。

逐批理由、临时决策和个人工作便签默认不加入公开补丁源表；能够长期解释发布状态、可复现且由测试约束的 `review_status` / `audit_flags` 可以按 [`02-source-data.md`](02-source-data.md) 的政策提升为公开字段。

### 给人工校对者的材料

按篇章或自然剧情段组织可连续阅读的材料，保留判断所需的上下文与清楚的场景、分支提示。用文字明确标注“沿用旧译”“新增／重写”“调整／拆合”，区分本轮需校对与仅供参考的内容，不能只靠颜色。

沿用稳定定位编号并标明本次候选版本，关联本页规定的适用原意依据与英文对照，提供便于直接填写改稿、备注、续读位置和交回意见的方式；不将每个片段或分支都变成独立确认任务。必要时另附全文参考，内部修改理由另行查阅，不因提供全文而默认要求重审全部旧译。收到人工修改后，按 [07 修改反查](07-change-impact.md) 确认采用并同步受影响位置。

## 9. 章节审核完成标准

1. 所有候选 CN 都经过逐句审核。
2. 每行都有可追踪的 `keep / revise / question` 结论。
3. 所有 `revise` 已给出新 CN，而不是只指出问题。
4. 所有 `question` 都有明确待确认事项。
5. 完成全章术语、称谓、角色语气和重复表达的一致性复查。
6. 审核提出的修改经确认采用后，按 [07 修改反查](07-change-impact.md) 完成受影响位置的复核，再将定稿文本交给技术写回和 QA。

逐句审核完成不等于全部疑点已经解决。交接时应分别说明未决问题、修改采用情况和关联
复核情况；未解决项不能作为已通过的定稿交付。技术、实机和发布后的修改同样适用 07。

独立复核不是制作的终点。技术与实机检查之后，由维护者人工检查并修改发现的错误，
复查修改结果后再发布对应版本。ParaTranz 主要承接发布后的协作校对与后续修订，
不能将其与发布前维护者已经完成的人工审核混为一谈。

## English summary

Independently check the declared meaning evidence: reread text, relisten to
audio and inspect image lettering in context. Working transcripts/OCR do not
replace those checks. Review confirmed additions in their actual source language;
identify assistance and verify function. English translations and old Chinese
cannot override Japanese original meaning, while official designs/templates
and calls can support separate presentation and technical decisions. A missing
same-form Japanese asset does not by itself block semantic review.
Preserve retention/terminology rules and per-item `keep/revise/question` decisions.
Review approval does not imply adoption, writeback, in-game verification or release.
Include correctly matched official English where available and compare it
independently without assuming the match or interpretation is correct. The
[PM association question](../../docs/research/localization/source-alignment.md)
requires checking records and scenes, not merely polishing Chinese. Conversely,
the [Photon `Hot Dog` decision](../../rUGP/docs/postmortems/pf-pm-latin-review-20260909.md)
preserves English and a character's misunderstanding; Latin letters alone are
not grounds for `revise`. The first case remains unresolved; the second is a
context-specific adopted decision.

For human proofreading, organize continuous reading by chapter or natural story
section, with necessary context and clear scene/branch cues. Explicitly label
reused translation, new/rewritten text and adjusted/split/merged text; separate
this round's review scope from reference-only context without relying on color.
Keep stable IDs and identify the current candidate version; link the applicable
meaning evidence and English comparison specified above. Offer a simple way to
enter edits, notes and a reading-resume point and return feedback. Do not make
every fragment or branch a separate confirmation task. A full-text reference may
help with context but does not automatically require re-reviewing all old text;
keep internal change reasoning separate. Confirm adoption of human edits and
check affected occurrences under [07 change impact](07-change-impact.md).
