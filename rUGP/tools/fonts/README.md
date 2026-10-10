# Photon 字体专项

[返回 rUGP 工具](../README.md) · [字体对应表](../../../Localization-MakeGamesSpeak/Fonts-ThatFitTheGame/runtime.md)

[repair_pm_vertical_metrics.py](repair_pm_vertical_metrics.py) 修复已知 PM 字体的竖向度量错误，固定该历史输入／输出摘要；它不是任意字体的通用修复器。仅在重现该问题时使用，对应测试为 `rUGP.tests.test_repair_pm_vertical_metrics`。

其他语言的覆盖和子集扩展继续复用 [localization 字体工具](../../../Localization-MakeGamesSpeak/Tools-LetToolsHandleRepetition/README.md)，字体文件来源、版本和游戏用途集中于 [fonts/](../../../Localization-MakeGamesSpeak/Fonts-ThatFitTheGame/README.md)。不要把历史输入哈希套到后来已经更新的 PF／PM 发布字体上。
