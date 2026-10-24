<p align="right">
  <a href="../../README.md"><img alt="简体中文" src="https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-%E9%98%85%E8%AF%BB-C62828?style=for-the-badge"></a>
  <a href="README.md"><img alt="English" src="https://img.shields.io/badge/English-Current-2F81F7?style=for-the-badge"></a>
</p>

# âge Games Chinese Localization Project

**AgeReVerse · RepressedAlliance / 压抑同盟**

Steam Simplified Chinese patches for Muv-Luv UNLIMITED: The Day After (TDA00–03), The Imperial Capital Burns, Muv-Luv photonflowers* (PF), and Muv-Luv photonmelodies♮ (PM). Kimi ga Nozomu Eien: Enhanced Edition (Kiminozo), optional community EER 1.0 compatibility and Another Episode Collection+ are available in unified 1.0.0「再会」.

Reverse engineering, tooling, and Chinese localization for âge games.

This is an unofficial, non-commercial localization project for selected Steam
Muv-Luv titles. It preserves Simplified Chinese test patches and publishes the
translation, terminology, image, font, format-tooling, and reverse-engineering
work needed by other language teams.

You must own the matching game. This repository does not provide the games,
cracks, complete original assets, or an original Steam `pack.bin`.

## Choose one entry

| **Players** | **Localizers and researchers** |
| --- | --- |
| **[Download, install, restore, and troubleshoot](player-guide.md)** | **[Texts, images, fonts, tools, and research](research-index.md)** |
| Only the package status, links, and safety information players need. | The asset map, multilingual workflow, AGE2, rUGP, and incident records. |

## Current status

| Scope | Player status | Public production/research material |
| --- | --- | --- |
| TDA00–03 and The Imperial Capital Burns | Current BETA installers published on 2026-09-20; see the [player guide](player-guide.md) for per-game versions and installation | Maintained text, inventories for 730 historical WebP paths, Imperial image copy, FPD/EGPACK tools, and loose-overlay findings |
| 光子之花 / Muv-Luv photonflowers* (PF) and 光子旋律 / Muv-Luv photonmelodies♮ (PM) | **BETA 0.1.2** ordinary releases, separate installers; see the [player guide](player-guide.md) | Maintained text, a 1,490-image PF/PM authority and route map, ICI/RIO/CRsa/RUO/Cr6Ti/CRip tools, guarded runtime components, and postmortems |
| Kimi ga Nozomu Eien: Enhanced Edition and Another Episode Collection+ | **[1.0.0「再会」](https://github.com/RepressedAlliance/AgeReVerse/releases/tag/kiminozo-1.0.0)** | [Project structure, text review, terminology and UI/image work](../../AGE2/games/kiminozo/README.md) |

Use the current packages linked in the [player guide](player-guide.md).
Older AGE2 packages and their limitations are retained as historical records. The 1,490-image Photon Release is a research and
localization asset, not an installer.

## Repository map

| Directory | Responsibility |
| --- | --- |
| **[Game Localization — Make Games Speak Your Language](../../Localization-MakeGamesSpeak/README.md)** | Practical text, image, typography, consistency and community-proofreading guides, plus reusable tools and their tests |
| [`AGE2/`](../../AGE2/README.md) | TDA/Imperial game-bound text and image identities, plus the released Kiminozo EE / optional EER / AEC+ project, FPD, EGPACK, WebP, loose overlays, tests, and postmortems |
| [`rUGP/`](../../rUGP/README.md) | Photon game-bound text and image identities, ICI, RIO, CRsa, RUO, Cr6Ti, CRip, runtime, and postmortems |
| [`docs/`](../README.md) | Player, research, maintenance, legal, and English documentation |

See the **[text, terminology, image, and font asset map](asset-map.md)** for
actual counts and placement rules. Engine-neutral methods live in
`Localization-MakeGamesSpeak/`; anything bound to a game resource ID, locale slot, path, or
codec lives under that game's `AGE2/games/` or `rUGP/games/` directory. Complete
official source assets are extracted locally from a contributor's lawful copy
and are never committed.

## Localization workflow

Kiminozo primarily carries forward Muzhi's human LE translation. AI-assisted
corrections to that legacy text were reviewed and revised by Muzhi. Only the
limited new/adjusted material uses the GPT-6 Sol / GPT-6 Astra translation and
independent-review workflow, followed by Muzhi's full human proofreading of that
material. The other seven patches primarily use AI-first translation and review,
with the maintainer's human decisions and subsequent community corrections;
separately supplied human translations are credited where applicable.

For text requiring an AI-first translation, the maintained process is: establish story context and terminology; produce a
first translation; independently classify every row as
`keep`/`revise`/`question`; resolve questions; bind through the correct engine;
run in-game QA; and feed player reports back into maintained source.

- [Complete English workflow](../../Localization-MakeGamesSpeak/Text-AITranslationWorthReading/workflow.en.md)
- [Start Korean, Russian, or another locale](../../Localization-MakeGamesSpeak/Text-AITranslationWorthReading/new-locale.md)
- [Localized image and Image 2 workflow](../../Localization-MakeGamesSpeak/Images-MakeItLookNative/tools.md)
- [Chinese workflow](../../Localization-MakeGamesSpeak/Text-AITranslationWorthReading/workflow.md)

## Credits and participation

The project warmly thanks 主任保护协会 for the loose-file resource overlay method
that started our localization journey. Subsequent extraction, translation, tool development
and patch production are our own work, with specific references documented separately.
GARbro, AFHook/AFEditor, rugptools, alterdec, RioX,
FatePackageManager, and mature patch projects supplied narrowly attributed
technical precedents. See [contributors and acknowledgments](../project/CONTRIBUTORS.md)
and the [reference comparison](../research/references.md).

[Report a patch/runtime problem](https://github.com/RepressedAlliance/AgeReVerse/issues/new?template=bug-report.yml)
· [Suggest a translation correction](https://github.com/RepressedAlliance/AgeReVerse/issues/new?template=translation-review.yml)
· [Contribute](../project/CONTRIBUTING.md)

Human proofreading and feedback credits include ScRm, 骁飞, Tsubaki-G, 柚子コショウ and 子冰; ParaTranz records also credit ScRemilia and X1AOFEI. 红桃皇后假说 provided part of the text for *Before the Cherry Blossoms Bloom*, and 木之 provided the Kiminozo LE translation, reviewed legacy-translation corrections and proofread the new/adjusted text; 压抑同盟 handled revision, porting, localized images and coordination; Muv-Luv Verse Team, Lemonov and TotSamiyMisha created the optional community EER Patch. Kiminozo testing and feedback: 垃圾站麻婆 and 一般路过咖喱. See the [contributor list](../project/CONTRIBUTORS.md) for scope and sources.

Original code is under the [MIT License](../../LICENSE). MIT does not
automatically license game content, translation text, fonts, derivative images,
release packages, or third-party components. See the
[asset and release policy](../project/asset-and-release-policy.md),
[third-party notices](../legal/THIRD_PARTY.md), and [legal notice](../legal/NOTICE.md).
