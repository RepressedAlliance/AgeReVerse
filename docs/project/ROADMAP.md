# Roadmap

[Player downloads](../player/README.md) · [Localization guide](../../Localization-MakeGamesSpeak/README.md) · [Research index](../en/research-index.md)

TDA00–03, The Imperial Capital Burns, photonflowers* and photonmelodies♮ have
published Chinese player packages. Current versions and installation instructions
are maintained in the player guide. Kiminozo EE, optional community EER 1.0
compatibility and AEC+ are available in unified 1.0.0「再会」.

## Kiminozo

Text proofreading, localized UI/images and unified packaging are complete for
1.0.0. Continue runtime checks across routes, resolutions, old saves and language
changes, and address player feedback with exact scene/resource identities.
The [project entry](../../AGE2/games/kiminozo/README.md) records support and
publication scope. Full dialogue tables, private correspondence and internal
review attachments remain outside the public repository.

## Make the existing tools easier to reuse

- Complete the public AGE2 path from a lawful clean installation to the
  maintained text, images, fonts and game-specific overlay. Existing format
  tools and the Imperial phase-one builder do not reproduce every current package.
- Complete the corresponding Photon extraction, binding and staging steps.
  The package assembler accepts sealed input roots; it does not reconstruct
  every private production input from a clean game installation.
- Keep exact resource identities and compatibility information with each tool.
  Add examples for other languages when a team exercises the workflow and
  reports actual engine constraints.

## Improve the released patches

- Resolve the [AGE2](../../AGE2/docs/limitations.md) and
  [Photon](../../rUGP/docs/limitations.md) issues with affected game, version and
  scene information. Priorities include PF's intermittent English pages and
  untranslated embedded English in PM's *Rebirth* ending animation.
- Check unclear voice lines, ruby/emphasis, language switching, old saves and
  remaining image routes in their actual contexts. A fixed sample does not
  establish full-route coverage.
- Continue ParaTranz proofreading and synchronize accepted changes into
  maintained tables, then the relevant release. Online edits do not update
  already downloaded packages automatically.

## Fonts, images and distribution

- Maintain the seven-game image-font registers and credits as images change.
  The listed release images now have font or original/generated-lettering
  associations. Recover missing historical font-file identities and production
  inputs where possible; affected materials remain listed in the
  [font limitations](../../Localization-MakeGamesSpeak/Fonts-ThatFitTheGame/font-evidence.md).
  Register source, license, modifications, actual use and adoption with each new
  image or revision, following the
  [font guide](../../Localization-MakeGamesSpeak/Fonts-ThatFitTheGame/registration.md).
- Preserve the unresolved rights findings for the five **historical** AGE2
  test ZIPs: font notices and some copied official UI fallbacks. These findings
  apply to those recorded archives, not automatically to every later package.
- Remediate the Photon V6 **research image bundle**, which includes 19
  byte-identical official-source PNGs. Its source metadata remains useful,
  but that does not grant redistribution permission.
- Keep current download instructions, release manifests and known limitations
  synchronized. Historical package identities are retained separately in the
  [release index](../player/release-index.json).

## Keep useful technical experience accessible

Turn a resolved failure into a concise explanation of the trigger, cause,
solution, applicable versions and remaining limits, with a regression when it
protects a real behavior. Keep per-run commands, local captures, temporary
candidates and execution logs in ignored local storage.

Legacy source-bearing tags or cached GitHub references require separate
publication review. If removal is needed, preserve a recoverable private copy
and coordinate with GitHub Support where ordinary ref changes are insufficient.

Additional games enter the supported list only when their engine, source
authority, redistribution scope and maintenance owner are established.
