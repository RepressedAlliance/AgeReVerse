# 图片汉化批量制作规范

[返回本地化入口](../README.md) · [图片工具与技术检查](tools.md) · [字体与许可证](../Fonts-ThatFitTheGame/README.md)

先遵守文本与图片共同的[翻译最高原则](../principles.md)，再决定具体视觉处理；制作方便或画面效果不能改变语言来源与翻译目标。

本规范适用于场景、背景、UI、标题、Logo、道具和插画内文字。共用同一套质量原则，按素材类型采用不同制作方法。目标是让中文看起来原本就在画面里，同时让一套素材保持一致，而不是逐张把字替换完就算完成。

## 1. 目标与边界

本规范按内容与功能确定中文任务，再分别选择原意依据、呈现方案、制作底稿和交付目标。原作含义来自日文文本、日语语音、画面与语境；图片通常以日文版适用原图为基础，英文设计供参考；确需复用英文版画布、模板或显示机制时，说明具体部分、用途与理由。缺少同形式日文图不排除任务，英文版独有资源也不自动构成新增内容或第二套制作任务。中文可覆盖 rUGP 现有 `translation` 目标。详见[中文版的定位与制作范围](../principles.md#中文版的定位与制作范围)。

下文用于编辑和像素检查的“原图”指实际选定底稿；原意来源、借鉴设计和目标格式分别关联。保护范围针对该底稿，换画布或新增叠层则遵守已确认的中文设计与引擎方案，不默认拿日文图约束所有制作。

1. **视觉自然优先。** 文字的位置、大小、方向、透视、留白、遮挡和材质必须成立，整张图不能出现明显修补痕迹。
2. **应汉化区域完整简体中文化，语言选择服从[翻译最高原则](../principles.md)。** 原图不改须区分有意保留日文、实际字形／含义／术语／表达均已符合简体中文，以及有明确依据的特殊惯例。除明确保留范围外，繁体／日式字形、假名和日式称谓都须处理，旧字残笔、小点与光晕清除完整；不能仅凭“能看懂”“身份标记”“装饰”“只是 Logo”“不影响剧情”或制作困难省略。七曜等特殊惯例不免除相邻说明的汉化；真实署名等有依据的原文保留区域不因此擦除或简化。原作已有英文保持英文，日文改用英文需确实适合并记录理由。
3. **尽可能保留信息。** 清楚可辨的文字严格依原意处理，尤其是剧情信息、人名、数字、价格、日期、操作含义。视觉优先不是改写这些信息的理由；有冲突时调整制作方案。
4. **无关内容尽可能不动。** 修改只覆盖文字及必要的底图修复范围，不能改变人物、物体、构图、颜色或其他已经通过的部分。
5. **整套一致性与单张还原同时验收。** 不得为了模仿某张字的外接框，破坏同套 UI 或素材的字号、字重、间距与效果体系。

## 2. 批量开始前：先盘点，再分组

优先使用已有制作记录、资源映射、通过版本和修订记录，找出实际未完成的范围。不要仅凭文件名相似判断同图，也不要重复制作已通过内容。

已有提取／解码与可编辑源文件同样先核对版本后复用，只补缺失、变更或失败部分。按[01 的清单与进度要求](01-extract-and-classify.md)说明计数单位、待核查与确定待制作范围，以及已细查、人工确认和实机状态，不能把未调查资源全算成待汉化。

先关联同一场景中的文字、语音、图片与版本差异，再确定中文需要表达什么、选择怎样呈现及如何交付。用途和对应关系不明确时分别列疑问，不要求尚未制作的任务已经在中文版生效。全量提取中的参考图不自动算作任务或成果；同一文案可复用，但每个实际目标保留身份、状态、尺寸与调用，不自动将所有语言路径纳入交付。

按功能和视觉体系分组，例如同一菜单的按钮、同一套状态图、同一招牌的昼夜版本、同一道具的不同镜头。记录各组的资源、语言、尺寸、透明度、使用位置和状态关系。相同像素可复用；不同透视、遮挡或光照需要分别适配。

先选能代表难度的样图：普通横排、竖排、透视、密集小字、透明发光文字等。样图通过后才扩展同组；不要把某一张偶然成功当成整个流程稳定。

## 3. 同套 UI、同套素材必须统一

每组先确定共用样式，保存为可复用配置或制作模板，再批量应用。至少包括：

| 项目 | 统一要求 |
| --- | --- |
| 字体 | 字体文件、字形版本、字重、简体中文区域字形与后备字体 |
| 尺寸 | 同级文字使用相同字号与缩放规则，不逐词拉伸压扁 |
| 排版 | 基线、对齐、字距、行距、边距与文字区域 |
| 外观 | 填色、渐变、描边、阴影、光晕、透明度与柔和程度 |
| 状态 | 普通、悬停、选中、按下、禁用使用同一几何基准，差异由状态规则定义 |
| 输出 | 渲染倍率、缩小方式、画布、透明度与实际显示比例 |

每批新制作／返修按[字体登记规范](../Fonts-ThatFitTheGame/registration.md)同步用字与[来源致谢](../Fonts-ThatFitTheGame/attribution.md)：字体身份和许可登记一次，素材组引用，多字体／局部例外单列。不能把运行时字体、安装过的候选或审核页用字直接算作游戏成品用字；生成字样也记录字体底稿及实际绘制方式。

**相同字号不等于每个词的墨迹外接框一样高。** 汉字本身有高低、宽窄差异；应依据字体字号、基线和代表字统一，不把每个词分别缩放到同一外接框。这会导致某些字偏小、笔画变形，或同组按钮忽大忽小。

较长文案先检查翻译是否简洁，再按全组规则处理换行、可用宽度或字号层级。不能某张随意减字号、另一张压横向宽度。确需例外时记录原因，并放在同组对照中验收。

一致性不是让全部图片一模一样：标题与正文可以有层级，不同系列 Logo 可以有独立风格；同一招牌在远近镜头中的屏幕尺寸也不同。应统一设计源样式，再施加对应透视、光照和距离效果，而不是强行统一最终像素高度。

## 4. 确定文案

- 需要翻译的信息：按实际文本、语音或画面及语境确认原意，统一术语、人名和同类标签，并独立复核。听译记录真实语音与片段定位，不只审核转写；缺少日语原作含义不能用英译兜底。真正新增信息先确认来源、用途与采用范围，按实际语源处理；辅助文案核对功能并注明性质，不一律要求日语语音。
- 模糊的装饰性小字：无法可靠识读时，可根据场景推定合理中文，或由图像生成工具提出候选，以实现整块视觉完整。记录为场景推定，不宣称是准确识读。
- 影响剧情或操作的信息：不能靠猜测定稿。优先查对应脚本、清晰版本或其他依据；仍无法解决则单列疑点。
- 一块区域有清晰字也有模糊字：分开控制。锁定已知文案与数字，只对不确定部分推定，不能让模型重写整块已知内容。

## 5. 先去旧字，再制作中文

优先复用正确的无字底、其他语言同底图或同组可还原区域；复杂底图可使用受限区域的图像编辑。先单独检查无字底，再加入中文，避免用新字掩盖旧字。

去字范围要包括旧字边缘、抗锯齿、描边、投影和光晕，但不能顺带擦掉背景线条、发丝、皮肤细节或邻近物体。留意文字被遮住的部分，不能把遮挡物一起重画或盖住。

中文制作通常优先使用可复现排字。手写、特殊 Logo、模糊装饰文字可采用适合的绘制或生成方法，但成品仍须满足文案、整套一致性、局部自然和背景保留要求。工具输出只是候选，提示词“其他完全不变”并不证明背景真的没变。

## 6. 场景／背景：文字必须属于所在物体

逐项匹配原图的文字区域，而不是在附近找空白处放字：

- **位置、大小、方向、留白：** 保持原来的版面层次、横竖排关系和视觉密度。
- **透视与曲面：** 招牌沿所在平面收缩，罐身文字沿圆柱弯曲；不能把正面平字直接贴上去。
- **遮挡与深度：** 前景物体、边框、发丝仍然挡住文字；文字不能覆盖不属于它的物体。
- **材质与光照：** 匹配印刷、粉笔、手写、灯箱等质感，以及反光、阴影、磨损和距离模糊。
- **密集信息：** 尽量保留原有分栏、数字、插图和空白，不能凭空增加文字块或挤占插图。

这些共同构成“视角要求”。即使每个字都正确，空间关系不成立也不通过。

## 7. 非场景素材：重点检查字体、效果与边缘

UI 按第 3 节成组制作和对照。Logo 除字形、粗细、笔势、间距外，还要比较颜色、饱和度、渐变方向、深色区域、阴影深浅与光晕扩散。柔和光晕不能变成一圈明显的硬描边；整体变淡也不能冒充柔和。

中文版需要的不同篇章、设计和状态的标题或 Logo，分别核对实际原意、选定底稿与采用设计，不能直接套用另一变体已通过的 Logo。通常以日文版适用原图为基础，参考英文设计；确需复用英文版画布或模板时说明具体用途与理由，不自动各做一套中文。保留日文原版已有的英文副标题；其他标记按第 1 节明确的处理范围制作，不能仅因用于装饰或身份识别就免译。英文版后来替换的文字仍按最高原则判断，不因它在底稿上就全部保留。

人物身上的涂鸦、胸牌和道具文字仍遵守空间关系：不得产生皮肤色块、马赛克、断发、硬抠边或不自然的覆盖。透明素材同时检查浅色、深色背景与边缘，避免黑边、白边和意外不透明区域。

从足够清晰的源图、字体或可编辑素材制作母版。把小尺寸预览放大不等于获得高清母版；最终须检查游戏实际显示尺寸，不能只看放大的制作图。

## 8. 每张自检，再检查整组

每张修改图都要与原图对照：先原尺寸整图，再放大局部，最后放回完整画面看是否自然。制作记录用于定位检查范围，不能代替查看成品。

检查清单：

- 不改的内容属于有意保留、已符合简体中文还是特殊惯例，范围与依据是否成立？应译区域的假名、繁体／日式字形、残笔、小点、旧字阴影是否处理完整？有效保留范围是否保持原样？
- 实际字形、含义、术语与表达是否完整符合简体中文，有无缺笔、乱码或变形？本项目的 `軍曹` 是否译为 `中士`，而非只简化为 `军曹`？不能只凭编码、OCR 或“能看懂”判断。
- 字体、颜色、粗细、阴影、光晕是否接近原图？
- 位置、方向、透视、留白、曲面和遮挡是否合理？
- 底图有无糊块、拼接、色差、破损或覆盖其他物体？
- 同组字体、字号、间距、基线和状态效果是否统一？
- 无关部分是否保持，画布、透明度和边缘是否正确？

再做资源和实机检查：正确语言槽、路径、覆盖优先级、运行时缩放和实际调用。文件存在、链接正常或技术检查通过，都不能代替视觉与实机验证。分别记录“已自检”“待人工确认”“已实机确认”，不要混称全部通过。

动态图层和连续帧还要按[04 自检要求](04-self-review.md)检查合成与播放，不能由单层、单帧推定整体通过。人工送审按接收设备提供能打开的材料、必要的动态预览及简单的意见交回方式，反馈关联稳定图片编号和候选版本；具体见下一项人工审核要求。

有疑问时给出实际原意依据、底稿、候选图、具体位置和原因。审核展示应支持整图／细节、底稿／中文切换、放大和移动，并保留张数、跳转与只看修改图的筛选。按[人工审核要求](05-human-review-and-delivery.md)提供官方日文／官方英文（有则提供）／之前的中文（有则提供）／当前中文，标明角色、版本和候选状态；附上面向人的修改位置、原因、保留决定与待确认问题说明。旧中文用于比较本次修正，不能代替日语原意依据。缺失对应如实说明，按来源角色提供适用的文字、语音和画面，不强制所有任务有日文原图。

## 9. 复用、返修与公开

返修定位到问题区域和关联素材组，修完检查本图及受影响的同组版本，不连带改动其他已通过素材。保存采用的文案、样式配置、来源映射和审核结论，使后续批次复用同一标准。

仍符合现行原则的保留与通过决定继续复用；仅因可读性、装饰分类或旧工具限制放过的内容须重新判断。已经确认的繁体／日式字形和未汉化用语属于待修，不能以历史妥协或已经发布为完成依据。

换字体、版本、字重轴或后备字来源时，更新实际采用配方和受影响的图片用字表；旧方案保留为历史。交付前补齐本批的公开字体来源与致谢。若实际携带字体软件，附对应完整声明并核对分发条件，不用其他字体的 OFL 文件代替；只交付图片的许可要求见[说明](../Fonts-ThatFitTheGame/attribution.md#图片致谢和随包许可证分别处理)。

公开仓库优先收录通用规范、可公开工具、样式模板和获准的校对／术语／少量样例。完整原文或译文、原始游戏图片、私人通信和未获准的素材不因参与制作就自动获得公开许可；记录和模板同样不能夹带这些内容。实际图片包的发布范围另行确认。

## English summary

Organize production by content/function, then distinguish meaning evidence,
presentation, authoring base and delivery targets. Japanese original meaning
uses text, audio, images and context. Normally author from a suitable Japanese
original, referencing English design; explain the part, purpose and reason for
necessary English-canvas/template or display-mechanism reuse. A missing Japanese
image does not exclude a task, and an edition-only asset is not necessarily new
content. Confirm actual provenance and scope for additions and identify assistance.
In editing/pixel checks, “original image” means the selected authoring base.
Preserve its protected regions and the actual target's geometry/alpha constraints;
canvas changes or added layers follow the established design/engine plan.
Review copy, visual integration, group states and every actual target separately.
Required Chinese must be fully Simplified Chinese in actual glyphs, meaning,
terminology and expression. Distinguish justified Japanese retention, already
compliant Chinese and explicitly adopted special conventions per region.
Readability, identity or decoration alone is not an exemption. Outside valid
retention, correct Traditional/Japanese glyphs, kana and untranslated terms;
`軍曹` needs this project's `中士`, not just simplified `军曹`. Inspect actual
strokes rather than relying on OCR or shared character codes. Preserve valid
original credits and special conventions within their scope, and reassess old
readability/decoration/tool-limit decisions. Known defects remain repairs even
if released; a historical compromise does not establish completion.
Reuse existing extraction/decoding, editable sources and approved work when
valid for the current version; fill gaps, changes and failures rather than
unpacking again. Declare counting units and distinguish investigation from
confirmed production, detailed inspection, human approval and runtime checks.
Inspect dynamic assets both individually and in composition/playback.
Human review compares official Japanese, optional official English, optional
previous Chinese and current Chinese with role/version/status labels and short
explanations of changes, reasons, intentional retention and open questions.
Provide materials that open on the reviewer's device, relevant dynamic previews
and a simple way to return feedback tied to stable image IDs and candidate versions.
Previous Chinese shows the revision, not authority for Japanese meaning; provide
actual text/audio/scene evidence where an image counterpart is missing. See the
[human review requirements](05-human-review-and-delivery.md).
Register actual fonts, retain unresolved limitations and publication boundaries,
and complete human corrections plus in-game checks before release.
