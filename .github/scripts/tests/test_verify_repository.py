from __future__ import annotations

import importlib.util
import copy
from pathlib import Path
import unittest
from tempfile import TemporaryDirectory


SCRIPT = Path(__file__).resolve().parents[1] / "verify_repository.py"
SPEC = importlib.util.spec_from_file_location("verify_repository", SCRIPT)
if SPEC is None or SPEC.loader is None:  # pragma: no cover - import machinery failure
    raise RuntimeError("could not load repository verifier")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class RepositoryPolicyHelperTests(unittest.TestCase):
    def current_release_example(self):
        packages = [
            {"game_id": "tda00", "version": "BETA 8.2.3", "release_tag": "tda00-BETA-8.2.3", "asset_name": "TDA00.zip"},
            {"game_id": "pm", "version": "1.0.0", "release_tag": "pm-1.0.0", "asset_name": "PM.zip"},
        ]
        for package in packages:
            package['asset_url'] = f"https://github.com/RepressedAlliance/AgeReVerse/releases/download/{package['release_tag']}/{package['asset_name']}"
        document = {"age2_player_packages": packages[:1], "photon_player_packages": packages[1:]}
        rows = [f"| {p['game_id']} | **{p['version']}** | [download]({p['asset_url']}) · [notes](https://github.com/RepressedAlliance/AgeReVerse/releases/tag/{p['release_tag']}) |" for p in packages]
        table = "| Game | Version | Download |\n| --- | --- | --- |\n" + '\n'.join(rows)
        return document, table

    def current_errors(self, document, table, name='README.md'):
        errors = []
        MODULE.check_current_player_releases(document, {name: table}, errors)
        return errors

    def test_current_releases_accept_future_beta_and_stable_versions(self):
        document, table = self.current_release_example()
        self.assertEqual(self.current_errors(document, table), [])

    def test_current_releases_allow_another_game_when_index_and_guides_agree(self):
        document, table = self.current_release_example()
        package = {"game_id": "another-game", "version": "2.0.0", "release_tag": "another-game-2.0.0", "asset_name": "Another.zip", "asset_url": "https://github.com/RepressedAlliance/AgeReVerse/releases/download/another-game-2.0.0/Another.zip"}
        document['age2_player_packages'].append(package)
        table += f"\n| Another | 2.0.0 | [download]({package['asset_url']}) · [notes](https://github.com/RepressedAlliance/AgeReVerse/releases/tag/another-game-2.0.0) |"
        self.assertEqual(self.current_errors(document, table), [])

    def test_current_release_checks_detect_one_guide_left_on_an_old_version(self):
        document, table = self.current_release_example()
        self.assertTrue(any('version is' in e for e in self.current_errors(document, table.replace('**BETA 8.2.3**', '**BETA 8.2.2**'))))

    def test_current_release_checks_detect_wrong_download_or_missing_notes(self):
        document, table = self.current_release_example()
        for edited in (table.replace('/TDA00.zip)', '/wrong.zip)'), table.replace('[notes](https://github.com/RepressedAlliance/AgeReVerse/releases/tag/tda00-BETA-8.2.3)', 'notes')):
            with self.subTest(edited=edited):
                self.assertTrue(any('matching visible' in e for e in self.current_errors(document, edited)))

    def test_current_release_checks_detect_missing_or_duplicate_rows(self):
        document, table = self.current_release_example()
        lines = table.splitlines()
        self.assertTrue(any('missing current row' in e for e in self.current_errors(document, '\n'.join(lines[:-1]))))
        self.assertTrue(any('duplicate current row' in e for e in self.current_errors(document, table + '\n' + lines[-1])))

    def test_current_release_checks_detect_unindexed_or_mixed_release_tags(self):
        document, table = self.current_release_example()
        extra = '| other | 2.0.0 | [notes](https://github.com/RepressedAlliance/AgeReVerse/releases/tag/other-2.0.0) |'
        self.assertTrue(any('not in the release index' in e for e in self.current_errors(document, table + '\n' + extra)))
        mixed = table.replace('/releases/tag/tda00-BETA-8.2.3)', '/releases/tag/tda00-BETA-8.2.4)')
        self.assertTrue(any('mixes release tags' in e for e in self.current_errors(document, mixed)))

    def test_current_release_checks_do_not_accept_hidden_table_rows(self):
        document, table = self.current_release_example()
        for hidden in ('<!--\n' + table + '\n-->', '```markdown\n' + table + '\n```'):
            with self.subTest(hidden=hidden):
                self.assertTrue(any('missing current row' in e for e in self.current_errors(document, hidden)))

    def test_current_release_index_rejects_duplicate_identity_and_bad_asset_url(self):
        document, table = self.current_release_example()
        for change in ('duplicate', 'bad_url', 'bad_tag', 'empty', 'non_object', 'missing_field'):
            edited = copy.deepcopy(document)
            if change == 'duplicate':
                edited['age2_player_packages'].append(copy.deepcopy(edited['age2_player_packages'][0]))
            elif change == 'bad_url':
                edited['age2_player_packages'][0]['asset_url'] = 'https://example.invalid/wrong.zip'
            elif change == 'bad_tag':
                edited['age2_player_packages'][0]['release_tag'] = '../escape'
            elif change == 'empty':
                edited['photon_player_packages'] = []
            elif change == 'non_object':
                edited['photon_player_packages'] = [None]
            else:
                del edited['photon_player_packages'][0]['version']
            with self.subTest(change=change):
                self.assertTrue(self.current_errors(edited, table))

    def test_current_release_checks_allow_historical_rows_and_notes_only_changelog(self):
        document, table = self.current_release_example()
        document['player_packages'] = [{'release_tag': 'tda00-beta0.1'}]
        historical = '| TDA00 | beta0.1 | [old](https://github.com/RepressedAlliance/AgeReVerse/releases/tag/tda00-beta0.1) |'
        self.assertEqual(self.current_errors(document, table + '\n' + historical), [])
        for package in document['age2_player_packages'] + document['photon_player_packages']:
            table = table.replace(f"[download]({package['asset_url']})", '')
        self.assertEqual(self.current_errors(document, table, name='docs/project/CHANGELOG.md'), [])
        self.assertTrue(self.current_errors(document, table))

    def test_private_review_and_quarantine_cannot_be_published(self):
        self.assertTrue(MODULE.is_private_review_csv('binding_id,jp_text,en_text,base_edit_sha256\n'))
        self.assertTrue(MODULE.is_private_review_csv('"en_text","jp_text","base_edit_sha256"\n'))
        self.assertFalse(MODULE.is_private_review_csv('binding_id,translated_text,jp_utf8_sha256,en_utf8_sha256\n'))
        self.assertTrue(MODULE.is_forbidden_public_path('.codex-trash/example/receipt.json'))

    def test_html_language_button_targets_are_visible_to_link_checks(self) -> None:
        text = '<a href="docs/en/README.md"><img src="https://example.invalid/badge.svg"></a>'
        self.assertEqual(MODULE.HTML_HREF.findall(text), ["docs/en/README.md"])

    def test_only_visible_markdown_links_count_as_release_links(self) -> None:
        visible = "[download](https://example.invalid/patch.zip)"
        hidden = (
            "<!-- [hidden](https://example.invalid/comment.zip) -->\n"
            "```markdown\n[code](https://example.invalid/code.zip)\n```\n"
            "`[inline](https://example.invalid/inline.zip)`"
        )
        self.assertEqual(
            MODULE.markdown_link_targets(visible + "\n" + hidden),
            {"https://example.invalid/patch.zip"},
        )

    def test_release_components_cannot_escape_the_expected_url(self) -> None:
        for value in ("../other", "owner/release", ".", "tag with spaces"):
            with self.subTest(value=value):
                self.assertIsNone(MODULE.SAFE_RELEASE_TAG.fullmatch(value))
        self.assertIsNotNone(MODULE.SAFE_RELEASE_TAG.fullmatch("tda01-beta0.2.2"))
        self.assertIsNotNone(
            MODULE.SAFE_RELEASE_COMPONENT.fullmatch("MuvLuv_TDA01_Patch.zip")
        )

    def test_public_tree_is_text_allowlisted_not_binary_blacklisted(self) -> None:
        for name in (
            "payload.bin",
            "runtime.so",
            "video.mp4",
            "font.woff2",
            "database.sqlite",
            ".env",
            "id_rsa",
        ):
            with self.subTest(name=name):
                self.assertFalse(MODULE.is_allowed_public_path(Path(name)))
        for name in ("tool.py", "hook.js", "test_hook.cjs", "table.csv", "README.md", ".gitignore", "LICENSE"):
            with self.subTest(name=name):
                self.assertTrue(MODULE.is_allowed_public_path(Path(name)))

    def test_generated_and_private_roots_stay_forbidden_when_force_added(self) -> None:
        for relative in (
            "outputs/leak.json",
            "output/report.txt",
            "archive/source.csv",
            "local-internal/handoff.md",
            "release_v9/package.txt",
            "workspace_full_copy_1/data.json",
        ):
            with self.subTest(relative=relative):
                self.assertTrue(MODULE.is_forbidden_public_path(relative))
        self.assertFalse(MODULE.is_forbidden_public_path("rUGP/tools/README.md"))

    def test_only_selected_player_screenshots_are_allowed(self) -> None:
        for relative in MODULE.APPROVED_PLAYER_SCREENSHOTS:
            self.assertTrue(MODULE.is_allowed_public_path(Path(relative)))
            self.assertTrue(MODULE.is_allowed_public_path(MODULE.ROOT / relative))
        for relative in (
            "docs/player/screenshots/tda00/unreviewed.jpg",
            "docs/player/screenshots/tda00/title.png",
            "rUGP/games/photonflowers/images/dialogue.jpg",
            "screenshots/tda00/title.jpg",
            "docs/player/screenshots/tda00/../tda00/title.jpg",
        ):
            with self.subTest(relative=relative):
                self.assertFalse(MODULE.is_allowed_public_path(Path(relative)))

    def test_screenshot_exception_rejects_other_formats_and_invalid_bytes(self) -> None:
        from PIL import Image

        with TemporaryDirectory() as directory:
            path = Path(directory) / "title.jpg"
            for format_name in ("JPEG", "PNG"):
                Image.new("RGB", (640, 360)).save(path, format=format_name)
                errors = []
                MODULE.check_player_screenshot(path, "title.jpg", errors)
                self.assertEqual(bool(errors), format_name != "JPEG")
            path.write_bytes(b"not an image")
            errors = []
            MODULE.check_player_screenshot(path, "title.jpg", errors)
            self.assertTrue(errors)

    def test_screenshot_exception_rejects_oversized_files_and_dimensions(self) -> None:
        from PIL import Image

        with TemporaryDirectory() as directory:
            path = Path(directory) / "title.jpg"
            Image.new("RGB", (1, 1)).save(path, format="JPEG")
            errors = []
            MODULE.check_player_screenshot(path, "title.jpg", errors)
            self.assertTrue(errors)
            path.write_bytes(b"x" * (1024 * 1024 + 1))
            errors = []
            MODULE.check_player_screenshot(path, "title.jpg", errors)
            self.assertTrue(errors)

    def test_high_confidence_secret_markers_are_detected(self) -> None:
        samples = {
            "private-key material": "-----BEGIN " + "PRIVATE KEY-----",
            "GitHub token": "gh" + "p_" + "A" * 40,
            "GitHub fine-grained token": "github_" + "pat_" + "A" * 50,
            "AWS access key": "AK" + "IA" + "A" * 16,
            "OpenAI-style API key": "s" + "k-" + "A" * 30,
        }
        for expected, sample in samples.items():
            with self.subTest(expected=expected):
                self.assertIn(expected, MODULE.secret_marker_labels(sample))
        self.assertEqual(MODULE.secret_marker_labels("ordinary documentation"), [])


if __name__ == "__main__":
    unittest.main()
