# 图片用字与制作样式

[字体入口](README.md) · **[七作用字总表](audit.md)** · [版本与资料限制](font-evidence.md) · [图片流程](../Images-MakeItLookNative/README.md) · [作者与许可](attribution.md) · [排字方法](typography.md)

图片字体按素材组维护。同一级文字统一字重、字号、字距、基线和特效，再分别适配透视、距离与光照；不能按每个词的墨迹外接框重新缩放。运行时正文用字与图片用字没有自动绑定关系。

本页按素材组列实际用字与样式。当前发布包、历史批次、本地候选、局部字层和生成参考分别登记；逐图清单与计数单位见[索引](image-font-index.json)。

制作过、已采用和已发布分别记录；绘制、生成或复用原字形不靠外观猜字体名。下面从当前发布包反查实际字层，再列本地在制和历史试样。

## 当前发布包的图片用字

五作 AGE2 当前发布清单包含 **859 个独立 WebP／AVIF 文件**。每个文件的路径、成品摘要、字体及来源记录见 [AGE2 发布图片用字表](age2-released-image-fonts.json)。采用版本如下：

| 作品 | 对应公开版本 | 图片文件 | 新排字／HTML 排字 | 原版图片原样沿用 |
| --- | --- | ---: | ---: | ---: |
| TDA00 | BETA 0.2.1 | 71 | 54 | 17 |
| TDA01 | BETA 0.3.3 | 118 | 93 | 25 |
| TDA02 | BETA 0.2.1 | 115 | 94 | 21 |
| TDA03 | BETA 0.2.7 | 153 | 110 | 43 |
| 帝都燃烧 | BETA 0.2.1 | 402 | 292 | 110 |

新排字素材确认用到 Noto Sans SC 可变字体、Noto Sans SC 静态 500、狮尾加糖宋体 Medium、思源黑体 SC Bold、思源宋体 CN Bold／Heavy。**思源黑体 Bold 仍用于发布版说明页、部分 HUD 和补充字幕，不是全部已经被替换的旧方案。** 原版日期、Logo、地图及部分日英共用图片按实际字节核对后记为沿用，不给它们虚构一个新字体。

上述新排字包含五作共 10 张开场说明贴图、两种内容，使用 Noto Sans SC、CSS 字重 600。保留配方的字体版本为 2.04，不代表保存了历史浏览器的完整加载日志。浏览器实际选字与后备字体的处理方法见[排字技术说明](typography.md)。

PF／PM 当前 **BETA 0.1.2** 的嵌入清单包含 **2,861 个 PNG 文件**。相同字节共用内容记录：PF 为 1,214 个文件／741 种内容，PM 为 1,647 个文件／985 种内容，两作合计 1,562 种不同内容。路径、字体、配方身份和字层继承见 [Photon 发布图片用字表](photon-released-image-fonts.json)。

其中 1,392 种内容涉及字体排字，另 170 种为原版字形沿用或已有记录的生成字样；一张图可以混有多个字体或生成字层。**旧的 1,490 图归档和早期“未安装”标记不代表当前包。** 例如小赖倒计时后来已发布，PF EX 标题的旧文楷／得意黑方案则已被生成字样替换。

两份逐图表共覆盖 **3,720 个发布图片文件**，范围是补丁清单列出的独立图片，不包含补丁未携带的原游戏资源。一张图可以同时使用多个字体、继承字层或生成字样；四张嵌入场景图和一张日历缩略图涉及颜色转换，按各自图像身份记录，不将转换后的图片写成字节完全相同。

部分 Windows 与思源旧配方缺当时字体文件摘要，已知字体名称／字重，但不能据此确认精确历史二进制版本；PM 一张“仅有声音”教程保留了 Noto Sans 计时字层，旧排版尚未完整复现验证。具体资源 ID 和文件名见[版本与资料限制](font-evidence.md)。当前 18 种微软雅黑常规体内容对应已知输入或其继承母版，不属于字体身份不明。

<details>
<summary><strong>English · Which font went into which image?</strong></summary>

