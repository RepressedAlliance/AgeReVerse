# 01 · 全量提取与分类

[流程总览](README.md) · [翻译最高原则](../principles.md) · 下一步：[02 文案与样式](02-copy-and-style.md)

**输入：**本次支持版本的合法本机游戏、已有提取清单与对应引擎工具。

## 全量提取

“全量”要求覆盖完整，不表示每轮都重新解包。先查已有提取／解码清单、对应游戏版本、可编辑源文件、已确认成品及当前交付映射；核对其是否适用于本次版本。可用的结果直接复用，只补提取缺失、发生变更或解码失败的部分。旧路径失效时，先查交接记录与当前制作目录，不能直接认定从未提取或从未制作。

1. 枚举所有资源包、松散资源、语言槽、共用资源及 fallback。使用 [AGE2](../../AGE2/README.md) 或 [rUGP](../../rUGP/tools/README.md) 提取和解码，不在共用目录另写一套引擎解析器。
2. 保留游戏、版本、原始路径／对象 ID、尺寸、模式与来源摘要。图片预览与源对象保持可追溯对应，不能只留下重命名后的 PNG。
3. 覆盖 UI、背景、CG、道具、姓名、日期、字幕、标题、透明叠层、逐帧序列和差分。不能只提取目录名含 `ui` 的文件，或把已有送审页当作全部图片。
4. 统计未解码、未关联、缺少预览的资源；列出失败原因和下一步位置，不能从总数里静默丢掉。
5. 完全相同的解码像素可以共用检查，但保留所有路径和调用映射。昼夜、按钮状态、透明度、裁切或文字有差异的图不能按相似度合并。

能对上“枚举资源 → 解码结果 → 待处理项”后进行分类；不能宣称所有图片已提取却没有说明未解码资源。

区分可直接查看的静态整图、需要组装的图层、连续帧序列与视频，保留组装或播放所需的对应关系。优先复用已有导出和合成预览，按实际使用效果识别文字；单层无字或某一帧正常，不能证明整个演出无须处理。视频提取、编码等实现使用对应引擎文档，不在这里另建技术流程。

## 分类、分组和确定范围

**先按内容与功能确定中文任务，再选择所需素材及应译区域。** 将图片与同场景的文本、语音和对象调用关联，区分原作已有内容换了载体、同一功能的不同官方设计、真正新增的信息以及尚未确认的对应关系。原作没有同形式日文图，也可能通过语音或其他画面传达了同一内容；没有找到对应不能当作已经证明不存在。

