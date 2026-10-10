# 图片用字与制作样式

[字体入口](README.md) · [图片流程](../Images-MakeItLookNative/README.md) · [来源与声明](attribution.md) · [用途汇总](image-font-usage.json) · [版本目录](catalog.json)

图片字体按素材组维护。同一级文字统一字重、字号、字距、基线和特效，再分别适配透视、距离与光照；不能按每个词的墨迹外接框重新缩放。运行时正文用字与图片用字没有自动绑定关系。

**完整清查仍在进行。** 当前发布包、10 月已选候选与历史制作分别追查；当前表已有对应不代表该图的旧稿、局部字层和生成参考也已查清。[历史图片用字记录](historical-image-fonts.json)随核对结果补充。

制作过、已采用和已发布分别记录；绘制、生成或复用原字形不靠外观猜字体名。下面从当前发布包反查实际字层，再列本地在制和历史试样。

## 当前发布包：已查到哪一步

五作 AGE2 当前发布清单中的 **859 个独立 WebP／AVIF 文件**已逐个核对本地打包副本与公开 SHA-256，并对应制作输出或原版来源。每个文件的路径、摘要、字体和来源记录见 [AGE2 发布图片用字表](age2-released-image-fonts.json)。这是来源核对，不是重新进行全图视觉审核或实机验收。

| 作品 | 核对的公开版本 | 图片文件 | 新排字／HTML 排字 | 原版图片原样沿用 |
| --- | --- | ---: | ---: | ---: |
| TDA00 | BETA 0.2.1 | 71 | 54 | 17 |
| TDA01 | BETA 0.3.3 | 118 | 93 | 25 |
| TDA02 | BETA 0.2.1 | 115 | 94 | 21 |
| TDA03 | BETA 0.2.7 | 153 | 110 | 43 |
| 帝都燃烧 | BETA 0.2.1 | 402 | 292 | 110 |

新排字素材确认用到 Noto Sans SC 可变字体、Noto Sans SC 静态 500、狮尾加糖宋体 Medium、思源黑体 SC Bold、思源宋体 CN Bold／Heavy。**思源黑体 Bold 仍用于发布版说明页、部分 HUD 和补充字幕，不是全部已经被替换的旧方案。** 原版日期、Logo、地图及部分日英共用图片按实际字节核对后记为沿用，不给它们虚构一个新字体。

上述新排字数包括五作共 10 张开场说明贴图。其字体依据打包说明与 HTML 模板声明为 Noto Sans SC；未重放历史 Chrome 的字体加载／回退过程，这 10 张与有相同字节制作输出的其他图片分别标注。

PF／PM 当前 **BETA 0.1.2** 的全部 **2,861 个 PNG 文件**已核对到公开 ZIP、安装器嵌入清单和制作来源。相同字节共用记录：PF 为 1,214 个文件／741 种内容，PM 为 1,647 个文件／985 种内容，两作合计 1,562 种不同内容。路径、字体、配方身份、字层继承和核对方法见 [Photon 发布图片用字表](photon-released-image-fonts.json)。

其中 1,392 种内容涉及字体排字，另 170 种为原版字形沿用或已有记录的生成字样；一张图可以混有多个字体或生成字层。**旧的 1,490 图归档和早期“未安装”标记不代表当前包。** 例如小赖倒计时后来已发布，PF EX 标题的旧文楷／得意黑方案则已被生成字样替换。

两份逐图表共覆盖 **3,720 个发布图片文件**，范围是上述清单列出的独立图片；不包含补丁没有携带的原游戏资源，也不宣称逐一枚举了所有原生资源记录。证据以制作文件摘要、相同字节／RGBA、明确继承关系为主；四张嵌入场景图及一张日历缩略图另外记录了实测的颜色转换差异，没有冒充字节一致。

仍有具体限制：Windows 旧配方未保存摘要或 TTC 索引的，不能确认当时字体的精确二进制版本；一张“仅有声音”教程沿用早期 Noto Sans 计时字层，其制作命令和字体配置已找到，但旧排版没有逐像素重放。前述 10 张 AGE2 HTML 说明图也保留声明与加载验证的区别。