The release registers cover 859 AGE2 WebP/AVIF files and 2,861 PNG files in PF/PM BETA 0.1.2. Photon duplicates share 1,562 content records, including 1,392 with font-rendered lettering and 170 with original or generated lettering. The tables preserve mixed fonts, inherited layers, versions and adoption status. Historical font binaries and one old timer layout retain material-specific [limitations](font-evidence.md). Local candidates and superseded trials are separate. See the [credits](attribution.md), [typography methods](typography.md) and [registration rules](registration.md).

</details>

## 已确认的制作输入

| 游戏／素材 | 使用的字体或方式 | 对应与范围 |
| --- | --- | --- |
| TDA00–03、帝都的菜单 UI | Noto Sans SC 可变字体 | UI 制作／精修脚本按 450 字重渲染；不等于游戏正文白无常 |
| 五作 telop、语音标签、地图标注 | NotoSansSC-500.ttf | 使用静态 500；与运行时 Hud 文件相同 |
| 五作日期／地点卡、TDA 剧情卡 | SweiSugarCJKsc-Medium.ttf | 狮尾加糖宋体 Medium；按原图排列与实际尺寸制作 |
| TDA02 人物介绍、TDA03 轨道港／高度介绍四张卡 | SourceHanSerifCN-Bold／Heavy.otf | 80px 姓名用 Bold，小号单位说明及港口／高度用 Heavy；检查的保留字库为 2.003，缺旧字体摘要的历史版本另见证据状态；不是全套卡都用狮尾 |
| 五作说明页、部分 HUD／补充字幕；帝都早期 telop／地点方案 | SourceHanSansSC-Bold.otf | 发布版仍有实际使用；帝都 telop／地点卡的后续批次另改为 Noto／Swei，按素材区分 |
| PF／PM 菜单、按钮、人物卡、说明等 | Noto Sans SC 可变字体 | 初期代表组与后续重排均有记录；具体字重随已确认组配置，不固定全作 700 |
| PF／PM 黑色章节标题、信用／书信、部分场景文字 | Noto Serif SC 可变字体 | 按组记录粗细、字距与效果；不会影响 GDI 正文 |
| PF 28 种烘焙字幕内容 | 制作当时的 PhotonR2 | 旧输入摘要 `aadf8950…ad4830b`；不同于后来扩字的运行时文件 |
| PF／PM 早期 56 张 CRmt 设计稿、PM 地图 v1 | PhotonCN-Regular.ttf | 旧批量排字、修订及 U0483 后续修图输入；与当前采用分别登记 |
| PF／PM 轨道擦除字幕 | Noto Sans SC 可变字体 | 90 条制作记录对应 44 种不同发布内容；有单独的字幕制作器，不能全部归给 PhotonR2 |
| PF EX 标题、PM《樱花盛开之前》标题／手写指示旧稿 | LXGWWenKaiGB-Medium.ttf | 霞鹜文楷 GB 1.522；历史配方对应此版本，部分素材后来更换字体 |
| PF EX 标题旧稿 | SmileySans-Oblique.ttf | 得意黑 2.0.1；历史试样，与当前定稿分开 |
| PF／PM 毛笔剧情卡、PM 手写指示、PF 证书颁发式 G1972／G2787 | MaShanZheng-Regular.ttf | 马善政 2.003；当前包采用，G2787 继承大图字层，不只是 10 月候选 |
| PM 剩余时间 G1294–G1304、教程内嵌 G2990–G2999 | Xiaolai-Regular.ttf | 小赖 3.126；11 个计时状态与 10 张教程图已进入当前包，保留原数字与秒字 |
| PF／PM 装备标题及两张搬用装备字层的选择 HUD | Microsoft YaHei 常规 | 18 种当前内容；两张 CRip008 HUD 同样继承微软雅黑字层 |
| PF／PM 八种中文语言按钮 | Microsoft YaHei Bold | 实际使用 `msyhbd.ttc`；与下方帝都在制备选分开 |
| PF／PM 舰艇字幕、剧情卡及学校黑色横幅 | KaiTi / simkai.ttf | 当前采用；PM G1401 继承 PF G1149 字幕。学校金字后来改成生成字样，但 G1961／G2803 黑色横幅仍有楷体 |
| PF／PM 时间／剧情卡、PM 研修日期后缀 | SimSun / simsun.ttc；MS Mincho / msmincho.ttc | 当前采用的 Windows 字体；原日文保留层与新排字分别记录 |
| PM 日历缩略图 G1049 的提供字幕 | NotoSansSC-Bold-700.ttf | 从 Noto Sans SC 可变字体导出静态 700，17px／8 倍渲染；字层来源不因手工合成而消失 |
| PF 蛋糕 G1952 | MaShanZheng-Regular.ttf | 本地 recipe-v1 候选，未发布、未做实机确认 |
| PM 基地地图 G4267／G4268 | NotoSerifSC-VF.ttf | 制作清单选中 v3，字重 500、16px；PhotonCN v1 已被替换 |
| PF 报纸 G2594、PF／PM 书店素材 | Noto Serif SC ＋ Noto Sans SC | 同图混用：报纸宋体 800／黑体 900，书店按文字段选择；不能只登记其中一种 |
| 五作共用 ORDER UI、帝都片尾岗位／场景等补漏图 | NotoSerifSC-VF.ttf | 原人物署名保留，岗位另译；片尾岗位配方记载 600／38px |
| 帝都便笺 2315、商店包装 1932 | KaiTi / simkai.ttf | 楷体，Windows 字体；便笺为静态审核候选，包装为局部累计稿，不冒充发布定稿 |
| 帝都制作备注 2011 备选、商店包装 1932 局部 | Microsoft YaHei / msyh.ttc、msyhbd.ttc | 微软雅黑常规／粗体；制作备注未批准，包装粗体用于两个小标签，整图仍待完成 |
| TDA01 明太子纸箱的中文括注 | SweiSugarCJKsc-SemiBold.ttf | 本地在制 SemiBold；与发布日期／地点卡的 Medium 分别登记 |
| TDA03 折叠便笺 1629 | MEBheiheiti.ttf | 本地在制美呗嘿嘿体；输入摘要 `7f59303f…62174b`，不同于发布包已补字的同名运行时文件 |
| 当前 PF EX 标题、樱花标题、部分学校金字和场景牌匾 | 生成字样／原字形沿用 | 采用提供的字层或生成母版；六张标题合成图没有在合成时另排字体 |

