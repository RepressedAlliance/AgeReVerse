# 本地化工具｜把时间留给翻译

**Localization Tools: Let Tools Handle the Repetition**

[返回本地化](../README.md) · [图片工具用法](../Images-MakeItLookNative/tools.md) · [测试](../Tests-CatchProblemsBeforePlayers/README.md)

<details>
<summary><strong>English · Let Tools Handle the Repetition — expand here</strong></summary>

Use the tool for the task in front of you. Install `requirements-dev.txt` and run the documented `python -m` commands from the repository root; each CLI provides `--help`.

| Task | Tool | Inputs and result |
| --- | --- | --- |
| Look up adopted terms and their evidence | [terminology.py](terminology.py) | Game ID and Japanese term → scoped glossary entries, baseline records and source links |
| Start a new locale | [create_locale_template.py](create_locale_template.py) | Explicit source-table columns and target locale → an identity-preserving blank worksheet and manifest |
| Check or extend font coverage | [font_coverage.py](font_coverage.py), [extend_font_subset.py](extend_font_subset.py) | Font and translated text → missing-codepoint report; compatible, appropriately licensed donor inputs → an explicitly extended font |
| Author and check PNG lettering | [Image tool guide](../Images-MakeItLookNative/tools.md) | Source, copy, masks and style → background/lettering candidates and constrained pixel or group checks |
| Pull community revisions | [Synchronization guide](../ParaTranz-KeepImprovingTogether/sync.md) | Existing project mapping and two-sided baseline → a reviewed change report and explicitly applied permitted updates |

Engine extraction, codecs, runtime integration and package builds remain in AGE2 or rUGP. These tools do not automatically translate, approve artwork, resolve conflicting revisions or publish a finished patch. When changing a tool, run its [focused regression tests](../Tests-CatchProblemsBeforePlayers/README.md).

</details>

让工具处理能明确描述的重复劳动，把精力留给理解剧情、判断译法和打磨画面。这里保留已经用于制作、可以跨引擎复用的工具；从任务选择需要的命令即可。

## 按任务选工具

| 我需要做什么 | 工具 | 提供什么 | 得到什么 |
| --- | --- | --- | --- |
| 查一个词现在怎样译、依据在哪里 | [terminology.py](terminology.py) | 游戏及日文检索词，可选择基线／历史 | 本作现行译法、适用范围和关联来源；也可检查基线关联 |
| 开始新的目标语言 | [create_locale_template.py](create_locale_template.py) | 源表、身份／源哈希／旧译列及目标语言 | 保留身份、清空旧译的独立工作表和说明清单 |
| 检查字体有没有缺字 | [font_coverage.py](font_coverage.py) | 字体、译文表及目标列 | 字符覆盖与缺字报告，不改译文 |
| 给已确认缺字的字体补字 | [extend_font_subset.py](extend_font_subset.py) | 可兼容且来源许可适当的基础／供字字体、字符和输入摘要 | 保留已有字形与度量的扩展字体及记录 |
| 恢复小块文字区域的无字底 | [build_deterministic_textless_background.py](images/build_deterministic_textless_background.py) | 源图、审核过的区域或遮罩 | 无字底、旧字遮罩和检查记录；适用于可从周边恢复的纹理 |
| 按固定样式制作普通 PNG 中文字 | [render_deterministic_localized_text.py](images/render_deterministic_localized_text.py) | 源图、无字底、文案、字体与样式配置 | 候选图、允许修改遮罩与排字记录 |
| 检查图片有没有改到范围外 | [verify_localized_image_invariants.py](images/verify_localized_image_invariants.py) | 源图、候选图、允许修改遮罩 | 尺寸、alpha、区域外像素与摘要检查 |
| 找出同组图片的度量异常 | [verify_localized_group_consistency.py](images/verify_localized_group_consistency.py) | 已有可信度量及同组记录 | 辅助异常报告，供逐组视觉复核 |
| 将确认的 ParaTranz 修订回流 | [sync_icb_paratranz.py](sync_icb_paratranz.py)、[sync_series_paratranz.py](sync_series_paratranz.py) | 本作映射、同步基线及在线导出或离线快照 | 变更报告；显式应用后更新允许范围内的中文及同步记录 |

## 从一个真实任务开始

从仓库根目录安装现有依赖：

```powershell
python -m pip install -r requirements-dev.txt
```

例如，查询 TDA00 的当前译法，再查看基线及对应来源：

```powershell
python -m Localization-MakeGamesSpeak.Tools-LetToolsHandleRepetition.terminology tda00 --term ウィル
python -m Localization-MakeGamesSpeak.Tools-LetToolsHandleRepetition.terminology tda00 --baseline --term ウィル
```

查询其他作时换成对应游戏 ID。新语言工作表见[新语言指南](../Text-AITranslationWorthReading/new-locale.md)，字体检查见[字体排版](../Fonts-ThatFitTheGame/README.md)，图片的完整输入与命令示例见[图片工具用法](../Images-MakeItLookNative/tools.md)。ParaTranz 的预检、应用范围和冲突处理按[维护者同步说明](../ParaTranz-KeepImprovingTogether/sync.md)执行。

## 修改或复用这些工具

[safe_output.py](safe_output.py)供需要发布新文件的工具复用，负责拒绝已有输出、路径别名和不完整发布。修改工具时先运行[对应测试](../Tests-CatchProblemsBeforePlayers/README.md)，检查本次涉及的行为。

引擎提取、解码、写回、运行时和安装构建放在 [AGE2](../../AGE2/README.md)／[rUGP](../../rUGP/tools/README.md)。PM 字体度量修复放在 [rUGP/fonts](../../rUGP/tools/fonts/README.md)；历史 ZIP 清单、Steam 来源核验、旧术语研究导出放在[研究工具](../../docs/research/localization/README.md)。

制作方可以使用适合的模型或编辑器完成翻译与视觉工作。这些工具处理明确的制作和校验环节；译文含义、视觉融合与实机表现仍按相应工作流判断。
