# 图片汉化｜让中文长在原画里

**Image Localization — Make It Look Like It Was Always There**

[返回本地化](../README.md) · **[翻译最高原则](../principles.md)** · [视觉制作规范](production.md) · [字体目录](../fonts-that-fit-the-game/README.md) · [现有工具用法](tools.md)

<details>
<summary><strong>English · Make It Look Like It Was Always There — expand here</strong></summary>

## English workflow

Five stages: extract and classify all images; confirm copy and style; produce images; self-review and repair; obtain human review and deliver through the engine. Follow the shared [translation principles](../principles.md#english-summary): translate Japanese into Chinese, preserve English present in the Japanese original, use English for Japanese only when justified, and translate English-edition-only assets from their corresponding Japanese voice.

Most Japanese lettering needs translation, but determine the translation and retention regions by function, player understanding and the original presentation first. Remove old lettering and its effects only where translation is needed, then author Chinese using reproducible typography, drawing or constrained image editing as appropriate. Match perspective, material, lighting and occlusion. Review every output at full-frame, native and magnified scales, then obtain the maintainer's review of the exact final candidate. Bind the approved output through the appropriate engine, test in game, and complete the maintainer's final corrections before release.

The stated Astra 6 / Image 2.5 baseline is the maintainer's practical reference, not a guaranteed ranking. A capable alternative still needs representative-image validation. Clear copy, prices and plot information are fixed; only unresolved decorative text may be reconstructed with an explicit record. Preserve unrelated pixels and distinguish authoring, human approval, engine verification and publication.

</details>

一块按钮、一张手写便条、一幅嵌着文字的场景，都有自己的字形、材质和空间关系。目标是让中文像原图本来就有的一部分：**视觉自然、空间关系正确，清楚的信息准确，同套素材一致，无关画面保持原样。** 这套步骤整理自本项目实际的图片提取、全量分类、UI／场景制作、返修及维护者审核过程。

大部分日文文案需要翻译，但不是看到日文就必须改图。先按[内容用途、玩家理解和原作表现](../principles.md#如何判断是否需要翻译)确定应译与保留区域，再安排制作；保留原图或部分文字也可以是经过核查的正确结果。

维护者从 2026 年 10 月起使用的经验基线是：视觉理解能力不低于 **Astra 6**，局部图像编辑能力不低于 **Image 2.5**，特别是对未选区域的保留能力。其他模型或工具具备相当能力时也可复用这套方法。这里是项目的经验基线，不是模型性能排行榜；仍要用代表图确认识读、空间理解、编辑范围和成品质量。旧批次的工具限制不作为新制作的固定限制。

## 五个阶段

编号表示制作的主要阶段，不要求把每个动作另立一步。提取和分类一起完成，去字与排字属于制作，最后由维护者审核并完成交付；具体素材按需要处理。

| 步骤 | 内容 | 本步交付 |
| --- | --- | --- |
| **01** | [全量提取与分类](01-extract-and-classify.md) | 所有图片的来源、分类、分组与处理决定；未解码项也有记录 |
| **02** | [确认文案、字体和样式](02-copy-and-style.md) | 遵守最高原则的已复核文案、同套样式和代表图 |
| **03** | [制作图片](03-produce.md) | 去字修底、中文制作和画面融合后的候选图 |
| **04** | [自检与返修](04-self-review.md) | 逐图、逐组检查过的最新候选与未决问题 |
| **05** | [人工审核与交付](05-human-review-and-delivery.md) | 维护者审核、修正后的成品，以及引擎绑定、实机检查与发布前收尾 |

先完成 UI、按钮、姓名、日期、字幕、标题等非场景素材，再处理普通场景背景。剧情用的信件、漫画、报纸或道具文字按剧情需要安排，不能因存在 `bg/` 就降成装饰背景。分类决定安排；**文字怎样附着在画面上**决定制作方法。

同一张图返修不必重走全流程：回到受影响步骤，复查本图和相关差分。已通过的字体、颜色、光晕和画面部分应保留，避免修一处又破坏另一处。

## 工作记录只保留必要内容

复用游戏现有清单或字段，不要求每作另造一套庞大表。至少能找到：游戏与源资源身份、分类／组、原文与已采用文案、保留／拟写决定、字体或绘制方式、当前成品、检查结果、维护者意见和最终交付位置。原图、候选和审核页留在本地制作目录，公开范围见[制作规范](production.md#9-复用返修与公开)。

“已制作”“已自检”“人工已确认”“实机已确认”“已发布”是不同事实，不能用一个 `done` 混称。也不能用文件存在、OCR 通过或模型档位替代查看图片。
