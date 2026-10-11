# 哪些已经确定，哪些仍缺旧版本证据

[七作总表](audit.md) · [完整发布逐图表：AGE2](age2-released-image-fonts.json)／[PF・PM](photon-released-image-fonts.json) · [补查验证记录](font-verification.json)

**字体名称／字重是否确定，与当时字体文件的精确版本是否有证据，是两件事。** 下面逐项列明已关闭的问题及仍缺历史文件证据的素材；不能把今天检查到的版本当成旧稿当时版本。

本次补查后，已登记汉化排字素材没有仅凭 CSS 后备列表或外观猜测而留下的未识别字体。未另行排字的官方原字形、手绘／生成字样按制作方式记录，不虚构字体名。完整图片清单仍以各逐图表为准，本页列的是证据精度差异。

## 开场说明：实际字体已经确认

TDA00、TDA01、TDA02、TDA03、帝都燃烧各有以下两个文件，共 10 个文件、两种内容：

- `root/assets/data/gui/textures/boot/00_note000_zh.webp`
- `root/assets/data/gui/textures/boot/00_v_note000_zh.webp`

保留的 HTML、Noto Sans SC 2.04 输入及原打包操作在 Chrome 中重放后，10 个文件的全部 RGB 像素均与发布图一致。匹配渲染实际使用 Noto Sans SC，CSS 字重为 600；故意令字体加载失败时回退到微软雅黑，与发布页有 231,159 个像素不同。**这处已经从“模板指定 Noto”补到实际字形确认，不再是字体身份缺口。** 版本 2.04 是匹配重放使用的保留输入版本，不冒充找回了当年浏览器的字体文件日志。

## 当前发布图：字体确定，旧文件身份未完全证实

下表保留具体素材标识。PF／PM 的同字节副本共用一条内容记录，资源 ID 与实际打包文件名一起列出；混用两款字体的同一张图会在两款字体下分别出现。

### PF／PM

