# 本地化最高原则：忠于日语原作，让中文准确传达

[返回本地化](README.md) · [文本流程](Text-AITranslationWorthReading/README.md) · [图片流程](Images-MakeItLookNative/README.md)

**这组原则同时适用于正文、界面、字幕、图片文案、Logo 和场景文字。** 先确认需要向中文玩家传达的内容与功能，再选择表达、素材和实现方式。文本与图片使用同一套判断方法，不能由文件后缀或语言槽代替内容判断。

**本项目以日译中为目标，应汉化的内容必须完整做到简体中文化。** 大部分日文都需要翻译，但有明确内容依据的原文保留另行说明范围与理由。完整汉化要求全量核查，处理应译内容的字形、含义、术语和表达；“中文玩家能看懂”不能作为合格或免译标准。未发现、未确认和未完成的内容不能算作已保留。

## 中文版的定位与制作范围

**以日语原作确定内容含义，以中文玩家的理解与操作需要选择呈现方案。** 日文文本、日语语音、画面与剧情语境共同提供原意依据；图片通常在日文版适用原图的基础上制作，保留原作构图与表现。官方英文译文、排版和演出用于对照与参考，不能替代日语原作裁定原意。

**参考英文设计、复用具体模板、覆盖原英文位置，分别说明。** 需要复用英文版的画布、模板或显示机制时，先确认中文用途，说明复用哪一部分、为什么需要，并核对实际目标约束。例如原作只有日语语音、英文版增加字幕时，可复用其字幕画布和显示机制，根据日语听译重新制作中文字幕。这不代表优先拿英文成品图改中文，也不代表把英文专用差分都另做一套中文；日文版已有适用原图时，通常仍以它为制作基础。

本项目的常见工作对象是**日文原作、官方英文本地化与中文候选**。英文对照可以帮助理解不同译法、定位场景、检查信息差异，并展示官方如何处理排版和演出，应保留其具体用途。日英含义不一致时，先确认是否确实对应同一句、同一场景，再回到日文／日语判断；不能把“英文是参考”理解为不看英文。没有官方英文时直接使用现有资料，其他官方语种也按相同方法处理。

开工时分别回答以下问题，不把某一语言版本排在所有问题的首位：

| 要确认什么 | 判断方法 |
| --- | --- |
| 内容与功能 | 按场景、信息和用途确定中文玩家需要理解或操作的内容；关联文字、语音、图片及各版差异，再划定应译与保留范围 |
| 原意依据 | 原作既有内容回到日文文本、日语语音、画面和上下文；文字与语音都可以直接作为输入，不要求先有一张日文图 |
| 呈现方案 | 保持原意和原作表现，为中文调整字幕、布局、分段与信息组织；可参考官方英文设计，不要求照搬任一版排版 |
| 制作底稿 | 通常使用日文版适用原图或由其制作的无字底；确需复用英文版画布或模板时，说明具体部分、中文用途和理由，并记录真实底稿及目标参数 |
| 交付目标 | 按引擎的语言路由、对象引用和覆盖机制确定资源、槽位与调用；预期方案在制作前说明，最终绑定与实机效果在交付时验证 |

例如，原作通过日语语音传达剧情，英文版为它增加字幕：这是同一原作内容的另一种呈现。中文版可以听译该语音，采用英文版已有的字幕模板和显示机制，再按中文阅读需要调整。日文图缺失或只是透明占位，不妨碍建立这项中文任务；英文字幕文字不因此成为原意依据。

**全量提取和对照，不等于分别汉化日英两套资源。** 先按内容与功能确定任务，再关联所需资源；同一信息可以对应多个实际交付对象，保留每个目标的身份和调用，不能因合并内容理解就丢掉状态、尺寸或路由差异。仅供比较的资源不计为待制作项或已完成成果；英文版设计有差异也不自动要求再做一套中文。

**翻译依据、制作底稿与写回槽位分开判断。** 例如 rUGP 使用日文与 `translation` 路由时，中文可覆盖 `translation` 槽原有英文内容，无须新建中文槽；这是写回位置，不表示内容按英文翻译，也不表示用英文图片当底稿。不能仅凭 `_ja`／`_en` 后缀排除实际目标，目标尺寸与编码按引擎确认。先确定中文用途并规划可行调用，不要求待制作内容已经在中文版中生效；用途或实现尚不明确时，分别说明待确认的问题。

## 语言怎么处理

