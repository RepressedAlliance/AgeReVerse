# 术语与全文一致性｜十万字，也不乱套

**Terminology & Consistency — Keep 100,000 Words Consistent**

[返回本地化](../README.md) · [术语维护规则](../text-ai-translation-worth-reading/04-terminology.md) · [修改反查](../text-ai-translation-worth-reading/07-change-impact.md) · [发布后多人校对](../paratranz-keep-improving-together/README.md)

<details>
<summary><strong>English · Keep 100,000 Words Consistent — expand here</strong></summary>

## English

A glossary is one part of maintaining a long translation. The reusable method is:

1. **Read the story and build a contextual baseline.** Record identities, relationships, aliases, naming variants, evidence, decisions and unresolved questions. Reuse applicable work; update it when the underlying evidence changes.
2. **Promote confirmed mappings to maintained glossaries.** Store Japanese, Chinese and usage conditions. The baseline still contains their evidence alongside contextual references, candidates and questions. Approval does not remove an entry's history.
3. **Carry the same decisions across batches.** Drafting and independent Japanese review use the current baseline. Check character voice, forms of address, references, recurring expressions and connections between scenes, including related UI and image copy.
4. **Trace adopted changes through related occurrences.** Search Japanese forms, aliases, old and new translations, then inspect context. Record required changes, already-correct occurrences, justified differences and unresolved cases. Full names, nicknames, different senses and deliberate jokes need not have identical wording.
5. **Integrate and recheck.** Update the maintained text and affected terminology or review records, reread relevant context, and perform the technical or in-game checks the change requires. The maintainer corrects the release candidate before publication; community revisions repeat the process for later versions.

The [complete English workflow](../text-ai-translation-worth-reading/workflow.en.md) explains how these activities fit into text production. The examples above link actual scoped revisions for an organization name, character names, and terminology changes affecting text and images.

This folder contains the Muv-Luv shared glossary and eight game-specific glossaries.
Use shared + own for the seven Muv-Luv games; Kiminozo uses only its own table.
Respect each entry's `context`; contextual baselines remain under each game's directory.
These are the maintained source files, not duplicate exports. Historical evidence is kept
in the [terminology records](../../docs/research/localization/terminology-history/README.md).

For another target language, create independent glossary files and target-language policies. These tables record the project's Chinese decisions; their structure and evidence method can be reused without inheriting every Chinese naming choice.

</details>

翻到下一章，人物不能突然换名字，称谓不能忘记关系，早先埋下的线索也不能在另一批翻译里变了意思。这里讲我们怎样从语境基线形成术语表，并让每次确认和修改落实到全文。

