# 本篇／AL 独立术语参考

这份参考独立于相邻的早期 101／193 项名单提取，不以旧词表为种子。词形、中文变体和说话人标签用于跨作比较，**不作为各作生效术语，也不允许自动替换**。两份参考有重叠，不相加计数。

| 内容 | 本篇 | AL |
| --- | ---: | ---: |
| 日文词形 | 403 | 529 |
| 中文变体 | 406 | 551 |
| 说话人标签对 | 167 | 296 |

- `ml-independent-baseline.json`、`al-independent-baseline.json`：词形、中文变体、分类、来源 ID 和日英中字段摘要。
- `ml-speaker-baseline.json`、`al-speaker-baseline.json`：完整标签对应；组合说话人不能计为单个人物。
- `shared-forms.json`：两作共有的 77 个归一化词形；共同出现不意味着可直接进入系列通用表。
- `discovery-freeze.json`：提取输入的身份与范围元数据，不是已删除例句的公开导出文件校验值。

词形包含专名、技术词、称谓和局部文化表达，不是全局强制术语。自动扫描范围也不代表全文人工通读或逐项审定。原译异体和疑点保留为比较资料，不直接当作推荐译法；光线级、女武神等项目规则继续以[现行术语](../../../../../Localization-MakeGamesSpeak/Glossaries-KeepItConsistent/README.md)为准。

完整官方例句和机器候选留在本地。导出器仅保留术语级标签与来源摘要，要求一个不存在的新输出目录：

```powershell
python docs/research/localization/tools/export_independent_main_al.py --source <本地独立提取目录> --destination <不存在的新输出目录>
```
