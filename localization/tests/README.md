# 共用工具检查

[工具目录](../tools/README.md) · [贡献验证说明](../../docs/project/CONTRIBUTING.md)

这里测试现行共用工具：新语言表、术语作用域、字体覆盖／子集扩展、图片区域约束／排字／同组度量、安全输出和 ParaTranz 回流。测试使用合成输入或可公开的数据，不需要原版游戏。

修改某个工具先跑其对应测试，例如：

```powershell
python -m unittest localization.tests.test_verify_localized_image_invariants -v
```

调整跨工具共用行为或整组迁移时再跑本目录：

```powershell
python -m unittest discover -s localization/tests -p "test_*.py" -v
```

历史资料及研究工具测试在 [docs/research/localization/tests](../../docs/research/localization/tests)，PM 字体专项测试归入 [rUGP/tests](../../rUGP/tests)。单纯修改教程措辞不要求重新跑各游戏全套测试；实际新工具或行为改变按风险补有意义的验证。

这些检查不判断译文原意，也不替代图片视觉审核或实机验证。
