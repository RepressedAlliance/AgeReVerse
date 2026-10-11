# 图片字幕排版：把字排正，也放对位置

[AGE2 技术案例](README.md) · [图片本地化流程](../../../Localization-MakeGamesSpeak/Images-MakeItLookNative/README.md)

图片字幕的最终显示由图片内部布局与脚本放置坐标共同决定。下面以帝都燃烧和 TDA 的 AGE2 字幕为例，说明怎样避免偏移、裁切和正文遮挡。

## 保留原版演出位置

原版既有单独显示的字幕，也有与正文同时出现的抬高字幕。将帝都的 `0,-2145,723`、`0,-2170,723` 统一改成普通字幕的 `0,-1550,723`，会消除演出为正文预留的空间。制作中文图片时保留对应场景的原始坐标，排版调整优先在原画布内完成。

日文字幕图也可能只是 1×1 透明占位。此时从配对素材和脚本确定画布与调用，不能把占位图当作最终图片尺寸。文案仍依据对应日语语音听译，英文只辅助定位与版式参照。

## 对齐实际可见的字形

字体测量框包含侧边距与标点留白，按测量框居中，实际文字仍可能偏移。先渲染文字和描边，再量取透明通道的非透明边界，按可见字形完成水平对齐并保持底边。

多行字幕另需固定基线距离。逐行继承不同字形中心、或按首行字体度量计算行距，都会让短行与长行看起来不齐。共享工具 [caption_layout.py](../../tools/images/caption_layout.py) 按可见字形排每一行；带小字注音的字卡保留原作字号层级与相对位置。

| 素材 | 实现参数示例 |
| --- | --- |
| 帝都字幕 | 1280×720 画布，24px 字号，2px 描边，32px 基线距离，可见底边 y=673 |
| TDA 普通开篇字卡 | 20px 字号，28px 基线距离；特殊小注音单独排版 |

这些是对应素材的参数。其他游戏应根据原画布、场景坐标与显示空间重新确定，不能照搬为统一标准。

## 控制字幕与正文共同占用的空间

中文增加一行可能超出抬高字幕的空间。帝都生成器统一字号并限制可见字高，超限时调整断行，不逐句缩字。对应英文字幕的可见高度用于空间参照；它不取代日语文案依据。

字幕中心左偏的修正也不能只改脚本坐标。TDA 附加字幕曾因字体测量框留下约 5.5–6px 偏差，后续候选改为最终可见字形对齐。候选图的静态修正与某个安装包的采用、实际剧情显示应分别确认。

## 复用时检查什么

- 保持原画布、可见字形底边与场景坐标，检查裁切、中心和抬高字幕的高度。
- 对照脚本的实际调用，区分单独字幕、与正文同显的字幕及未调用记录。
- 回到对应剧情检查同显、清除时机与语言切换。图片和脚本静态检查不能代替这些实机行为。

实现见[帝都生成器](../../games/imperial-capital-burns/tools/build_phase1.py)的 `render_telop`、`patch_telop_positions` 及共享排版工具。

## English

Preserve scene-specific caption positions. Center the rendered alpha bounds rather than font advance boxes, use consistent line pitch, and fit raised captions into the space shared with dialogue. The numerical recipes above are specific to Imperial and ordinary TDA cards. Static layout, package adoption and in-game behavior are separate checks.
