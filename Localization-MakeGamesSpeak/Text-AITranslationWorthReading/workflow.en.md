# Complete localization workflow: first translation to player feedback

[中文](workflow.md) · [Localization workspace](../README.md) ·
[Start a new language](new-locale.md) · [Asset map](../../docs/en/asset-map.md) ·
[Image workflow](../Images-MakeItLookNative/README.md) · [Ordered standards](README.md) ·
[Translation principles](../principles.md#english-summary)

This is the process developed while working on the TDA, The Imperial Capital
Burns, and Photon texts. Its core is not “ask an AI to translate a whole
spreadsheet.” Story comprehension, terminology, first translation, independent
review, engine binding, in-game QA, and player feedback are separate stages with
different evidence.

Text and image work share the [localization principles](../principles.md#english-summary).
Define the Chinese task by scene, information and function, then distinguish
meaning evidence, presentation, authoring base and delivery target. Japanese text,
audio, images and context establish original meaning. Normally author images
from suitable Japanese originals and use English design as a reference. If a
Chinese task needs an English-edition canvas, template or display mechanism,
identify the reused part, its purpose and the reason. An originally English
writeback slot does not select English artwork as the base or make English the
translation source.

Our usual comparison is **Japanese original / official English / Chinese candidate**.
Keep the English counterpart where available for alternative wording, scene
location, discrepancy checks and localization design. If meanings differ, verify
that the records represent the same content before checking the Japanese source.
English comparison is useful without being mandatory for every item. See the
[project examples](../principles.md#how-we-use-english-project-examples).

Translate Japanese into Chinese, preserve English present in the Japanese
original, and use English for Japanese only when it better serves the meaning
and context, with a recorded reason. Listening-based translation is a normal
input path, with no requirement for matching Japanese text or imagery. Another
edition's new display or medium may carry existing original content. Genuinely
added information or assistance needs confirmed provenance, Chinese purpose and
adopted scope; review its actual original language and function rather than
requiring nonexistent Japanese audio. Both listening passes check the actual
audio, not just a working transcript or English translation.

Comparing all locales does not require localizing both official resource sets.
One content item may have several actual targets; preserve each target's identity,
state and calls. Reference-only resources do not count toward production. Plan
Chinese use and feasible implementation before authoring, then verify actual
binding at delivery; the content need need not already be implemented in Chinese.
Chinese may replace English in rUGP's existing `translation` slot without a new
Chinese slot. Language suffixes do not exclude an actual Chinese target;
select the authoring base separately rather than inferring it from that slot.

After full inspection, content requiring localization must be fully Simplified
Chinese in actual glyphs, meaning, terminology and expression. Being understandable
to Chinese readers is insufficient. Under the [three unchanged-content cases](../principles.md#english-summary),
distinguish intentional Japanese retention, content already meeting Simplified
Chinese requirements, and explicitly adopted special conventions, region by region.
Real staff credits and song titles without verified official Chinese names may have
justified retention scopes. Approved Japanese weekday notation is a deliberate
convention, not ordinary compliant Chinese. These examples are not a closed whitelist.

Pass scope, reason and confirmation to independent review. Outside justified
retention, correct Traditional/Japanese glyphs, kana and Japanese terms or forms
of address; character conversion alone is not translation. For example, this
project's `軍曹` needs `中士`, not merely simplified `军曹`. Reassess old decisions
based only on readability, decoration or tool limits: known defects need repair,
uncertain cases need review. Reuse still-valid retention, without treating either
removal of every Japanese character or an old tool compromise as completion.

```text
lawful extraction; content/function inventory; source and target planning
        ↓
read the story; establish relationships and terminology
        ↓
first translation by complete scene
        ↓
independent review: keep / revise / question
        ↓
resolve questions; re-freeze terminology and cross-scene consistency
        ↓
AGE2 or rUGP binding, writeback, and automated validation
        ↓
in-game QA: initial full-route coverage, then affected-area regression
        ↓
maintainer's manual checks, corrections, and verification of fixes
        ↓
complete production and publish the test release
        ↓
post-release player reports and ParaTranz community proofreading
        ↓
return findings to maintained text/terminology/source and release again
```

Passing one stage never substitutes for the next. Fluent target text does not
prove the Japanese was understood; static decoding does not prove runtime
acceptance; a game launch does not prove complete text, image, and font coverage.

Start verification with the checks directly affected by the change. Reuse prior
results when their inputs, rules, and tools still apply. Expand or repeat checks
for relevant failures, new evidence, dependency changes, or explicit delivery
requirements; stop once the relevant checks pass and no issues remain. Do not
add repeated hashes, baseline rebuilds, smoke tests, backups, rollback rehearsals,
dry-runs, or acceptance tables merely for reassurance. Engine-required checks at
write and installation time still run at those operations.

## 0. Freeze lawful inputs and stable identities

1. Extract source data from a game copy you lawfully own.
2. Record the game/build, Steam App ID, resource path, object identity or offset,
   and SHA-256 of every relevant source.
3. Do not use an absolute workstation path or a mutable spreadsheet row number
   as the only identity.
4. A public table may retain the exact source-field hash without mirroring the
   complete official script. Other contributors re-extract locally and join by
   stable identity plus hash.
5. Keep AGE2 and rUGP extraction, writer, and runtime paths independent.
6. Link text, voice, images and edition differences by scene and function.
   Keep accurate official English correspondence and its comparison role where
   available. The [PM association question](../../docs/research/localization/source-alignment.md)
   shows why row order or similar wording alone cannot establish a match.
   Establish the Chinese information need before choosing assets. A missing
   same-form Japanese resource calls for checking other media; distinguish an
   uncertain correspondence from a confirmed addition.
7. Link meaning evidence, chosen presentation/base and intended targets through
   existing manifests or notes. Resource hashes establish identity/version, not
   semantic authority. Do not invent Japanese fields or a universal new table.

Output: content/function scope, lawful resource identities, meaning evidence,
presentation/base and target plan, scene order, and unresolved correspondence
or structural questions.

## 1. Understand the story and establish terminology first

Do not start with randomly sampled rows. Before bulk translation:

- read or listen to the current route/scene in order, with surrounding material
  and the image context needed to understand it;
- record character relationships, status differences, forms of address,
  speech habits, and current emotion;
- inventory names, organizations, ranks, machines, weapons, operations,
  locations, and recurring jokes;
- merge already established series terminology;
- put a new term into a candidate list instead of inventing a different answer
  every time it appears;
- mark uncertain story, speaker, address, or term decisions as `question`.

The glossary is a story-understanding tool established before the first pass,
not merely a cleanup table produced after translation.

Output: scene summary, relationship/address notes, frozen terminology baseline,
retention decisions and unresolved questions.

## 2. First translation: produce candidates

Translate complete scenes or natural story blocks in stable resource order.
Every maintained row should retain the equivalent of:

| Field | Purpose |
| --- | --- |
| `id` / `stable_id` | Identity that survives sorting and export |
| `resource_file` / `egpack` / `rio_file` | Route back to the game resource |
| `scene`, `speaker_jp` | Story and speaker context |
| source evidence and links | Preserve `source_text_sha256` for an actual source text field; link audio/image resources and segments/regions separately from working transcripts, without fabricated text fields or hashes |
| target text | First-pass candidate |
| status | `translated`, `question`, or `blocked` |

This pass aims for accurate source understanding and natural target-language
writing from the declared meaning evidence. It does not perform engine writeback.
For original content, English slots, old translations, OCR and machine output
cannot replace checking Japanese text/audio or source images. Record audio
locations and uncertainties for listening-based work. Confirmed additions use
their actual original language; assistance is identified and checked against
function. Referencing English segmentation, reusing a specifically needed English
canvas/template, or writing to an originally English target does not change the
evidence required to establish original meaning.

Compare official English as another interpretation that may suggest questions;
both translation and independent review still check Japanese text/audio directly.
For example, [AGE2 subtitles](../../AGE2/docs/postmortems/caption-layout.md) can use
the actual English-edition canvas and compare segmentation while translating
Japanese speech. The [unresolved TDA01 cheer ending](../../AGE2/docs/limitations.md)
remains a question pending relistening, not an English-based final line.

Output: candidate text, terminology additions, questions, batch range, and the
next stable starting point.

## 3. Second pass: independent review

The second pass is not target-language polishing. The reviewer rereads the
declared meaning evidence, context and character relationships: reread text,
relisten to audio and inspect source images, rather than merely accepting a
first-pass transcript. Review confirmed additions in their declared source
language and check functional instructions against actual behavior and purpose.
Presentation and delivery receive separate checks; similarity to an English
template does not decide meaning. The reviewer assigns exactly one result:

- `keep`: retain the candidate;
- `revise`: supply corrected text and the material reason;
- `question`: evidence remains insufficient; state what is needed.

Use another reviewer, another agent conversation, or at least a genuinely
independent pass when possible. Never default an entire batch to `keep`, and do
not make preference-only rewrites without source support. `revise` and
`question` are review results, not first-pass statuses.

Output: row-level decisions, before/after text, reasons, unresolved questions,
and review statistics.

## 4. Resolve questions and re-freeze terminology

A `question` must not silently disappear before packaging. Consult as needed:

- later scenes and other occurrences of the same expression;
- text/audio in the actual source language, speaker, expression, and staging;
- screenshots and the actual resource call site;
- official setting material or established series usage;
- control codes, locale slots, and image context.

After resolution, follow [07 change-impact review](07-change-impact.md)
to check related occurrences, update affected text and glossaries, and preserve
contextually justified differences. Missing Japanese meaning cannot be approved
by an English fallback. Identify meaning, edition correspondence, presentation
and implementation questions separately; a missing Japanese image does not by
itself mean the original meaning is unavailable.

## 5. Bind and write through the correct engine

Only semantically reviewed text enters the engine layer:

Check the chosen authoring base and actual target objects rather than inferring
the writeback language from the meaning source. Shared copy still needs each
target's dimensions, states and calls checked. Chinese may replace an existing
rUGP `translation` target or use a verified AGE2 `_en` path. Implement additional
presentation only through supported engine capabilities; do not invent slots.

- **AGE2:** extract required FPD members from a lawful `pack.bin`; build exact
  EGPACK changes; handle UI, WebP, and fonts; publish as a LocalAppData loose
  overlay.
- **rUGP:** locate CRsa, Cr6Ti, CRip, and related objects through ICI/RIO;
  select a proven static RUO route or an exact-build guarded runtime; verify
  capacity, parents, endpoints, and constraints such as error 8311.

Record input hash, output hash, tool version, and the fields permitted to change.
Extraction does not imply repacking, and one passing record does not prove every
record carrying the same class label.

## 6. Automated quality gates

A release candidate must be covered by the applicable checks below. For routine
edits, run affected checks and reuse still-applicable results for unchanged
parts. Source-build, tool, or shared-dependency changes expand the affected scope;
a local text edit does not require repeating the entire suite:

- stable IDs, row counts, duplicates, and missing records;
- source hashes against the frozen build;
- control codes, encoding, capacity, offsets, and parent references;
- terminology consistency and retired translations;
- font coverage across every maintained target string;
- image dimensions, mode, alpha, permitted changes, hashes and family layout
  against the selected base and target format;
- package members, destinations, and rollback information;
- absence of original containers, workstation paths, secrets, test images, and
  fonts without provenance.

Automated tests prove only their explicit assertions; they are not in-game
evidence.

## 7. In-game QA

When establishing coverage for a game, language, and resource implementation,
cover the title and settings screens, first dialogue, save/load, backlog, every
route and choice, speakers, achievements, fonts, each modified image family, and
rollback. Image QA must detect more than visibility: colour swaps, tearing,
alpha damage, wrong endpoints, English fallback, Japanese/translation route
differences, and shared/common behavior all matter.
For adopted or added Chinese presentation, verify readable and accurate
information, voice/subtitle correspondence, segmentation and display/clear
timing, and conflicts with dialogue or controls. Another edition's working
implementation does not replace these Chinese-edition checks.

For later local revisions, check the changed locations, necessary context, and
affected functions rather than replaying every route for a sentence edit. Game
build, writer, font, or shared-resource changes require broader relevant coverage.
Investigate an unclear impact scope and run full regression where needed. Record
existing coverage and why it remains applicable; missing checks are not passes.
Package build, installation, and uninstall checks still follow engine rules.

Each finding should identify game/build, route/date/scene, surrounding dialogue,
screenshot, stable resource ID, and exact reproduction steps.

## 8. Maintainer's final checks before release

The final production step is the maintainer's manual review and correction of
identified wording, terminology, missing text, layout, image text, and in-game
display problems. Verify the fixes and related impacts under 07, rerun affected writeback and checks, and then
publish the corresponding version. Player packages already include the manual
corrections completed for that release; they are not unreviewed AI drafts.
This does not claim complete professional Japanese-to-Chinese proofreading.
Record the actual coverage and unresolved issues for each version.

## 9. Post-release feedback and ParaTranz proofreading

ParaTranz primarily supports community proofreading and revisions after release,
separately from the maintainer's pre-release checks and corrections. Works in
progress may also open collaboration early. Accepted edits must be checked and
packaged for a later release; syncing them to GitHub does not update installed patches.

A player report is a third layer of real-environment evidence, not permission to
replace one generated file in a Release manually.

1. Confirm the game, patch version, locale selection, and other installed mods.
2. Use the screenshot, scene, and surrounding dialogue to find the stable ID.
3. Consult meaning evidence/terminology, chosen presentation/base or actual
   binding as appropriate to distinguish translation, design, font, image,
   installation and game-version problems.
4. Fix maintained source or code—not only a generated EGPACK, RIO, or WebP.
5. Follow 07 to synchronize affected occurrences and rerun relevant automated checks and scenes.
6. Document the fix and produce a new reproducible Release.

## 10. What becomes public

Publish:

- stable translation tables, glossaries, and durable review states;
- image copy, lawful textless/localized authorities or manifests, hashes, and
  production method;
- font source, license, coverage report, and reproducible build method;
- codecs, package tools, tests, incident reports, and reproducible commands.

Do not publish by default:

- original game containers or complete official resources;
- transient prompts, chat logs, failed batches, and personal notes;
- workstation paths, credentials, or fonts without explainable provenance;
- intermediate output that cannot reproduce or explain the final result.

Record an image-generation/edit request only when it materially affects a
reproducible visual result. Ordinary text translation does not require every
prompt; rules, maintained data state, and verification tools are more useful.

## 11. Apply the method to Korean, Russian, or another locale

Reuse the stages and identities, not Chinese prose conventions:

1. Re-extract lawful source and join it by the published hashes.
2. Create separate `ko`, `ru`, or other target files; never overwrite Japanese
   evidence or `zh-Hans` output.
3. Establish locale-specific terminology, address, punctuation, typography,
   line breaking, and font policy.
4. Complete both passes, question resolution, engine binding, in-game QA, and
   the maintainer's manual corrections before release, followed by community revisions.

Continue with the [new-locale guide](new-locale.md) and the
[asset map](../../docs/en/asset-map.md).