<details>
<summary><strong>English · Which font went into which image?</strong></summary>

The release registers cover 859 standalone AGE2 WebP/AVIF files and all 2,861 PNG files in the embedded PF/PM BETA 0.1.2 manifests. Photon duplicates share 1,562 image records, including 1,392 contents with font-rendered lettering and 170 with original or generated lettering. Bindings record exact hashes, RGBA identity, inherited layers or measured colour conversions. This establishes provenance within that file scope, not a new runtime/visual approval or a complete historical rendering replay. Windows historical bytes, ten HTML font-loading cases and one old timer layout retain explicit limitations. Local candidates and superseded trials are separate. See [credits](attribution.md) and [registration rules](registration.md).

</details>

## 已确认的制作输入

| 游戏／素材 | 使用的字体或方式 | 对应与范围 |
| --- | --- | --- |
| TDA00–03、帝都的菜单 UI | Noto Sans SC 可变字体 | UI 制作／精修脚本按 450 字重渲染；不等于游戏正文白无常 |
| 五作 telop、语音标签、地图标注 | NotoSansSC-500.ttf | 使用静态 500；与运行时 Hud 文件相同 |
| 五作日期／地点卡、TDA 剧情卡 | SweiSugarCJKsc-Medium.ttf | 狮尾加糖宋体 Medium；按原图排列与实际尺寸制作 |
| TDA02 人物介绍、TDA03 轨道港／高度介绍四张卡 | SourceHanSerifCN-Bold／Heavy.otf | 思源宋体 CN 2.003；80px 姓名用 Bold，小号单位说明及港口／高度用 Heavy；不是全套卡都用狮尾 |
| 五作说明页、部分 HUD／补充字幕；帝都早期 telop／地点方案 | SourceHanSansSC-Bold.otf | 发布版仍有实际使用；帝都 telop／地点卡的后续批次另改为 Noto／Swei，按素材区分 |
| PF／PM 菜单、按钮、人物卡、说明等 | Noto Sans SC 可变字体 | 初期代表组与后续重排均有记录；具体字重随已确认组配置，不固定全作 700 |
| PF／PM 黑色章节标题、信用／书信、部分场景文字 | Noto Serif SC 可变字体 | 按组记录粗细、字距与效果；不会影响 GDI 正文 |
| PF 28 种烘焙字幕内容 | 制作当时的 PhotonR2 | 旧输入摘要 `aadf8950…ad4830b`；不同于后来扩字的运行时文件 |
| PF／PM 轨道擦除字幕 | Noto Sans SC 可变字体 | 90 条制作记录对应 44 种不同发布内容；有单独的字幕制作器，不能全部归给 PhotonR2 |
| PF EX 标题、PM《樱花盛开之前》标题／手写指示旧稿 | LXGWWenKaiGB-Medium.ttf | 霞鹜文楷 GB 1.522；保留副本的摘要与旧配方、回放证据一致；部分后来改用其他字体 |
| PF EX 标题旧制作／精确回放 | SmileySans-Oblique.ttf | 得意黑 2.0.1；原存档字体摘要与回放记录一致，不把每个历史候选都写成当前定稿 |
| PF／PM 毛笔剧情卡、PM 手写指示、PF 证书颁发式 G1972／G2787 | MaShanZheng-Regular.ttf | 马善政 2.003；当前包采用，G2787 继承大图字层，不只是 10 月候选 |
| PM 剩余时间 G1294–G1304、教程内嵌 G2990–G2999 | Xiaolai-Regular.ttf | 小赖 3.126；11 个计时状态与 10 张教程图已进入当前包，保留原数字与秒字 |
| PF／PM 装备标题及两张搬用装备字层的选择 HUD | Microsoft YaHei 常规 | 18 种当前内容；两张 CRip008 HUD 同样继承微软雅黑字层 |
| PF／PM 八种中文语言按钮 | Microsoft YaHei Bold | 实际使用 `msyhbd.ttc`；与下方帝都在制备选分开 |
| PF／PM 舰艇字幕、剧情卡及学校黑色横幅 | KaiTi / simkai.ttf | 当前采用；PM G1401 继承 PF G1149 字幕。学校金字后来改成生成字样，但 G1961／G2803 黑色横幅仍有楷体 |
| PF／PM 时间／剧情卡、PM 研修日期后缀 | SimSun / simsun.ttc；MS Mincho / msmincho.ttc | 当前采用的 Windows 字体；原日文保留层与新排字分别记录 |
| PM 日历缩略图 G1049 的提供字幕 | NotoSansSC-Bold-700.ttf | 从 Noto Sans SC 可变字体导出静态 700，17px／8 倍渲染；字层来源不因手工合成而消失 |
| PF 蛋糕 G1952 | MaShanZheng-Regular.ttf | 10 月 recipe-v1 最后记录为本地静态验收通过，未做实机确认 |
| PM 基地地图 G4267／G4268 | NotoSerifSC-VF.ttf | 制作清单选中 v3，字重 500、16px；PhotonCN v1 已被替换 |
| PF 报纸 G2594、PF／PM 书店素材 | Noto Serif SC ＋ Noto Sans SC | 同图混用：报纸宋体 800／黑体 900，书店按文字段选择；不能只登记其中一种 |
| 五作共用 ORDER UI、帝都片尾岗位／场景等补漏图 | NotoSerifSC-VF.ttf | 原人物署名保留，岗位另译；片尾岗位配方记载 600／38px |
| 帝都便笺 2315、商店包装 1932 | KaiTi / simkai.ttf | 楷体，Windows 字体；便笺为静态审核候选，包装为局部累计稿，不冒充发布定稿 |
| 帝都制作备注 2011 备选、商店包装 1932 局部 | Microsoft YaHei / msyh.ttc、msyhbd.ttc | 微软雅黑常规／粗体；制作备注未批准，包装粗体用于两个小标签，整图仍待完成 |
| TDA01 明太子纸箱的中文括注 | SweiSugarCJKsc-SemiBold.ttf | 本地在制 SemiBold；与发布日期／地点卡的 Medium 分别登记 |
| TDA03 折叠便笺 1629 | MEBheiheiti.ttf | 本地在制美呗嘿嘿体；输入摘要 `7f59303f…62174b`，不同于发布包已补字的同名运行时文件 |
| 当前 PF EX 标题、樱花标题、部分学校金字和场景牌匾 | 生成字样／原字形沿用 | 追到选中的字层或生成母版；六张提供的标题合成图与发布图 RGBA 相同，没有在合成时另排字体 |