1. **日文原作中的日文，原则上译成中文；是否保留按下文的通用方法判断。** 从实际承载信息的文本、语音或画面翻译，再用剧情语境核对。听译是正常输入方式，不依赖是否存在英文素材。
2. **日文原版中本来就使用英文的内容，保留英文。** 这是保留原作的语言选择；不能把“英文版把日文换成了英文”误当成此类情况，也不能因路径带 `_ja` 就假定图里一定是日文。
3. **只有日文确实用英文表达更合适时，才可译成英文。** 根据原意、作品设定和场景功能判断，并记录采用理由；不能因为英文版已有译法、排版更省事或工具更擅长英文就改变目标。专名、缩写等沿用已确认的项目决定。
4. **区分原作内容与其他版本真正新增的信息。** 载体或显示方式新增，不等于内容新增；先查对应的原作文字、语音、画面和场景。确实没有日语对应的新增信息，按下文确认用途、来源与采用范围，不强行寻找不存在的语音，也不自动纳入汉化。

## 官方英文具体怎么用

下面用本项目的经验说明英文在不同环节的作用。例子帮助应用通用原则，不要求其他作品照搬同一设计或采用决定。

| 用途 | 项目中的例子 | 怎样用于中文制作 |
| --- | --- | --- |
| 对照含义与发现错配 | [PM 源槽关联疑点](../docs/research/localization/source-alignment.md)：同一条记录中的日文与英文说话人、内容不一致 | 保留日英对照，先查索引、调用和场景语音，再判断中文；该条仍待核，不能写成已修复或所有发布版均受影响 |
| 参考或采用字幕呈现 | [AGE2 图片字幕](../AGE2/docs/postmortems/caption-layout.md)：日文图可能是 1×1 透明占位，英文版有实际字幕画布 | 中文含义从对应日语语音听译，英文字幕帮助定位与比较分段，其画布、模板和显示机制可按实际目标采用 |
| 比较设计而不强制照搬 | [Photon 的 U0478](../rUGP/docs/crmt-family.md)：日文竖排 4 层、英文横排 6 层，已有中文竖排 4 层方案 | 日英设计都展示，中文可选择合适方案；分别核对每个实际目标的尺寸、层级与调用，不按英文层数机械复制 |
| 判断原作英文是否应保留 | [AGE2 菜单](../AGE2/docs/postmortems/image-layout.md)保留原英文主体，只在日文副标题区域制作中文；[Photon HUD](../rUGP/docs/postmortems/pending-hook-entry-points-20260909.md)在日文图片模式也出现 `36mm chain gun` 等英文 | 区分原作英文与英文本地化替换文字，按图内各部分处理；HUD 实际资源对应仍待核，不能只因画面含英文就判漏译或替换失败 |
| 保留人物表达与笑点 | [Photon 外语表达](../rUGP/docs/postmortems/pf-pm-latin-review-20260909.md)对 `Hot Dog` 采用“热狗（Hot Dog）”并保留角色猜错 | 结合日文语境处理原作中的外语、缩写和读音梗；不能把所有拉丁字母当成残留，也不能把本例变成跨作品固定替换 |

## 如何判断是否需要翻译

**默认处理应汉化内容，并完整做到简体中文化。** 对话、旁白、选项、界面、操作提示、说明和剧情线索通常都应译成中文；场景文字、服装／机体标记和道具文字也按具体内容判断，不能因为不是主线、属于装饰、字小或制作困难就免译。

原文或原图不改时，区分以下三种情况：

| 情况 | 判断依据 | 处理方式 |
| --- | --- | --- |
| 1. 有意保留日文原文 | 原写法本身需要保留，例如真实人员署名、没有经核实官方中文译名的曲目原题，或经确认保留的原画文字 | 说明具体内容、范围与理由，独立复核；此范围保留原写法，不擅自简化姓名或改造原题 |
| 2. 原内容已经符合简体中文要求 | **实际字形、含义、术语与表达都与目标简体中文一致**，不只是汉字相似或能猜懂 | 直接复用，无须为改而改；这是内容已经合格，不是保留日文的例外 |
| 3. 沿用有明确依据的特殊表达惯例 | 字形与简体中文相同，但表达方式不同；项目有意采用并确认其范围，例如沿用本篇与 Alternative 官汉的七曜星期标记 | 记录采用惯例与依据；这是有意保留的一种，不能冒充第 2 类，也不能推广为同类素材全部免译 |

**除明确保留范围外，繁体字形、日式字形、假名和未汉化的日式称谓／用语都应处理。** 同一个汉字编码也可能显示不同地区字形，要看实际画面与笔画，不能只看 OCR 或字符表。只转换繁简不足以完成翻译：例如 `軍曹` 改为 `军曹` 仍未完成，按本项目[军衔术语](Glossaries-KeepItConsistent/decisions.md)应为 `中士`。保留手写、材质与构图不等于保留这些文字问题。

