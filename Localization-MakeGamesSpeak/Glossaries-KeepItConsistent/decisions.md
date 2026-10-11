# 术语取舍：同一个词，也要看它在说什么

[术语与全文一致性](README.md) · [术语流程](../Text-AITranslationWorthReading/04-terminology.md) · [修改反查](../Text-AITranslationWorthReading/07-change-impact.md)

术语表约束的是特定对象与语境的译法。下面这些项目实例说明，怎样把确定的对应落实到全文，同时保留有意义的差异。

## 词形相同，不代表对象相同

| 例子 | 处理 | 可复用的方法 |
| --- | --- | --- |
| `ウィル` 与 `ウィルス` | 人名不能命中“病毒”的片假名子串 | 检索先检查词边界，再读语境 |
| `響` 与 `影響`、`心に響いた` | 普通词里的字不作为姓名映射 | 区分完整姓名栏与正文普通词 |
| 帝都 `コントロール` | 操作“控制”与“岚山管制”呼号分别判断 | 完整呼号可以定名，普通用法不全局替换 |
| 帝都 `乳歯`、`九段に向かった` | 保留候补生戏称和人物去向的语境处理 | 整句理解存入基线，不包装成无条件专名 |
| 帝都 `悪酔い` | 强化装备设定中的特定反应 | 是否列为术语取决于作品含义，不能只按日常词义分类 |

当前译法与使用限制以各作术语表及基线为准；旧来源中的错误映射、候选和普通表达不能自动回流。

## 称谓、呼号与全称分别维护

- 日式军衔采用项目的中文名称：少佐／中佐／大佐对应少校／中校／上校，大尉对应上尉，曹长／军曹／伍长对应上士／中士／下士。“临时”身份仍需保留。
- “战术步行战斗机”是全称，“战术机”是简称，不在每句中强行展开。
- 队名可使用“女武神／女武神中队”，无线电呼号中的 `Valkyrie` 加编号与 `Valkyrie Mam` 按呼号使用；姓名栏映射不能拿来替换正文子串。
- `ハイヴ` 的一般义项采用“巢穴”，例如 `佐渡島ハイヴ` 对应“佐渡岛巢穴”；`Original HIVE` 等专名形式单独判断。

## 改一处之后，继续查哪里

TDA03 的 NORAD 名称修订涉及正文与 ruby 锚文本，不能只改屏幕上看得到的一处。角色姓名的正式长名、简称和戏谑改名则要分别核对，避免把人物语气也改平。

正文改名也会影响姓名卡、徽章、字幕和地图文字。先找到对应素材和当前版本，再修改图片文案与配方；旧制作候选不能因文字相同就覆盖较新的资源。文字、图片和运行时姓名颜色各有自己的输入，必须沿实际引用关系同步。

本篇／Alternative 的参考译法用于比较，不直接覆盖各作决定。项目已选择的光线级、女武神等名称仍按现行语境使用；有分歧时记录理由，再反查受影响的位置。

## English

Treat terminology as a scoped decision. Match whole names and speaker labels, distinguish ordinary words from fictional concepts, and preserve meaningful differences between full names, nicknames and callsigns. A revised name may affect dialogue, ruby anchors, image lettering and runtime color aliases; trace their actual resource bindings rather than applying a global string replacement. Current game glossaries and contextual baselines remain the authority.