可变字体输入为 Noto Sans SC 2.04、Noto Serif SC 2.02，精确文件身份见[目录](catalog.json)。字号、轴值、描边和间距随对应素材组配方维护，不能将同一家族名当成全作统一排版参数。

## 倒计时试样与装备旧稿

PM“剩余时间”教程制作时使用过下列字体试样；当前发布版最终采用小赖。保留历史用字便于维护来源和样式，不表示继续采用这些备选。

| 字体输入 | 历史图片与用途 | 当前采用情况 |
| --- | --- | --- |
| 资源圆体 CN Medium 0.990 | `A-resource-han-rounded-medium.png`，22px | 历史试样 |
| 寒蝉圆黑 Medium 3.700 | `B-chill-round-gothic-medium.png`，22px | 历史试样；不是寒蝉全圆体 |
| 源泉圆体丹 GenSenRounded2 TC H 2.100 | `B-gensen-rounded-heavy.png`，22px | 历史试样 |
| 霞鹜 975 圆体 SC 700W 26.207 | `C-lxgw-975-yuan-700.png`，22px | 历史试样 |
| 猫啃网糖圆体 20210702 | `A-maoken-tangyuan.png`，22px | 历史试样；文件名与 SFNT 版本字符串均保留 |
| 有梦体 Yomeng Script 0.9.1 | `C-yomeng-script.png`，22px，半像素填充描边 | 历史试样 |

另有站酷快乐体 24px 与小赖 22px 试样。逐张输出、字体摘要和排版参数见[历史用字表](historical-image-fonts.json)。

装备标题的 33 张早期候选使用 `msyhl.ttc` **微软雅黑 Light**，随后更换为常规体。旧输出与清单已被覆盖，现存常规体成品和保留参考字体不能代替旧稿的精确文件身份；Light 用途仍登记为历史输入。

