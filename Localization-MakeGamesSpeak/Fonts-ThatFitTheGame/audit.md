# 七作图片用字：从成品查回每一套字体

**Image Font Audit — Follow the Lettering Back to Its Source**

[字体入口](README.md) · [素材与样式](images.md) · [作者与许可](attribution.md) · [精确文件身份](catalog.json) · [核查范围与对应索引](audit-scope.json)

本次把 **PM、PF、帝都燃烧、TDA00–03** 可访问的图片制作资料重新查了一遍：当前发布图、早期批次、旧稿、返修、局部字层、提供的字幕图，以及供图像模型编辑的排字底稿都包括在内。共登记 **37 项字体输入／字重／版本，其中 36 项有实际素材排字或底稿用途，1 项仅有字体比较用途**。这不是 37 个字体家族，也不是当前补丁附带 37 套字体。

下面先查作品，再查字体。具体资源 ID、输出摘要、配方来源和替换关系保存在逐图表中。原图沿用、手绘和生成字样按实际方式记录；没有排字字体时，不凭外观猜一个名称。

## 从作品查

| 作品 | 当前发布图片里的排字输入 | 另外追回的用字与用途 |
| --- | --- | --- |
| TDA00 | Noto Sans SC 可变／静态 500、狮尾加糖宋体 Medium、思源黑体 SC Bold | 最早 7 张姓名图与 9 张 OP 字幕的思源黑体；本地 ORDER UI 的 Noto Serif SC |
| TDA01 | Noto Sans SC 可变／静态 500、狮尾加糖宋体 Medium、思源黑体 SC Bold | 明太子纸箱括注的狮尾加糖宋体 SemiBold |
| TDA02 | Noto Sans SC 可变／静态 500、狮尾加糖宋体 Medium、思源黑体 SC Bold、思源宋体 CN Bold／Heavy | 按介绍卡实际字层区分宋体字重，不把它们全部归给狮尾 |
| TDA03 | Noto Sans SC 可变／静态 500、狮尾加糖宋体 Medium、思源黑体 SC Bold、思源宋体 CN Heavy | 折叠便笺的美呗嘿嘿体原始输入，区别于补字后的运行时字体 |
| 帝都燃烧 | Noto Sans SC 可变／静态 500、狮尾加糖宋体 Medium、思源黑体 SC Bold | 本地 Noto Serif SC、便笺／包装的楷体、制作备注备选及包装小标签的微软雅黑常规／粗体 |
| PF | Noto Sans SC、Noto Serif SC、旧 PhotonR2、马善政、楷体、宋体、微软雅黑常规／粗体 | 早期 PhotonCN CRmt 稿；旧 EX 标题的霞鹜文楷 GB／得意黑；SimHei 单字修订；学校金字的旧楷体与后续生成字样分开 |
| PM | Noto Sans SC、Noto Serif SC、Noto Sans SC 静态 700、小赖、马善政、楷体、宋体、MS Mincho、微软雅黑常规／粗体 | 早期 PhotonCN CRmt／地图稿、霞鹜文楷 GB、微软雅黑 Light 装备稿；BIZ 四种字体、Noto Sans JP、等线粗体设置页稿；倒计时八种试样 |

这里的“当前发布”以核查的版本为准：TDA00 0.2.1、TDA01 0.3.3、TDA02 0.2.1、TDA03 0.2.7、帝都 0.2.1，以及 PF／PM 0.1.2，均为 BETA。字体名出现于某作的旧稿，不表示该作当前成品继续使用它。

## 从字体查

同一个家族的不同文件、字重和 TTC 索引分别登记。下表括号内数量是本目录的具体输入项数；作者、上游和许可原文入口见[致谢](attribution.md)，版本与摘要见[目录](catalog.json)。

