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


if __name__ == '__main__':
    unittest.main()
