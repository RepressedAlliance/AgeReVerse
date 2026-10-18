# Release process

This checklist governs new releases. Historical AGE2 packages remain recorded separately from the 2026-09-20 BETA installers; use the current download table and each release's manifest and validation scope in the [player guide](../player/README.md).

## 1. Freeze inputs

- Record the game, Steam build/depot identity where available, and SHA-256 of every modified source file. A separately obtained clear-name depot manifest may be checked with [`verify_steam_depot_manifest.py`](../research/localization/tools/verify_steam_depot_manifest.py); the result proves content-map agreement, not Steam-signature authenticity.
- Freeze canonical translation/image manifests and the source commit.
- Build in a fresh staging directory; never package a live game directory directly.

## 2. Build and verify

- Run the AGE2, rUGP, and engine-neutral localization test suites plus repository hygiene checks.
- Run the engine-specific builder with all version gates enabled.
- Rebuild in a second clean directory and compare normalized outputs.
- Verify every archive member against the generated manifest.

## 3. Audit contents

- Reject absolute local paths, credentials, logs, debug symbols, caches, original complete archives, and unapproved candidates.
- Confirm font licenses and third-party notices travel with their binaries.
- Confirm the installer touches only the named game and that restoration is documented.
- For 光子之花/光子旋律, require the confirmed Steam locale/app-ID preflight and revalidate its in-memory manifest seal immediately before the first write; a saved report alone is not authorization.

## 4. Publish

- Use a game-specific tag; do not use one Photon game's approval to publish the other.
- Attach the player package, SHA-256 list, support matrix, known limitations, and source commit.
- Update the matching current section of [`release-index.json`](../player/release-index.json): `age2_player_packages` for AGE2 or `photon_player_packages` for Photon. Record the new version, tag, immutable asset name/URL, size, SHA-256, install roots and actual limitations. Keep `player_packages` for historical AGE2 identities; do not insert a new current release there.
- Update the root download table, both player guides, the current-package table in the changelog and the game project's release reference. Run `python .github/scripts/verify_repository.py`; it checks current versions and links against the index without pinning them to old version numbers.
- Use the Chinese community name followed by the full Steam title in the Release title and identify the matching Steam app in the notes. The repository About link should lead to the player download table, rather than the mixed Release list.
- Keep the Git tree free of the generated ZIP/DLL/archive.

## 5. Post-release

- Install the downloaded asset, not the local staging copy, onto a clean supported game.
- Record full-route testing and triage feedback by game/version/resource identity.
- Preserve superseded releases for provenance unless they expose unsafe or unauthorized material; mark them obsolete rather than silently replacing bytes under the same tag.


## 更新版本信息 / Keeping release information in sync

发布新版本时，在 `age2_player_packages` 或 `photon_player_packages` 更新当前条目，再同步首页、中文／英文玩家指南、变更记录的当前版本表和游戏项目的发布引用。`player_packages` 保存历史 AGE2 测试包，不用于登记新下载。

运行 `python .github/scripts/verify_repository.py` 检查当前版本号、附件链接和发布说明链接是否一致。检查不固定旧版本号，不要求未来包复用历史文件摘要。Release 标题采用“中文圈常用名或简称｜完整 Steam 名称｜汉化补丁版本”，正文标明适用的 Steam 作品；侧栏下载入口指向首页下载表。
