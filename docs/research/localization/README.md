# 本地化研究与历史记录

[研究入口](../README.md) · [当前本地化制作](../../../Localization-Make-Games-Speak/README.md)

这里保留仍有查证和回归价值的旧资料，日常制作从 `Localization-Make-Games-Speak/` 开始。

| 资料 | 用途 |
| --- | --- |
| [原文保留核对](original-retention-20261010.md) | TDA00–03、帝都燃烧、PF／PM 的署名、曲名与原画保留依据，以及君望、PF／PM 七曜日期图的既有决定 |
| [references](references) | 2026-09-09 本篇／AL Steam 来源核验和独立术语发现；参考研究，不是当前七作术语表 |
| [reviews](reviews) | 旧审核批次、修复依据和人工校对过程；不代表此后所有译文必须等于旧句子 |
| [terminology-history/](terminology-history/README.md) | 旧混合表、逐作恢复和范围审计；当前表在 [glossaries](../../../Localization-Make-Games-Speak/Glossaries-Keep-It-Consistent/README.md) |
| [tools](tools) | 研究用术语证据导出、Steam 来源核验和历史 ZIP 图片清单 |
| [tests](tests) | 上述研究与历史数据的来源、公开边界和已知回归检查 |

研究工具不用于直接翻译、修图或构建补丁。PM 专属字体度量修复已归入 [rUGP/tools/fonts/](../../../rUGP/tools/fonts)，共用制作工具保留在 [Localization-Make-Games-Speak/Tools-Let-Tools-Handle-Repetition/](../../../Localization-Make-Games-Speak/Tools-Let-Tools-Handle-Repetition/README.md)。

需要修改研究代码或其数据契约时再运行本组测试：

```powershell
python -m unittest discover -s docs/research/localization/tests -p "test_*.py" -v
```

历史文件中的原始提交、来源摘要和旧位置用于描述当时事实，保留其含义；当前入口与代码引用已调整到新位置。不得将研究候选、旧版数量或历史包内容宣称为当前玩家版本的状态。
