import csv
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from collections import Counter

from importlib import import_module
_localization_terminology = import_module('localization-make-games-speak.tools-let-tools-handle-repetition.terminology')
BASELINE_COLUMNS = _localization_terminology.BASELINE_COLUMNS
COMPACT_COLUMNS = _localization_terminology.COMPACT_COLUMNS
GAMES = _localization_terminology.GAMES
MUV_LUV_GAMES = _localization_terminology.MUV_LUV_GAMES
ROOT = _localization_terminology.ROOT
baseline_consistency_errors = _localization_terminology.baseline_consistency_errors
baseline_group = _localization_terminology.baseline_group
candidate_terms = _localization_terminology.candidate_terms
evidence_numbers = _localization_terminology.evidence_numbers
load_game = _localization_terminology.load_game
read_baseline = _localization_terminology.read_baseline
read_evidence = _localization_terminology.read_evidence
read_table = _localization_terminology.read_table


class TerminologyScopeTests(unittest.TestCase):
    def test_seven_games_explicitly_load_only_common_and_own_table(self):
        common = read_table(ROOT / "localization-make-games-speak/glossaries-keep-it-consistent/muv-luv.ja-zh-Hans.csv")
        for game, engine in MUV_LUV_GAMES.items():
            own = read_table(ROOT / "localization-make-games-speak/glossaries-keep-it-consistent" / f"{game}.ja-zh-Hans.csv")
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
        own = read_table(ROOT / "localization-make-games-speak/glossaries-keep-it-consistent/kiminozo.ja-zh-Hans.csv")
        effective = load_game("kiminozo")
        self.assertEqual(set(effective), set(own))
        self.assertTrue(all(row['scope'] == 'kiminozo' for row in effective.values()))
        self.assertNotIn('レーザー級', effective)
        self.assertEqual(effective['竹尾タケオ']['cn'], '竹尾竹雄')
        self.assertEqual(effective['タケス']['cn'], '竹卡斯')
        self.assertEqual(effective['バトル・テッカ']['cn'], 'BattleTech')
        self.assertEqual(effective['ＳｍａｌｌＤｉｓｋ']['cn'], 'CD')
        rows = read_evidence('kiminozo')
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
                own = read_table(ROOT / 'localization-make-games-speak/glossaries-keep-it-consistent' / f'{game}.ja-zh-Hans.csv')
                with (ROOT / engine / 'games' / game / 'terminology/baseline.ja-zh-Hans.csv').open(encoding='utf-8-sig', newline='') as stream:
                    baseline = {row['jp'] for row in csv.DictReader(stream)}
                self.assertFalse(set(own) - baseline, '本作术语必须全部保留在基线中')

    def test_all_eight_baselines_preserve_current_translations_and_complete_scope(self):
        for game in GAMES:
            with self.subTest(game=game):
                terms = read_table(ROOT / 'localization-make-games-speak/glossaries-keep-it-consistent' / f'{game}.ja-zh-Hans.csv')
                rows = read_baseline(game)
                history = read_evidence(game)
                self.assertEqual(baseline_consistency_errors(terms, rows), [])
                self.assertTrue(all(set(row) == set(COMPACT_COLUMNS) for row in rows))
                current = [row for row in rows if baseline_group(row) == 'current']
                for index, term in enumerate(terms.values(), 2):
                    row = next(row for row in current if row['jp'] == term['jp'])
                    self.assertEqual(row['basis'], term['context'])
                    self.assertTrue(all(history[number-2]['jp'] == term['jp'] for number in evidence_numbers(row)))
                for row in rows:
                    if row['kind'] != 'term':
                        for number in evidence_numbers(row):
                            self.assertIn(history[number-2]['basis'], row['basis'], '合并来源不能省略原有使用条件')
        pf = read_evidence('photonflowers')
        self.assertEqual(sum(baseline_group(row) == 'noise' for row in pf), 746)
        for game in ('tda01', 'tda02', 'tda03', 'photonflowers'):
            term = read_table(ROOT / 'localization-make-games-speak/glossaries-keep-it-consistent' / f'{game}.ja-zh-Hans.csv')['軌道降下兵']
            self.assertIn('本作采用轨道空降兵', term['context'])
            self.assertNotIn('本作采用轨道降下兵', term['context'])

    def test_baseline_consistency_requires_current_translation_and_scope(self):
        terms = {'伍長': {'jp': '伍長', 'cn': '下士', 'context': '中文军衔；仅在军衔语境使用'}}
        old = {'jp': '伍長', 'cn': '伍长', 'status': 'confirmed', 'basis': '旧来源已确认', 'source': 'legacy'}
        self.assertTrue(baseline_consistency_errors(terms, [old]))
        current = dict(old, cn='下士', basis=terms['伍長']['context'], source='current-glossary-20261009-tda00')
        self.assertEqual(baseline_consistency_errors(terms, [old, current]), [])
        self.assertTrue(baseline_consistency_errors(terms, [dict(current, basis='军衔')]))
        self.assertTrue(baseline_consistency_errors(terms, [dict(current, cn='伍长')]))
        self.assertTrue(baseline_consistency_errors(terms, [dict(current, status='candidate')]))
        self.assertTrue(baseline_consistency_errors(terms, [current, dict(current)]))

    def test_baseline_reading_groups_preserve_historical_status_and_candidates(self):
        noise = {'source': 'pf-ex-baseline', 'status': 'contextual', 'basis': '类别：regex_address_false_positive'}
        self.assertEqual(baseline_group(noise), 'noise')
        self.assertEqual(noise['status'], 'contextual')
        self.assertEqual(baseline_group(dict(noise, status='excluded')), 'excluded')
        self.assertEqual(baseline_group({'source':'legacy', 'status':'confirmed', 'basis':'历史确认'}), 'reference')
        self.assertEqual(baseline_group({'source':'pm-shard-baseline', 'status':'candidate', 'basis':'全文机械扫描候选'}), 'candidate')
        self.assertEqual(baseline_group({'source':'legacy', 'status':'question', 'basis':'待核'}), 'question')

    def _compact_fixture(self, root, sources, entries):
        folder = root / 'AGE2/games/tda00'
        (folder / 'terminology/history').mkdir(parents=True)
        (folder / 'project.toml').write_text(
            'terminology_baseline = "terminology/baseline.ja-zh-Hans.csv"\n'
            'terminology_evidence = "terminology/history/evidence-20261009.csv"\n', encoding='utf-8')
        for path, columns, rows in [
            (folder / 'terminology/baseline.ja-zh-Hans.csv', COMPACT_COLUMNS, entries),
            (folder / 'terminology/history/evidence-20261009.csv', BASELINE_COLUMNS, sources),
        ]:
            with path.open('w', encoding='utf-8', newline='') as stream:
                writer = csv.DictWriter(stream, fieldnames=columns)
                writer.writeheader()
                writer.writerows(rows)

    def test_compact_baseline_merges_sources_and_retains_original_statuses(self):
        old = dict(jp='伍長', cn='伍长', status='candidate', chapter='第一章', source='old',
                   source_row='2', source_status='candidate', occurrences='2', basis='旧候选')
        newer = dict(old, cn='下士', status='confirmed', source_row='3', source_status='confirmed', basis='后续审定')
        entry = dict(jp='伍長', cn='下士', kind='term', chapter='第一章', basis='中文军衔；仅限军衔', evidence_rows='2;3')
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self._compact_fixture(root, [old, newer], [entry])
            self.assertEqual(read_baseline('tda00', root), [entry])
            self.assertEqual(read_evidence('tda00', root), [old, newer])

    def test_compact_baseline_rejects_wrong_evidence_and_missing_live_candidates(self):
        source = dict(jp='名词', cn='', status='candidate', chapter='第一章', source='old',
                      source_row='2', source_status='candidate', occurrences='', basis='尚待审定')
        entry = dict(jp='其他', cn='', kind='candidate', chapter='第一章', basis='尚待审定', evidence_rows='2')
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self._compact_fixture(root, [source], [entry])
            with self.assertRaisesRegex(ValueError, 'Wrong JP evidence'):
                read_baseline('tda00', root)
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self._compact_fixture(root, [source], [])
            with self.assertRaisesRegex(ValueError, 'silently omitted'):
                read_baseline('tda00', root)

    def test_compact_baseline_does_not_merge_different_meanings_or_promote_candidates(self):
        source = dict(jp='词', cn='译法一', status='question', chapter='第一章', source='old',
                      source_row='2', source_status='question', occurrences='', basis='仍有疑问')
        for cn, kind, error in [('译法二', 'question', 'Different Chinese meanings'),
                                ('译法一', 'candidate', 'source status changed'),
                                ('译法一', 'context', 'source status changed')]:
            with self.subTest(cn=cn, kind=kind), tempfile.TemporaryDirectory() as temp:
                root = Path(temp)
                entry = dict(jp='词', cn=cn, kind=kind, chapter='第一章', basis='仍有疑问', evidence_rows='2')
                self._compact_fixture(root, [source], [entry])
                with self.assertRaisesRegex(ValueError, error):
                    read_baseline('tda00', root)

    def test_baseline_cli_returns_structured_current_terms_and_sources(self):
        result = subprocess.run([sys.executable, '-X', 'utf8', str(ROOT/'localization-make-games-speak/tools-let-tools-handle-repetition/terminology.py'),
                                 'tda00', '--baseline', '--term', 'ウィル'],
                                capture_output=True, text=True, encoding='utf-8', check=True)
        data = json.loads(result.stdout)
        self.assertEqual(data['current_term']['cn'], '威尔')
        self.assertEqual(len([row for row in data['evidence'] if row['kind']=='term']), 1)
        self.assertTrue(data['sources'])
        self.assertTrue(all(row['jp']=='ウィル' and isinstance(row['evidence_row'], int) for row in data['sources']))

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
