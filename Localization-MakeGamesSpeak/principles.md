# 本地化最高原则：忠于日语原作，让中文准确传达

[返回本地化](README.md) · [文本流程](Text-AITranslationWorthReading/README.md) · [图片流程](Images-MakeItLookNative/README.md)

**这组原则同时适用于正文、界面、字幕、图片文案、Logo 和场景文字。** 先确认需要向中文玩家传达的内容与功能，再选择表达、素材和实现方式。文本与图片使用同一套判断方法，不能由文件后缀或语言槽代替内容判断。

**本项目以日译中为目标，大部分日文都需要翻译，但并非所有日文都必须改成中文。** 是否翻译，应结合内容用途、中文玩家的理解需要和原作表现判断。完整汉化要求全量核查、翻译应译内容，并说明有意保留的内容；未发现、未确认和未完成的内容不能算作已保留。

## 中文版的定位与制作范围

**以日语原作确定内容含义，以中文玩家的理解与操作需要选择呈现方案。** 日文文本、日语语音、画面与剧情语境共同提供原意依据；官方各版本中的设计、素材和实现可以按用途采用、组合或调整。官方英文译文用于比较和发现疑点，不能替代日语原作裁定原意；英文版的字幕画布、排版、图层或调用机制则可以成为实际制作依据，不限于旁观参考。

开工时分别回答以下问题，不把某一语言版本排在所有问题的首位：

| 要确认什么 | 判断方法 |
| --- | --- |
| 内容与功能 | 按场景、信息和用途确定中文玩家需要理解或操作的内容；关联文字、语音、图片及各版差异，再划定应译与保留范围 |
| 原意依据 | 原作既有内容回到日文文本、日语语音、画面和上下文；文字与语音都可以直接作为输入，不要求先有一张日文图 |
| 呈现方案 | 为中文选择适当的字幕、布局、分段与信息组织；可以采用或调整官方日英版本中的方案，保持原意和作品表现 |
| 制作底稿 | 明确实际使用的原图、无字底、图层或模板及其版本；可以来自适用的任一官方版本，不能用“日文优先”代替尺寸、样式与保护范围判断 |
| 交付目标 | 按引擎的语言路由、对象引用和覆盖机制确定资源、槽位与调用；预期方案在制作前说明，最终绑定与实机效果在交付时验证 |

例如，原作通过日语语音传达剧情，英文版为它增加字幕：这是同一原作内容的另一种呈现。中文版可以听译该语音，采用英文版已有的字幕模板和显示机制，再按中文阅读需要调整。日文图缺失或只是透明占位，不妨碍建立这项中文任务；英文字幕文字不因此成为原意依据。

**全量提取和对照，不等于分别汉化日英两套资源。** 先按内容与功能确定任务，再关联所需资源；同一信息可以对应多个实际交付对象，保留每个目标的身份和调用，不能因合并内容理解就丢掉状态、尺寸或路由差异。仅供比较的资源不计为待制作项或已完成成果；英文版设计有差异也不自动要求再做一套中文。

**翻译依据与写回槽位分开判断。** 例如 rUGP 使用日文与 `translation` 路由时，中文可覆盖 `translation` 槽原有英文内容，无须新建中文槽。不能仅凭 `_ja`／`_en` 后缀排除制作底稿或实际目标。先确定中文用途并规划可行调用，不要求待制作内容已经在中文版中生效；用途或实现尚不明确时，分别说明待确认的问题。

## 语言怎么处理

1. **日文原作中的日文，原则上译成中文；是否保留按下文的通用方法判断。** 从实际承载信息的文本、语音或画面翻译，再用剧情语境核对。听译是正常输入方式，不依赖是否存在英文素材。
2. **日文原版中本来就使用英文的内容，保留英文。** 这是保留原作的语言选择；不能把“英文版把日文换成了英文”误当成此类情况，也不能因路径带 `_ja` 就假定图里一定是日文。
3. **只有日文确实用英文表达更合适时，才可译成英文。** 根据原意、作品设定和场景功能判断，并记录采用理由；不能因为英文版已有译法、排版更省事或工具更擅长英文就改变目标。专名、缩写等沿用已确认的项目决定。
4. **区分原作内容与其他版本真正新增的信息。** 载体或显示方式新增，不等于内容新增；先查对应的原作文字、语音、画面和场景。确实没有日语对应的新增信息，按下文确认用途、来源与采用范围，不强行寻找不存在的语音，也不自动纳入汉化。

## 如何判断是否需要翻译

**先看玩家是否需要读懂它传达的信息。** 对话、旁白、选项、界面、操作提示以及需要阅读的说明和剧情线索，通常都应译成中文。这是大部分文本和图片文案的处理方向；不能因为内容不是主线剧情、文字很小或制作困难就省略。