| 字体 | 具体图片／资源 | 发布包 PNG 文件名 |
| --- | --- | --- |
| 楷体 KaiTi | `G3454` | `PM / 0000364418_893B93E51E156AED.png` |
| 楷体 KaiTi | `G4066` | `PM / 0000013936_6EB628F09B777B0F.png` |
| 楷体 KaiTi | `pf:rio000:0x1ad9066c`<br>`pm:rio000:0x65d847dc` | `PF / 0000026702_B308B8FEF0F42048.png`<br>`PF / 0000053442_24DFFF492D0A77F9.png`<br>`PM / 0000026702_B308B8FEF0F42048.png`<br>`PM / 0000053442_24DFFF492D0A77F9.png` |
| 楷体 KaiTi | `G3002` | `PM / 0000675758_B1FF83611990934A.png` |
| 楷体 KaiTi | `pf:rio000:0x1b1485dc`<br>`pm:rio000:0x6613c74c` | `PF / 0000019270_BAA2CF78596E7FCD.png`<br>`PF / 0000034784_0272ED1AE3C3C8AF.png`<br>`PM / 0000019270_BAA2CF78596E7FCD.png`<br>`PM / 0000034784_0272ED1AE3C3C8AF.png` |
| 楷体 KaiTi | `pf:rio000:0x1b14616c`<br>`pm:rio000:0x6613a2dc` | `PF / 0000009820_698A1909FC181C3F.png`<br>`PF / 0000009942_25E04E73329ECDA1.png`<br>`PM / 0000009820_698A1909FC181C3F.png`<br>`PM / 0000009942_25E04E73329ECDA1.png` |
| 楷体 KaiTi | `pf:rio000:0x1b1416e4`<br>`pm:rio000:0x66135854` | `PF / 0000009840_C3145D18AD8257E7.png`<br>`PF / 0000026568_9B4E2317EBB0D129.png`<br>`PM / 0000009840_C3145D18AD8257E7.png`<br>`PM / 0000026568_9B4E2317EBB0D129.png` |
| 楷体 KaiTi | `pf:rio000:0x1ada109c`<br>`pm:rio000:0x65d9520c` | `PF / 0000023552_D98ADB64636D98D3.png`<br>`PF / 0000034094_7331F57F7F0D67D1.png`<br>`PM / 0000023552_D98ADB64636D98D3.png`<br>`PM / 0000034094_7331F57F7F0D67D1.png` |
| 楷体 KaiTi | `pf:rio000:0x1b13d94c`<br>`pm:rio000:0x66131abc` | `PF / 0000008876_49B696954DCF7718.png`<br>`PF / 0000020116_72EE0AC42B589D07.png`<br>`PM / 0000008876_49B696954DCF7718.png`<br>`PM / 0000020116_72EE0AC42B589D07.png` |
| 楷体 KaiTi | `pf:rio000:0x1ad9a148`<br>`pm:rio000:0x65d8e2b8` | `PF / 0000020028_5D470FB3CA470087.png`<br>`PF / 0000037994_8ADA778D878496A8.png`<br>`PM / 0000020028_5D470FB3CA470087.png`<br>`PM / 0000037994_8ADA778D878496A8.png` |
| 宋体 SimSun | `pm:rio000:0x66411b4c` | `PM / 0000004248_EC577E00F70C5616.png`<br>`PM / 0000012774_CF9ACBE8D3DC8ED4.png` |
| 宋体 SimSun | `pm:rio000:0x66401de8` | `PM / 0000004656_9A957A5E061285D8.png`<br>`PM / 0000011716_D277F6873D7008B7.png` |
| 宋体 SimSun | `pf:rio000:0x1ad9066c`<br>`pm:rio000:0x65d847dc` | `PF / 0000026702_B308B8FEF0F42048.png`<br>`PF / 0000053442_24DFFF492D0A77F9.png`<br>`PM / 0000026702_B308B8FEF0F42048.png`<br>`PM / 0000053442_24DFFF492D0A77F9.png` |
| 宋体 SimSun | `pm:rio000:0x66413e90` | `PM / 0000007448_C41E39062DF4ABCC.png`<br>`PM / 0000011172_D138A695F21F11FE.png` |
| 宋体 SimSun | `pf:rio000:0x1ad9a148`<br>`pm:rio000:0x65d8e2b8` | `PF / 0000020028_5D470FB3CA470087.png`<br>`PF / 0000037994_8ADA778D878496A8.png`<br>`PM / 0000020028_5D470FB3CA470087.png`<br>`PM / 0000037994_8ADA778D878496A8.png` |
| MS Mincho | `pm:rio000:0x66405bec` | `PM / 0000003736_11FBA7FC4FF0788A.png`<br>`PM / 0000013880_5512F3F029F4F734.png` |
| MS Mincho | `pm:rio000:0x6640ae5c` | `PM / 0000003550_3262D4CD8E672DF9.png`<br>`PM / 0000013360_DED966C5F051B3F5.png` |
| MS Mincho | `pm:rio000:0x6640c99c` | `PM / 0000003458_49C85FD9FD2DE070.png`<br>`PM / 0000013054_A831FD797F916F27.png` |
| MS Mincho | `pm:rio000:0x664077f0` | `PM / 0000003468_0FC29A70760036E9.png`<br>`PM / 0000013066_2CAF7AFA0023618B.png` |
| MS Mincho | `pm:rio000:0x664092a4` | `PM / 0000003702_0CA517047261B807.png`<br>`PM / 0000013674_B8745B5DB5CB95F6.png` |
| MS Mincho | `pm:rio000:0x6640404c` | `PM / 0000003702_BBE3D9528C5C7679.png`<br>`PM / 0000013674_F59FB6AF2354414A.png` |
| MS Mincho | `pm:rio000:0x6640e43c` | `PM / 0000003636_AA0A3E2490FCF352.png`<br>`PM / 0000013688_FF36734988553601.png` |
| MS Mincho | `pm:rio000:0x6640ffc4` | `PM / 0000003584_57F597247BBC737B.png`<br>`PM / 0000013430_89B07EB3DA3249E4.png` |
| 微软雅黑 Bold | `G3800` | `PM / 0000057670_D6E6432AECB95882.png` |
| 微软雅黑 Bold | `G3799` | `PM / 0000068118_C89B87CEB230FC72.png` |
| 微软雅黑 Bold | `G2561` | `PF / 0000057686_74F454CE1391EE10.png` |
| 微软雅黑 Bold | `G3803` | `PM / 0000098838_1480A854E174B031.png` |
| 微软雅黑 Bold | `G3804` | `PM / 0000078942_EF483CBBF8EAC053.png` |
| 微软雅黑 Bold | `G2564` | `PF / 0000100136_44850EF199CD2558.png` |
| 微软雅黑 Bold | `G2565` | `PF / 0000078396_39E281B934D1660E.png` |
| 微软雅黑 Bold | `G2560` | `PF / 0000062644_27807F2EA0A2FB05.png` |