**按实际内容划分范围。** 同一行或同一张图可以分别适用上述情况与正常翻译：保留署名不免除岗位翻译，保留七曜不免除相邻说明翻译。“身份标记”“画面装饰”“中文玩家能看懂”都不能单独成为保留理由。

这套方法同样适用于新内容，不以是否出现在例子中为准。目录名、英文版有没有翻译、OCR 是否检出日文或改图难度，都不能单独决定应译与否。依据不足列为待确认；已经确认需要修正但尚未处理的内容列为待修。**旧工具能力不足造成的妥协属于待修问题，不能改记为原文保留或据此算作汉化完成。**

## 哪些原文应该保留

下面是上述判断在项目中的常见例子，用于说明如何取舍，**不是穷尽清单，也不是只有列出的内容才允许保留**。

| 内容 | 处理原则 | 仍需翻译或另行确认的部分 |
| --- | --- | --- |
| 曲目名称、片尾歌曲原题 | 没有经核实的官方中文译名时，保留原题，不自行创造正式中文歌名；有官方译名时按项目决定采用 | 歌词、歌曲说明和播放操作不随歌名免译。已有项目中文候选不等于官方译名；确需采用项目译名，由维护者明确确认并注明性质 |
| 片尾真实人员、声优、公司及团体署名 | 保留原署名写法，包括汉字、假名、笔名和拉丁字母，不擅自简化、音译或汉化姓名 | 岗位、职责、演唱／作词等标签仍译成中文；虚构角色姓名、军衔和称谓按作品术语处理。混合一行时只翻译应译部分 |
| 已确认保留的壁纸、插画和画内装饰 | 只在有明确内容理由、经确认的原画文字范围内保留原写法；不能仅因存在假名就推翻有效决定 | 保留原画美术不等于文字免译。图库图注、菜单、标题说明和其他应汉化文字仍须完整简体中文化；“装饰”或“不影响剧情”本身不是保留理由 |
| 已确认沿用的日期、日历图 | 字形、含义和表达均已符合简体中文的年月日直接复用；七曜星期标记如月、火、水、木、金、土、日，按明确采用的特殊惯例保留，不机械改成“星期一”等 | 七曜属于第 3 类，不是因“能看懂”就认定为普通中文。数字、顺序和圈记不擅改，地点、事件说明、操作提示等另行处理；某张日期图保留不代表全部日期素材都免译 |

其他包装、漫画拟声、场景陈设及后续新内容也按上述方法判断。既有决定可供相同用途的内容参考，但仍要核对具体语境。核查实例与限制，包括君望、PF／PM 七曜日期图的既有保留决定，见[原文保留实例](../docs/research/localization/retention-examples.md)。

保留决定复用现有备注、决定记录或本地旁表，能找到作品、资源／文本稳定身份、保留范围、理由和维护者确认即可，不强制新建一套表或状态枚举。**“保留原文”是内容决定，二审的 `keep` 是审核结论，两者不能混用。** 保留项同样经过独立复核，确认没有误留正文、岗位或图注；文字与图片中的同一原题、署名应一致。

尚无决定或依据不足时继续列为 `question`／待确认。符合上述依据的既有保留决定可以复用，不反复要求翻译；若旧决定仅依据“看得懂”、装饰分类或工具限制，则重新判断并区分待确认与待修，不能直接沿用为合格。范围改变时，按[修改反查](Text-AITranslationWorthReading/07-change-impact.md)复查相关文本和图片。规则更新不自动批准或回退全部既有候选，也不表示旧补丁的问题已经修复。

## 官方版本差异怎么处理

“英文版独有素材”只说明资源分布，不能直接说明内容来源。尚未找到日文对应，也不能当作已经证明不存在。按实际关系处理：

| 差异 | 处理方式 |
| --- | --- |
| 原作已有内容，其他版本增加了载体或显示方式 | 关联同一场景的原作文本、语音或画面，为中文采用适合的呈现。原意仍独立核对，不要求补造同形式的日文资源 |
| 同一内容或功能存在不同官方设计 | 通常以日文版适用原图制作，参考英文设计改善中文阅读与画面效果；确需复用英文版画布或模板时说明具体用途与理由。只制作中文方案所需资源，保留实际状态与调用差异 |
| 真正新增的信息、功能说明或辅助提示 | 先确认来源、中文用途和采用范围。新增剧情按其实际原始语源翻译、独立审核并说明来源；功能说明还需核对实际行为。中文版自行补充的辅助文案明确其性质，不能伪装成日语原文或擅自添加剧情 |
| 对应关系或含义仍不明确 | 标为 `question`／`blocked`，说明缺少什么。不能把英语直译或反译日语当作已确认的日语原作依据 |