可变字体实际输入是 Noto Sans SC 2.04、Noto Serif SC 2.02；文件摘要已核对制作记录与本机输入，见目录。每个组的具体渲染参数仍跟随对应游戏素材；字体来源确定不等于该组所有成品已重新视觉验收。

## 追回的倒计时试样与装备旧稿

PM 的“剩余时间”教程还保留着八张字体试样。用保留的字体文件和制作器重放后，八张都与旧图的 RGBA 像素完全一致；因此下面六项确实用于图片试作，并非只下载过字体。

| 字体输入 | 历史图片与用途 | 当前采用情况 |
| --- | --- | --- |
| 资源圆体 CN Medium 0.990 | `A-resource-han-rounded-medium.png`，22px | 历史试样 |
| 寒蝉圆黑 Medium 3.700 | `B-chill-round-gothic-medium.png`，22px | 历史试样；不是寒蝉全圆体 |
| 源泉圆体丹 GenSenRounded2 TC H 2.100 | `B-gensen-rounded-heavy.png`，22px | 历史试样 |
| 霞鹜 975 圆体 SC 700W 26.207 | `C-lxgw-975-yuan-700.png`，22px | 历史试样 |
| 猫啃网糖圆体 20210702 | `A-maoken-tangyuan.png`，22px | 历史试样；文件名与 SFNT 版本字符串均保留 |
| 有梦体 Yomeng Script 0.9.1 | `C-yomeng-script.png`，22px，半像素填充描边 | 历史试样 |

另外两张是站酷快乐体 24px 与小赖 22px；**当前发布的倒计时最终用小赖**，不能把这些备选统称为发布字体。逐张输出与字体摘要、排版参数和重放结果见[历史记录](historical-image-fonts.json)。