这些分别是楷体 **10 种**内容、宋体 **5 种**、MS Mincho **8 种**、微软雅黑粗体 **8 种**。合计 31 项字体／内容关系，涉及 **29 种不同图片内容**，不是 31 张互不重复的图片。字体由实际制作记录、代码或字层继承确认；缺的是当时字体文件的摘要等身份记录。宋体、MS Mincho 与当前微软雅黑制作器均使用 Pillow 的默认 TTC 索引 0，不能再笼统说这些字体的索引也都不知道。

**已排除在缺口外的素材：**18 种当前微软雅黑常规体内容已有旧文件摘要或可验证的母版继承；其中选择 HUD 的 G2600／G2606／G4327／G4332 共两种内容，继承相同装备字形蒙版。楷体的 PF G1961、G2803、G1149，PM G1401、G4375、G4376 共六种内容，也有旧摘要或已确认母版关系。详见逐图表与补查记录。

### TDA／帝都的思源字体

思源黑体 SC Bold 涉及 40 个发布文件；思源宋体 CN Bold／Heavy 涉及另外四张不同的介绍图，其中“大上律子”同图混用两种字重。共 **44 个游戏／文件路径**。字体和字重已由实际制作器及对应成品确认；目录中的黑体 2.001、宋体 2.003 是检查的保留文件版本，没有旧文件摘要的条目不能据此声称历史二进制完全相同。