听译记录语音、场景与必要片段定位、工作用转写和疑点，初译和独立二审都核对实际语音；文字识读与 OCR 同样回到源画面核对。保留实际资源身份和来源，不捏造 JP 槽或把工作转写当成官方文本。关键原意听不清、对应关系不能确认时，不能用英文译文兜底定稿。工作记录遵守已有的[来源与公开边界](Text-AITranslationWorthReading/02-source-data.md)。

复用现有清单、备注或旁表关联内容、原意依据、采用的呈现／底稿与交付目标即可，不强制每项另建多列表或重复审批。图片允许的非剧情装饰拟写仍须注明，不能冒充原文识读或代替剧情、操作、数字等明确内容的翻译。

审核分别确认原意与语言处理、中文呈现及技术交付。经确认保留的原文不算漏译；文案正确不能代替画面和实机检查。真实未解决问题保留范围与状态，规则更新不自动批准既有候选。

## English summary

Localize the information and functions needed by Chinese-speaking players. Determine the meaning of existing original content from Japanese text, Japanese audio, images and story context. Normally author images from a suitable Japanese-edition original, preserving its composition and artistic expression. Compare official English wording, layout and staging without letting them override Japanese meaning.

Distinguish **English design reference, reuse of a specific template, and writeback to an originally English target**. When a Chinese task needs an English-edition canvas, template or display mechanism, identify the reused part, its purpose and the reason for using it, then verify the target constraints. For Japanese spoken story with English-added subtitles, this may mean reusing the subtitle canvas/mechanism while creating Chinese subtitles from Japanese audio. It does not mean preferring English finished artwork or localizing every English-only variant. Use a suitable Japanese original as the normal image base where one exists.

Our usual comparison is **Japanese original / official English localization / Chinese candidate**. Keep the English counterpart where available: it can offer another interpretation, help locate a scene, reveal information differences and demonstrate an official design. When meanings differ, first verify that the records and scenes actually correspond, then resolve the original meaning against Japanese. No English counterpart is required when none exists; other official languages can serve the same comparative roles.

Keep five decisions distinct: **content/function, meaning evidence, presentation, authoring base and delivery target**. Organize tasks by scene, information and purpose, then link the relevant resources across languages and media. Listening-based translation is an ordinary input path, not an exception restricted to English-only assets. For example, Japanese spoken story may receive Chinese subtitles using an English-edition subtitle template and display mechanism. A missing Japanese image or transparent placeholder does not exclude that task.

Full extraction and comparison do not require localizing both official resource sets. Select the Chinese solution and its required resources; retain the identity and calls of every actual target, including differing states, dimensions and routes. Reference-only resources count as neither pending production nor completed outputs. A language suffix alone determines neither an asset's role nor its eligibility.

Plan Chinese use and feasible delivery before production, then verify binding and in-game behavior at delivery. The content need does not have to be already implemented in Chinese. Chinese may replace English in rUGP's existing `translation` slot without creating a separate Chinese slot. This is a destination decision, not an English translation source or a choice of English artwork as the base. Verify target geometry/encoding independently of language suffixes.

Preserve English intentionally present in the Japanese original; do not confuse it with English substituted by a localization. Render Japanese in English only when it better fits the meaning and context, with a recorded reason.

Content requiring localization must be fully Simplified Chinese in its actual glyphs, meaning, terminology and expression. Being understandable to Chinese readers is not sufficient. Dialogue, narration, choices, UI, instructions and story information normally need translation; scene lettering, clothing/equipment markings and props require content-specific assessment rather than blanket decoration or identity exemptions.

Distinguish three reasons for leaving content unchanged:

| Case | Requirement and treatment |
| --- | --- |
| 1. Intentional Japanese retention | The original wording itself has a justified role to preserve, such as real staff credits, song titles without a verified official Chinese name, or explicitly approved artwork lettering. Record and independently review its exact scope and reason; do not arbitrarily simplify names or rewrite original titles. |
| 2. Already compliant Simplified Chinese | Actual glyphs, meaning, terminology and expression all match the intended Simplified Chinese. Reuse it unchanged; this is compliant content, not a Japanese-retention exception. |
| 3. An explicitly adopted special convention | Glyphs match Simplified Chinese but the expression differs, and the project deliberately adopts a supported convention within a defined scope. Japanese weekday notation following the official Chinese Muv-Luv/Alternative treatment is an example. This is a form of intentional retention, not case 2 or an exemption for all date assets. |

