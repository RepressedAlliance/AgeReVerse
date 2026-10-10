# 文本翻译｜让 AI 翻译值得读下去

**Text Translation: Make AI Translation Worth Reading**

[返回本地化](../README.md) · **[翻译最高原则](../principles.md)** · [完整工作流](workflow.md) · [English workflow](workflow.en.md) · [新语言指南](new-locale.md)

<details>
<summary><strong>English · Make AI Translation Worth Reading — expand here</strong></summary>

Natural-sounding lines still need accurate story context, consistent characters and correct connections between scenes. The method below separates drafting, independent review, adopted changes and final human corrections. Read the [complete English workflow](workflow.en.md) for the full stages and the [consistency guide](../Glossaries-KeepItConsistent/README.md#english) for maintaining decisions across batches.

Read 01–03 to establish the game, authoritative source and table mapping. Then
read the story and freeze terminology (04), translate complete scenes (05), and
independently review each candidate against Japanese (06). Resolve questions and
update terminology, then trace and resolve change impacts (07) before engine
writeback, automated checks and in-game QA. Apply 07 whenever later edits occur.
The numbers describe workflow order, not rule precedence.

Before these steps, apply the shared [translation principles](../principles.md#english-summary)
to both text and images, including Japanese-voice transcription for assets
exclusive to the official English edition.

</details>

一句话读着顺，不代表放进整部作品仍然正确。这里讲怎样让 AI 参与长篇翻译，同时守住原意、人物关系、语气和前后呼应。

沿用本项目已经使用的文本流程：通读剧情并建立术语 → 按场景初译 → 独立日文对照二审 → 解决疑点与联动修改 → 技术写回和实机检查 → 维护者人工修正、复查 → 发布。各阶段的输入、输出和状态见[完整工作流](workflow.md)。术语表如何形成、修改怎样影响全文，另见[术语与全文一致性](../Glossaries-KeepItConsistent/README.md)。

先按最高原则确定语言来源与处理：日译中，保留日文原版已有英文；日文改用英文需有适当理由。官方英文版独有素材用对应日语语音听译，初译和二审都核对语音，不改成英译中。图片文案也使用同一原则。

文件名前的 `01`—`07` 表示规范的阅读和使用顺序。前三份用于确认项目与数据；
正文工作的核心顺序是：**通读剧情并冻结术语 → 初译 → 独立二审 → 解决疑点并同步术语
→ 修改反查与联动复核 → 技术写回与 QA → 玩家反馈复核**。07 在修改时持续使用，
不只在二审结束后执行。编号不表示后读的规则可以覆盖前面的规则。

## 按什么顺序读和用

| 顺序 | 规范 | 什么时候用 | 进入下一步前要明确什么 |
| --- | --- | --- | --- |
| 01 | [单个游戏项目清单](01-game-project.md) | 新游戏或接手任务时 | 游戏、引擎、目标语言，以及正文、术语、图片和字体的权威入口；已有项目先读其 `project.toml` 和 README |
| 02 | [补丁源表规则](02-source-data.md) | 提取、核对来源及每次修改源表时 | 版本、JP 原文槽、稳定 ID、源哈希、scene 顺序与修改范围；公开表没有 JP 全文时需从合法本机源数据连接 |
| 03 | [翻译与图片表字段约定](03-table-schemas.md) | 选择现有表或新建工作表时 | 身份、源证据、目标译文和状态分别在哪一列；已有表保留历史字段映射 |
| 04 | [章节术语工作流](04-terminology.md) | 正文初译前，之后每批持续使用 | 通读剧情与人物关系、扫描全章专名、核对总表、冻结章节术语基线，并列出疑点 |
| 05 | [简体中文初译规则](05-translation.md) | 按完整 scene 或自然剧情段初译时 | 产出候选译文、`translated / question / blocked` 状态、术语增量和下一批起点 |
| 06 | [独立审核规则](06-review.md) | 每批候选完成后，独立重新阅读 JP 时 | 逐句给出 `keep / revise / question`，记录修改理由，复查全章一致性 |
| 07 | [修改反查规则](07-change-impact.md) | 译文、术语或理解依据变化后 | 确认受影响范围、同步关联位置、记录例外与未决项，复核修改结果 |

接手已有章节时先核验 01—03 的现有成果，再加载该章冻结术语进入当前批次。
这些准备工作不用在每一批重新建一遍，但来源或版本发生变化时必须重新核验。

验证从本次改动直接影响的项目开始。已有结果仍适用于当前输入、规则和工具时可以复用；
只有相关失败、新证据、依赖变化或明确交付要求，才扩大或重复检查。相关检查通过且没有
未解决问题后停止，不为增加信心重复哈希、重建基线，或额外叠加冒烟、备份、回滚演练、
dry-run 和验收表。引擎规定的写入、安装前校验仍在实际操作时执行。

## 二审之后还要做什么

1. **解决疑点：**按[完整工作流第 4 步](workflow.md#4-解决-question-并再次冻结术语)
   补齐上下文、语音、截图或设定证据。`question` 有记录不代表已经解决；缺少依据的
   `blocked` 项也不能交付定稿。修改术语后返回 04 更新基线；按 [07 修改反查](07-change-impact.md)
   检查并同步受影响位置，再交给技术写回。
2. **技术写回与自动检查：**定稿后按对应引擎的 [AGE2](../../AGE2/docs/quality.md)
   或 [rUGP](../../rUGP/docs/quality.md) 规则验证控制符、编码、容量、资源绑定与打包。
3. **实机与反馈：**完成[实机 QA](workflow.md#7-实机-qa)，玩家反馈再回到 JP、
   术语和可维护源表复核，修正后按 07 反查并重跑相关检查。

初译自检不能代替独立二审，二审通过不能代替技术验证或实机检查。

## 规则冲突时怎样判断

- **原意判断：**以当前版本 JP 原文及其剧情上下文为依据；英文版独有素材用对应日语语音听译。英文槽、旧中文、OCR 和
  模糊匹配只能帮助发现问题，不能用于兜底定稿；缺少依据就记录 `question` 或 `blocked`。
- **固定译名：**先用本章已冻结且适用于该语境的项目译法和公共术语表，再按
  [术语确认依据](04-terminology.md#4-译法确认依据) 补充证据。若基线、总表或 JP
  语境相互冲突，应记录并确认变更，不能静默选一个覆盖其他记录。
- **中文表达：**在原意准确、信息完整、人物关系正确和术语一致的前提下调整语序与文风；
  不能为了顺口删改剧情信息，也不能因个人偏好改掉已确认译名。
- **章节补充：**可以细化角色语气、专属术语和资源特点，不能降低初译与审核的硬规则。
- **数据与技术：**稳定身份和源字段遵守 02，列映射遵守 03，控制符和写回合约遵守
  对应引擎规范。语义正确与技术可用都必须通过，不能互相替代。

## 与以前翻译时的用法对应

旧 TDA 交接要求先读共通规则、源文件位置与检查方法，再处理章节；Photon 的
初译、二审分支进一步明确了下面的依赖：

- 原 `TERMINOLOGY_WORKFLOW.md` 要求先扫描全章、核对总表并冻结基线，对应现在的 04。
- 原 `TRANSLATION_RULES.md` 把术语基线列为初译开工条件，对应现在的 05。
- 原 `REVIEW_RULES.md` 要求候选完成后重新阅读 JP、逐句审核，对应现在的 06。
- 原 `TECHNICAL_QA_RULES.md` 的职责现在分别由 AGE2 与 rUGP 的技术规范承担。

项目清单、源数据和字段规范排为 01—03，用于确认开工条件；04—06 延续
“先术语、再初译、后独立审核”的使用顺序；07 补充修改后的关联检查与同步。
完整阶段和交付要求以[完整工作流](workflow.md)为准。

译文仍跟随各作品放在 [AGE2](../../AGE2/games/README.md) 或 [rUGP](../../rUGP/games/README.md) 的游戏目录，现行术语及其维护方法集中于[术语与全文一致性](../Glossaries-KeepItConsistent/README.md)。图片文案可复用日文识读、术语和二审要求，但图片制作另走[图片流程](../Images-MakeItLookNative/README.md)。

发布后的其他参与者主要通过 [ParaTranz](../ParaTranz-KeepImprovingTogether/README.md) 校对，改文经确认后回到源表、完成相关验证，再进入新版本。它不替代已经完成的发布前人工修改。