| 游戏 | 发布资源路径 | 确定的字体 |
| --- | --- | --- |
| 帝都燃烧 | `root/assets/data/gui/textures/manual/12_bg000_pc_zh.webp` | 思源黑体 SC Bold |
| 帝都燃烧 | `root/assets/data/gui/textures/manual/12_bg000_sp_zh.webp` | 思源黑体 SC Bold |
| 帝都燃烧 | `root/assets/data_spec/gui/textures/manual/12_bg000_pc_zh.webp` | 思源黑体 SC Bold |
| 帝都燃烧 | `root/assets/data_spec/gui/textures/manual/12_bg000_sp_zh.webp` | 思源黑体 SC Bold |
| TDA00 | `root/assets/data/gui/textures/manual/12_bg000_pc_zh.webp` | 思源黑体 SC Bold |
| TDA00 | `root/assets/data/gui/textures/manual/12_bg000_sp_zh.webp` | 思源黑体 SC Bold |
| TDA00 | `root/assets/data_spec/adv/game/chr/920オブジェクト/テロップ類大縦半分_/テロップ類大縦半分_転送完了_ck.webp` | 思源黑体 SC Bold |
| TDA01 | `root/assets/data/gui/textures/manual/12_bg000_pc_zh.webp` | 思源黑体 SC Bold |
| TDA01 | `root/assets/data/gui/textures/manual/12_bg000_sp_zh.webp` | 思源黑体 SC Bold |
| TDA01 | `root/assets/data_spec/adv/game/chr/01TDA_600_戦術機オブジェクト/02HUD情報_/HUD_対電磁パルス防御_対電磁パルス防御_ck.webp` | 思源黑体 SC Bold |
| TDA01 | `root/assets/data_spec/adv/game/chr/01TDA_600_戦術機オブジェクト/02HUD情報_/HUD_情報01TDA第６次シアトル_DRAKE03 強制介入_ck.webp` | 思源黑体 SC Bold |
| TDA01 | `root/assets/data_spec/adv/game/chr/01TDA_600_戦術機オブジェクト/02HUD情報_/HUD_情報01TDA第６次シアトル_再起動待機中_ck.webp` | 思源黑体 SC Bold |
| TDA01 | `root/assets/data_spec/adv/game/chr/01TDA_600_戦術機オブジェクト/02HUD情報_/HUD_情報01TDA第６次シアトル_再起動開始_ck.webp` | 思源黑体 SC Bold |
| TDA01 | `root/assets/data_spec/adv/game/chr/01TDA_600_戦術機オブジェクト/02HUD情報_/HUD_情報01TDA第６次シアトル_待機中_ck.webp` | 思源黑体 SC Bold |
| TDA01 | `root/assets/data_spec/adv/game/chr/01TDA_600_戦術機オブジェクト/02HUD情報_/HUD_情報01TDA第６次シアトル_注意：停滞緩解剤注射_ck.webp` | 思源黑体 SC Bold |
| TDA01 | `root/assets/data_spec/adv/game/chr/01TDA_710_オブジェクト/991_201008追加英文テロップ/TDA01_020_起_第６次シアトル防衛線01_1_ck.webp` | 思源黑体 SC Bold |
| TDA01 | `root/assets/data_spec/adv/game/chr/01TDA_710_オブジェクト/991_201008追加英文テロップ/TDA01_020_起_第６次シアトル防衛線01_2_ck.webp` | 思源黑体 SC Bold |
| TDA01 | `root/assets/data_spec/adv/game/chr/01TDA_710_オブジェクト/991_201008追加英文テロップ/TDA01_020_起_第６次シアトル防衛線01_3_ck.webp` | 思源黑体 SC Bold |
| TDA01 | `root/assets/data_spec/adv/game/chr/01TDA_710_オブジェクト/991_201008追加英文テロップ/TDA01_020_起_第６次シアトル防衛線01_4_ck.webp` | 思源黑体 SC Bold |
| TDA01 | `root/assets/data_spec/adv/game/chr/01TDA_710_オブジェクト/991_201008追加英文テロップ/TDA01_130_転_BETA大規模再襲撃03_1_ck.webp` | 思源黑体 SC Bold |
| TDA01 | `root/assets/data_spec/adv/game/chr/01TDA_710_オブジェクト/991_201008追加英文テロップ/TDA01_130_転_BETA大規模再襲撃03_2_ck.webp` | 思源黑体 SC Bold |
| TDA01 | `root/assets/data_spec/adv/game/chr/900_戦術機コクピットオブジェクト/0000高頻度使用オブジェクト/010テロップ類大縦半分_秘匿　夕呼_佐渡島最上_ck.webp` | 思源黑体 SC Bold |
| TDA01 | `root/assets/data_spec/adv/game/chr/900_戦術機コクピットオブジェクト/テロップ類大縦半分_/テロップ類大縦半分_着座情報転送中_ck.webp` | 思源黑体 SC Bold |
| TDA01 | `root/assets/data_spec/adv/game/chr/900_戦術機コクピットオブジェクト/テロップ類大縦半分_/テロップ類大縦半分_転送完了_ck.webp` | 思源黑体 SC Bold |
| TDA02 | `root/assets/data/gui/textures/manual/12_bg000_pc_zh.webp` | 思源黑体 SC Bold |
| TDA02 | `root/assets/data/gui/textures/manual/12_bg000_sp_zh.webp` | 思源黑体 SC Bold |
| TDA02 | `root/assets/data_spec/adv/game/chr/01TDA_600_戦術機オブジェクト/02HUD情報_/HUD_情報02TDA2話_味方機損傷_ck.webp` | 思源黑体 SC Bold |
| TDA02 | `root/assets/data_spec/adv/game/chr/01TDA_600_戦術機オブジェクト/02HUD情報_/HUD_情報02TDA2話_演習プログラム停止_ck.webp` | 思源黑体 SC Bold |
| TDA02 | `root/assets/data_spec/adv/game/chr/35演出用画像/020_デイアフター２話/律子登場テロップ_大上律子中尉_ck.webp` | 思源宋体 CN Bold、思源宋体 CN Heavy |
| TDA02 | `root/assets/data_spec/adv/game/chr/35演出用画像/020_デイアフター２話/律子登場テロップ_楠本さやか軍曹_ck.webp` | 思源宋体 CN Bold |
| TDA02 | `root/assets/data_spec/adv/game/chr/900_戦術機コクピットオブジェクト/0000高頻度使用オブジェクト/010テロップ類大縦半分_秘匿　夕呼_佐渡島最上_ck.webp` | 思源黑体 SC Bold |
| TDA02 | `root/assets/data_spec/adv/game/chr/900_戦術機コクピットオブジェクト/テロップ類大縦半分_/テロップ類大縦半分_着座情報転送中_ck.webp` | 思源黑体 SC Bold |
| TDA02 | `root/assets/data_spec/adv/game/chr/900_戦術機コクピットオブジェクト/テロップ類大縦半分_/テロップ類大縦半分_転送完了_ck.webp` | 思源黑体 SC Bold |
| TDA03 | `root/assets/data/gui/textures/manual/12_bg000_pc_zh.webp` | 思源黑体 SC Bold |
| TDA03 | `root/assets/data/gui/textures/manual/12_bg000_sp_zh.webp` | 思源黑体 SC Bold |
| TDA03 | `root/assets/data_spec/adv/game/chr/01TDA_710_オブジェクト/991_201008追加英文テロップ/TDA03C2_H0258_ck.webp` | 思源黑体 SC Bold |
| TDA03 | `root/assets/data_spec/adv/game/chr/01TDA_710_オブジェクト/991_201008追加英文テロップ/TDA03C_J0001_ck.webp` | 思源黑体 SC Bold |
| TDA03 | `root/assets/data_spec/adv/game/chr/01TDA_710_オブジェクト/991_201008追加英文テロップ/TDA03C_J0002_ck.webp` | 思源黑体 SC Bold |
| TDA03 | `root/assets/data_spec/adv/game/chr/01TDA_710_オブジェクト/991_201008追加英文テロップ/TDA03C_J0003_ck.webp` | 思源黑体 SC Bold |
| TDA03 | `root/assets/data_spec/adv/game/chr/01TDA_710_オブジェクト/991_201008追加英文テロップ/TDA03C_J0004_ck.webp` | 思源黑体 SC Bold |
| TDA03 | `root/assets/data_spec/adv/game/chr/01TDA_710_オブジェクト/991_201008追加英文テロップ/TDA03C_J0005_ck.webp` | 思源黑体 SC Bold |
| TDA03 | `root/assets/data_spec/adv/game/chr/01TDA_710_オブジェクト/991_201008追加英文テロップ/TDA03C_J0006_ck.webp` | 思源黑体 SC Bold |
| TDA03 | `root/assets/data_spec/adv/game/chr/01TDA_710_オブジェクト/TDA3話テロップ_/TDA3話テロップ_国連宇宙総軍宇宙港“ＯＳＰ－１４００”_ck.webp` | 思源宋体 CN Heavy |
| TDA03 | `root/assets/data_spec/adv/game/chr/01TDA_710_オブジェクト/TDA3話テロップ_/TDA3話テロップ_地球低軌道１４００Ｋｍ　 _ck.webp` | 思源宋体 CN Heavy |

