# 01 · 全量提取与分类

[流程总览](README.md) · [翻译最高原则](../principles.md) · 下一步：[02 文案与样式](02-copy-and-style.md)

**输入：**本次支持版本的合法本机游戏、已有提取清单与对应引擎工具。

## 全量提取

1. 枚举所有资源包、松散资源、语言槽、共用资源及 fallback。使用 [AGE2](../../AGE2/README.md) 或 [rUGP](../../rUGP/tools/README.md) 提取和解码，不在共用目录另写一套引擎解析器。
2. 保留游戏、版本、原始路径／对象 ID、尺寸、模式与来源摘要。图片预览与源对象保持可追溯对应，不能只留下重命名后的 PNG。
3. 覆盖 UI、背景、CG、道具、姓名、日期、字幕、标题、透明叠层和差分。不能只提取目录名含 `ui` 的文件，或把已有送审页当作全部图片。
4. 统计未解码、未关联、缺少预览的资源；列出失败原因和下一步位置，不能从总数里静默丢掉。
5. 完全相同的解码像素可以共用检查，但保留所有路径和调用映射。昼夜、按钮状态、透明度、裁切或文字有差异的图不能按相似度合并。

能对上“枚举资源 → 解码结果 → 待处理项”后进行分类；不能宣称所有图片已提取却没有说明未解码资源。

## 分类、分组和确定范围

**先按内容与功能确定中文任务，再选择所需素材及应译区域。** 将图片与同场景的文本、语音和对象调用关联，区分原作已有内容换了载体、同一功能的不同官方设计、真正新增的信息以及尚未确认的对应关系。原作没有同形式日文图，也可能通过语音或其他画面传达了同一内容；没有找到对应不能当作已经证明不存在。

复用现有清单或备注，分别关联原意依据、中文呈现、制作底稿、当前成品和预期交付对象。原作含义以日文文本、日语语音、画面和语境确认；适用的官方日英设计与素材均可供制作采用，不凭 `_ja`／`_en` 后缀分类。先确定中文用途并规划实现，不要求任务已经在中文版生效。rUGP 的现有 `translation` 槽可以是实际目标；真正新增信息按[总则](../principles.md#官方版本差异怎么处理)确认来源、用途和范围，不统一强制听译。用途或对应关系不明则说明待确认事项，最后交付阶段验证实际绑定。

有日英版本时，清单保留**官方日文、官方英文、中文候选**的对应与共用关系。英文图即使不制作，也能帮助发现不同设计、字幕和调用；不要删掉这种对照，也不要把每张对照图自动计成制作任务。例如 [Photon HUD 的英文](../../rUGP/docs/postmortems/pending-hook-entry-points-20260909.md)在日文图片模式也能出现，不能直接归成英文版遗漏；[AGE2 菜单](../../AGE2/docs/postmortems/image-layout.md)则可以保留原英文主体、只替换日文副标题。具体应译区域仍须逐图判断。

提取和查看的资源总数、中文版待制作项及已完成成品分别统计。仅供参考的差分保留在对照清单中，不计入待制作数量或完成成果；去重检查仍保留各语言和调用关系，不能把同像素的所有路径都自动列为中文交付目标。

逐图看实际内容，OCR、文件名和目录只作辅助。

| 功能 | 例子 | 需要另外识别的关系 |
| --- | --- | --- |
| 界面与独立文字 | 按钮、菜单、姓名、日期、字幕 | 同级排版、状态、选中光晕、语言槽 |
| 标题与 Logo | 主标题、章节标题、不同篇章变体 | 每版设计、英文副标题、透明效果 |
| 剧情读物与道具 | 信件、漫画、报纸、地图、人物涂鸦 | 剧情用途、脚本／语音依据、物体透视 |
| 场景文字 | 招牌、海报、包装、书页 | 昼夜、距离、曲面、光照和遮挡 |
| 无需修改／待确认 | 无文字、已认可保留项、无法识读项 | 具体保留原因或疑问位置 |

对每图分别决定：**需要制作、已有可复用成品、明确保留、无须汉化、待确认**。旧“已完成”记录要对照最新成品；旧“保留”决定遇到后来的新要求，要以该项最后明确决定为准。

将同一菜单、按钮全状态、连续日期、人物卡和同场景差分归为组。列出实际存在的成员，不按想象补出缺少的状态。Logo 设计不同的变体分别记录，不能共用一张成品冒充全部完成。

根据最高原则区分原作有意使用的英文与英文本地化译文，后者不因出现在底稿上就按原作英文保留。按[内容用途、玩家理解和原作表现](../principles.md#如何判断是否需要翻译)划定应译与保留区域，不以有无日文决定是否改图。大部分承担阅读功能的日文应译；原文主要用于身份识别、画面表现或可在中文语境直接沿用时，可说明理由后保留。已有例子帮助判断，新素材不因未列出就必须重绘；同一图的装饰和阅读信息分别处理。先确认范围，再检查应译区域的日式字形；既有决定须核对具体语境，不机械跨游戏套用。

**输出：**全量清单、可浏览原图、素材组和优先顺序。每张图均有去向，未解码或待确认项有原因和下一步位置。剧情图即使放在背景目录，也不会漏入最低优先级。

## English summary

Extract all resources and retain undecoded/unmatched entries. Define Chinese
tasks by content/function and link the same scene across text, audio and images.
Distinguish existing content in another medium, alternative designs, genuine
additions and uncertain correspondence. Link meaning evidence, presentation,
authoring base and intended targets separately through existing records.
Suitable official-edition resources may be production inputs regardless of
suffix; Chinese use need not already be implemented. Keep every actual target's
identity/state/calls. Confirm genuine additions under the shared principles.
Reference-only variants do not count as pending or completed Chinese production.
Where Japanese and English editions exist, retain Japanese/English/Chinese
correspondence and shared relationships even for comparison-only images.
The [Photon HUD case](../../rUGP/docs/postmortems/pending-hook-entry-points-20260909.md)
contains English in Japanese image mode too; [AGE2 menus](../../AGE2/docs/postmortems/image-layout.md)
keep original English main lettering while replacing Japanese subtitles. These
examples require region-by-region decisions, not filename-based language guesses.
