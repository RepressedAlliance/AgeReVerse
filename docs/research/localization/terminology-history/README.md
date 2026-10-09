# 术语查证与历史记录

[返回现行术语表](../../../../localization/glossaries/README.md)

本目录保存历史快照与审计证据。记录中的原始路径、数量和哈希描述当时的状态；当前表的位置以现行术语入口和各作 project.toml 为准。

2026-09-09 按维护者确认进行[本篇／AL对齐及中文军衔修订](../reviews/main-al-alignment-20260909.md)。历史基线保留原始译法，修订记录逐条列出新旧译法。

后续完成的[独立发现目录](../references/main-al-independent-20260909/README.md)包含本篇403项、AL529项及77个共同词形；先独立发现再交叉比较，不是旧101／193项参考名单的命中扩展。

本篇／Alternative 的 [Steam 术语参考快照](../references/main-al-steam-20260909/README.md)单独存放，仅供查证，尚未加入生效术语表。

系列通用表为 [muv-luv.ja-zh-Hans.csv](../../../../localization/glossaries/muv-luv.ja-zh-Hans.csv)，目前 **146 条**。
Muv-Luv七作使用“通用表 + 本作术语表”，君望独立使用本作表，不继承其他作品的专表。基线用于查证和审校，不作为自动替换字典加载。

| 作品／本轮整理明细 | 本作术语表 | 基线证据记录 | 去重后的日文写法数 |
| --- | ---: | ---: | ---: |
| [TDA00](../../../../AGE2/games/tda00/terminology/review-20261009.md) | [135 条](../../../../localization/glossaries/tda00.ja-zh-Hans.csv) | [382 条](../../../../AGE2/games/tda00/terminology/baseline.ja-zh-Hans.csv) | 363 |
| [TDA01](../../../../AGE2/games/tda01/terminology/review-20261009.md) | [89 条](../../../../localization/glossaries/tda01.ja-zh-Hans.csv) | [196 条](../../../../AGE2/games/tda01/terminology/baseline.ja-zh-Hans.csv) | 189 |
| [TDA02](../../../../AGE2/games/tda02/terminology/review-20261009.md) | [98 条](../../../../localization/glossaries/tda02.ja-zh-Hans.csv) | [220 条](../../../../AGE2/games/tda02/terminology/baseline.ja-zh-Hans.csv) | 206 |
| [TDA03](../../../../AGE2/games/tda03/terminology/review-20261009.md) | [115 条](../../../../localization/glossaries/tda03.ja-zh-Hans.csv) | [261 条](../../../../AGE2/games/tda03/terminology/baseline.ja-zh-Hans.csv) | 242 |
| [帝都燃烧](../../../../AGE2/games/imperial-capital-burns/terminology/review-20261009.md) | [183 条](../../../../localization/glossaries/imperial-capital-burns.ja-zh-Hans.csv) | [186 条](../../../../AGE2/games/imperial-capital-burns/terminology/baseline.ja-zh-Hans.csv) | 183 |
| [光子之花](../../../../rUGP/games/photonflowers/terminology/review-20261009.md) | [313 条](../../../../localization/glossaries/photonflowers.ja-zh-Hans.csv) | [566 条](../../../../rUGP/games/photonflowers/terminology/baseline.ja-zh-Hans.csv) | 447 |
| [光子旋律](../../../../rUGP/games/photonmelodies/terminology/review-20261009.md) | [750 条](../../../../localization/glossaries/photonmelodies.ja-zh-Hans.csv) | [4410 条](../../../../rUGP/games/photonmelodies/terminology/baseline.ja-zh-Hans.csv) | 2672 |
| 君望（本篇及番外） | [167 条](../../../../localization/glossaries/kiminozo.ja-zh-Hans.csv) | [360 条](../../../../AGE2/games/kiminozo/terminology/baseline.ja-zh-Hans.csv) | 359 |

上表按2026-10-09当前CSV统计；日期命名的恢复清单和修订记录保留当时的数量。

“去重后的日文写法数”只合并`jp`文字完全相同的记录，不合并全角／半角或其他原文写法。同一日文在不同来源、状态和语境中可以留下多条记录，所以这一列小于基线记录数；不是删掉了这些资料。

各作基线是本作术语的父集，保留全部本作术语的依据，并包含语境项、候选和待核记录。条目提升为术语后仍留在基线；同一日文的不同来源或语境可以分别记录。

基线保留同一词的不同来源、不同状态和语境，**记录数不等于已确认术语数**。同一个词也可在通用表和专表有各自的使用依据，两表行数不能直接相加。TDA01–03 是依据旧词库及本作日文重建的基线，不冒充旧的完整人工审定表。

