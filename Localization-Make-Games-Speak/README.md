# 游戏本地化｜让游戏说你的语言

**Game Localization — Make Games Speak Your Language**

[返回首页](../README.md) · [各游戏资产](../docs/research/asset-map.md) · [参与贡献](../docs/project/CONTRIBUTING.md)

<details>
<summary><strong>English · Make Games Speak Your Language — expand here</strong></summary>

Learn how we turn AI-assisted drafts and edited artwork into a maintained game localization. Start with the problem you want to solve:

| Topic | Guide | What you can reuse |
| --- | --- | --- |
| Text translation | [Make AI Translation Worth Reading](Text-AI-Translation-Worth-Reading/README.md) | Story context, first-pass translation, independent Japanese review, change tracing and human corrections before release |
| Image localization | [Make It Look Like It Was Always There](Images-Make-It-Look-Native/README.md#english-workflow) | Five stages from extraction and classification through copy, production, repair and human review |
| Fonts and typography | [Don't Let Fonts Give Your Patch Away](Fonts-That-Fit-The-Game/README.md) | Runtime and image font choices, provenance, coverage and layout checks |
| Terminology and consistency | [Keep 100,000 Words Consistent](Glossaries-Keep-It-Consistent/README.md#english) | Contextual baselines, approved glossaries and tracing an adopted change through related occurrences |
| ParaTranz collaboration | [Keep Improving the Translation, Together](ParaTranz-Keep-Improving-Together/README.md) | Shared references, community proofreading and reviewed revisions for later releases |
| Localization tools | [Let Tools Handle the Repetition](Tools-Let-Tools-Handle-Repetition/README.md) | Task-based commands, inputs and outputs for reusable authoring and synchronization tools |
| Automated tests | [Catch Problems Before Players Do](Tests-Catch-Problems-Before-Players/README.md) | Focused regressions for tools, data identities, image constraints and synchronization conflicts |

The [complete English text workflow](Text-AI-Translation-Worth-Reading/workflow.en.md) and [new-language guide](Text-AI-Translation-Worth-Reading/new-locale.md) explain how to adapt the method to another target language. Engine-neutral authoring stays here; extraction, encoding, runtime binding and packaging stay in AGE2 or rUGP. Historical evidence is under [research](../docs/research/localization/README.md).

Both text and image lettering follow the shared [translation principles](principles.md#english-summary): Japanese to Chinese, retaining English present in the Japanese original. English-edition-only assets are translated from their corresponding Japanese voice, not from the English edition's wording.

Most Japanese text needs translation, but retention depends on function, player understanding and the original presentation. Assess each relevant part; familiar examples are not an exhaustive list of what may remain unchanged.

The maintainer reviews and corrects the release candidate **before publication**. ParaTranz revisions are reviewed, integrated and verified for a later release; an online edit does not update an installed patch.

</details>

把你喜欢的游戏，变成你读得懂的样子。

这里公开我们怎样用 AI 协助翻译长篇剧情、让中文融入原画、选择合适的字体，并通过独立复核和人工修改完成汉化。你可以从一个具体问题开始，把这些方法用到自己的作品和目标语言中。

## 你想先解决什么问题？

| 你正在做什么 | 从这里开始 | 可以学到什么 |
| --- | --- | --- |
| 翻译长篇剧情，担心 AI 理解错、译文读不下去 | **[文本翻译｜让 AI 翻译值得读下去](Text-AI-Translation-Worth-Reading/README.md)** | 理解剧情、按场景初译、独立日文复核、解决疑点，到发布前人工修正 |
| 汉化 UI、标题、字幕或场景里的文字 | **[图片汉化｜让中文长在原画里](Images-Make-It-Look-Native/README.md)** | 提取分类、确认文案与样式、制作、自检返修、人工审核与交付 |
| 选字、补字，或让正文和图片字体贴合游戏 | **[字体排版｜别让字体出卖你的补丁](Fonts-That-Fit-The-Game/README.md)** | 区分运行时与图片用字，核对来源、覆盖、字宽和实际显示 |
| 跨章节、跨批次翻译，避免人名和设定前后打架 | **[术语与全文一致性｜十万字，也不乱套](Glossaries-Keep-It-Consistent/README.md)** | 从语境基线形成术语表，维持称谓与语气，修改后反查正文、界面和图片 |
| 邀请更多人校对，让发布后的修订进入新版本 | **[ParaTranz 多人校对｜一起把译文磨得更好](ParaTranz-Keep-Improving-Together/README.md)** | 共同参考原文与术语、讨论修改、确认采用，再同步回源表 |
| 少做重复劳动，把精力留给理解和制作 | **[本地化工具｜把时间留给翻译](Tools-Let-Tools-Handle-Repetition/README.md)** | 按任务选择术语查询、工作表、字体、图片和校对同步工具 |
| 修改工具后，确认它没有悄悄破坏数据 | **[自动化测试｜先替玩家发现问题](Tests-Catch-Problems-Before-Players/README.md)** | 用公开或合成输入检查身份、作用域、输出、图片边界与同步冲突 |

## 先确定该译什么，再开始制作

**先读[翻译最高原则](principles.md)：目标是日译中；日文原版已有英文保留英文，日文只有确实更适合时才译成英文。官方英文版独有素材找对应日语语音听译成中文。正文翻译和图片制作一体适用。**

**大部分日文需要翻译，但不是所有日文都要替换。** 根据内容用途、玩家理解和原作表现区分应译与保留范围；同一段文字或图片也可以部分翻译、部分保留。曲名、署名、原画与日期标记等是帮助理解的例子，新的内容同样按这一原则判断，不能仅因仍有日文就判漏译。

## 从候选到玩家拿到的版本

**本项目的文本有 AI 参与，但不是 AI 直出。** 初译后独立对照日文复核，解决疑点、统一术语，完成技术与实机检查；维护者再人工检查、修改错误并复查结果，完成后才发布。玩家下载的版本已经包含发布前的人工修改。ParaTranz 和玩家反馈继续推动后续版本修正，不能反过来理解为“先发布未经处理的生成稿”。详见[文本完整流程](Text-AI-Translation-Worth-Reading/workflow.md)。

图片流程采用相同的责任划分：制作方先逐图自检、修正，再交维护者人工审核；审核通过的具体成品才能进入引擎适配和版本制作。视觉检查、人工确认、实机确认和发布分别记录。

术语贯穿整个过程。基线保存判断依据和未决问题，现行表提供已确认译法；改动人物称谓、设定或理解依据时，要回查相关出现位置。[全文一致性方法](Glossaries-Keep-It-Consistent/README.md#从基线到全文一致性)说明怎样把一项决定落实到长篇文本中。

想制作其他语言版本，可以结合[英文完整流程](Text-AI-Translation-Worth-Reading/workflow.en.md)和[新语言指南](Text-AI-Translation-Worth-Reading/new-locale.md)，从自己的合法游戏副本建立原文、目标语言术语和独立工作表。英文说明可直接在各页开头展开。

## 具体素材放在哪里

| 内容 | 位置 |
| --- | --- |
| 各作译文、图片文案、资源映射和语境基线 | [AGE2/games/](../AGE2/games/README.md)、[rUGP/games/](../rUGP/games/README.md) 下对应作品 |
| FPD／EGPACK／WebP 提取、写回、松散覆盖 | [AGE2 工具](../AGE2/README.md) |
| RIO／CRsa／RUO／ICI、Photon 路由和运行时 | [rUGP 工具](../rUGP/tools/README.md) |
| 历史词库、旧审核批次、来源调查 | [本地化研究记录](../docs/research/localization/README.md)；保留查证价值，不作为当前制作入口 |

原始游戏图片、完整官方文本、私人校对材料、生成缓存和本地审核图库留在获准的制作环境。公开仓库维护方法、可公开的译文／术语、身份记录和工具；成品图和字体的发布范围依各自来源与许可判断。研究记录不会自动升级为现行术语或已发布成果。
