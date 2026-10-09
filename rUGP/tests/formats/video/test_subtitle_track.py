import copy
import csv
from fractions import Fraction
import json
from pathlib import Path
import unittest

from rUGP.tools.video.subtitle_track import build_ass


DATA = Path(__file__).resolve().parents[3] / 'games/photonmelodies/video-localization'


class SubtitleTrackTests(unittest.TestCase):
    def setUp(self):
        self.timeline = json.loads((DATA / 'rebirth-ending-subtitles.frames.json').read_text(encoding='utf-8'))
        with (DATA / 'rebirth-text.zh-CN.csv').open(encoding='utf-8-sig', newline='') as stream:
            self.rows = list(csv.DictReader(stream))

    def test_ass_event_membership_at_every_source_frame(self):
        def seconds(value):
            hours, minutes, tail = value.split(':')
            return 3600 * int(hours) + 60 * int(minutes) + Fraction(tail)

        events = [line.split(',', 9) for line in build_ass(self.timeline, self.rows, 'Microsoft YaHei').splitlines()
                  if line.startswith('Dialogue:')]
        self.assertEqual(len(events), 22)
        for cue, event in zip(self.timeline['captions'], events):
            start, end = seconds(event[1]), seconds(event[2])
            actual = [frame for frame in range(self.timeline['frame_count']) if start <= Fraction(frame, 30) < end]
            self.assertEqual(actual, list(range(cue['start_frame'], cue['end_frame'])), cue['id'])

    def test_reject_missing_text_and_overlapping_cues(self):
        with self.assertRaisesRegex(ValueError, 'missing caption text'):
            build_ass(self.timeline, self.rows[0:33], 'Microsoft YaHei')
        invalid = copy.deepcopy(self.timeline)
        invalid['captions'][1]['start_frame'] = invalid['captions'][0]['end_frame'] - 1
        with self.assertRaisesRegex(ValueError, 'overlapping'):
            build_ass(invalid, self.rows, 'Microsoft YaHei')


if __name__ == '__main__':
    unittest.main()