PF `G2685`“制作／著作”的历史候选使用 **SimHei 黑体 5.05** 将“製”重排为“制”，其余原字和 âge 标志沿用原图。该候选未列入当前发布清单，属于素材修改用途，不是只作字体比较。

## 早期批次与字体替换

PM 早期右键菜单的 54 张按钮先用**微软雅黑粗体**，后改为常规体，并调整阴影与抗锯齿。[历史表](historical-image-fonts.json)按资源、成品和字体记录 209 项不同版本；脚本中的备用字体不因此算作实际用字。

TDA00 早期的 **7 张姓名贴图和 9 张 OP 字幕**使用思源黑体 SC Bold。姓名贴图改过全名、简称及对齐方案，OP 字幕改过颜色与布局；制作器沿用同一个字体，并覆盖相同输出路径，所以只给现存输出记录摘要，不冒充每一轮旧图的字节证据。部分中文姓名图仍沿用 `_ja.webp` 文件名，不能按后缀把它们误判成未修改的日文原图。

PF／PM 早期 CRmt 有 **56 张 PhotonCN 排字设计稿**：39 张低风险组、17 张单独设计组。U0006、U0479 的配方身份及 U0329、U0483／U0484／U0486 的修订关系见 [CRmt 历史用字表](historical-crmt-image-fonts.json)。这些是两作共用的历史 U 编号，不换算成未经确认的游戏资源偏移。

**U0483 的 PhotonCN 中文稿还用于后续局部修图**。生成编辑要求保留中文内容与位置、修复文字底板，因此保留该字体的底稿来源。生成后的笔画可能变化，不能据此将每一笔都归为原字体；旧设计稿也不自动算入当前发布成品。

PM 早期设置页“画面模式”和右键“保存”按钮使用过 **BIZ UDGothic Regular／Bold、BIZ UDPGothic Regular／Bold、Noto Sans JP、等线粗体**，见[历史用字表](historical-git-image-fonts.json)。BIZ 的 `R.ttc`／`B.ttc` 分别使用索引 0（等宽）和 1（比例宽度），同一个 TTC 文件名不能代替具体字体身份。

这部分包含 279 项制作输出记录、194 种保留的 PNG 内容，以及未保存成品的排版试算。历史表分别记录已有成品、仅存制作记录和继承字层，不能将重复版本数加进发布数量。阴影或颜色不同的图片也不等于完整像素相同。

旧配方的 BIZ“开源候选”标记已纠正：实际读取的是 Microsoft 随 Windows 提供的 TTC，保留文件的许可声明也如此；不是另行发行的 Google Fonts／Morisawa OFL 字库。Noto Sans JP 则按实际 Noto 输入登记。字体身份、历史摘要及作者见[版本目录](catalog.json)，许可区别见[致谢](attribution.md)。

[历史素材版本表](historical-image-variants.json)收录 **1,933 项游戏／成品内容**，包括旧稿和返修；其中 1,871 项有保留输出，62 项仅存制作记录。557 项内容与当前发布表重叠，不能全部算成新增图片。各行保留素材标识、成品摘要、字体与来源指针。

PF 学校金字 `G1891` 的后续版本已把楷体字层换成生成字样；旧楷体试稿和仍沿用楷体的黑色布幅分别保留。复制旧配方后要同步实际字层的字体字段，避免将历史输入误写成当前用途，方法见[字层继承](typography.md)。

## 本地在制与局部稿

[在制图片用字表](unreleased-image-fonts.json)另列 **365 项本地候选**：AGE2 24 个系列的 328 张图片及 Photon 37 张修改图。本地选择、维护者确认、实机验证和发布采用是不同状态，分别记录。

AGE2 候选中有 311 张使用 Noto Sans SC 静态 500、7 张 Noto Sans SC 可变字体、6 张 Noto Serif SC、各 1 张狮尾 SemiBold、美呗嘿嘿体、楷体，以及 1 张生成字样。另有 21 张原图按决定保留、21 张资源待完成；帝都商店局部稿和制作备注备选等已见用字仍列在上表和用途汇总中，不把它们当作整图完稿。