## 旧稿与本地局部：字体名字确定，部分历史文件已覆盖

以下是旧稿或未发布素材，不能误说成玩家当前正在使用这些试样。具体成品摘要、字体字段和来源指针仍在相应历史表中。

| 素材 | 确定的用字 | 仍缺什么 |
| --- | --- | --- |
| PF／PM 33 张早期装备候选 | 微软雅黑 Light，`msyhl.ttc`，Pillow 默认索引 0 | 后来换成常规体并覆盖输出／清单；未保存旧字体摘要 |
| PM 早期右键菜单 54 个按钮／状态，209 项不同版本 | 首轮微软雅黑 Bold，后续 Regular | 旧报告保存了实际文件名和成品记录，缺当时字体文件摘要 |
| TDA00 最早 7 张姓名图、9 张 OP 字幕 | 思源黑体 SC Bold | 多轮同路径覆盖，未保留每轮字体文件摘要和旧成品 |
| PM “画面模式”绿色／红色字体试样，共 14 个输出 | 等线 DengXian Bold，`Dengb.ttf`，索引 0 | 成品仍在 Git 中，旧字体摘要未保存 |
| PM 同两种设置标题的 6 张微软雅黑试样 | 微软雅黑 Regular | 成品仍在 Git 中，旧字体摘要未保存 |
| 帝都便笺 2315，`letter-astra-v1/cn.png` | 楷体 KaiTi | 具体字体已确认，未在该旧记录中保存字体摘要 |
| 帝都包装 1932 的局部累计稿、制作备注 2011 的备选 | 包装用楷体及微软雅黑 Bold；备注备选用微软雅黑 Regular／Bold | 字体用途已追到配方；是局部／备选状态，不能当作发布完稿 |

<details>
<summary><strong>展开具体旧稿标识</strong></summary>

**微软雅黑 Light 装备稿（33 个组）：**

