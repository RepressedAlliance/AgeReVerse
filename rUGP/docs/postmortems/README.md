# rUGP 技术案例：理解格式，也理解游戏怎样使用它

These guides explain reusable format and runtime behavior for the pinned Photon builds. Start with [support limits](../limitations.md) when applying them to another version or building a player package.

## Text and storage

| Guide | What you can learn |
| --- | --- |
| [CRsa text](crsa-text.md) | Direct CString and VM text-pool storage, control units and read-only extraction |
| [Native fields](crsa-fields.md) | Bodies, annotations, instructions, call parameters and stable identities |
| [Native writeback](crsa-writeback.md) | Rebinding, pool capacity, PF cumulative RUO and PM fixed-volume staging |
| [Error 8311](error-8311.md) | Why embedded NUL padding breaks a counted CString |
| [Backlog Return to Game](backlog-return-action-20260910.md) | Engine action identifiers must retain their registered names |
| [Special monologues](pm-special-text-20260911.md) | A control byte and its argument form one display directive |

## Images and runtime

| Guide | What you can learn |
| --- | --- |
| [Cr6Ti](cr6ti.md), [CRip007](crip007.md), [CRip008](crip008.md) | Record extent, codec profiles, alpha and independent decoding |
| [RUO](ruo-overlay.md) / [ICI growth](ici-resize-metadata.md) | Redirects, cumulative footers, duplicate lengths and wrapper metadata |
| [Shared/common images](shared-common-images.md) | Proving a shared endpoint without guessing a locale fallback |
| [Image transport](image-transport-runtime.md) | Parent selection, state geometry, timer layers and guarded runtime routes |
| [Runtime validation](runtime-validation.md) | Production transactions, partial rectangles, padded lengths and final delivery tables |
| [Scene entry points](pending-hook-entry-points-20260909.md) | Static references, prefetch, unlock conditions and unobserved calls |
| [PM Album selector](pm-album-selector-20260909.md) | Revoke stale object authority when metadata changes |
| [PF festival presentation](pf-festival-presentation-20260909.md) | A translated thumbnail does not exercise a full or partial animated frame |
| [PM image admission](pm-image-admission-20260909.md) | Keep installed hooks and the production admission contract consistent |
| [Player image index](player-image-index-20260910.md) | A binary-search table must be sorted in the final package |
| [CRmt family](../crmt-family.md) | Parent/mip/CRimp layers, tagged integers and cross-locale geometry |

## Typography and translation

| Guide | What you can learn |
| --- | --- |
| [Font runtime](font-runtime.md) | Private font family, GDI selection and exact-build proxy loading |
| [Missing glyphs](pf-font-coverage-20260914.md) / [PM metrics](pm-er-20260909.md) | Include annotations and menu glyphs, preserve font metrics, ship matching DLLs |
| [Chinese layout](pf-pm-layout-audit-20260906.md) | Semantic line breaks and rebinding without overwriting later corrections |
| [Speaker colours](speaker-colors-20260906.md) | Chinese aliases and the engine's active style lookup |
| [Foreign-language expressions](pf-pm-latin-review-20260909.md) | Translate terms while retaining dialogue voice, abbreviations and wordplay |
| [Terminology choices](terminology-20260908.md) | Resolve context before applying a glossary match |

For tool usage, use the [tool index](../../tools/README.md). For prior work and attribution, use [technical references](../../../docs/research/README.md). Build checks, a structurally valid resource and an actual scene observation answer different questions; each guide states the behavior it covers.
