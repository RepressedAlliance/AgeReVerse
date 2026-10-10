# 图片用字与制作样式

[字体入口](README.md) · [图片流程](../Images-MakeItLookNative/README.md) · [来源与声明](attribution.md) · [使用记录](image-font-usage.json) · [版本目录](catalog.json)

图片字体按素材组维护。同一级文字统一字重、字号、字距、基线和特效，再分别适配透视、距离与光照；不能按每个词的墨迹外接框重新缩放。运行时正文用字与图片用字没有自动绑定关系。

**2026-10-11 已回查七作保留的主要制作目录、脚本、配方、审核与版本记录。** 下面按实际用途补齐字体，而不是只列运行时字体或已下载的文件。使用记录分为制作、历史候选、部分完成、已替换等状态；本次没有重新逐张认证所有发布包，不能把本地完成写成玩家版已采用。缺失的旧版本与发布绑定明确列在[记录缺口](image-font-usage.json)中；绘制、生成或复用原字形不靠外观猜字体名。

<details>
<summary><strong>English · Which font went into which image?</strong></summary>

The usage registry links seven-game material groups to exact font identities and retained production evidence. It distinguishes authored candidates, static review, partial work, superseded recipes and release adoption. Newly recovered inputs include LXGW WenKai GB, Smiley Sans, Xiaolai, earlier Ma Shan Zheng lettering, Source Han Serif and Windows fonts. A typesetting input is not proof that a current release uses that image. See [credits and licensing](attribution.md) and [registration rules](registration.md) for reuse.

</details>

## 已确认的制作输入

| 游戏／素材 | 使用的字体或方式 | 对应与范围 |
| --- | --- | --- |
| TDA00–03、帝都的菜单 UI | Noto Sans SC 可变字体 | UI 制作／精修脚本按 450 字重渲染；不等于游戏正文白无常 |
| 五作 telop、语音标签、地图标注 | NotoSansSC-500.ttf | 使用静态 500；与运行时 Hud 文件相同 |
| 五作日期／地点卡、TDA 剧情卡 | SweiSugarCJKsc-Medium.ttf | 狮尾加糖宋体 Medium；按原图排列与实际尺寸制作 |
| TDA02 人物介绍、TDA03 轨道港／高度介绍四张卡 | SourceHanSerifCN-Bold／Heavy.otf | 思源宋体 CN 2.003；80px 姓名用 Bold，小号单位说明及港口／高度用 Heavy；不是全套卡都用狮尾 |
| 帝都早期 telop／地点方案 | SourceHanSansSC-Bold.otf | 历史方案；后续对应批次改为 Noto／Swei，不能当当前统一字体 |
| PF／PM 菜单、按钮、人物卡、说明等 | Noto Sans SC 可变字体 | 初期代表组与后续重排均有记录；具体字重随已确认组配置，不固定全作 700 |
| PF／PM 黑色章节标题、信用／书信、部分场景文字 | Noto Serif SC 可变字体 | 按组记录粗细、字距与效果；不会影响 GDI 正文 |
| PF／PM 烘焙字幕 | 制作当时的 PhotonR2 | 旧输入摘要 `aadf8950…ad4830b`；不同于后来扩字的运行时文件 |
| PF EX 标题、PM《樱花盛开之前》标题／手写指示旧稿 | LXGWWenKaiGB-Medium.ttf | 霞鹜文楷 GB 1.522；保留副本的摘要与旧配方、回放证据一致；部分后来改用其他字体 |
| PF EX 标题旧制作／精确回放 | SmileySans-Oblique.ttf | 得意黑 2.0.1；原存档字体摘要与回放记录一致，不把每个历史候选都写成当前定稿 |
| PF／PM 毛笔标题、PM 手写指示、PF 证书颁发式 G1972 | MaShanZheng-Regular.ttf | 马善政 2.003；早期已用于制作，不只是 10 月新下载的候选 |
| PM 剩余时间 G1294–G1304、教程内嵌 G2990–G2999 | Xiaolai-Regular.ttf | 小赖 3.126；11 个倒计时状态与 10 张教程图共用字形，保留数字与秒字；审核记录明确未安装 |
| PF 蛋糕 G1952 | MaShanZheng-Regular.ttf | 10 月 recipe-v1 最后记录为本地静态验收通过，未做实机确认 |
| PM 基地地图 G4267／G4268 | NotoSerifSC-VF.ttf | 制作清单选中 v3，字重 500、16px；PhotonCN v1 已被替换 |
| PF 报纸 G2594、PF／PM 书店素材 | Noto Serif SC ＋ Noto Sans SC | 同图混用：报纸宋体 800／黑体 900，书店按文字段选择；不能只登记其中一种 |
| 五作共用 ORDER UI、帝都片尾岗位／场景等补漏图 | NotoSerifSC-VF.ttf | 原人物署名保留，岗位另译；片尾岗位配方记载 600／38px |
| 帝都便笺 2315、商店包装 1932；Photon 故事卡旧稿 | KaiTi / simkai.ttf | 楷体，Windows 字体；便笺为静态审核候选，包装为局部累计稿，不冒充发布定稿 |
| Photon 故事／时间卡旧稿、PM 研修日期旧稿 | SimSun / simsun.ttc；MS Mincho / msmincho.ttc | 宋体／MS 明朝，Windows 字体；实际排字记录与当前发布状态分开 |
| 帝都制作备注 2011 备选、商店包装 1932 局部 | Microsoft YaHei / msyh.ttc、msyhbd.ttc | 微软雅黑常规／粗体；制作备注未批准，包装粗体用于两个小标签，整图仍待完成 |
| 手写、特殊 Logo、复杂场景拟写 | 绘制／区域图像编辑 | 没有真实字体文件时记录方法与已确认成品，不虚构字体名 |

