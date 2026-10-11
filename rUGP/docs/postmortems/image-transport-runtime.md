# Photon images: why a correct bitmap can still fail in game

## Locate the layer responsible

| Symptom | Investigate |
| --- | --- |
| Japanese or English remains | Selected image language, locale endpoint and parent reference |
| Blank label or white screen | Serialized extent, parent ownership, ICI/RUO transport |
| Wrong colours or stripes | Codec profile, integer semantics, alpha and guarded tail |
| One state changes, others do not | Multi-state bank geometry and partial rectangles |
| Replacement reverts or tears | Redecode order, surface lifetime and stale write authority |

A source and its translation peer may have different geometry. Multiple logical sources may alias one physical target. A decoder accepting a larger record does not authorize overwriting the following object.

## Watermelon tutorial: counters are not complete frames

PM's tutorial uses eleven dynamic counter payloads and twelve logical complete frames, with two frames sharing one physical payload. Correct counter replacement therefore leaves the complete-frame label unchanged. The official Translation-field bitmap itself can still contain Japanese; visible language alone does not identify the selected slot.

Build complete-frame sidecars from their authenticated Translation payloads. Change only the timer band, preserving unrelated pixels and the dimmed `SOUND ONLY` state. The zero-second cue crosses the longer Chinese label: a broad yellow colour key copies shadows, while a simple visible-pixel copy leaves gaps. Repair the old cue fragments using the matching 300-second background, restore the Chinese glyph pixels, then render one closed 4px ellipse at 8× supersampling without text overlap.

The image-language setter also requires the correct parent-stack identity. For the pinned PM build, command `0x237` uses parent RVAs `0x43132`, `0x42409`, `0x122EB8` and `0x12D327`. Loading a saved tutorial can omit a setter action. The selector can establish Translation from an authenticated complete-frame payload only while language is unknown and no surface/write lease is active; Japanese payloads do not authorize localized writes.

See the [tutorial route table](../../evidence/photon/images/pm-watermelon-timer-runtime-routes-20260904.json) for exact logical and physical identities. The corrected tutorial was observed through its zero-second explanation, choice and live minigame; this does not establish every dynamic image route.

## Choose transport per authenticated endpoint

1. Use an exact native record when format, geometry and available extent are supported.
2. Use one cumulative RUO when the complete redirected record and reference graph are supported.
3. Rebuild an authenticated parent when a growing child requires it and that parent writer is available.
4. Use the exact-build runtime for decoded surfaces or font behavior that archive replacement cannot safely represent.
5. Leave unsupported endpoints explicit rather than guessing a fallback.

The hook is version- and identity-gated. Treat source image, localized image, encoded record, logical endpoint, physical target and runtime observation separately. One visual state does not authorize sibling states. Compare actual caller extent and draw rectangle, and check the final delivery table after packaging; see [runtime validation](runtime-validation.md).

The baseline [route catalog](../../evidence/photon/routes/README.md) classifies 1,490 logical image routes. It does not supply every clean-install-to-runtime transport or replace whole-game visual checks. Known unresolved entries and component limits remain in [support scope](../limitations.md).
