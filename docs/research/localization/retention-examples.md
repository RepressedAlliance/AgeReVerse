# 原文保留实例：翻译信息，尊重原作的表达

[翻译原则](../../../Localization-MakeGamesSpeak/principles.md) · [图片制作](../../../Localization-MakeGamesSpeak/Images-MakeItLookNative/README.md)

应汉化的内容必须完整做到简体中文化，不能以“中文玩家能看懂”代替字形、术语和表达要求。下列实例区分[三种不改的情况](../../../Localization-MakeGamesSpeak/principles.md#如何判断是否需要翻译)：有意保留日文、原内容已经符合简体中文，以及有明确依据的特殊表达惯例。第 3 类属于有意保留，不能混同于普通中文已经合格。

## 片尾：署名与岗位分开处理

TDA00–03 与帝都燃烧的片尾保留真实人员、公司署名及歌曲原题，岗位、角色与军衔仍译成中文。例如《最後のエデン》《星海を往く希望の歌》保留原题；这不免除歌词或歌曲说明的翻译。真实工作人员姓名与虚构角色姓名适用不同规则。

片尾应按脚本实际调用的记录判断。未调用的旧歌曲记录不能直接计为玩家可见的漏译，文字已经准备好也不意味着滚动画面接入与排版已经完成。

## 同一类图片，也可能采用不同决定

| 素材 | 项目处理 | 适用范围 |
| --- | --- | --- |
| TDA 地图、道具与日期卡 | 按具体文字区分三类不改理由与正常翻译 | 地点、人物卡说明或剧情信息不能因汉字可读而免译；应译文字须使用正确简体字形与中文术语 |
| 帝都异常反复书写的信纸 | 保留原作表现 | 不编造一封通顺的中文信；其他需要阅读的信件另行处理 |
| PF 书店招牌／书脊 | 逐项确认具体的原文保留依据，或判断是否已经符合简体中文 | “环境陈设”本身不构成免译理由；旧决定仅凭分类、可读性或工具限制时须重新判断 |
| PM 壁纸、品牌字样和画内拟声 | 仅复用有明确内容依据的既有保留范围 | 保留原画美术不等于文字全部保留；图库图注、菜单和操作说明单独汉化 |

AGE2 素材的具体决定可在各作 `images/copy/native-card-decisions.json` 与 `native-art-decisions.json` 查询；Photon 的图片分类见[CRmt 素材说明](../../../rUGP/evidence/photon/crmt/README.md)。内容保留、制作完成与补丁实际采用分别记录，不能互相代替。

## 汉字可读，不等于已经汉化

原图的实际字形、含义、术语和表达都与目标简体中文一致时，可以直接复用；不能只凭文字编码相同或 OCR 结果判断字形。反之，繁体／日式字形和未汉化的日式称谓需要修正。例如手写人物名单中的 `軍曹`，只改成 `军曹` 仍不合格，按本项目[军衔术语](../../../Localization-MakeGamesSpeak/Glossaries-KeepItConsistent/decisions.md)应为 `中士`。修正文字时仍保留原有手写风格、纸张、构图和其他画面。

这与保留真实工作人员的原署名不同：有依据保留的原署名不擅自简化，普通中文中的角色称谓则应完整汉化。旧工具能力不足而留下的文字问题属于待修，不能拿历史妥协作为保留先例或汉化完成的证明；已发布也不代表问题已消失。

## 日期后的七曜星期标记

君望、PF／PM 已确认的日期图沿用“月、火、水、木、金、土、日”等星期标记。字形虽然与简体中文相同，星期表达仍有区别；项目参考 Muv-Luv 本篇与 Alternative 官方中文的处理，明确采用这项特殊惯例（第 3 类），并非因为“玩家能看懂”就当作第 2 类。不机械改成“星期一”等，也不改变数字、顺序或圈记。

保留范围是已确认的日期图及星期标记。相邻的事件说明、章节文字、地点和操作信息仍按内容判断；TDA 的年月日素材也不能直接代替其他作品的具体决定。

## 尚未确认的内容

PM 的 `pm:rio004:0x68966c24` 与 `pm:rio004:0x68967f2c` 两张片尾曲名存在项目中文候选，原记录仍待确认。项目候选不等于官方中文译名，也不能据此自动批准替换原题或回退现有素材。

原图保留也不说明每个补丁的语言槽与资源映射已经正确接入；实际采用情况应查看对应作品和发布版本。

## English

Content requiring localization must be fully Simplified Chinese in actual glyphs, meaning, terminology and expression. Distinguish intentional Japanese retention, content already meeting all those requirements, and an explicitly adopted special convention. Real staff credits and song original titles can have justified retention scopes; decoration or identity alone is not an exemption. Reassess historical decisions based only on readability, classification or tool limitations rather than declaring them complete.

Inspect the actual lettering even when character codes or OCR match. In a handwritten roster, `軍曹` merely simplified to `军曹` still needs localization: this project's rank terminology uses `中士`. Preserve handwriting and artwork while correcting the text; this differs from preserving an actual staff member's original credit. Old technical compromises remain repair work, including in already released images.

Approved Kiminozo and PF/PM date cards retain Japanese weekday notation following the official Chinese Muv-Luv/Alternative treatment. Their glyphs match Simplified Chinese but their expression differs, so this is the special-convention case, a form of intentional retention rather than ordinary compliant Chinese. Translate adjacent labels, role descriptions, gallery captions, instructions and required story information separately. Retention, completion and actual release adoption remain distinct.
