# Speaker colours: match Chinese names against the active style list

`千鶴` → `千鹤`, `純夏` → `纯夏` and `みちる` → `美知留` change the displayed name. The original engine matcher can then miss its Japanese alias and leave the name white. Translating the label does not automatically extend colour lookup.

## Use the current native style

Replacing a root default alias table did not establish that it became the active game's table. The runtime instead tries original matching first, then retries an exact reviewed Chinese name through its Japanese counterpart against the **current** native alias list. The native style entry supplies colour and effects; the hook does not rewrite the palette, dialogue, save data or style order, and does not grow the native 32-WCHAR alias storage.

Both pinned executables use a 217-byte UTF-16 matcher: displayed name in ECX, colon-separated aliases in EDX and boolean result in EAX.

| Game | Matcher RVA | CALL RVA | Original CALL bytes |
| --- | --- | --- | --- |
| PF | `0xB4E80` | `0xB4FEA` | `E8 91 FE FF FF` |
| PM | `0xB6B30` | `0xB6C8A` | `E8 A1 FE FF FF` |

The proxy verifies the host hash, instruction context and original target before replacing that CALL. Matcher SHA-256: `2C9D152FA5885E8EBD76CB6595D99DC1EA2FA2783FE29CD0E85EE5FDCBD4DF97`. Addresses are version-specific; see [runtime build options](../../runtime/README.md) for configuration and package identities.

## Rebind text repairs instead of overwriting whole records

Malformed `姓名【正文】` must be restored to `【姓名】「正文」`; a missing speaker wrapper must also be restored. Use `rebase_speaker_prefix_repairs.rebind_entries` against effective destination plaintext before `edit_native_fields`. It preserves current body wording and U+0003/U+000A decisions, rejects other drift, and treats already repaired fields as no-ops.

Do not copy an old complete RIO/RUO over newer layout work. PM later-volume edits retain the fixed-extent storage route. The known JP/EN speaker discrepancy is still separate from colour matching; see [source alignment](../../../docs/research/localization/source-alignment.md).

## Check both matches and non-matches

Run the original matcher with native aliases, reviewed Chinese aliases and a source name that has no matching style. Recognize numeric prefixes such as `3:` and `10:` without swallowing the actual name. Sample colour restoration has been confirmed in both games; it does not establish every old-save transition, backlog state or newly added name. Test these conditions when changing aliases or integrating a new build.
