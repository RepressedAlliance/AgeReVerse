# 图片制作的现有辅助工具

[分步流程](README.md) · [视觉规范](production.md) · [字体](../Fonts-ThatFitTheGame/README.md)

这些工具处理普通 PNG，不读取游戏容器。先用对应引擎提取／解码，再按当前图的需要选择工具。常规 UI 可确定性排字；复杂 Logo、手写和场景融合也可使用绘制或受限区域的图像编辑，均需逐图自检和人工审核。

技术检查只证明尺寸、alpha 或区域约束等明确条件，不证明译文、视觉或实机质量。历史 ZIP 成员清单属于[研究工具](../../docs/research/localization/README.md)，不能当成全量游戏图片提取器。

安装仓库依赖：

```powershell
python -m pip install -r requirements-dev.txt
```

### 1. Build a textless layer

For a small, texture-consistent label, give the detector an audited
`left top right bottom` rectangle. The command creates
`clean_background.png`, `old_text_mask.png`, and `qa.json` in a new output
directory; it refuses to reuse an existing directory.

```powershell
python -m Localization-MakeGamesSpeak.Tools-LetToolsHandleRepetition.images.build_deterministic_textless_background `
  --source work/source.png `
  --asset-id "game:stable-resource-id" `
  --text-patch 120 40 360 105 `
  --output-dir work/textless
```

If automatic neutral-glyph detection is unsuitable, pass a separately reviewed
grayscale mask with `--mask`. Do not use harmonic filling for artwork whose
hidden structure cannot be inferred from its immediate surroundings; use an
official peer/family consensus or a constrained text-removal edit instead.

### 2. Render target-language text deterministically

Create a versioned style profile that pins the variable-font file by SHA-256,
weight, size, tracking, anchor, alignment, fill, strokes, shadow, and font
license identity. The renderer verifies the font hash, renders at 8x, emits the
candidate and allowed-change mask, and restores every outside-mask pixel from
the source before saving.

```powershell
python -m Localization-MakeGamesSpeak.Tools-LetToolsHandleRepetition.images.render_deterministic_localized_text `
  --source work/source.png `
  --clean-background work/textless/clean_background.png `
  --old-text-mask work/textless/old_text_mask.png `
  --target-text-file work/translation.txt `
  --profile work/style-profile.json `
  --output work/candidate.png `
  --allowed-mask work/allowed-mask.png `
  --qa work/render-qa.json
```

The current `photon-deterministic-*` schema names are retained for compatibility
with the reviewed Photon work. The programs themselves are engine-neutral PNG
authoring tools. A profile is not portable until its font and license can be
obtained lawfully by another builder.

### 3. Prove the single-image invariants

```powershell
python -m Localization-MakeGamesSpeak.Tools-LetToolsHandleRepetition.images.verify_localized_image_invariants `
  --source work/source.png `
  --candidate work/candidate.png `
  --allowed-mask work/allowed-mask.png `
  --asset-id "game:stable-resource-id" `
  --output work/invariant-qa.json
```

This gate proves size, alpha, mask confinement, and hashes. It deliberately
does not claim that the wording, typography, encoder, resource route, or
in-game composition is correct.

The renderer may legitimately change alpha where a new anti-aliased glyph,
stroke, or shadow lies inside the allowed mask. The invariant gate therefore
requires exact RGBA (including alpha) outside that mask and reports alpha
changes inside and outside separately; it does not require global alpha
identity.

### 4. Check font coverage

Before rendering a batch, audit the visible target-language code points. Name
the translated column explicitly when a table does not use a recognized field:

```powershell
python -m Localization-MakeGamesSpeak.Tools-LetToolsHandleRepetition.font_coverage `
  work/TargetFont.ttf `
  AGE2/games/tda00/translations/ja-zh-Hans.csv `
  --column cn_text `
  --output work/font-coverage.json
```

For a `.ttc` or `.otc` collection, add the zero-based `--face-index` selected
by the game/profile. The tool intentionally refuses to union cmap coverage
across faces, because that could pass even though no single runtime face has
all required glyphs.

Coverage is only a cmap gate. It does not prove game font selection, shaping,
metrics, wrapping, clipping, or glyphs that were already rasterized into an
image.

### 5. Review a style family

`verify_localized_group_consistency.py` accepts a reviewed JSON specification
containing one approved representative, explicit tolerances, and measured
metrics for every member. It catches outliers but always leaves contact-sheet
review pending:

```powershell
python -m Localization-MakeGamesSpeak.Tools-LetToolsHandleRepetition.images.verify_localized_group_consistency `
  --spec work/family-spec.json `
  --output work/family-qa.json
```

This last command validates supplied measurements; it does not infer semantic
equivalence or choose the representative. Until a project's metric-extraction
recipe is documented, treat those measurements as reviewed inputs rather than
automatically generated truth.

All commands in this section refuse to overwrite an input or an existing
output/report. Use a new staging path for each run, then promote the reviewed
hash; delete or archive an obsolete staging artifact explicitly rather than
letting a rerun replace it silently.

## Publication boundary

Git should retain the stable copy table, resource identity, source/output
hashes, masks or profiles only when their redistribution has been reviewed,
deterministic tools, and durable QA conclusions. Original game images, failed
candidates, raw model request/response ledgers, credentials, caches, and bulk
comparison galleries remain local. Approved localized image bytes may be
published as a separately hashed Release asset when the project has explicitly
reviewed that redistribution; a manifest alone must not pretend those bytes are
available from a clean clone.


## 历史审核资料

[2026-09-09 Photon 图库记录](../../rUGP/evidence/photon/images/static-review-20260909/README.md)描述当时的候选、状态和路由，不是后来发布包的自动视觉证明。当前送审要求见[人工审核](05-human-review-and-delivery.md)，最新候选与实际打包引用需一致。可复用现有 [rUGP 静态审核工具](../../rUGP/tools/images/README.md)，生成图库留在本地。
