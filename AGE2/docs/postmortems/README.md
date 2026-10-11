# AGE2 技术案例与适用范围

从问题中提炼可复用的方法：格式边界、资源选择、文字布局与版本兼容性。各项说明实现与仍有的限制。

- [图片字幕排版](caption-layout.md)：原版演出坐标、可见字形对齐与行距。
- [UI 与场景图布局](image-layout.md)：跨作尺寸、光晕锚点、地图补注与覆盖漏项。
- [语言缓存与资源读取](language-switch-cache.md)：相同文字切换字形、原生内存生命周期与文件长度。
- [细横线显示](horizontal-bar.md)：字符存在但缩放后不可见的字体修正。
- [当前范围与待确认事项](../limitations.md)：内容、显示与发布版本的实际边界。

- [`tda03-achievement-uistring.md`](tda03-achievement-uistring.md): a TDA02
  `uistring.epk` was accidentally shipped in TDA03 beta0.1–beta0.1.5, breaking
  chapter/achievement mappings; fixed in beta0.1.6.
- [`loose-overlay-boundary.md`](loose-overlay-boundary.md): why LocalAppData
  `data/root` is a higher-priority loose namespace, not an automatic full
  extraction of `pack.bin`, and why whole-directory rollback is unsafe.
- [`structural-empty-records.md`](structural-empty-records.md): five verified
  empty bookkeeping slots became explicit no-op records instead of apparent
  missing translations or silent row deletions.
- [`font-glyph-substitution-retired.md`](font-glyph-substitution-retired.md):
  the lossy character-replacement workaround was removed in favor of real font
  coverage, routing, metrics and license checks.
- [`public-snapshot-release-alignment.md`](public-snapshot-release-alignment.md):
  a maintained translation table, runtime authority and historical ZIP are
  separate claims; the current AGE2 end-to-end rebuild remains partial.

New technical notes should explain the observable behavior, cause, usable correction and remaining support limits. Keep game-specific parameters scoped to the corresponding assets.