装备标题还有一轮使用 `msyhl.ttc` 的 **微软雅黑 Light** 旧稿：五套共用字样生成了 33 张候选，随后改用常规微软雅黑。制作对话保存了语法修复后成功生成 33 张、再更换字体的顺序；旧输出及清单被覆盖，不能拿今天的字体摘要或常规版成品代替旧稿的字节证据。这项也单独登记，不遗漏实际用过的 Light，也不把它说成当前包采用。

## 本地在制与局部稿

[在制图片用字表](unreleased-image-fonts.json)另列 10 月两轮制作的 **365 项**：AGE2 24 个系列的 328 张已登记静态候选，以及 Photon 37 张修改图。当前文件摘要对应现存候选与其记录；没有把本地看图、维护者最终确认和实机验证混成同一种通过状态。

AGE2 候选中有 311 张使用 Noto Sans SC 静态 500、7 张 Noto Sans SC 可变字体、6 张 Noto Serif SC、各 1 张狮尾 SemiBold、美呗嘿嘿体、楷体，以及 1 张生成字样。另有 21 张原图按决定保留、21 张资源待完成；帝都商店局部稿和制作备注备选等已见用字仍列在上表和用途汇总中，不把它们当作整图完稿。

Photon 已批准的本地范围为 37 张修改与 1 张核对后沿用的 G2506。蛋糕 G1952 及其 G2463／G2792 差分继承马善政字层；书店／报纸混用 Noto Sans／Serif；其他食品、说明纸、拟声字和地图按各自制作器登记。手绘矢量、生成墨迹、原字形局部修正分别记录；范围外素材和地图旧 PhotonCN v1 也保留其待处理／被替换状态。这轮没有替换当前公开补丁。

PF／PM 旧制作中还找到 **SimHei 5.05**、**MS Gothic 5.32** 人物／署名字体比较和 **ZCOOL KuaiLe 2.001** 标题试样。它们单独登记为比较／试样，不能由“试过”推定最终采用。SimHei、MS Gothic 属 Windows 字体；ZCOOL 为 OFL 字体，来源见[上游](https://github.com/googlefonts/zcool-kuaile)。

对照表、审核页标题用过 Arial、Consolas、Segoe UI、微软雅黑；AGE2 正文字体比较还试过多种霞鹜、狮尾、寒蝉及日文字体。它们不是因此就成了游戏图片字体。原图保留、原字形搬用、模型绘制字样也分别记录方法，不另造字体身份。原版商业字体及运行时方案见[运行时表](runtime.md)。

先前 35,034 个脚本／文本记录的检索只用于发现线索，历史重复文件不算成品数量。这次另外从发布图片逐项追到制作输出、配置、原版来源及后续返修；[用途汇总](image-font-usage.json)与两份逐图表保留文件名、摘要和实际采用关系。完整审核门户、私人对话、原游戏图与字体二进制不上传。维护者保留的源记录只有身份和用途摘要公开，读者不能把这些摘要当成已获得完整制作工程。

## 新批次怎么选

1. 对照原图的笔势、粗细、宽高、层级和用途，而不是仅凭“宋体／黑体”名字。
2. 从已确认素材组复用字体与样式；新风格先做代表图，交维护者确认再批量。
3. 字体文件、版本、字重轴、字号、间距、基线、颜色与特效进入组配方；按[登记规范](registration.md)同步来源、许可和素材对应。适合生成／绘制的字样记录制作方式，成品文案与笔画仍逐字检查。
4. 给每项成品保留其实际采用的配方。找不到旧配方时标注未核实，不因为外观看起来接近就追认某个字体。
5. 对原尺寸、整图和局部放大分别检查；同字族覆盖检查不能证明透视、遮挡、光照和笔画正确。

君望对话形成的新工作方法包括朱雀仿宋菜单方案，以及按独立 Logo、手写和场景文字选择绘制／生成方式。这属于在制作品的已选样式，另按[君望项目](../../AGE2/games/kiminozo/images/README.md)维护，不写成上述七作已经采用的字体。