| 字体输入 | 实际用途 | 状态／许可类别 |
| --- | --- | --- |
| Noto Sans SC：可变、静态 500、静态 700（3） | 七作 UI／说明／卡片；AGE2 telop、标签和地图；PM G1049 提供的缩略图字幕 | 发布及在制；OFL |
| Noto Serif SC 可变（1） | PF／PM 章节、信用、书信、报纸等；AGE2 本地 UI 与片尾岗位 | 发布及在制；OFL |
| 狮尾加糖宋体 Medium、SemiBold（2） | 五作日期／地点卡；TDA01 纸箱中文括注 | Medium 发布、SemiBold 在制；OFL |
| 思源黑体 SC Bold（1） | AGE2 说明、HUD、补充字幕；TDA00 早期姓名／OP；帝都早期方案 | 发布及历史；OFL |
| 思源宋体 CN Bold、Heavy（2） | TDA02 人物介绍、TDA03 轨道港／高度介绍 | 发布；OFL |
| PhotonCN、旧 PhotonR2（2） | PhotonCN：56 张早期 CRmt 稿、U0483 修图底稿及 PM 地图 v1；旧 PhotonR2：PF 28 种字幕内容 | 历史／发布分别记录；思源黑体派生、OFL |
| 霞鹜文楷 GB Medium（1） | PF EX、PM 樱花标题与手写指示旧稿 | 已有后续替换；OFL |
| 得意黑 Oblique（1） | PF EX 标题旧稿 | 后来改用生成字样；OFL |
| 马善政（1） | PF／PM 毛笔卡、PM 手写指示、PF 证书颁发式和本地蛋糕字样 | 发布及在制；OFL |
| 小赖（1） | PM 11 个倒计时状态及 10 张内嵌教程图 | 已发布；OFL |
| 站酷快乐体（1） | PM 倒计时教程字体试样 | 试过，最终改用小赖；OFL |
| 资源圆体 CN Medium（1） | PM 倒计时试样 | 历史试样；OFL |
| 寒蝉圆黑 Medium（1） | PM 倒计时试样 | 历史试样；OFL |
| 源泉圆体丹 GenSenRounded2 TC Heavy（1） | PM 倒计时试样 | 历史试样；OFL |
| 霞鹜 975 圆体 SC 700W（1） | PM 倒计时试样 | 历史试样；OFL |
| 猫啃网糖圆体 20210702（1） | PM 倒计时试样 | 历史试样；OFL |
| 有梦体 Yomeng Script 0.9.1（1） | PM 倒计时试样 | 历史试样；OFL |
| 美呗嘿嘿体原始图片输入（1） | TDA03 折叠便笺 | 本地在制；作者使用声明，不是 OFL |
| 楷体 KaiTi（1） | PF／PM 剧情／舰艇字幕、学校黑色布幅；帝都便笺与包装局部 | 发布及在制；Windows 字体 |
| 宋体 SimSun（1） | PF／PM 时间／剧情卡 | 已发布；Windows 字体 |
| MS Mincho（1） | PM 研修日期后缀 | 已发布；Windows 字体 |
| 微软雅黑 Regular、Bold、Light（3） | 装备、HUD、语言按钮、PM 早期菜单；帝都局部与备选；Light 为后来更换的装备稿 | 当前、历史与备选分开；Windows 字体 |
| 黑体 SimHei（1） | PF G2685“制作／著作”候选中单独重排“制” | 历史候选；Windows 字体 |
| BIZ UDGothic／UDPGothic Regular、Bold（4） | PM 设置页与“保存”按钮各轮试稿，按 TTC 索引区分等宽／比例宽度 | 历史；实际输入为 Windows 文件，不能套用另一套 OFL 发行的许可 |
| Noto Sans JP 可变（1） | PM 早期“画面模式”试稿 | 历史；OFL |
| 等线 DengXian Bold（1） | PM 早期设置页试稿 | 历史；Windows 字体 |

以上为 **36 项有素材用途的输入**。另登记的 **MS Gothic（1）仅有署名字体比较证据**，没有把它算作游戏图片实际用字。Arial、Consolas、Segoe UI 等审核页／对照表标签，以及纯正文比较用字同样不因此进入游戏图片的用字名单。

## 查到具体图片和旧版本

| 记录 | 能查什么 |
| --- | --- |
| [AGE2 发布图](age2-released-image-fonts.json) | 五作 859 个独立图片文件、字体、原图沿用及来源 |
| [PF／PM 发布图](photon-released-image-fonts.json) | 2,861 个 PNG 文件，对应 1,562 种不同内容；字层继承和混用 |
| [本地已选候选](unreleased-image-fonts.json) | 365 项本地候选；没有冒充已发布或已实机通过 |
| [历史专项](historical-image-fonts.json) | 计时试样、Light 装备稿、SimHei 单字、PM 早期菜单和 TDA00 姓名／OP |
| [逐图历史版本](historical-image-variants.json) | 1,933 项游戏／成品内容，含旧稿、返修、字体字段和源记录指针 |
| [Git 追回的早期制作](historical-git-image-fonts.json) | 已移出工作区的 PM 字体试稿；BIZ 索引、旧摘要及继承关系 |
| [早期 CRmt 排字](historical-crmt-image-fonts.json) | 56 张 PhotonCN 设计稿、修订与 U0483 后续生成输入 |

这些表彼此有重叠：历史版本中有 557 项内容同时存在于当前发布表，Git 记录和专项记录也可能重复。不能将各表行数相加，宣称制作过那么多不同图片。局部稿与尚未完成的资源另外保留状态，不因发现其字体就标成完稿。

## 证据与边界

核查从保存的工程、制作会话和 Git 历史找输入，再用逐图配方、成品摘要、字层继承与必要的重放确认用途。只安装过字体、脚本备用列表和“仿 Noto 风格”提示词都不能单独证明实际使用。生成前用过字体底稿的仍登记底稿；仅依据官方原图生成的，不倒推成字体排字。

仍如实保留几个精度限制：部分 Windows 旧稿没有保存当时的字体摘要／TTC 索引；10 张 AGE2 开场说明图依据制作记录与 Noto Sans 声明归档，未重放历史浏览器加载；一张 Photon 声音教程的旧计时布局没有逐像素重放。美呗作者页面本次无法读取，沿用已有来源声明，不声称重新完整核验授权。这些限制不以今天的字体或补做的图来填造证据。

本次结论适用于 **2026-10-11 已盘点到的可访问资料**。原图中未另行排字的官方字样不猜字体，已经丢失或未提供的私人资料也不声称能够重建。核查资料身份与表间对应见 [audit-scope.json](audit-scope.json)。以后每批新图、返修和换字体同步遵循[登记规范](registration.md)，把实际输入、采用版本和声明留下。

<details>
<summary><strong>English · What this audit establishes</strong></summary>

The audit reconciles the retained image-production records for PM, PF, Imperial Capital Burns and TDA00–03, including releases, superseded drafts, local partials, supplied text layers and font prototypes used for generation. There are 36 material typography/prototype inputs, plus one comparison-only MS Gothic entry; these are file/face/version records, not family counts or fonts shipped today. The registers distinguish actual release adoption, trials, inherited layers, original artwork and generated lettering. Historical byte identity, browser loading and unavailable author-page evidence remain explicit limitations. Read the [credits](attribution.md), [exact identities](catalog.json) and [registration rules](registration.md) before reusing an input.

</details>