Photon 已批准的本地范围为 37 张修改与 1 张核对后沿用的 G2506。蛋糕 G1952 及其 G2463／G2792 差分继承马善政字层；书店／报纸混用 Noto Sans／Serif；其他食品、说明纸、拟声字和地图按各自制作器登记。手绘矢量、生成墨迹、原字形局部修正分别记录；范围外素材和地图旧 PhotonCN v1 也保留其待处理／被替换状态。这轮没有替换当前公开补丁。

PF／PM 的旧字体比较记录还出现 **SimHei 5.05**、**MS Gothic 5.32**。SimHei 后来确实用于前述 PF 单字修订；MS Gothic 只有比较证据，没有确认游戏素材用途。**ZCOOL KuaiLe 2.001** 则确认用于 PM 倒计时教程的 24px 试样，最终改用小赖。SimHei、MS Gothic 属 Windows 字体；ZCOOL 为 OFL 字体，来源见[上游](https://github.com/googlefonts/zcool-kuaile)。

对照表、审核页标题用过 Arial、Consolas、Segoe UI、微软雅黑；AGE2 正文字体比较还试过多种霞鹜、狮尾、寒蝉及日文字体。它们不是因此就成了游戏图片字体。原图保留、原字形搬用、模型绘制字样也分别记录方法，不另造字体身份。原版商业字体及运行时方案见[运行时表](runtime.md)。

[用途汇总](image-font-usage.json)和[逐图表索引](image-font-index.json)关联素材、字体和采用范围。部分制作配方仅保留在维护者本地，公开的身份与用途摘要不等于完整可重建工程，缺失范围见[资料限制](font-evidence.md)。

源身份、实际用途与必要配方公开维护；私人对话、逐次核查日志、原游戏图和字体二进制不作为文档附件上传。

## 剧情视频中的烘焙文字

PM《再诞》开头／结尾旁白、两版《时空的欠片》回顾标题和 PF《告白》倒计时，
共五条 CRsi 候选均实际使用 Noto Sans SC 2.04 可变字体。
字体文件 SHA-256 为 `763146584cf0710223441356b4395e279021b0806c196614377a7a0174ae074a`，
直接使用原可变字体排字，未补字、子集化或混用后备字体。

| 素材组 | 实际排字 | 配方与当前成果 |
| --- | --- | --- |
| 再诞双段旁白 | `wght=400`、22px、1.1px 黑描边，8 倍采样 | [共用配方](../../rUGP/games/photonmelodies/video-localization/rebirth-ending-style.json)的 `narration`；[制作说明](../../rUGP/games/photonmelodies/video-localization/README.md) |
| 两版回顾标题 | `wght=600`、30px、2.5px 字距，4 倍采样；分别跟随源动画的位置、缩放和光晕 | [标题制作说明](../../rUGP/docs/story-video-labels.md) |
| 告白倒计时标签 | `wght=900`；校正面板平面上栏80px、下栏190px，4 倍采样后反投影 | 同上，保留源数字带和镜头裁切 |

按素材组登记在[使用表](image-font-usage.json)的 `video_material_groups`，不将每帧
累加到本页的独立图片数量。上述五条资源尚未包含在玩家包中；解码、画面审阅和
实机状态以各自制作说明为准。技术标签全图文试样不是再诞当前生产选择。

## 新批次怎么选

1. 对照原图的笔势、粗细、宽高、层级和用途，而不是仅凭“宋体／黑体”名字。
2. 从已确认素材组复用字体与样式；新风格先做代表图，交维护者确认再批量。
3. 字体文件、版本、字重轴、字号、间距、基线、颜色与特效进入组配方；按[登记规范](registration.md)同步来源、许可和素材对应。适合生成／绘制的字样记录制作方式，成品文案与笔画仍逐字检查。
4. 给每项成品保留其实际采用的配方。找不到旧配方时标注未核实，不因为外观看起来接近就追认某个字体。
5. 对原尺寸、整图和局部放大分别检查；同字族覆盖检查不能证明透视、遮挡、光照和笔画正确。

君望在制 UI 的样式包括朱雀仿宋菜单方案，以及按独立 Logo、手写和场景文字选择绘制／生成方式；另按[君望项目](../../AGE2/games/kiminozo/images/README.md)维护。