**再看保留原文是否更符合它在作品中的作用。** 有些文字主要用于身份识别、署名、表现环境或构成原画，保留原写法能准确识别对象、尊重原作设计，且不妨碍玩家理解必要信息时，可以保留。原文在中文语境中含义明确、表达适用，也可以直接沿用，不必为替换而重做。判断须结合实际用途与上下文，不能只看它是否含假名或是不是汉字。

**按实际内容划分范围。** 同一行或同一张图可以部分翻译、部分保留：身份名称与说明、画面装饰与阅读信息分别判断。保留一部分不代表整句、整图或整个目录都无须翻译。

这套判断同样适用于尚未遇到的新内容，不以是否出现在下面的例子中为准。目录名、英文版有没有翻译、OCR 是否检出日文或改图难度，都不能单独决定应译与否。保留项说明范围和理由，按现有流程复核；无法可靠判断的内容列为待确认。

## 哪些原文应该保留

下面是上述判断在项目中的常见例子，用于说明如何取舍，**不是穷尽清单，也不是只有列出的内容才允许保留**。

| 内容 | 处理原则 | 仍需翻译或另行确认的部分 |
| --- | --- | --- |
| 曲目名称、片尾歌曲原题 | 没有经核实的官方中文译名时，保留原题，不自行创造正式中文歌名；有官方译名时按项目决定采用 | 歌词、歌曲说明和播放操作不随歌名免译。已有项目中文候选不等于官方译名；确需采用项目译名，由维护者明确确认并注明性质 |
| 片尾真实人员、声优、公司及团体署名 | 保留原署名写法，包括汉字、假名、笔名和拉丁字母，不擅自简化、音译或汉化姓名 | 岗位、职责、演唱／作词等标签仍译成中文；虚构角色姓名、军衔和称谓按作品术语处理。混合一行时只翻译应译部分 |
| 已确认保留的壁纸、插画和画内装饰 | 保留原画构图、作品字标、署名及已确认不承担阅读任务的装饰文字，不能仅因存在假名就重绘 | 图库图注、菜单、标题说明和剧情／操作所需信息分别处理；不能把壁纸原画保留决定套到另一张带说明文字的图上 |
| 已确认沿用的日期、日历图 | 保留原有年月日和日期后的七曜星期标记，如月、火、水、木、金、土、日；不机械改成“星期一”等，也不改变数字、顺序或圈记 | 地点、事件说明、操作提示等另行判断；某张日期图保留不代表全部日期素材都免译 |

其他包装、漫画拟声、场景陈设及后续新内容也按上述方法判断。既有决定可供相同用途的内容参考，但仍要核对具体语境。核查实例与限制，包括君望、PF／PM 七曜日期图的既有保留决定，见[原文保留实例](../docs/research/localization/retention-examples.md)。

保留决定复用现有备注、决定记录或本地旁表，能找到作品、资源／文本稳定身份、保留范围、理由和维护者确认即可，不强制新建一套表或状态枚举。**“保留原文”是内容决定，二审的 `keep` 是审核结论，两者不能混用。** 保留项同样经过独立复核，确认没有误留正文、岗位或图注；文字与图片中的同一原题、署名应一致。

尚无决定或依据不足时继续列为 `question`／待确认。已经确认的保留项不反复要求翻译；新的剧情证据或维护者决定改变其适用范围时，按[修改反查](Text-AITranslationWorthReading/07-change-impact.md)复查相关文本和图片。通用原则不能代替对具体候选的审核、采用或返修决定。

## 官方版本差异怎么处理

“英文版独有素材”只说明资源分布，不能直接说明内容来源。尚未找到日文对应，也不能当作已经证明不存在。按实际关系处理：

| 差异 | 处理方式 |
| --- | --- |
| 原作已有内容，其他版本增加了载体或显示方式 | 关联同一场景的原作文本、语音或画面，为中文采用适合的呈现。原意仍独立核对，不要求补造同形式的日文资源 |
| 同一内容或功能存在不同官方设计 | 按中文阅读、画面效果和引擎约束选择、组合或调整方案；只制作采用方案所需的资源，保留实际状态与调用差异 |
| 真正新增的信息、功能说明或辅助提示 | 先确认来源、中文用途和采用范围。新增剧情按其实际原始语源翻译、独立审核并说明来源；功能说明还需核对实际行为。中文版自行补充的辅助文案明确其性质，不能伪装成日语原文或擅自添加剧情 |
| 对应关系或含义仍不明确 | 标为 `question`／`blocked`，说明缺少什么。不能把英语直译或反译日语当作已确认的日语原作依据 |

听译记录语音、场景与必要片段定位、工作用转写和疑点，初译和独立二审都核对实际语音；文字识读与 OCR 同样回到源画面核对。保留实际资源身份和来源，不捏造 JP 槽或把工作转写当成官方文本。关键原意听不清、对应关系不能确认时，不能用英文译文兜底定稿。工作记录遵守已有的[来源与公开边界](Text-AITranslationWorthReading/02-source-data.md)。

