import unittest

from rUGP.tools.video.technical_track import build_ass


class TechnicalTrackTests(unittest.TestCase):
    def test_reveal_survives_dimming_and_price_blink(self):
        layout = dict(schema='photon-crsi-technical-layout/1', source_global_offset=1,
                      text_variant='long', overlays=[dict(
                          occurrence='notice.secret', text_id='notice.secret',
                          detection_span=[0, 5],
                          target=dict(alignment=5, x=512, y=300, font_size=100, ass_color='6600F1'))])
        analysis = dict(schema='photon-crsi-technical-analysis/1', source_global_offset=1,
                        overlays=[dict(occurrence='notice.secret', mask_index=0,
                                       signal_start_frame=0, peak=100)])
        arrays = dict(signal_0=[20, 40, 100, 0, 50], coverage_0=[.5, 1, 1, 0, 1])
        rows = [dict(id='notice.secret', variant='both', layer='notice', target_text='绝密')]
        events = [line for line in build_ass(layout, analysis, arrays, rows, 'Microsoft YaHei').splitlines()
                  if line.startswith('Dialogue:')]
        self.assertEqual(len(events), 4)  # blink-off frame has no event
        self.assertTrue(events[0].endswith('绝{\\alpha&HFF&}密'))
        # All glyphs have appeared, even though measured brightness is only 40%.
        self.assertTrue(events[1].endswith('绝密'))
        self.assertIn('\\alpha&H99&', events[1])
        self.assertTrue(events[-1].endswith('绝密'))
        self.assertIn('\\alpha&H80&', events[-1])


if __name__ == '__main__':
    unittest.main()
