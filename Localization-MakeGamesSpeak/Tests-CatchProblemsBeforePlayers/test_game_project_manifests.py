from __future__ import annotations

import tomllib
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
EXPECTED = {
    "AGE2": {
        "imperial-capital-burns",
        "kiminozo",
        "tda00",
        "tda01",
        "tda02",
        "tda03",
    },
    "rUGP": {"photonflowers", "photonmelodies"},
}


class GameProjectManifestTests(unittest.TestCase):
    def test_every_supported_game_has_a_valid_manifest(self) -> None:
        for engine, expected_games in EXPECTED.items():
            games_root = ROOT / engine / "games"
            actual_games = {
                path.parent.name for path in games_root.glob("*/project.toml")
            }
            self.assertEqual(actual_games, expected_games)

            for game_id in sorted(expected_games):
                manifest_path = games_root / game_id / "project.toml"
                with manifest_path.open("rb") as stream:
                    manifest = tomllib.load(stream)

                self.assertEqual(manifest["schema_version"], 1)
                self.assertEqual(manifest["game_id"], game_id)
                self.assertEqual(manifest["engine"], engine)
                self.assertIsInstance(manifest["steam_app_id"], int)
                self.assertEqual(manifest["target_locales"], ["zh-Hans"])
                relative_paths = list(manifest["translation_authorities"])
                if game_id == "kiminozo":
                    self.assertEqual(manifest["development_status"], "in-development")
                    self.assertEqual(manifest["translation_authorities"], [])
                    self.assertNotIn("player_release_tag", manifest)
                    self.assertNotIn("image_authority", manifest)
                    self.assertEqual(manifest["steam_app_id"], 1777440)
                    self.assertEqual(manifest["components"]["main"]["resource_root"], "kiminozs")
                    self.assertEqual(manifest["components"]["additional"]["resource_root"], "kiminoaz")
                    self.assertEqual(manifest["components"]["additional"]["steam_app_id"], 3112140)
                    relative_paths.extend([
                        "README.md", "translations/README.md",
                        "terminology/README.md", "images/README.md",
                    ])
                else:
                    self.assertTrue(manifest["translation_authorities"])
                    relative_paths.append(manifest["image_authority"])
                relative_paths.append(manifest["font_policy"])
                for optional_key in ("terminology_authority", "terminology_common_authority", "terminology_baseline", "terminology_evidence", "image_copy_authority"):
                    if optional_key in manifest:
                        relative_paths.append(manifest[optional_key])

                for relative_path in relative_paths:
                    target = manifest_path.parent / relative_path
                    self.assertTrue(
                        target.is_file(),
                        f"{manifest_path}: missing referenced file {relative_path}",
                    )


if __name__ == "__main__":
    unittest.main()
