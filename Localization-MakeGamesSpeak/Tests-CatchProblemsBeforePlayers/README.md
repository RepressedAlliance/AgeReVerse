# 自动化测试｜先替玩家发现问题

**Automated Tests: Catch Problems Before Players Do**

[工具目录](../Tools-LetToolsHandleRepetition/README.md) · [贡献验证说明](../../docs/project/CONTRIBUTING.md)

<details>
<summary><strong>English · Catch Problems Before Players Do — expand here</strong></summary>

These regressions exercise the reusable localization tools with synthetic inputs or public data. They need no original game installation.

- **Templates and manifests:** preserve source identities, create independent locale worksheets and resolve the maintained project paths.
- **Terminology:** load only the applicable common and game-specific tables and reconcile adopted terms with contextual baselines and evidence.
- **Fonts:** distinguish visible characters from control tokens, report missing coverage, and preserve existing glyphs and metrics when extending a subset.
- **Images:** test background/lettering behavior, masks, alpha, outside-region pixels and explicit group metrics.
- **Output and synchronization:** refuse unsafe output aliases or existing destinations, preserve permitted data, and detect conflicting community and repository edits.

Run the test matching the changed behavior first. Use the full directory command above for shared changes or a directory migration. Historical research tests remain under [docs/research/localization/tests](../../docs/research/localization/tests); engine-specific tests remain with their engines. A documentation wording change normally needs content/link verification rather than a full game test run.

Automated checks establish their explicit technical conditions. Meaning, visual quality and in-game presentation still require the relevant human and game review.

</details>

一次“只是改了个工具”的修改，也可能让词条身份丢失、其他作品术语混进来，或让图片改到指定范围之外。这里把这些能明确判断的问题交给自动检查，帮助维护者在交付前发现回归。

测试使用合成输入或可公开的数据，不需要原版游戏。按本次修改选择对应检查即可。

## 这些测试在替我们盯什么

| 修改涉及什么 | 对应测试 | 重点检查 |
| --- | --- | --- |
| 新语言工作表 | [工作表测试](test_create_locale_template.py) | 保留身份和源绑定，独立创建空白目标列，拒绝不明确的字段 |
| 游戏清单与术语 | [项目清单](test_game_project_manifests.py)、[术语作用域](test_terminology_scopes.py) | 引用文件存在，只加载通用＋本作的适用表，现行术语与基线／来源关联一致 |
| 字体覆盖与补字 | [覆盖检查](test_font_coverage.py)、[子集扩展](test_extend_font_subset.py) | 正确区分可见字符与控制符，报告缺字，保留已有字形与度量 |
| 无字底和排字 | [无字底](test_build_deterministic_textless_background.py)、[排字](test_render_deterministic_localized_text.py) | 合成图上的遮罩、样式、alpha 和范围外像素约束 |
| 图片与同组校验 | [图片边界](test_verify_localized_image_invariants.py)、[同组度量](test_verify_localized_group_consistency.py) | 发现尺寸、修改范围及明确度量条件的异常 |
| 新文件输出 | [安全输出](test_safe_output.py) | 拒绝已有输出和路径别名，完整发布新文件 |
| ParaTranz 回流 | [帝都同步](test_sync_icb_paratranz.py)、[系列同步](test_sync_series_paratranz.py) | 保留词条身份与结构，识别双方改文冲突，限制允许写入的范围 |

## 改哪个工具，先跑哪个测试

例如，修改了图片范围检查：

```powershell
python -m unittest Localization-MakeGamesSpeak.Tests-CatchProblemsBeforePlayers.test_verify_localized_image_invariants -v
```

调整跨工具共用行为或整组迁移时，再跑本目录：

```powershell
python -m unittest discover -s Localization-MakeGamesSpeak/Tests-CatchProblemsBeforePlayers -p "test_*.py" -v
```

历史资料及研究工具测试在 [docs/research/localization/tests](../../docs/research/localization/tests)，PM 字体专项测试归入 [rUGP/tests](../../rUGP/tests)。单纯修改教程措辞不要求重新跑各游戏全套测试；实际新工具或行为改变按风险补有意义的验证。

这些检查不判断译文原意，也不替代图片视觉审核或实机验证。
