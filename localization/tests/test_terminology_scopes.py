import csv
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from collections import Counter

from localization.tools.terminology import GAMES, MUV_LUV_GAMES, ROOT, candidate_terms, load_game, read_table


class TerminologyScopeTests(unittest.TestCase):
    def test_seven_games_explicitly_load_only_common_and_own_table(self):
        common = read_table(ROOT / "localization/glossaries/muv-luv.ja-zh-Hans.csv")
        for game, engine in MUV_LUV_GAMES.items():
            own = read_table(ROOT / "localization/glossaries" / f"{game}.ja-zh-Hans.csv")
            effective = load_game(game)
            self.assertEqual(set(effective), set(common) | set(own))
            self.assertNotIn("ァァ", effective)
            self.assertNotIn("ウチ", effective)
            self.assertNotIn("多分隊長", effective)
            self.assertFalse(any(r["cn"] == "轨道潜水员" for r in effective.values()))
        self.assertIn("ウィル", load_game("tda00"))
        self.assertNotIn("ウィル", load_game("photonflowers"))
        self.assertIn("ファング", load_game("imperial-capital-burns"))
        self.assertNotIn("ファング", load_game("tda00"))
        self.assertEqual(load_game("photonflowers")["ミキ"]["cn"], "壬姬")
        self.assertEqual(load_game("photonmelodies")["ピアティフ"]["cn"], "皮亚蒂芙")
        self.assertNotIn("ピアティフ", load_game("tda00"))
        self.assertEqual(load_game("photonmelodies")["武"]["cn"], "武")
        self.assertNotIn("量子電導脳", common)

    def test_longest_match_and_katakana_boundaries(self):
        glossary = load_game("tda00")
        self.assertFalse(candidate_terms("ウィルス", glossary))
        self.assertEqual([r["jp"] for r in candidate_terms("重レーザー級", glossary)], ["重レーザー級"])
        self.assertEqual([r["jp"] for r in candidate_terms("レーザー級", glossary)], ["レーザー級"])
        self.assertEqual([r["jp"] for r in candidate_terms("ウィル", glossary)], ["ウィル"])
        self.assertEqual(candidate_terms("anything", {}), [])

    def test_kiminozo_uses_own_terms_and_keeps_contextual_candidates_separate(self):
        own = read_table(ROOT / "localization/glossaries/kiminozo.ja-zh-Hans.csv")
        effective = load_game("kiminozo")
        self.assertEqual(set(effective), set(own))
        self.assertTrue(all(row['scope'] == 'kiminozo' for row in effective.values()))
        self.assertNotIn('レーザー級', effective)
        self.assertEqual(effective['竹尾タケオ']['cn'], '竹尾竹雄')
        self.assertEqual(effective['タケス']['cn'], '竹卡斯')
        self.assertEqual(effective['バトル・テッカ']['cn'], 'BattleTech')
        self.assertEqual(effective['ＳｍａｌｌＤｉｓｋ']['cn'], 'CD')
        with (ROOT / 'AGE2/games/kiminozo/terminology/baseline.ja-zh-Hans.csv').open(encoding='utf-8', newline='') as stream:
            rows = list(csv.DictReader(stream))
        self.assertEqual(len(rows), len({(row['source'], row['source_row']) for row in rows}))
        baseline = {row['jp']: row for row in rows if row['source'] != 'kiminozo-glossary-20261009'}
        confirmed = [row for row in rows if row['source'] == 'kiminozo-glossary-20261009']
        self.assertEqual(len(confirmed), len(own))
        for row in confirmed:
            term = list(own.values())[int(row['source_row']) - 2]
            self.assertEqual((row['jp'], row['cn'], row['basis']), (term['jp'], term['cn'], term['context']))
            self.assertEqual(row['status'], 'confirmed')
        self.assertEqual(baseline['名古屋打ち']['cn'], '小蜜蜂')
        self.assertEqual(baseline['名古屋打ち']['status'], 'question')
        self.assertEqual(baseline['女コス好きのニーソックスマニア']['cn'], '女COSER过膝袜的狂热爱好者')
        self.assertEqual(baseline['写ってます']['cn'], '一次性胶卷相机')
        self.assertEqual(baseline['ジオ・フロント']['cn'], '地底都市')
        self.assertEqual(baseline['ＳＤ']['cn'], 'CD')
        for jp in ('アルファ０１', 'チャーリー０１', 'ブラヴォー０１'):
            self.assertEqual(baseline[jp]['status'], 'candidate')
            self.assertNotIn(jp, effective)
        for row in rows:
            self.assertTrue(row['chapter'] and row['basis'] and row['source'] and row['source_row'])
            self.assertFalse(any(ord(c) < 32 for value in row.values() for c in value))

    def test_each_game_glossary_is_subset_of_its_baseline(self):
        for game, engine in GAMES.items():
            with self.subTest(game=game):
                own = read_table(ROOT / 'localization/glossaries' / f'{game}.ja-zh-Hans.csv')
                with (ROOT / engine / 'games' / game / 'terminology/baseline.ja-zh-Hans.csv').open(encoding='utf-8-sig', newline='') as stream:
                    baseline = {row['jp'] for row in csv.DictReader(stream)}
                self.assertFalse(set(own) - baseline, '本作术语必须全部保留在基线中')

    def test_every_input_row_has_one_disposition_and_old_bytes_are_preserved(self):
        audit = json.loads((ROOT / "docs/research/localization/terminology-history/scope-audit-20260908.json").read_text(encoding="utf-8"))
        for source in audit["sources"]:
            entries = [r for r in audit["records"] if r["source"] == source["name"]]
            self.assertEqual(len(entries), source["rows"])
            self.assertEqual({r["row"] for r in entries}, set(range(2, source["rows"] + 2)))
            self.assertTrue(all(r["state"] in ("scoped", "pending", "excluded") for r in entries))
        self.assertEqual(len(audit["records"]), 2568)
        self.assertEqual(dict(Counter(r["state"] for r in audit["records"])), audit["disposition_counts"])
        # This incomplete audit is retained as history, not a current-table oracle.
        self.assertEqual(audit['status'], 'withdrawn-incomplete-source-inventory')
        self.assertEqual(audit['superseded_by'], 'recovery-20260908.json')
        for source, filename in [("mixed", "mixed-20260908.csv"), ("imperial", "imperial-20260908.csv")]:
            raw = (ROOT / "docs/research/localization/terminology-history" / filename).read_bytes()
            expected = next(s for s in audit["sources"] if s["name"] == source)
            self.assertEqual(hashlib.sha256(raw).hexdigest(), expected["sha256"])
            records = list(csv.DictReader(raw.decode("utf-8-sig").splitlines()))
            entries = [r for r in audit["records"] if r["source"] == source]
            self.assertEqual([(r["jp"],r["cn"]) for r in records], [(r["jp"],r["cn"]) for r in entries])

    def test_no_duplicate_empty_or_control_bearing_terms(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "terms.csv"
            for content in ["jp,cn,context\n詞,词,test\n詞,词,test\n",
                            "jp,cn,context\n詞,,test\n",
                            "jp,cn,context\n詞,词,test\x03\n"]:
                path.write_text(content, encoding="utf-8")
                with self.assertRaises(ValueError):
                    read_table(path)


if __name__ == "__main__":
    unittest.main()
