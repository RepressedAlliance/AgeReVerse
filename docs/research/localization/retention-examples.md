# 原文保留实例：翻译信息，尊重原作的表达

[翻译原则](../../../Localization-MakeGamesSpeak/principles.md) · [图片制作](../../../Localization-MakeGamesSpeak/Images-MakeItLookNative/README.md)

大部分日文需要译成中文。保留原文则是一项有明确范围的内容决定：它应符合素材用途，保留原作的表达，并让玩家读懂需要理解的信息。

## 片尾：署名与岗位分开处理

TDA00–03 与帝都燃烧的片尾保留真实人员、公司署名及歌曲原题，岗位、角色与军衔仍译成中文。例如《最後のエデン》《星海を往く希望の歌》保留原题；这不免除歌词或歌曲说明的翻译。真实工作人员姓名与虚构角色姓名适用不同规则。

片尾应按脚本实际调用的记录判断。未调用的旧歌曲记录不能直接计为玩家可见的漏译，文字已经准备好也不意味着滚动画面接入与排版已经完成。

## 同一类图片，也可能采用不同决定

| 素材 | 项目处理 | 适用范围 |
| --- | --- | --- |
| TDA 地图、道具与日期卡 | 按具体素材决定保留或译字 | 原图保留不免除地点、人物卡说明或剧情信息的翻译 |
| 帝都异常反复书写的信纸 | 保留原作表现 | 不编造一封通顺的中文信；其他需要阅读的信件另行处理 |
| PF 书店招牌／书脊 | 环境陈设可保留 | 一旦承担剧情阅读任务，应重新判断 |
| PM 壁纸、品牌字样和画内拟声 | 按已确认的原画范围保留 | 图库图注、菜单和操作说明单独翻译 |

AGE2 素材的具体决定可在各作 `images/copy/native-card-decisions.json` 与 `native-art-decisions.json` 查询；Photon 的图片分类见[CRmt 素材说明](../../../rUGP/evidence/photon/crmt/README.md)。内容保留、制作完成与补丁实际采用分别记录，不能互相代替。

## 日期后的七曜星期标记

君望、PF／PM 已确认的日期图沿用“月、火、水、木、金、土、日”等星期标记。项目采用这一呈现方式时参考了 Muv-Luv 本篇与 Alternative 官方中文的处理；不机械改成“星期一”等，也不改变数字、顺序或圈记。

保留范围是已确认的日期图及星期标记。相邻的事件说明、章节文字、地点和操作信息仍按内容判断；TDA 的年月日素材也不能直接代替其他作品的具体决定。

## 尚未确认的内容

PM 的 `pm:rio004:0x68966c24` 与 `pm:rio004:0x68967f2c` 两张片尾曲名存在项目中文候选，原记录仍待确认。项目候选不等于官方中文译名，也不能据此自动批准替换原题或回退现有素材。

原图保留也不说明每个补丁的语言槽与资源映射已经正确接入；实际采用情况应查看对应作品和发布版本。

## English

Retain original wording when it serves attribution, identifies a work or preserves an approved part of the artwork without hiding information players need. Translate role labels, gallery captions, instructions and required story text separately. Approved date cards in Kiminozo and PF/PM retain Japanese weekday notation. A retention decision is distinct from an unfinished translation or an asset already included in a release.