复用现有清单或备注，分别关联原意依据、中文呈现、制作底稿、当前成品和预期交付对象。原作含义以日文文本、日语语音、画面和语境确认；图片通常以日文版适用原图制作，英文设计供参考；确需复用英文版具体画布或模板时，说明用途与理由，不凭 `_ja`／`_en` 后缀推定素材角色。先确定中文用途并规划实现，不要求任务已经在中文版生效。rUGP 的现有 `translation` 槽可以是实际目标；真正新增信息按[总则](../principles.md#官方版本差异怎么处理)确认来源、用途和范围，不统一强制听译。用途或对应关系不明则说明待确认事项，最后交付阶段验证实际绑定。

有日英版本时，清单保留**官方日文版用图、官方英文版用图、中文候选**的对应关系。按[版本归属规则](../principles.md#图片属于哪个版本)，先查日文版原包与已有提取记录，再按该游戏已核实的语言槽、索引／脚本选择和资源映射确认各版用图，并追到共用或回退资源。记录对应版本、资源身份与采用依据即可；槽位来源不能由图内语言、OCR 或未经核实的文件名决定。未能确定则保留来源待核，不能因为日文版图里有英文就挪到英文栏。

| 已确认的关系 | 怎样登记 |
| --- | --- |
| 日英路由引用同一资源 | 日英共用资源，保留两版用途与引用 |
| 不同资源的解码像素相同 | 日英像素相同，保留各自资源身份；不能据此推定共用同一对象 |
| 英文路由沿用日版／共用图，没有独立差分 | 标明沿用及依据，不当作缺少英文版画面 |
| 日英有不同像素或独立差分 | 关联同场景、同状态，另检查哪些区域英译、保留日文或仅作罗马字转写；不同图不代表全图已英译 |
| 对应图未取得、未解码或关系未核实 | 说明具体缺口，不直接写不存在，也不拿其他图凑配对 |

图内语言和中文处理范围在上述归属之外逐区识别。英文版用图即使不制作，也能帮助发现设计、字幕和调用差异，不自动计为制作任务。例如 [Photon HUD 的英文](../../rUGP/docs/postmortems/pending-hook-entry-points-20260909.md)在日文图片模式也能出现，画面有英文不能直接归成英文版遗漏；[AGE2 菜单](../../AGE2/docs/postmortems/image-layout.md)可保留原英文主体、只替换日文副标题。来源、像素比较与最终实机状态分别说明，复用适用的已有映射，不为送审重复启动每个场景。

提取和查看的资源总数、中文版待制作项及已完成成品分别统计，并说明计数单位：资源路径、去重图片、文字区域、素材组或帧数，不能混着相减或计算完成率。仅供参考的差分保留在对照清单中，不计入待制作数量或完成成果；复用同一成品的多个目标不重复算作新制作图片。去重检查仍保留各语言和调用关系，不能把同像素的所有路径都自动列为中文交付目标。

逐图看实际内容，OCR、文件名和目录只作辅助。

| 功能 | 例子 | 需要另外识别的关系 |
| --- | --- | --- |
| 界面与独立文字 | 按钮、菜单、姓名、日期、字幕 | 同级排版、状态、选中光晕、语言槽 |
| 标题与 Logo | 主标题、章节标题、不同篇章变体 | 每版设计、英文副标题、透明效果 |
| 剧情读物与道具 | 信件、漫画、报纸、地图、人物涂鸦 | 剧情用途、脚本／语音依据、物体透视 |
| 场景文字 | 招牌、海报、包装、书页 | 昼夜、距离、曲面、光照和遮挡 |
| 无需修改／待确认 | 无文字、已认可保留项、无法识读项 | 具体保留原因或疑问位置 |

对每图分别决定：**需要制作、已有可复用成品、明确保留、无须汉化、待确认**。旧“已完成”记录要对照最新成品；旧“保留”决定遇到后来的新要求，要以该项最后明确决定为准。

**待核查不等于待汉化。** 进度说明分别列出仍需识读／解码／确认用途的范围、已确认需要制作或返修的范围，以及可复用、保留、无须修改的范围。概览筛选、逐图细查、制作方自检、人工确认和实机检查分别说明；初览过不能报成逐图审核通过，静态成品完成也不能报成实机完成。范围尚未确定时给出已知数量与未知范围，不据此推算总完成率。复用现有清单即可，不要求新建一套庞大台账。

将同一菜单、按钮全状态、连续日期、人物卡和同场景差分归为组。列出实际存在的成员，不按想象补出缺少的状态。Logo 设计不同的变体分别记录，不能共用一张成品冒充全部完成。

根据最高原则区分原作有意使用的英文与英文本地化译文，后者不因出现在底稿上就按原作英文保留。原图不改时按[三类情况](../principles.md#如何判断是否需要翻译)说明：有意保留日文、实际字形／含义／术语／表达均已符合简体中文，或沿用有明确依据的特殊惯例。七曜星期标记属于特殊惯例，不能只凭字形相同就当作普通中文已经合格。同图分区判断，身份标记、装饰或“玩家能看懂”本身不免译。

应汉化区域中的繁体／日式字形、假名和未汉化的日式称谓均须处理；字符编码或 OCR 相同不能证明画面字形相同。既有决定核对具体范围与依据，仍适用的直接复用；仅凭可读性、装饰分类或旧工具限制的决定须重新判断。已知文字问题列为待修，依据不足列为待确认，不把历史妥协当成保留或完成，也不机械跨游戏套用。

**输出：**全量清单、可浏览原图、素材组和优先顺序。每张图均有去向，未解码或待确认项有原因和下一步位置。剧情图即使放在背景目录，也不会漏入最低优先级。

## English summary

Complete coverage does not mean unpacking everything again. First locate and
check existing extraction/decoding inventories, game versions, editable sources,
approved outputs and current delivery mappings. Reuse valid results and extract
only missing, changed or failed parts. A broken old path calls for checking
handover records and current directories, not assuming the work never existed.
Retain undecoded/unmatched entries. Distinguish static images, composed layers,
frame sequences and video; preserve composition/playback relationships and reuse
existing exports/previews. Judge lettering in its actual use: one textless layer
or clean frame does not establish that the whole sequence needs no work. Keep
video extraction/encoding implementation in the relevant engine documentation.
Define Chinese
tasks by content/function and link the same scene across text, audio and images.
Distinguish existing content in another medium, alternative designs, genuine
additions and uncertain correspondence. Link meaning evidence, presentation,
authoring base and intended targets separately through existing records.
Normally author from a suitable Japanese original and reference English design.
Identify any necessary English-canvas/template reuse and its purpose/reason;
filename suffixes do not determine roles. Chinese use need not already be implemented. Keep every actual target's
identity/state/calls. Confirm genuine additions under the shared principles.
Reference-only variants do not count as pending or completed Chinese production.
Declare counting units: resource paths, deduplicated images, lettering regions,
groups or frames. Do not mix them to calculate remaining work or completion.
Multiple targets reusing an output are not multiple newly authored images.
Separate investigation from confirmed production/repair and from reuse,
intentional retention or no-change decisions. Report overview screening,
detailed inspection, self-review, human approval and in-game checks separately.
Do not infer an overall completion rate while scope remains unknown; give known
counts and unknown coverage. Reuse existing records rather than adding a large
mandatory ledger.
For unchanged regions, distinguish justified Japanese retention, content already
meeting Simplified Chinese glyph/meaning/terminology/expression requirements,
and explicitly adopted special conventions such as approved weekday notation.
Readability, identity or decoration alone is insufficient. Inspect actual glyphs,
not just OCR or character codes. Reassess old decisions based only on those weak
reasons or tool limits: known defects need repair, uncertain cases need review.
Reuse still-valid decisions without treating historical compromises as complete.
Where Japanese and English editions exist, retain official Japanese-edition and
English-edition image roles alongside Chinese candidates. Establish provenance
from verified slots, indices/script selection and resource mappings, following
shared objects and fallback; visible language, OCR or unverified filenames do not
determine the edition. Search original Japanese packages and existing extracts
first. Retain version, identity and the existing mapping evidence; unknown origin
remains unresolved rather than being guessed from English lettering.
Distinguish a shared resource from equal decoded pixels in separate resources;
retain both roles and all resource identities. Verified English reuse without a
separate variant is not a missing English-edition view. Independent/different
English images may still contain Japanese, partial translations or romanization.
Distinguish unfetched, undecoded and unresolved counterparts from confirmed
absence. Assess visible language and Chinese treatment separately by region.
Keep static provenance, pixel comparison and final in-game status distinct;
reuse valid mappings rather than replaying each scene just to prepare review.
The [Photon HUD case](../../rUGP/docs/postmortems/pending-hook-entry-points-20260909.md)
contains English in Japanese image mode too; [AGE2 menus](../../AGE2/docs/postmortems/image-layout.md)
keep original English main lettering while replacing Japanese subtitles. These
examples require region-by-region decisions, not filename-based language guesses.
