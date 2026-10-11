# 细横线缩小后消失：字形覆盖之外的排版问题

[字体入口](../../../Localization-MakeGamesSpeak/Fonts-ThatFitTheGame/README.md) · [技术案例](README.md)

TDA02 中文 Log 曾在小窗口中看不到 U+2015 横线，最大化后却可见。字符存在、字形生成成功且未越界，也不能保证最终缩放后的细线可见；栅格位置和缩放会共同影响结果。

[strengthen_horizontal_bar.py](../../tools/font/strengthen_horizontal_bar.py) 在独立命名的字体副本中将 U+2015 加厚到同字体 U+2014 的厚度，保留字宽、进位和垂直中心，并重建该字形以避免旧 hint 抵消修改。配置只更换对应文件引用，原字库保留。

这是一项字体字形修正，没有证明引擎 GPU 缩放根因已解决。修改后应重新加载字体，检查其他字形、水平进位及字体度量；再在小窗口、最大化、恢复小窗口三种状态下观察实际显示。离线栅格覆盖增加不能替代这一步。

对应字体可能同时用于其他中文界面，影响范围要按实际配置判断。字体来源、许可与派生修改一并登记；当前已发布字体见[运行时对应表](../../../Localization-MakeGamesSpeak/Fonts-ThatFitTheGame/runtime.md)。

## English

A covered glyph can disappear after downscaling. The U+2015 workaround changes one glyph in a separately named font while preserving advance and metrics; it is not a general GPU-renderer fix. Verify the font's other glyphs and test the final display at different window sizes.