`G2278`、`G2280`、`G2288`、`G2596`、`G2597`、`G2598`、`G2599`、`G2600`、`G2602`、`G2603`、`G2604`、`G2605`、`G2606`、`G2651`、`G2652`、`G2751`、`G2752`、`G4294`、`G4295`、`G4296`、`G4297`、`G4298`、`G4299`、`G4324`、`G4325`、`G4326`、`G4327`、`G4328`、`G4329`、`G4330`、`G4331`、`G4366`、`G4367`

**PM 早期菜单（54 个资源）：**

- `pm:rio002:0x487932c0`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x4879f0fc`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x487aa7f4`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x487b61e4`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x487c143c`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x487ca6b0`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x487d37b0`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x487dba64`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x487e38dc`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x487ee400`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x487f8a3c`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x48804988`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x488101d0`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x48816298`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x48821e18`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x48827b14`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x488334e0`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x488393b4`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x48844d80`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x4884a770`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x48855c6c`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x48860d04`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x4886baac`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x48876dd0`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x48881670`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x4888a864`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x48893424`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x4889afd0`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x488a2b94`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x488aa8a0`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x488b2714`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x488b8ad4`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x488bf760`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x488c53b0`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x488cb7c8`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x488d2738`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x488d9f58`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x488e2aa8`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x488eaaec`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x488f2614`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x488fa570`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x48901af0`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x48909614`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x489113ac`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x48915300`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x4891c460`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x48923a94`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x4892b0f8`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x4892ec6c`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x48936280`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x4893a308`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x48941aac`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x4894526c`：微软雅黑 Bold／微软雅黑 Regular
- `pm:rio002:0x4894b818`：微软雅黑 Bold／微软雅黑 Regular

**TDA00 姓名图与 OP（16 个输出）：**

- `tda00_name_ui_work/out/11_name00_ja.webp`
- `tda00_name_ui_work/out/11_name01_ja.webp`
- `tda00_name_ui_work/out/11_name02_ja.webp`
- `tda00_name_ui_work/out/11_name03_ja.webp`
- `tda00_name_ui_work/out/11_name04_ja.webp`
- `tda00_name_ui_work/out/11_name05_ja.webp`
- `tda00_name_ui_work/out/11_name_non_ja.webp`
- `tda00_op_work/op01_cn.webp`
- `tda00_op_work/op02_cn.webp`
- `tda00_op_work/op03_cn.webp`
- `tda00_op_work/op04_cn.webp`
- `tda00_op_work/op05_cn.webp`
- `tda00_op_work/op06_cn.webp`
- `tda00_op_work/op07_cn.webp`
- `tda00_op_work/op08_cn.webp`
- `tda00_op_work/op09_cn.webp`

**PM 设置标题的等线／微软雅黑输出：**

