"""Keep Imperial Capital Burns' classification tied to adopted project data."""
import csv
import json
from collections import Counter
import unittest

from localization.tools.terminology import (
    ROOT, baseline_consistency_errors, load_game, read_baseline, read_evidence,
    read_table,
)


class ImperialTerminologyReviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.review = json.loads((ROOT / 'docs/research/localization/terminology-history/imperial-review-20261009.json').read_text(encoding='utf-8'))
        cls.terms = read_table(ROOT / 'localization/glossaries/imperial-capital-burns.ja-zh-Hans.csv')
        cls.baseline = read_baseline('imperial-capital-burns')
        cls.evidence = read_evidence('imperial-capital-burns')
        folder = ROOT / 'AGE2/games/imperial-capital-burns/translations'
        with (folder / 'main.ja-zh-Hans.csv').open(encoding='utf-8-sig', newline='') as stream:
            cls.body = {x['id']: x for x in csv.DictReader(stream)}
        with (folder / 'speakers.ja-zh-Hans.csv').open(encoding='utf-8-sig', newline='') as stream:
            cls.speakers = list(csv.DictReader(stream))

    def test_current_tables_reconcile_and_all_terms_remain_in_parent_baseline(self):
        meta = self.review['after']
        self.assertEqual(len(self.terms), meta['terms'])
        self.assertEqual(len(self.baseline), meta['baseline'])
        self.assertEqual(len(self.evidence), meta['source_records'])
        self.assertEqual(dict(Counter(x['kind'] for x in self.baseline)), meta['kinds'])
        self.assertEqual(list(self.terms.values()), self.review['current_glossary'])
        self.assertEqual(baseline_consistency_errors(self.terms, self.baseline), [])

    def test_old_translations_survive_reclassification_without_becoming_global_terms(self):
        old = self.review['original_classification']
        self.assertEqual(len(old), 183)
        self.assertEqual(Counter(x['action'] for x in old), {'term': 135, 'context': 47, 'excluded': 1})
        for entry in old:
            jp, cn = entry['jp'], entry['cn']
            self.assertTrue(entry['reason'] and entry['previous_context'])
            if entry['action'] == 'term':
                self.assertEqual(self.terms[jp]['cn'], cn)
            elif entry['action'] == 'context':
                self.assertNotIn(jp, self.terms)
                self.assertTrue(any((x['jp'], x['cn'], x['kind']) == (jp, cn, 'context') for x in self.baseline))
            else:
                self.assertNotIn(jp, self.terms)
                self.assertFalse(any(x['jp'] == jp for x in self.baseline))
        self.assertEqual(self.terms['悪酔い']['cn'], '恶醉')
        for jp, cn in [('九段に向かった', '去了九段'), ('乳歯', '乳牙')]:
            self.assertTrue(any(x['jp'] == jp and x['cn'] == cn and x['kind'] == 'context' for x in self.baseline))
        self.assertNotIn('響', load_game('imperial-capital-burns'))
        changed = self.review['evidence_changes']
        self.assertEqual(len(changed), 1)
        self.assertEqual(changed[0]['after']['jp'], '響')
        self.assertEqual(changed[0]['after']['status'], 'excluded')
        for key in ('jp', 'cn', 'source', 'source_row', 'source_status', 'occurrences'):
            self.assertEqual(changed[0]['before'][key], changed[0]['after'][key])

    def test_all_speaker_mappings_have_exact_adopted_chinese_and_actual_calls(self):
        additions = [x for x in self.review['additions'] if x['source'] == 'imperial-speakers-20261009']
        self.assertEqual(len(additions), len(self.speakers))
        self.assertEqual(len(additions), 91)
        for entry in additions:
            speaker = self.speakers[int(entry['source_row']) - 2]
            self.assertEqual((entry['jp'], entry['cn']), (speaker['expected_text'], speaker['replacement_text']))
            calls = [x['id'] for x in self.body.values() if x['speaker_jp'] == entry['jp']]
            self.assertEqual(entry['record_ids'], calls)
            self.assertTrue(calls)
            self.assertTrue(any((x['jp'], x['cn'], x['kind']) == (entry['jp'], entry['cn'], entry['kind']) for x in self.baseline))

    def test_new_body_records_reference_current_adopted_text_and_unique_source_keys(self):
        self.assertEqual(self.evidence[264:], self.review['source_additions'])
        for entry, source in zip(self.review['additions'], self.review['source_additions']):
            self.assertEqual((entry['jp'], entry['cn'], entry['source'], entry['source_row']),
                             (source['jp'], source['cn'], source['source'], source['source_row']))
            self.assertEqual(len(entry['record_ids']), len(set(entry['record_ids'])))
            records = [self.body[x] for x in entry['record_ids']]
            self.assertTrue(records)
            self.assertEqual(source['occurrences'], str(len(records)))
            self.assertEqual(entry['scenes'], list(dict.fromkeys(x['scene'] for x in records)))
            if entry['source'] == 'imperial-body-20261009':
                self.assertEqual(entry['source_row'], entry['record_ids'][0] + ':' + entry['jp'])
                self.assertTrue(any(entry['cn'] in x['cn_text'] for x in records))
        coverage = self.review['coverage']
        self.assertEqual(coverage['current_body_rows'], len(self.body))
        self.assertEqual(coverage['scenes'], len({x['scene'] for x in self.body.values()}))

    def test_ambiguous_short_model_and_original_spelling_variants_keep_separate_scopes(self):
        short = [x for x in self.baseline if x['jp'] == '７７式']
        self.assertEqual(len(short), 1)
        self.assertEqual(short[0]['kind'], 'context')
        source = next(x for x in self.review['additions'] if x['jp'] == '７７式')
        self.assertEqual(source['record_ids'], ['game_t00234'])
        self.assertEqual(short[0]['chapter'], self.body['game_t00234']['scene'])
        self.assertNotIn('７７式', self.terms)
        for jp in ('７７式強化装備', '７７式気密装甲兜', '７４式長刀', '７４式訓練用近接長刀',
                   '月詠真耶', '月詠真那', '斉御司', '斎御司経盛', '嵐山の嵐', 'あらしやまのあらし'):
            self.assertIn(jp, self.terms)
        self.assertEqual(self.terms['月詠真耶']['cn'], '月咏真耶')
        self.assertEqual(self.terms['月詠真那']['cn'], '月咏真那')
        self.assertEqual(self.terms['アラシヤマ・コントロール']['cn'], '岚山管制')


if __name__ == '__main__':
    unittest.main()