复用现有清单、备注或旁表关联内容、原意依据、采用的呈现／底稿与交付目标即可，不强制每项另建多列表或重复审批。图片允许的非剧情装饰拟写仍须注明，不能冒充原文识读或代替剧情、操作、数字等明确内容的翻译。

审核分别确认原意与语言处理、中文呈现及技术交付。经确认保留的原文不算漏译；文案正确不能代替画面和实机检查。真实未解决问题保留范围与状态，规则更新不自动批准既有候选。

## English summary

Localize the information and functions needed by Chinese-speaking players. Determine the meaning of existing original content from Japanese text, Japanese audio, images and story context. Choose suitable presentation, production materials and implementation from the official editions, adapting them for Chinese. English translation can reveal discrepancies but does not override the Japanese meaning; an English-edition canvas, layer, layout or display mechanism can be an actual production input.

Keep five decisions distinct: **content/function, meaning evidence, presentation, authoring base and delivery target**. Organize tasks by scene, information and purpose, then link the relevant resources across languages and media. Listening-based translation is an ordinary input path, not an exception restricted to English-only assets. For example, Japanese spoken story may receive Chinese subtitles using an English-edition subtitle template and display mechanism. A missing Japanese image or transparent placeholder does not exclude that task.

Full extraction and comparison do not require localizing both official resource sets. Select the Chinese solution and its required resources; retain the identity and calls of every actual target, including differing states, dimensions and routes. Reference-only resources count as neither pending production nor completed outputs. A language suffix alone determines neither an asset's role nor its eligibility.

Plan Chinese use and feasible delivery before production, then verify binding and in-game behavior at delivery. The content need does not have to be already implemented in Chinese. Chinese may replace English in rUGP's existing `translation` slot without creating a separate Chinese slot. An English-marked target does not make the work English-to-Chinese translation.

Preserve English intentionally present in the Japanese original; do not confuse it with English substituted by a localization. Render Japanese in English only when it better fits the meaning and context, with a recorded reason.

Most Japanese text should be translated into Chinese, but not every Japanese inscription needs replacement. Decide by its function, what Chinese-speaking players need to understand, and its role in the original presentation. Dialogue, narration, choices, UI, instructions and other information meant to be read normally require translation. Original wording may remain when it primarily identifies a person or work, expresses the setting or forms part of the artwork, and retaining it preserves that role without obstructing necessary understanding. Wording already suitable in Chinese may also remain. Assess separate parts of a line or image independently.

Song titles without a verified official Chinese name, real staff/actor/company credits, approved artwork and date/calendar notation are examples of this reasoning, not an exhaustive list of permitted exceptions. Translate role labels, lyrics, gallery captions and required story/operation information separately. Apply the same reasoning to new material; a filename, OCR result, English-edition treatment or editing difficulty alone does not settle the decision. A project translation candidate is not an official title or an approval to replace the original.

Record the exact retention scope, resource identity, reason and maintainer confirmation using existing notes or decision records. A retention decision is distinct from the review verdict `keep` and still requires independent checking. Missing evidence or unfinished work remains unresolved; the rule does not automatically approve or revert existing candidates.

Distinguish official-edition differences:

- **Existing original content, another medium or display:** link the Japanese text, voice or scene and choose a suitable Chinese presentation; no same-form Japanese asset is required.
- **Alternative designs for the same content/function:** select, combine or adapt a design for Chinese and the engine, producing its required resources rather than every official variant.
- **Genuinely added information or assistance:** confirm provenance, Chinese purpose and adopted scope. Translate added story from its actual original language and review it independently; verify functional instructions against actual behavior. Identify Chinese-authored assistance as such. Do not automatically adopt additions, require nonexistent Japanese audio or misrepresent them as Japanese original content.
- **Uncertain correspondence or meaning:** retain `question`/`blocked` and identify the missing evidence. Not finding a Japanese counterpart does not prove none exists.

For listening-based work, record the audio, scene/segment location, working transcript and uncertainties. Both passes check the actual audio; Japanese original content is checked against Japanese speech. OCR is likewise checked against the source image. Resource identity, meaning evidence and authoring inputs remain distinct; never fabricate a Japanese field/hash or present a working transcript as official text. Missing or unclear Japanese meaning cannot be approved through an English fallback.

Use existing manifests, notes or sidecar records to link these roles; no new universal table or repeated approval is required. Decorative reconstruction remains explicitly identified and cannot replace known story, operational or numeric information. Review meaning/language choices, Chinese presentation and technical delivery separately. Keep genuine limitations and publication boundaries; this policy does not retroactively approve existing candidates.
