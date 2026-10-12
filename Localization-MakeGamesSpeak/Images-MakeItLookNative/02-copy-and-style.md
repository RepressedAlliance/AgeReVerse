# 02 · 确认文案、字体和样式

[上一步](01-extract-and-classify.md) · [流程总览](README.md) · [下一步](03-produce.md)

**输入：**内容／功能分类、实际原意依据、可选底稿及同套素材，已有文本／术语与最后采用的修订。

## 先确认文字

沿用 01 的内容与功能范围，分别确定原意依据、中文呈现、实际制作底稿和目标规划。原作含义回到日文文本、日语语音、画面与语境；排版、信息组织、图层和显示机制可采用适用的官方日英方案，再按中文阅读与画面效果调整。选用英文版底稿或现有 `translation` 目标不等于按英文译文裁定含义，也不自动增加另一套交付。

先遵守[翻译最高原则](../principles.md)：目标是日译中，日文原版已有英文保持英文；只有确实更适合英文表达的日文才采用英文，并说明理由。能读清的人名、操作提示、标题、数字、价格和剧情线索必须忠实处理。

按[通用判断方法](../principles.md#如何判断是否需要翻译)先锁定应译与保留区域；有依据保留的内容不送入自动擦字／重绘范围，不限于曲名、署名、装饰、日期标记等示例。保留一部分不代表整图免译：例如保留壁纸原画时仍单独处理图库图注，保留署名时仍翻译岗位。待审核的中文曲名候选不能自动替代原题。

按实际载体识读、回读或听译，独立复核原意；语音输入记录资源、必要片段／场景定位、工作转写和疑点，不能只审第一轮转写。日文图缺失不影响采用语音或文本依据，关键含义不明仍待确认。真正新增信息先确认来源与采用范围，辅助文案还需核对功能并明确性质。按[文本初译和独立审核](../Text-AITranslationWorthReading/README.md)核对译文和[现行术语](../Glossaries-KeepItConsistent/README.md)，不采用已被维护者改掉的旧候选。

有官方英文时，准确对应它的文案和画面，参考其译法、字幕分段、信息层级和版式；与日语有出入时回到原作核对。以 [AGE2 图片字幕](../../AGE2/docs/postmortems/caption-layout.md)为例：日文图可能只有透明占位，英文图可以提供实际画布与排版，中文文案则从对应日语语音听译。TDA01 欢呼字幕仍有[一句末尾待复听](../../AGE2/docs/limitations.md)，英文可作为待核线索，不能据此把该句当成已定稿。

选定底稿时说明来自哪个资源、借鉴哪些设计、允许改变哪些区域以及目标格式约束。普通替换在相应画布内制作；需要新叠层、换画布或重排时，先确认引擎能够承载并记录中文方案，不以不存在的日文图或透明占位限定版式。

无法识读的**非剧情装饰小字**，可结合完整场景拟写合理中文，也可由生成工具提出候选。注明“场景拟写”及用途；不能冒充识读结果。涉及剧情或操作、无法确认的信息集中列疑问，给出实际图片、位置、候选文字和依据。清楚字与模糊字混在一块时分别约束，不允许模型连已知数字一起重写。

## 再确定同套样式

从[字体目录](../Fonts-ThatFitTheGame/README.md)选型，记录具体文件／版本、字重、字号、字距、行距、基线、颜色、描边、光晕、阴影和输出方式。图片字体不自动沿用游戏正文的运行时字体。手写或生成 Logo 没有真实字体文件时如实记录绘制方式。

每批新图和返修都按[字体登记规范](../Fonts-ThatFitTheGame/registration.md)记录实际用字：来源、作者、许可、文件身份和修改情况进入字体目录，游戏／素材组引用对应条目。同图混用、实际后备字、TTC 字体索引和可变轴分别写清；仅作试样不标为最终采用。字体作过生成底稿或参考输入时也保留来源，不能因后续修图就略去。复用现有组配方，不另造每张必填的重复表。

先选横排、竖排、透明效果、密集文字、透视／曲面、模糊小字等有代表性的图试做，按当前授权交维护者确认，再批量复用。同级文字统一设计源样式，之后按各图适配光照与透视；**不要把每个词分别缩放到相同墨迹外接框**。长文案按整组规则调整，确需例外时解释原因。

**输出：**经过复核的文案、统一样式和已确认样图。疑点与保留项明确；样图成功不等于全批自动通过。

## English summary

Choose meaning evidence, Chinese presentation, authoring base and target plan
separately. Original meaning uses Japanese text/audio/images in context; official
designs, layers and display mechanisms from either edition may be adapted.
Independently check actual text, images or audio, not only transcripts. Confirm
the provenance and adopted scope of genuine additions, and identify functional
assistance. Declare the selected base, borrowed design, editing scope and target
constraints; verify engine support before changing canvas or adding a layer.
Keep approved terminology/retention decisions, register actual font use and
establish representative samples before applying a shared style.
Keep the official English copy/image where available for wording, segmentation,
hierarchy and layout comparison. In the [AGE2 subtitle case](../../AGE2/docs/postmortems/caption-layout.md),
English supplies a usable canvas while Japanese speech supplies the meaning.
One [TDA01 cheer ending](../../AGE2/docs/limitations.md) still needs relistening;
English may guide the question but does not make that line final.