想直接查词，可以跳到[各作术语表与基线](#各作术语表与基线)；想把方法用到自己的项目，从下面开始。

## 从基线到全文一致性

### 1. 先读作品，建立有语境的基线

初译前通读声明范围内的剧情，整理人物关系、称谓、专名、别名、写法变体和固定表达，再与已有术语逐项核对。对关键用例记录出处、适用范围、采用理由和仍待确认的问题；拿不准的词先保留为候选或疑点。

**基线保存理解和决定的依据。** 它包含确认术语，也包含语境参考、候选和待核项。条目进入术语表后，依据仍留在基线中；“冻结”表示当前按这一版推进，后续有新证据仍可修改。现有扫描和基线仍适用时直接复用，补查变化的部分。详细做法见[04 术语流程](../text-ai-translation-worth-reading/04-terminology.md#3-章节开工前的全章扫描)。

### 2. 把确认的译法整理成现行术语表

将对应明确、已确认且适于复用的专名或固定表达写入 `jp,cn,context` 三列表；使用限制跟着译法一起保存。具体来源、争议和审定理由继续由基线与来源记录承接。

Muv-Luv 七作按本作 `project.toml` 加载 **系列通用表＋本作专表**；君望独立使用本作表。各作专表不互相继承。只有确认具有跨作适用依据的词条，才提升到通用表；同一日文在不同语境下可以有不同译法。

### 3. 每批翻译和复核都接着同一套决定往下走

初译前加载当前基线，遇到新专名补入候选记录。独立复核重新对照日文和上下文，除了检查术语，还要看人物称呼、角色语气、指代、重复表达和剧情衔接。文本、界面与图片中指向同一对象的文字，也要核对采用决定。

全文一致性允许有依据的差异：全名与简称、正式称呼与亲昵称呼、同一词的不同义项，分别按场景处理。不能为了字面统一抹掉人物关系、语气或作品中的玩笑。具体判断见[06 独立审核](../text-ai-translation-worth-reading/06-review.md)。

### 4. 改一处，反查受同一决定影响的位置

确认新译法或新的剧情理解后，同时查原文、别名、写法变体、旧中文和新中文，回读相关场景、分支、铺垫与回应。逐项判断需要修改、已经符合、应保留差异或仍待确认；检索命中只是线索。

局部错字通常只需复核当前句与必要上下文；涉及人名、设定或理解依据的变更，则追到相关出现位置。检查范围内的正文、界面、ruby 锚点和图片文字各自落实；范围外事项记录并交接。操作要求见[07 修改反查](../text-ai-translation-worth-reading/07-change-impact.md)。

### 5. 同步采用结果，再复查修改后的全文关系

把确认采用的修改写入当前正文或其生效记录，并同步受影响的术语、基线和说明。回读必要上下文，核对同一决定是否已落实；技术检查和实机检查按实际影响执行。发布前，维护者还会人工检查、修改发现的错误并复查结果。

发布后的 [ParaTranz 校对与玩家反馈](../paratranz-keep-improving-together/README.md)继续沿用这套方法：修改回到原文和语境判断，确认后进入可维护源表和后续版本。

## 我们实际怎样处理过

| 例子 | 一致性工作涉及什么 | 记录 |
| --- | --- | --- |
| TDA03 的 NORAD 名称 | 对照完整机构名统一相关正文，并同步 ruby 锚文本；原文写法有缺字时仍结合明确指代判断 | [逐项修改记录](../../docs/research/localization/reviews/age2-norad-consistency-20260915.json) |
| TDA03 的角色姓名 | 同步姓名相关出现位置，保留正式长名、简称及戏谑改名的区别 | [姓名一致性记录](../../docs/research/localization/reviews/age2-name-consistency-20260915.json) |
| 七作术语修订 | 确认人名、军衔等采用范围，反查正文和现行表；正文改名后另追踪姓名卡、徽章等图片影响 | [术语对齐与图片联动](../../docs/research/localization/reviews/main-al-alignment-20260909.md) |

这些记录展示具体范围内的处理方法，各自说明了完成内容与未验证部分。

## 各作术语表与基线

这里集中存放 Muv-Luv 系列通用表和八作现行术语表。点击 CSV 即可在 GitHub 查看日文、中文和使用语境；各作说明提供对应基线与来源入口。

| 范围 | 术语表 | 条目数 | 基线与来源 |
| --- | --- | ---: | --- |
| 系列通用 | [muv-luv.ja-zh-Hans.csv](muv-luv.ja-zh-Hans.csv) | 146 | 按各作语境确认适用范围 |
| TDA00 | [tda00.ja-zh-Hans.csv](tda00.ja-zh-Hans.csv) | 135 | [本作基线](../../AGE2/games/tda00/terminology/README.md) |
| TDA01 | [tda01.ja-zh-Hans.csv](tda01.ja-zh-Hans.csv) | 89 | [本作基线](../../AGE2/games/tda01/terminology/README.md) |
| TDA02 | [tda02.ja-zh-Hans.csv](tda02.ja-zh-Hans.csv) | 98 | [本作基线](../../AGE2/games/tda02/terminology/README.md) |
| TDA03 | [tda03.ja-zh-Hans.csv](tda03.ja-zh-Hans.csv) | 115 | [本作基线](../../AGE2/games/tda03/terminology/README.md) |
| 帝都燃烧篇 | [imperial-capital-burns.ja-zh-Hans.csv](imperial-capital-burns.ja-zh-Hans.csv) | 306 | [本作基线](../../AGE2/games/imperial-capital-burns/terminology/README.md) |
| 光子之花 | [photonflowers.ja-zh-Hans.csv](photonflowers.ja-zh-Hans.csv) | 313 | [本作基线](../../rUGP/games/photonflowers/terminology/README.md) |
| 光子旋律 | [photonmelodies.ja-zh-Hans.csv](photonmelodies.ja-zh-Hans.csv) | 750 | [本作基线](../../rUGP/games/photonmelodies/terminology/README.md) |
| 君望（本篇及番外） | [kiminozo.ja-zh-Hans.csv](kiminozo.ja-zh-Hans.csv) | 167 | [本作基线](../../AGE2/games/kiminozo/terminology/README.md) |

每张表使用 `jp`（日文）、`cn`（中文）、`context`（适用语境）三列。
同一词在不同作品中的人物、称谓或场景可能不同，请连同语境阅读；各作专表不互相继承。
表中条目数按各表分别统计，不代表去重后的系列总数或全篇人工校对进度。

## 君望术语与基线

君望公开167条术语与360条基线记录：基线包含全部167条确认术语的依据，以及193条语境、候选和待核记录，涵盖本篇及番外已有整理结果，后续随审核更新。
[本作说明](../../AGE2/games/kiminozo/terminology/README.md)列出来源与待核状态。
基线放在`AGE2/games/kiminozo/terminology/`，是本作术语的父集，但不作为自动替换字典加载；君望也不继承Muv-Luv通用表。

## 维护与查词

直接编辑这里对应的现行表；各游戏的 `project.toml` 已指向这些文件，无须维护第二份副本。
新增或修改译法时，先在本作基线记录出处和判断依据，审定后更新现行表；有跨作依据才提升到通用表。

```powershell
python localization-make-games-speak/tools-let-tools-handle-repetition/terminology.py tda00 --term ウィル
python localization-make-games-speak/tools-let-tools-handle-repetition/terminology.py photonflowers --term ミキ
python localization-make-games-speak/tools-let-tools-handle-repetition/terminology.py kiminozo --term タケス
```

工具只读取本作明确登记的表；Muv-Luv通用与本作同词异译会报错。君望只读本作表，工具不会自动改写正文。

## 查证与历史资料

基线CSV仍放在各作品的`terminology/`中，本目录只集中维护现行术语表。各作品首页的“术语与基线”入口说明本作来源、适用范围和当前数量。

旧版本、恢复清单、审计记录及各作基线入口统一放在[术语查证与历史记录](../../docs/research/localization/terminology-history/README.md)。
候选、争议与历史译法不作为现行术语加载。

八作主基线都包含各自现行术语的中文和完整使用限制，每条现行术语只列一次；相同译法合并来源，不同语境、候选和待核状态保留区别。主表六列用于阅读及程序处理，原始九列来源表另存于本作`terminology/history/`。可用`--baseline --term 日文`同时取得条目和关联来源，或用`--baseline --group candidate`只看候选；加`--history`读取原始来源。逐作改动、数量及尚缺具体篇章定位的资料见上述整理明细。
