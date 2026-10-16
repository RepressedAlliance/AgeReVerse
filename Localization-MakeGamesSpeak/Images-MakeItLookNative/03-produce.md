# 03 · 制作图片：去字、排字与画面融合

[上一步](02-copy-and-style.md) · [流程总览](README.md) · [下一步](04-self-review.md)

**输入：**02 选定的制作底稿、已复核文案、已确认呈现与样式，以及允许修改和需要保护的区域。去字与中文制作是同一阶段内的处理动作，根据文字存在方式选择方法。

本步的“原图”指实际采用的制作底稿，通常是日文版适用原图或由其制作的合法无字底；确需复用英文版画布或模板时，沿用 02 明确的具体部分、中文用途和理由，不默认拿英文成品图改中文。原意依据另行关联。像素保护针对该底稿和声明范围，输出画布、有效区域与图层仍须满足实际目标格式。新增叠层或换画布沿用已确认的中文设计及引擎方案，不能为了通过像素检查缩回日文透明占位，也不能无依据放宽保护范围。

## 先确定最小完整文字单元

**文案按完整单元确认，修改范围按实际缺陷确定，验收仍看完整单元。** 词组、整行广告、招牌标题等共用一套笔迹和排版，不能以“只改一个字”或改动像素最少作为质量目标。能够完整清除旧字，并让新字与原有字体／笔迹、字重、基线、字距和效果一致时，可以局部修补。

局部修补留下残笔、叠影、混杂字形、拼接感或间距失衡，无法可靠修干净时，应重做**最小完整视觉文字单元**，清除该单元需要替换的旧字后统一排字、绘制或受控编辑，不能继续用新字盖旧字。必要时更新声明的文字修改范围；重做完整词组或整行不等于重绘整图，仍保护无关画面、原作英文、数字和明确保留文字，不改动已合格的其他单元。

## 清除旧字、修复底图

先完整清除需要替换的旧文字，再制作中文。去字包括主笔画、抗锯齿边缘、碎点、描边、阴影、光晕和裁切／遮挡处残笔，不能靠新字盖住、靠模糊掩盖。按最高原则保留的原作英文不纳入去字区。

按实际底图选择方法：正确的无字底或同底语言图 → 同组能恢复的背景 → 修复／仿制 → 局部生成式编辑。复杂材质可直接采用效果更好的区域修图，不必反复用已证明不合适的硬覆盖。清楚底图不必调用模型；复杂图也不强制使用某个固定算法。

允许修改区域覆盖旧字及必要特效，保护人物五官、发丝、泪痕、皮肤、物体轮廓、图案、应保留的英文、数字和前景遮挡。区域外恢复／保留原图像素，并用[图像检查工具](tools.md)确认实际差异；提示词“其他不变”不能当作证明。透明图允许文字区内部的 alpha 随新字变化，区域外仍须保留，不能机械要求整张 alpha 完全一致。

单独查看无字底的整图和放大细节，修掉色差、矩形补丁、重复纹理、糊块和断边。复制旧图像素回补时警惕重新带回旧字。对于一体生成的手写／Logo 方案，仍先确定去字与保护范围，并把底图缺陷和新文字缺陷分别检查。

## UI、日期、字幕和独立标题

普通排版优先复用[确定性排字工具](tools.md)，统一字体、字号、字重、间距、基线和状态效果。匹配字高字宽、重心、留白、颜色、渐变、阴影和光晕。不要压扁中文以塞进原框，不要逐词改变字重或只修按钮一个状态。

Logo 与手写可采用绘制或受控生成，再校正实际文案和笔画。按已选中文方案制作所需变体，通常以日文版适用原图为基础，英文设计用于样式对照；确需复用英文版具体画布或模板时，沿用 02 确认的部分、用途与理由，不自动各做一套中文。根据选定底稿、作品风格与中文阅读检查效果；柔和原字不能无故变成硬描边，浓艳颜色不能无故变灰淡。按[最高原则](../principles.md)保留原作已有的英文副标题，装饰文字则沿用 02 已明确的处理范围，不因属于装饰就保留，也不把英文版后来替换的内容一概保留。

应汉化区域完整采用简体中文的字形、术语与表达，不能只替换假名或做繁简转换。手写、印刷与生成字都检查实际笔画，不能让日式字形、繁体字形或日式称谓混入；原图文字已经全部合格时才直接复用。明确保留的原文与特殊惯例限于 02 确认的范围，保留纸张、笔迹风格和构图不能成为保留文字缺陷的理由。

## 附着在物体上的文字

先看完整场景，再制作局部。招牌服从平面透视，罐身跟随曲面，书页跟随方向与折痕，皮肤涂鸦跟随形状、光照和遮挡。位置、大小、方向、透视、留白与前后关系同时成立，不能像平面贴纸。

让字的锐度、对比度、颗粒、磨损和模糊度服从材质及距离。远处字不异常清晰，暗处字不自发光；新字仍被头发、物体或画面边缘遮挡。人物身上的文字也用这套要求，不因文件分类是 CG 就忽略空间关系。

## 使用图像编辑模型

可用于去字、恢复背景、特殊字形／Logo、手写效果和获准的装饰拟写，**不限制为只能生成无字底**。任务说明应包含：允许改哪里、锁定译文和数字、允许拟写哪里、保护什么，以及空间、材质和效果参考。

每次生成只是候选。检查中文实际笔画，纠正重排海报、修改价格、移动物体、损伤人物等错误；需要时恢复区域外原图。能力和档位不替代结果检查，失败时调整方法，不能反复把同类缺陷交给维护者。

**输出：**候选图及可复用配方。遵守选定底稿的保护范围和实际目标的画布、有效位置与透明边缘要求；用于游戏的母版与放大预览分开。

## English summary

Produce from the selected base, checked copy and approved Chinese design/style.
Normally use a suitable Japanese original or its lawful textless derivative.
Any necessary English-canvas/template reuse follows 02's specified part, Chinese
purpose and reason; English finished artwork is not the default base.
Meaning evidence is linked separately. Pixel preservation applies to that
base and the declared edit mask, while canvas, alpha and geometry must satisfy
the actual target format. Added layers or canvas changes need the established
engine/design plan, not a blanket relaxation of constraints. Select suitable
typesetting, painting or constrained editing, preserving unrelated artwork,
spatial relationships and approved retention. Make only the chosen variants,
and keep runtime masters distinct from enlarged previews.
Required Chinese regions must be fully Simplified Chinese in glyphs, terminology
and expression, including handwriting and generated lettering. Check actual
strokes; removing kana or converting Traditional characters alone is insufficient.
Reuse original lettering only when fully compliant or within a justified original
retention/special-convention scope from 02. Preserving artistic style does not
justify preserving text defects.
Confirm the whole lettering unit's copy, choose the edit scope from actual
defects, and review the complete unit afterward. A one-character repair is
acceptable when old lettering is fully removed and the font/handwriting,
weight, baseline, spacing and effects remain consistent. Minimal character or
pixel changes are not the quality goal. If local repair cannot remove remnants,
double strokes, mixed glyphs, seams or spacing imbalance reliably, rebuild the
smallest complete visual lettering unit with clean removal and consistent
typesetting/drawing/editing. Update the declared text-editing scope as needed;
this does not authorize whole-image repainting or changes to unrelated artwork,
original English, numbers, approved retention or other correct units.