可变字体实际输入是 Noto Sans SC 2.04、Noto Serif SC 2.02；文件摘要已核对制作记录与本机输入，见目录。每个组的具体渲染参数仍跟随对应游戏素材；字体来源确定不等于该组所有成品已重新视觉验收。

PF／PM 旧制作中还找到 **SimHei 5.05**、**MS Gothic 5.32** 人物／署名字体比较和 **ZCOOL KuaiLe 2.001** 标题试样。它们单独登记为比较／试样，不能由“试过”推定最终采用。SimHei、MS Gothic 属 Windows 字体；ZCOOL 为 OFL 字体，来源见[上游](https://github.com/googlefonts/zcool-kuaile)。

对照表、审核页标题用过 Arial、Consolas、Segoe UI、微软雅黑；AGE2 正文字体比较还试过多种霞鹜、狮尾、寒蝉及日文字体。它们不是因此就成了游戏图片字体。原图保留、原字形搬用、模型绘制字样也分别记录方法，不另造字体身份。原版商业字体及运行时方案见[运行时表](runtime.md)。

本次从八组保留目录检查 35,034 个脚本／文本记录文件，再交叉核对具体配方、字体元数据与采用记录。统计包含历史重复文件，不是成品张数；原始游戏图、依赖、HTML 预览与超大文本未用于字体名检索。公开的 [22 组使用记录及 46 项证据身份](image-font-usage.json)保留可追溯的文件名与摘要，不上传本地绝对路径、完整审核门户或字体二进制。旧记录未保存字体摘要／TTC 字体索引时，当前文件元数据不能反证历史版本。

## 新批次怎么选

1. 对照原图的笔势、粗细、宽高、层级和用途，而不是仅凭“宋体／黑体”名字。
2. 从已确认素材组复用字体与样式；新风格先做代表图，交维护者确认再批量。
3. 字体文件、版本、字重轴、字号、间距、基线、颜色与特效进入组配方；按[登记规范](registration.md)同步来源、许可和素材对应。适合生成／绘制的字样记录制作方式，成品文案与笔画仍逐字检查。
4. 给每项成品保留其实际采用的配方。找不到旧配方时标注未核实，不因为外观看起来接近就追认某个字体。
5. 对原尺寸、整图和局部放大分别检查；同字族覆盖检查不能证明透视、遮挡、光照和笔画正确。

君望对话形成的新工作方法包括朱雀仿宋菜单方案，以及按独立 Logo、手写和场景文字选择绘制／生成方式。这属于在制作品的已选样式，另按[君望项目](../../AGE2/games/kiminozo/images/README.md)维护，不写成上述七作已经采用的字体。