Outside justified retention regions, correct Traditional/Japanese glyph forms, kana and untranslated Japanese terms or forms of address. Shared character codes or successful OCR do not prove matching glyphs; inspect the actual lettering and strokes. Merely changing `軍曹` to `军曹` is insufficient: the [project rank terminology](Glossaries-KeepItConsistent/decisions.md) uses `中士`. Preserve the handwriting, material and composition while fixing the text.

Assess regions independently: retaining a credit or weekday marker does not exempt role labels, adjacent explanations, lyrics, gallery captions or other required Chinese text. Examples are not a closed whitelist. A decoration/identity label, readability, filename, English-edition treatment, OCR result or editing difficulty alone cannot justify retention. A project title candidate is neither an official translation nor approval to replace the original.

Record scope, resource identity, reason and maintainer confirmation through existing notes. A retention decision is distinct from the review verdict `keep`. Reuse still-valid decisions; reassess old decisions justified only by readability, decoration or tool limitations, distinguishing uncertain cases from confirmed repairs. Old tool-limit compromises remain repair work, not intentional retention or completed localization. Policy changes neither automatically approve/revert all existing candidates nor fix old releases; check affected occurrences when a decision changes.

Distinguish official-edition differences:

- **Existing original content, another medium or display:** link the Japanese text, voice or scene and choose a suitable Chinese presentation; no same-form Japanese asset is required.
- **Alternative designs for the same content/function:** normally use the suitable Japanese original as the base, with English design as a reference for Chinese readability and appearance. Explain any necessary English-canvas/template reuse and produce only the Chinese solution's required resources.
- **Genuinely added information or assistance:** confirm provenance, Chinese purpose and adopted scope. Translate added story from its actual original language and review it independently; verify functional instructions against actual behavior. Identify Chinese-authored assistance as such. Do not automatically adopt additions, require nonexistent Japanese audio or misrepresent them as Japanese original content.
- **Uncertain correspondence or meaning:** retain `question`/`blocked` and identify the missing evidence. Not finding a Japanese counterpart does not prove none exists.

For listening-based work, record the audio, scene/segment location, working transcript and uncertainties. Both passes check the actual audio; Japanese original content is checked against Japanese speech. OCR is likewise checked against the source image. Resource identity, meaning evidence and authoring inputs remain distinct; never fabricate a Japanese field/hash or present a working transcript as official text. Missing or unclear Japanese meaning cannot be approved through an English fallback.

Use existing manifests, notes or sidecar records to link these roles; no new universal table or repeated approval is required. Decorative reconstruction remains explicitly identified and cannot replace known story, operational or numeric information. Review meaning/language choices, Chinese presentation and technical delivery separately. Keep genuine limitations and publication boundaries; this policy does not retroactively approve existing candidates.

### How we use English: project examples

| Use | Project example and lesson |
| --- | --- |
| Compare meaning and detect mismatches | The [PM source-association question](../docs/research/localization/source-alignment.md) has different Japanese/English speakers and content. Preserve both for comparison and check indices, calls and scene audio before judging Chinese. This case remains unresolved, with no confirmed affected player release. |
| Adopt subtitle presentation | [AGE2 caption layout](../AGE2/docs/postmortems/caption-layout.md) describes Japanese 1×1 transparent placeholders and actual English-edition subtitle canvases. Translate Japanese speech; English subtitles help locate and compare segments, while suitable canvases/templates/display mechanisms may support production. |
| Compare designs without copying blindly | [Photon U0478](../rUGP/docs/crmt-family.md) has four vertical Japanese layers, six horizontal English layers and a four-layer vertical Chinese design. Show both official designs, choose for Chinese, and verify each actual target's geometry, layers and calls separately. |
| Preserve original English | [AGE2 menus](../AGE2/docs/postmortems/image-layout.md) keep the English main lettering and replace Japanese subtitles. [Photon HUD observations](../rUGP/docs/postmortems/pending-hook-entry-points-20260909.md) include `36mm chain gun` in Japanese image mode too. Distinguish original English from localization substitutions; the HUD's exact resource correspondence remains unresolved, so English on screen alone proves neither omission nor replacement failure. |
| Preserve character expression and jokes | The [Photon language decisions](../rUGP/docs/postmortems/pf-pm-latin-review-20260909.md) retain the misunderstanding in `Hot Dog` with “热狗（Hot Dog）”. Check foreign expressions, abbreviations and pronunciation jokes in Japanese context rather than deleting every Latin word or applying this decision to unrelated works. |

These examples explain the general decisions; they are not universal designs or replacement rules.
