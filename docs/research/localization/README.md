# 本地化参考与研究工具

[研究入口](../README.md) · [本地化制作方法](../../../Localization-MakeGamesSpeak/README.md)

这里提供跨作品比较所需的参考词对、来源定位和研究工具。日常制作使用现行术语表及各作基线，参考译法不直接覆盖项目决定。

| 内容 | 怎样使用 |
| --- | --- |
| [原文保留实例](retention-examples.md) | 分清片尾署名、歌曲原题、画内陈设、日期标记与应译的信息 |
| [多语言源槽关联](source-alignment.md) | 按记录与脚本确认同一句，并保留 PM 的未决关联疑点 |
| [本篇／AL 独立术语参考](references/main-al-independent-20260909/README.md) | 按词形、中文变体、说话人标签及来源 ID 比较用法 |
| [Steam 参考快照](references/main-al-steam-20260909/README.md) | 查看较早的参考词对与提取边界 |
| [术语回归数据](terminology-history/README.md) | 维护来源关联，防止旧错误、跨作污染和资料丢失 |
| [研究工具](tools) | 导出术语级参考、验证 Steam 来源或读取历史 ZIP 图片清单 |
| [研究测试](tests) | 验证这些数据契约与已知回归，不代替语义审核或实机测试 |

`reviews/` 中保留的结构化修改与上下文数据供回归和查找具体修订使用。翻译取舍的阅读入口是[术语实例](../../../Localization-MakeGamesSpeak/Glossaries-KeepItConsistent/decisions.md)与各作基线。

研究工具需要用户自行提供合法取得的本地输入，不用于直接翻译、修图或构建玩家补丁。PM 字体度量工具见 [rUGP/fonts](../../../rUGP/tools/fonts)，共用制作工具见[本地化工具](../../../Localization-MakeGamesSpeak/Tools-LetToolsHandleRepetition/README.md)。

修改本组代码或数据契约时运行：

```powershell
python -m unittest discover -s docs/research/localization/tests -p "test_*.py" -v
```