## 应该看哪张表

君望本篇及附加篇仍在制作中，本轮首次公开术语和语境基线；来源及待核状态见[君望说明](../../../../AGE2/games/kiminozo/terminology/README.md)。这是独立整理的本作数据，不属于下述Muv-Luv七作历史恢复范围。

- 查系列稳定译法：通用表。
- 校对当前作品：本作术语表，必须连同 context 使用。
- 查旧译、候选、篇章限制、争议和为什么没有采用：本作基线。

术语表三列为 `jp,cn,context`。基线九列、状态与来源编号的含义见[公开基线字段与状态](../../../../localization/text/04-terminology.md#公开基线字段与状态)。状态描述该条来源记录，不能代替当前术语表及实际语境。空中文候选保留为待查资料。

旧“激光级”、拟声片段“ァァ”等可能出现在基线或历史表中，**不代表它们恢复为现行采用译法**。光线级、重光线级及壬姬遵循当前修正。

2026-10-09先补齐24条现行术语的基线记录：TDA02两条、TDA03三条、光子之花十五条、光子旋律四条。译法和使用限制沿用已收录的现行表，未改旧记录或正文；[补录记录](baseline-additions-20261009.json)保留来源版本和逐条内容。

## 七作基线的现行决定同步（2026-10-09）

随后逐作追加现行采用记录，共1683条，分别对应七作本作术语表的每一条。新增行保留现行中文及完整使用限制，并关联旧来源；旧基线记录原样保留。基线行数因此增加，术语条数和日文写法数没有增加，也没有修改游戏正文。

原基线中有45项尚未记录现行中文：TDA00、TDA01、TDA02各1项，TDA03有4项，帝都燃烧3项，光子之花18项，光子旋律17项。这是按“作品×条目”统计的资料同步缺口，不是45处新的正文错译。各作整理明细逐项列出旧中文、现行采用及使用范围；现行表中43条失效资料路径和8条与现行中文不一致的说明也已修正，日文和中文列没有改变。

读取工具将现行采用、历史／语境参考、候选、待核问题、原已排除及旧依据已注明的扫描误命中分开显示，原状态不回写。光子之花的746条普通表达／误命中沿用旧依据分类；其他候选仍需按语境审定，不因本轮整理而自动确认。

TDA02、TDA03、光子之花、光子旋律共107项尚无具体篇章定位，各作明细列出了条目及现有资料限制。新增记录保留已知的本作／合集范围和使用限制，不把来源表行号当作游戏台词编号；未定位也不等于未出现。

## 来源与完整性

[恢复说明](recovery-20260908.md)记录原表规模、TDA 重建方法和未完成的语义确认；[恢复清单](recovery-20260908.json)记录原文件提交号、哈希和逐作计数。

完整恢复的独立输入包括：帝都燃烧 185 条、光子之花 EX 表 88 条及基线 945 条、光子之花 AL 表 98 条、光子旋律时空的欠片表 417 条及基线 2,321 条、光子旋律憧憬／再诞表 341 条，以及 TDA00 草案 369 条。不同表间有重复，不相加当作独立词总量。

[首次审计](scope-audit-20260908.md)已撤回“资料齐全／完成”结论，仅保留为历史。[旧混合表](mixed-20260908.csv)和[帝都旧表](imperial-20260908.csv)是历史校验副本，不参与加载。官方完整日英例句不重新公开，保留术语和来源定位。

## 使用与维护

每作`project.toml`明确指定`terminology_authority`、`terminology_baseline`；Muv-Luv七作另指定`terminology_common_authority`。君望不登记通用表。读取工具不会扫描、拼接其他作品或历史目录。

```powershell
python localization/tools/terminology.py photonflowers --term ミキ
python localization/tools/terminology.py tda00 --term ウィル
python localization/tools/terminology.py tda00 --baseline --term ウィル
python localization/tools/terminology.py photonflowers --baseline --group noise
python localization/tools/terminology.py photonmelodies --check-baseline
```

通用与本作出现同词异译时工具报错，不能以加载顺序覆盖。候选匹配采用片假名边界，避免ウィル命中ウィルス；单字人名仍须严格按人物/说话人语境判断。没有自动改写正文的操作。

新增或修改术语先在本作基线记录出处、状态和适用范围，审定后再改对应使用表；有跨作依据才提升到通用表。新增语言建立独立文件，不覆盖简体中文。具体规则见 [章节术语工作流](../../../../localization/text/04-terminology.md)。
