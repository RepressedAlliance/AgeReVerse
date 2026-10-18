# 变更记录 / Changelog

本页区分**当前可下载补丁、公开仓库成果和历史测试包**。下载、安装及各作已知问题请以[玩家指南](../player/README.md)和对应发布说明为准。

This page distinguishes current player packages, repository work and historical test packages. Repository changes reach players only when included in a published package.

## 当前可下载补丁 / Current player packages

| 作品 / Game | 当前版本 / Version | 说明 / Notes |
| --- | --- | --- |
| **TDA00**<br><sub>[\[TDA00\] Muv-Luv Unlimited: THE DAY AFTER - Episode 00 REMASTERED](https://store.steampowered.com/app/1407100/)</sub> | **BETA 0.2.1** | [发布说明 / Release notes](https://github.com/RepressedAlliance/AgeReVerse/releases/tag/tda00-BETA-0.2.1) |
| **TDA01**<br><sub>[\[TDA01\] Muv-Luv Unlimited: THE DAY AFTER - Episode 01 REMASTERED](https://store.steampowered.com/app/1407090/)</sub> | **BETA 0.3.3** | [发布说明 / Release notes](https://github.com/RepressedAlliance/AgeReVerse/releases/tag/tda01-BETA-0.3.3) |
| **TDA02**<br><sub>[\[TDA02\] Muv-Luv Unlimited: THE DAY AFTER - Episode 02 REMASTERED](https://store.steampowered.com/app/1342410/)</sub> | **BETA 0.2.1** | [发布说明 / Release notes](https://github.com/RepressedAlliance/AgeReVerse/releases/tag/tda02-BETA-0.2.1) |
| **TDA03**<br><sub>[\[TDA03\] Muv-Luv Unlimited: THE DAY AFTER - Episode 03 REMASTERED](https://store.steampowered.com/app/789830/)</sub> | **BETA 0.2.7** | [发布说明 / Release notes](https://github.com/RepressedAlliance/AgeReVerse/releases/tag/tda03-BETA-0.2.7) |
| **帝都燃烧篇**<br><sub>[The Imperial Capital Burns - Muv-Luv Alternative Total Eclipse](https://store.steampowered.com/app/2630300/)</sub> | **BETA 0.2.1** | [发布说明 / Release notes](https://github.com/RepressedAlliance/AgeReVerse/releases/tag/imperial-capital-burns-BETA-0.2.1) |
| **光子之花（PF）**<br><sub>[Muv-Luv photonflowers\*](https://store.steampowered.com/app/889700/)</sub> | **BETA 0.1.2** | [发布说明 / Release notes](https://github.com/RepressedAlliance/AgeReVerse/releases/tag/pf-BETA-0.1.2) |
| **光子旋律（PM）**<br><sub>[Muv-Luv photonmelodies♮](https://store.steampowered.com/app/889710/)</sub> | **BETA 0.1.2** | [发布说明 / Release notes](https://github.com/RepressedAlliance/AgeReVerse/releases/tag/pm-BETA-0.1.2) |

君望 Steam 本篇及附加篇仍在制作，尚未发布补丁。公开仓库中的新文本、图片、视频或运行时改动，不会自动更新玩家已经下载的版本。

Kiminozo and its additional episodes remain in development. New text, images, videos or runtime work in Git is not automatically part of an existing download.

## 公开仓库中的制作与研究成果 / Repository work

- 完成光子之花／光子旋律全量 CRsa 漏项复核：补译并写回 40 处对白／提示，逐项审校 265 个批注字段，保持 260 个兵装名参数不变；加入哈希锁定的光子旋律固定长度分卷构建器，并记录光子之花／光子旋律实机字体、排版和 831／8311 验收。
- 首页优先呈现玩家下载：中文常用名与完整 Steam 名称对应；制作与研究另设第二部分，英文说明可原地展开。安装、恢复与已知问题由玩家指南补充。
- 新增中英文文本/术语/图片/字体资产地图，明确 `Localization-MakeGamesSpeak/`、各游戏目录、本仓库 Releases 与本地忽略工作区的边界，并同时索引五作 730 个 AGE2 WebP 路径与光子之花/光子旋律 1,490 项图片权威。
- 新增完整英文两轮本地化工作流，使韩语、俄语等团队不必依赖中文摘要即可复现剧情/术语、初译、`keep/revise/question`、写回、QA 与玩家反馈闭环。
- 更新 Codex 贡献说明为 GitHub 可识别的 `Co-authored-by: Codex <codex@openai.com>`，并重写对主任保护协会的致谢，准确表达其 AGES 汉化思路是本项目开始制作补丁的起点。
- 重新逐项比较 GARbro、AFHook、rugptools、FatePackageManager 与成熟翻译项目，把采用的优点和主动补足的缺点写入长期参考文档。
- 建立中文优先的四类入口：玩家、AGE2 研究者、rUGP 研究者和其他语言本地化制作者。
- 为七部游戏加入统一 `project.toml`，明确引擎、Steam App ID、文本、图片与字体权威。
- 从五个 AGE2 历史 Release 机械生成 730 个 WebP 路径的可复核清单；光子之花/光子旋律继续分别索引 636/854 项共用 Photon 图片权威。
- 公开五阶段文本本地化工作流，说明独立复核、疑点处理、技术与实机检查，以及发布前维护者的人工修改；发布后通过 ParaTranz 校对和玩家反馈继续修订。
- 新增贡献者与具体致谢页，记录人类维护责任、OpenAI Codex 的受监督辅助，以及主任保护协会、GARbro、AFHook、rugptools 与 FatePackageManager 的准确贡献边界。
- 将活动证据目录改为稳定语义路径，版本留在 schema、Git 历史和 Release tag 中。
- 规定新表的规范字段，同时保留已有哈希封存表的历史表头，避免为表面统一破坏来源证明。

- Split the unrelated AGE2 and legacy rUGP implementations into independent top-level systems.
- Completed the 光子之花/光子旋律 CRsa omission review: wrote 40 dialogue/prompt fields, reviewed 265 annotation fields, preserved all 260 armament-name parameters, added hash-locked fixed-extent 光子旋律 volume staging, and recorded 光子之花/光子旋律 runtime layout and 831/8311 checks.
- Promoted stable translation tables, format libraries, runtime source, packaging code, tests, and release evidence; removed one-off workstation probes from the public tool surface.
- Added English and Chinese player/developer entry points, rights boundaries, provenance guidance, and reusable image-localization documentation.
- Added direct player-package links, exact LocalAppData destinations, checksum instructions and explicit rollback/Steam Verify boundaries for all five historical AGE2 betas.
- Published 57,547 reviewed Photon dialogue rows without the complete official Japanese dialogue, together with stable IDs, exact source-field hashes and reproducible export evidence.
- Added the read-only GARbro-derived ICI/RIO catalogue, conservative CRsa extraction CLI, and synthetic regressions without redistributing game archives.
- Added a safe first-image decoder that turns one exact catalogued Cr6Ti/CRip007/CRip008 extent into a review PNG and path-redacted report without modifying the RIO.
- Added the 1,490-entry Photon locale-route authority and verifier, distinguishing 1,448 translation peers from 42 proven shared/common endpoints.
- Added fail-closed, reproducible Photon runtime builds and a hash-locked package assembler for already sealed roots; the clean-install-to-sealed-root pipeline remains incomplete.
- Documented rUGP investigations including AGES Internal Error 8311, RUO overlays, Cr6Ti, CRip007, CRip008, CRsa, fonts, and shared/common image routing.
- Preserved the ICI duplicate-size/outer-header metadata failure and the native/RUO/runtime image-transport failure chain as bounded postmortems rather than publishing data-specific repair probes.
- Replaced bulk Japanese AGE2 dialogue fields with source hashes while preserving stable context and Chinese work; added provenance reports and an open historical-Release alignment audit.
- Added explicit `text`/`structural_empty` AGE2 record kinds so five legal engine bookkeeping slots round-trip through the public exporter and are verified no-ops, plus a 246-identity text-free manual review ledger for symbol/quotation findings.
- Fixed the Imperial phase-one builder's previously unreachable installer path and made a valid font-license input mandatory when packaging its font.
- Added a strict local-source-to-EGPACK change builder, portable AGE2 text exporter, engine-neutral locale-template generator, font coverage audit, deterministic image authoring tools and tests.
- Added a read-only, synthetic-tested Steam depot-manifest content checker so AGE2 and rUGP builders can bind selected legal local inputs to a reviewed file/chunk map without publishing workstation paths.
- Added a strict 光子之花/光子旋律 Steam locale preflight with app-ID, dual-language-field and apply-time manifest-seal checks for future Photon installers; other rUGP games remain fail-closed.
- Added an exact machine-readable index for all five historical player ZIPs and the reviewed Photon image asset, including hashes, sizes, install roots and known safety limitations.
- Hardened public artifact writers, the Photon runtime builder, Imperial image routes and rUGP evidence exporters against partial output, overwrite races, path escape, target swaps, malformed identities and case-insensitive collisions.
- Removed the obsolete lossy Chinese-to-Japanese glyph substitution helper rather than presenting it as font support.
- Expanded Windows/Linux CI to run AGE2, rUGP and engine-neutral localization suites plus source compilation, repository-policy checks and pinned Zig runtime builds.
- Added a `docs/` audience hub and clarified the repository-vs-Release checksum names, file-size thresholds and sanitized historical-package caveats.
- Audited every public Release asset and synchronized the root guides, machine-readable index, and Release-page warnings: known-bad versions are visibly superseded, current historical packages are marked rights-remediation pending, and the Photon V6 asset is explicitly a non-installer research artifact.
- Replaced Imperial telop and event-card Japanese prose with exact source hashes and line-count evidence while retaining stable resource identities and localized copy.
- Made Photon package timestamps explicit, recorded the Python/NumPy/zlib build environment, and added CI smoke tests for every documented public CLI entry point.
- Hardened repository policy against force-added local/generated roots, binary payloads, symlinks, unsafe Release identifiers, hidden download links, workstation paths, and high-confidence credential patterns.
- Historical source-bearing Release tags and cached GitHub references still require separately authorized public-scope review; current source-tree cleanup does not establish their removal.

## 历史测试包 / Historical test packages

| Release | Notable scope |
| --- | --- |
| The Imperial Capital Burns beta0.1 | Dialogue, speakers, choices, system UI, image text, name/date/location cards, font and loose-overlay installer |
| TDA03 beta0.1.6 | Historical package with achievement-related fixes; superseded by the current BETA listed above |
| TDA02 beta0.1 | Dialogue, visible UI, subtitle/name images and font |
| TDA01 beta0.2.2 | Consolidated dialogue, terminology, image and display feedback fixes |
| TDA00 beta0.1 | JP-baseline workflow with speaker, ruby and XML-call-order auditing |

以上为历史测试包，不是当前下载列表。保留其版本身份、技术范围与已知分发问题，详见[历史包说明](../player/historical-age2.md)；这些历史问题不自动适用于后来的版本。

These entries are historical packages, not the current download list. Their identities and recorded distribution limitations remain documented in the [historical package guide](../player/historical-age2.md); those findings are not blanket claims about later releases.