- `pm:rio002:0x4785acb0`：`artifacts/photon_resource_inventory/replacement_drafts/pm_options_text_style_search_20260703/rank_02_green_DengXianBold.png`，等线 DengXian Bold
- `pm:rio002:0x4785c2c8`：`artifacts/photon_resource_inventory/replacement_drafts/pm_options_text_style_search_20260703/rank_02_red_DengXianBold.png`，等线 DengXian Bold
- `pm:rio002:0x4785acb0`：`artifacts/photon_resource_inventory/replacement_drafts/pm_options_text_style_search_20260703/rank_03_green_DengXianBold.png`，等线 DengXian Bold
- `pm:rio002:0x4785c2c8`：`artifacts/photon_resource_inventory/replacement_drafts/pm_options_text_style_search_20260703/rank_03_red_DengXianBold.png`，等线 DengXian Bold
- `pm:rio002:0x4785acb0`：`artifacts/photon_resource_inventory/replacement_drafts/pm_options_text_style_search_20260703/rank_05_green_DengXianBold.png`，等线 DengXian Bold
- `pm:rio002:0x4785c2c8`：`artifacts/photon_resource_inventory/replacement_drafts/pm_options_text_style_search_20260703/rank_05_red_DengXianBold.png`，等线 DengXian Bold
- `pm:rio002:0x4785acb0`：`artifacts/photon_resource_inventory/replacement_drafts/pm_options_text_style_search_20260703/rank_07_green_DengXianBold.png`，等线 DengXian Bold
- `pm:rio002:0x4785c2c8`：`artifacts/photon_resource_inventory/replacement_drafts/pm_options_text_style_search_20260703/rank_07_red_DengXianBold.png`，等线 DengXian Bold
- `pm:rio002:0x4785acb0`：`artifacts/photon_resource_inventory/replacement_drafts/pm_options_text_style_search_20260703/rank_08_green_DengXianBold.png`，等线 DengXian Bold
- `pm:rio002:0x4785c2c8`：`artifacts/photon_resource_inventory/replacement_drafts/pm_options_text_style_search_20260703/rank_08_red_DengXianBold.png`，等线 DengXian Bold
- `pm:rio002:0x4785acb0`：`artifacts/photon_resource_inventory/replacement_drafts/pm_options_text_style_search_20260703/rank_10_green_DengXianBold.png`，等线 DengXian Bold
- `pm:rio002:0x4785c2c8`：`artifacts/photon_resource_inventory/replacement_drafts/pm_options_text_style_search_20260703/rank_10_red_DengXianBold.png`，等线 DengXian Bold
- `pm:rio002:0x4785acb0`：`artifacts/photon_resource_inventory/replacement_drafts/pm_options_text_style_search_20260703/rank_11_green_DengXianBold.png`，等线 DengXian Bold
- `pm:rio002:0x4785c2c8`：`artifacts/photon_resource_inventory/replacement_drafts/pm_options_text_style_search_20260703/rank_11_red_DengXianBold.png`，等线 DengXian Bold
- `pm:rio002:0x4785acb0`：`artifacts/photon_resource_inventory/replacement_drafts/pm_options_text_style_search_20260703/rank_12_green_MicrosoftYaHei.png`，微软雅黑 Regular
- `pm:rio002:0x4785c2c8`：`artifacts/photon_resource_inventory/replacement_drafts/pm_options_text_style_search_20260703/rank_12_red_MicrosoftYaHei.png`，微软雅黑 Regular
- `pm:rio002:0x4785acb0`：`artifacts/photon_resource_inventory/replacement_drafts/pm_options_text_style_search_20260703/rank_13_green_MicrosoftYaHei.png`，微软雅黑 Regular
- `pm:rio002:0x4785c2c8`：`artifacts/photon_resource_inventory/replacement_drafts/pm_options_text_style_search_20260703/rank_13_red_MicrosoftYaHei.png`，微软雅黑 Regular
- `pm:rio002:0x4785acb0`：`artifacts/photon_resource_inventory/replacement_drafts/pm_options_text_style_search_20260703/rank_16_green_MicrosoftYaHei.png`，微软雅黑 Regular
- `pm:rio002:0x4785c2c8`：`artifacts/photon_resource_inventory/replacement_drafts/pm_options_text_style_search_20260703/rank_16_red_MicrosoftYaHei.png`，微软雅黑 Regular

</details>

[逐图历史版本表](historical-image-variants.json)还保留上述字体的其他返修／沿用记录。部分历史字体摘要缺失不等于字体名称没找到；有些行与当前发布表或专项旧稿重复，不能相加当作额外图片数量。

## 字体已经确定，但有其他验证限制

| 具体图片／素材 | 已确定的字体 | 实际限制 |
| --- | --- | --- |
| PM “仅有声音”教程，`pm:rio000:0x6544f288`；发布文件 `PhotonR2Assets/v6/payload/PM/pm_rio000_6544f288.png` | Noto Sans SC；补充标签与继承的早期计时字层同属该字体，计时配方保留旧字体摘要 | 未逐像素重放旧计时布局；这是布局重放范围，不是字体身份不明 |
| TDA03 折叠便笺 1629，`folded-note-v8/cn.png` | 美呗嘿嘿体 3.000，旧输入摘要与保留文件一致 | 作者网页本次无法读取；影响重新核验授权原文，不影响字体身份 |
| 历史表中 62 项没有现存成品的制作记录 | 各行已有实际字体字段 | 只能核对旧制作记录，不能对已丢失图片进行像素重放 |

<details>
<summary><strong>English · Font identity is separate from historical byte identity</strong></summary>

The retained boot HTML and Noto Sans SC input reproduce every RGB pixel of all ten released textures; the Microsoft YaHei fallback control differs. The four selection-HUD group aliases inherit two contents from a font-hashed equipment glyph mask. Remaining filename-only historical records identify the font face but do not establish the exact historical font binary. The tables above enumerate those release materials and historical batches. The sound-only tutorial limitation concerns old-layout replay; the MEB note limitation concerns renewed reading of its author-license page. Neither is an unidentified font. Original glyphs and generated or painted lettering receive their actual methods rather than guessed font names.

</details>
