# 04 · 自检与返修

[上一步](03-produce.md) · [流程总览](README.md) · [下一步](05-human-review-and-delivery.md)

**输入：**最新候选、实际原意依据、选定底稿／中文设计、文案与同组差分。制作方先修掉能自行判断的问题，再交人工审核。

先核对内容与功能范围及实际目标，再分别检查原意、中文呈现和制作约束。原作含义回到日文文本、日语语音、画面与语境；画面检查对照选定底稿和中文设计，不要求每项都有日文图。底稿或目标来自英文版不能代替原意复核，也不能仅凭语言后缀排除。

日英图片都存在时，保留两版对照，检查有无漏掉的阅读信息，并比较版式、状态和图层。例如 [Photon U0478](../../rUGP/docs/crmt-family.md)的日文是竖排 4 层、英文是横排 6 层，已有中文竖排 4 层方案；不能因为中文层数不同于英文就判错，也不能只检查同一内容的一个目标就认定全部通过。

送审前按[版本归属规则](../principles.md#图片属于哪个版本)核对预览图与语言槽、索引／脚本引用的关联，而非看图中文字给日英栏归类。日文版含英文、英文版含日文或日英同图都可能正确；“共用资源”与“不同资源但同像素”分别核对，不能把同图直接判错配或把独立英文图判为全图已英译。已确认沿用不标缺图，未取得、未解码与对应待核不写成不存在。来源核对通过也不免除应译区域的简体中文检查。

| 尺度 | 主要查看 |
| --- | --- |
| 整图 | 是否自然，构图、视觉重心、物体关系是否改变 |
| 原始尺寸 | 实际阅读效果、字号、间距、清晰度和层级 |
| 局部放大 | 旧字碎点、坏笔画、繁体／日式字形、硬边、糊块、纹理与遮挡 |

逐张检查：文案／数字正确；应汉化区域在实际字形、含义、术语和表达上完整简体中文化；无不应保留的假名、繁体／日式字形和日式称谓；中文笔画完整；颜色和特效贴合；位置、透视、曲面、材质、留白、遮挡自然；声明保护范围内的人物和画面未改坏；画布和透明边缘符合选定底稿／目标格式与已确认的中文设计。

先按[三类不改的情况](../principles.md#如何判断是否需要翻译)复核范围和依据，再确认保留内容没有被误擦、改字或变形。直接复用的普通中文须逐项符合简体中文要求；七曜等特殊惯例单独确认，不能混为普通中文。明确原文保留范围外，繁体／日式字形与未汉化用语均属缺陷；例如 `軍曹` 仅改为 `军曹` 仍不合格，本项目采用 `中士`。

“能看懂”、OCR 没有检出日文或画面没有假名都不能证明合格；OCR 查到日文也只是复核线索，不能自动擦除有依据保留的原题或署名。保留原画不免除同图应译说明，旧工具妥协不作为保留依据，已知缺陷未修不能报为通过。

同时核对[最高原则](../principles.md)：原作已有英文没有被误删，日文改用英文有明确理由；原意按实际文字、语音或画面独立复核。真正新增信息的来源与采用范围明确，辅助文案符合功能且没有冒充原作。不能把“文字通顺”当成来源已确认，也不能把来源可靠当成中文呈现已合格。

检查同套菜单、按钮全状态、连续日期、昼夜、裁切和其他差分，防止只改一张、错复用日期或带错底图。自动尺寸／像素／字体覆盖检查用来发现技术问题，不能证明视觉、语义或实机质量。

图层素材按实际组合查看，检查叠放顺序、透明度、文字与背景的关系；连续帧按正确顺序和时机播放，检查字形、位置、颜色与边缘是否稳定，有无闪烁、漂移或接缝。单层、单帧检查仍须保留，但不能代替合成与连续播放检查，也不能由一帧效果推定整段通过。

按缺陷回到对应阶段：错译或来源问题回 02，残字、排版和融合问题回 03。保留已通过部分；返修后看本图和受影响同组，已有检查仍有效时不扩大成全批重做。

**输出：**已自检候选、未决问题及准确的当前版本引用。不能只检查缩略图、图片链接或解码成功，就写“视觉通过”。

## English summary

Check task scope and targets, then review meaning, Chinese presentation and
production constraints separately. Original meaning returns to Japanese
text/audio/images in context; visuals use the selected base and Chinese design,
not a mandatory Japanese counterpart. Verify copy, retention, actual source
correspondence, protected artwork, target geometry/alpha and group states at
full-frame, native and magnified scales. Confirm sources/scope for additions and
function for assistance. Technical image checks do not prove meaning, appearance
or runtime behavior. Repair affected parts and preserve still-valid work.
Check the three unchanged-content cases and their scope. Ordinary unchanged
Chinese must meet actual glyph, meaning, terminology and expression requirements;
approved weekday conventions remain a separate retention case. Outside justified
retention, Traditional/Japanese glyphs, kana and Japanese terms need correction:
`軍曹` merely changed to `军曹` still needs this project's `中士`. Readability,
clean OCR or no kana cannot prove compliance. OCR also cannot automatically erase
justified original titles/credits. Old tool compromises are unresolved repairs,
not retention reasons or passing results.
Inspect layers in their actual composition, including order, transparency and
the relationship between lettering and background. Play frame sequences in the
correct order/timing and check stable lettering, position, color and edges for
flicker, drift or seams. Individual layer/frame checks do not replace composition
and playback checks or establish that an entire sequence passed.
Keep Japanese/English comparison where both images exist to detect omitted
information and inspect layout, state and layer differences. [Photon U0478](../../rUGP/docs/crmt-family.md)
has four vertical Japanese layers, six horizontal English layers and a four-layer
vertical Chinese design. A layer-count difference from English is not itself a
defect, and one checked target does not prove all targets passed.
Check review views against verified slots, indices/script references and resource
identities, not visible language. English in a Japanese-edition image, Japanese
in an English-edition image, and equal images can all be correct. Verify shared
resources separately from equal pixels in distinct resources; neither identity
nor difference alone proves a mismatch or full English translation. Verified
reuse is not missing imagery; distinguish unfetched, undecoded and unresolved
counterparts from confirmed absence. Correct provenance does not exempt required
regions from full Simplified Chinese review.
