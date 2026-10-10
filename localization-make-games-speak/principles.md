# 翻译最高原则：以日文原作为依据，目标是日译中

[返回本地化](README.md) · [文本流程](text-ai-translation-worth-reading/README.md) · [图片流程](images-make-it-look-native/README.md)

**这组原则同时适用于正文、界面、字幕、图片文案、Logo 和场景文字。** 文本翻译与图片制作使用同一套语言依据，不能因素材形态或所在语言槽不同而改变目标。具体制作步骤、字体和工具选择都服从这些原则。

**本项目以日译中为目标，大部分日文都需要翻译，但并非所有日文都必须改成中文。** 是否翻译，应结合内容用途、中文玩家的理解需要和原作表现判断。完整汉化要求全量核查、翻译应译内容，并说明有意保留的内容；未发现、未确认和未完成的内容不能算作已保留。

## 语言怎么处理

1. **日文原作中的日文，原则上译成中文；是否保留按下文的通用方法判断。** 以原作文字、画面、日语语音及剧情上下文理解含义，英文版只能辅助定位和发现差异，不能代替日文依据。
2. **日文原版中本来就使用英文的内容，保留英文。** 这是保留原作的语言选择；不能把“英文版把日文换成了英文”误当成此类情况，也不能因路径带 `_ja` 就假定图里一定是日文。
3. **只有日文确实用英文表达更合适时，才可译成英文。** 根据原意、作品设定和场景功能判断，并记录采用理由；不能因为英文版已有译法、排版更省事或工具更擅长英文就改变目标。专名、缩写等沿用已确认的项目决定。
4. **官方英文版独有、找不到对应官方日文文字或图片的素材，找到对应日语语音后听译成中文。** 英文可帮助找场景和语音，译文含义仍以实际听到的日语及上下文为依据，不直接把官方英文译成中文，也不把英文反译的日语冒充原文。

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

其他包装、漫画拟声、场景陈设及后续新内容也按上述方法判断。既有决定可供相同用途的内容参考，但仍要核对具体语境。核查实例与限制，包括君望、PF／PM 七曜日期图的既有保留决定，见[原文保留记录](../docs/research/localization/original-retention-20261010.md)。

保留决定复用现有备注、决定记录或本地旁表，能找到作品、资源／文本稳定身份、保留范围、理由和维护者确认即可，不强制新建一套表或状态枚举。**“保留原文”是内容决定，二审的 `keep` 是审核结论，两者不能混用。** 保留项同样经过独立复核，确认没有误留正文、岗位或图注；文字与图片中的同一原题、署名应一致。

尚无决定或依据不足时继续列为 `question`／待确认。已经确认的保留项不反复要求翻译；新的剧情证据或维护者决定改变其适用范围时，按[修改反查](text-ai-translation-worth-reading/07-change-impact.md)复查相关文本和图片。此次规则补充不自动批准、回退或重写已有候选。

## 英文版独有素材怎么确认

记录源素材和场景、对应日语语音的定位信息、听到的内容与疑点，再按现有初译和独立复核流程确认中文。听译是日文依据的一种形式，不要求补造不存在的官方日文文本。工作用转写遵守已有的[来源与公开边界](text-ai-translation-worth-reading/02-source-data.md)，不因此公开完整语音或台词。

找不到对应日语语音，或关键部分听不清时，列为 `question`／`blocked` 并说明缺少的依据；不能用英文槽兜底定稿。图片允许的非剧情装饰拟写另行注明，不能冒充原文识读或日语听译，更不能代替剧情、操作、数字等明确内容的翻译。

审核同时确认两件事：**来源是否可靠、语言处理是否符合以上原则。** 经确认保留的原文、原作本来使用的英文和有理由采用的英文不算漏译；无保留决定的残留和缺少日文依据的英文替换不能因此自动通过。

## English summary

The Chinese patch translates from the Japanese original. The same policy covers text, UI, subtitles and image lettering. Preserve English already present in the Japanese original; English substituted by the official English edition is a different case. Render Japanese in English only when it better fits the original meaning and context, with a recorded reason.

Most Japanese text should be translated into Chinese, but not every Japanese inscription needs replacement. Decide by its function, what Chinese-speaking players need to understand, and its role in the original presentation. Dialogue, narration, choices, UI, instructions and other information meant to be read normally require translation. Original wording may remain when it primarily identifies a person or work, expresses the setting or forms part of the artwork, and retaining it preserves that role without obstructing necessary understanding. Wording already suitable in Chinese may also remain. Assess separate parts of a line or image independently.

Song titles without a verified official Chinese name, real staff/actor/company credits, approved artwork and date/calendar notation are examples of this reasoning, not an exhaustive list of permitted exceptions. Translate role labels, lyrics, gallery captions and required story/operation information separately. Apply the same reasoning to new material; a filename, OCR result, English-edition treatment or editing difficulty alone does not settle the decision. A project translation candidate is not an official title or an approval to replace the original.

Record the exact retention scope, resource identity, reason and maintainer confirmation using existing notes or decision records. A retention decision is distinct from the review verdict `keep` and still requires independent checking. Missing evidence or unfinished work remains unresolved; the rule does not automatically approve or revert existing candidates.

For assets exclusive to the official English edition, locate the corresponding Japanese voice and translate what is actually heard into Chinese, checking the scene context independently. English may help locate the material but is not the translation authority. Record the audio location and listening uncertainties; do not invent a Japanese source by back-translating English. If the necessary Japanese evidence cannot be found or understood, keep the item unresolved rather than approving an English-based fallback.
