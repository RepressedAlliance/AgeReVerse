# Photon 历史审校文本与来源绑定

[现行文字资产](../../../../games/README.md) · [章节维护方式](../../../../docs/chapter-texts.md)

本目录的 manifest 绑定四组故事共 **57,547 行**历史审校中文，不包含完整官方日文。它用于来源比较、导出和回归，不是当前玩家包的文本版本索引。继续修改请从各作 `translations/` 与 `text-data/` 进入；69／151 行的旧精确运行时契约也不代表两作只汉化了这些文字。

| 历史表 | 行数 |
| --- | ---: |
| [光子之花 / Alternative](../../../../games/photonflowers/text-data/history/reviewed/alternative.zh-Hans.csv) | 6,033 |
| [光子之花 / Extra](../../../../games/photonflowers/text-data/history/reviewed/extra.zh-Hans.csv) | 6,931 |
| [光子旋律 / Adoration + Resurrection](../../../../games/photonmelodies/text-data/history/reviewed/adoration-resurrection.zh-Hans.csv) | 8,407 |
| [光子旋律 / Shard of Spacetime](../../../../games/photonmelodies/text-data/history/reviewed/shard-of-spacetime/) | 36,176 |

行内保存调用顺序、稳定 ID、RIO 分卷、CRsa 场景、日文源字段摘要和中文译文。说话人与完整原文是本地合法输入，不写入这些公开 CSV。导出器检查顺序、唯一身份、RIO／场景关联、必需字段、内嵌 NUL、源摘要与预期行数。

## 按既定来源导出

输入必须与对应 manifest 的源身份一致，输出使用不存在的新文件：

```powershell
python -m rUGP.tools.text.export_reviewed_translation `
  "<private-comparison.csv>" `
  "<new-public.zh-Hans.csv>" `
  --expect-source-sha256 <SHA256> `
  --expect-id-prefix pf --expect-rows 6033
```

《时空的欠片》按 RIO 分卷拆为三个文件；需要比较时按 manifest 顺序连接，临时合并文件放在忽略目录。现行译文可继续接受校对，历史快照的固定身份用于回归，不冻结后续修改。

## English

These manifests bind 57,547 historical reviewed Chinese rows for source comparison and regression. They do not identify the current player text. Edit the maintained game tables; the small legacy runtime contracts describe specific bindings, not the total amount translated.
