# 最小共用工具

[返回本地化](../README.md) · [图片工具用法](../images/tools.md) · [测试](../tests/README.md)

只保留已经有用途、可以跨引擎复用的制作和校对工具。按当前工作选择所需项，不要求每次制作固定跑完全部命令。

| 工作 | 工具 | 什么时候用 |
| --- | --- | --- |
| 新语言空白工作表 | [create_locale_template.py](create_locale_template.py) | 开始新的目标语言，清掉旧译文、保留明确身份 |
| 字体覆盖与必要补字 | [font_coverage.py](font_coverage.py)、[extend_font_subset.py](extend_font_subset.py) | 选字／改文检查覆盖；确认缺字后才扩展子集 |
| 小区域无字底 | [build_deterministic_textless_background.py](images/build_deterministic_textless_background.py) | 适合从周边纹理恢复的区域；复杂背景改用适当修图方式 |
| 通用 PNG 排字 | [render_deterministic_localized_text.py](images/render_deterministic_localized_text.py) | 固定字体和样式的普通排版；不是所有 Logo／场景的强制做法 |
| 尺寸、alpha 与修改范围 | [verify_localized_image_invariants.py](images/verify_localized_image_invariants.py) | 检查实际候选图的画布与区域外像素 |
| 同组度量 | [verify_localized_group_consistency.py](images/verify_localized_group_consistency.py) | 已有可信度量时辅助找异常，仍需看整组图片 |
| ParaTranz 同步 | [sync_icb_paratranz.py](sync_icb_paratranz.py)、[sync_series_paratranz.py](sync_series_paratranz.py) | 维护者确认后按[同步说明](../paratranz/sync.md)回流中文 |
| 内部共用 | [terminology.py](terminology.py)、[safe_output.py](safe_output.py) | 当前术语加载与安全输出；由上面工具复用 |

引擎提取、解码、写回、运行时和安装构建放在 [AGE2](../../AGE2/README.md)／[rUGP](../../rUGP/tools/README.md)。PM 字体度量修复放在 [rUGP/fonts](../../rUGP/tools/fonts/README.md)；历史 ZIP 清单、Steam 来源核验、旧术语研究导出放在[研究工具](../../docs/research/localization/README.md)。

不在此新增模型 API 驱动、全自动分类器、通用游戏打包器或一套重复的浏览器审核系统。制作方可以使用现有模型／编辑器完成视觉工作，这些工具只补实际需要的可复用环节。
