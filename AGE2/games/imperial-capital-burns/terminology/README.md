# 帝都燃烧篇术语与基线

[返回本作](../README.md) · [术语维护规则](../../../../localization-make-games-speak/text-ai-translation-worth-reading/04-terminology.md)

- [本作术语表](../../../../localization-make-games-speak/glossaries-keep-it-consistent/imperial-capital-burns.ja-zh-Hans.csv)：306条，查当前采用译法和使用限制。
- [主基线](baseline.ja-zh-Hans.csv)：405条，401种日文写法，包含全部本作术语及其他语境／历史译法。
- [来源记录](history/evidence-20261009.csv)：491条，用于追溯，不与主表重复计数。
- [系列通用表](../../../../localization-make-games-speak/glossaries-keep-it-consistent/muv-luv.ja-zh-Hans.csv)：与本作表共同使用，不加载其他作品专表。

数量按2026-10-09当前CSV统计，不代表全文译文的人工审核进度。

## 如何使用

先查术语表，再按`context`判断是否适用于当前人物、装备、呼号或语境。基线是术语表的父集：每条现行术语保留一条`term`，其他用法按`kind`区分。相同日文、中文和类别合并来源；不同中文分别保留，不能因日文字串相同就全局替换。

主表六列为`jp,cn,kind,chapter,basis,evidence_rows`。当前有306条`term`、96条`context`和3条`reference`。`reference`保留“兵士级”“战时特别法”“战术机”等旧来源译法，不覆盖现行采用。“乳歯”是对候补生的戏称，“九段に向かった”是维护者审定的整句处理，均留在语境基线；“悪酔い”有明确的强化装备设定含义，继续作为术语。

字段和状态见[共用说明](../../../../localization-make-games-speak/text-ai-translation-worth-reading/04-terminology.md#公开基线字段与状态)。`evidence_rows`指向本目录来源CSV的记录编号，含表头从1计；`source_row`指向原输入记录，两者不能混用。

## 来源与覆盖范围

原先公开基线只承接185条旧独立表和79条暂定专表；后者没有增加新的日文词形，并不是另一份覆盖全文的详细基线。本轮保留原264条来源记录，仅为误命中“響→响”追加排除依据，不抹去原中文或旧状态字段。

| 来源标识 | 含义 |
| --- | --- |
| `imperial-old` | 185条旧独立表记录 |
| `selected-imperial-capital-burns` | 79条先前暂定专表记录 |
| `imperial-speakers-20261009` | 当前说话人表全部91条映射，逐条核对实际调用；专名和普通／合说标签分别分类 |
| `imperial-body-20261009` | 从当前正文补录136条词项及适用限制，不是136条新译文 |


现行正文共5564条、72个场景，91条说话人映射均有实际调用。旧日文对照按ID逐条核验，与现行`source_text_sha256`全部一致；用现行中文进行词项复核，不拿旧版中文覆盖现稿。本轮另对全文专名候选逐项定位，补入现行正文和说话人表中已采用的译法。普通身份、合说姓名栏只作为语境映射；完整人名、地名、呼号、型号及设定术语才进入术语表。“７７式”在不同装备名称里指代不同，因此仅把与82式机体比较的用法收为语境项。

历史来源的状态和出现次数保留原口径，不跨来源相加。新增说话人来源的`source_row`是当前说话人CSV含表头的记录编号；新增正文来源使用`记录ID:日文词项`，让同一句中的不同词项能分别定位。新增`occurrences`按含该词项的记录数统计，长词内包含的短词也可能计入，不能当作独立概念出现次数。

主表`chapter`列最多展开两个场景，更多场景通过[逐条复核记录](../../../../docs/research/localization/terminology-history/imperial-review-20261009.json)中的`scenes`、`record_ids`查询。完整官方例句不随公开表发布；这次没有重新实机测试或进行一轮全文翻译校对，也不声称已穷尽所有隐含典故。

[整理明细](review-20261009.md)列出分类及补录的具体变化。程序按本作`project.toml`读取，查询示例：

```powershell
python localization-make-games-speak/tools-let-tools-handle-repetition/terminology.py imperial-capital-burns --baseline
python localization-make-games-speak/tools-let-tools-handle-repetition/terminology.py imperial-capital-burns --baseline --term 悪酔い
python localization-make-games-speak/tools-let-tools-handle-repetition/terminology.py imperial-capital-burns --baseline --history
python localization-make-games-speak/tools-let-tools-handle-repetition/terminology.py imperial-capital-burns --check-baseline
```
