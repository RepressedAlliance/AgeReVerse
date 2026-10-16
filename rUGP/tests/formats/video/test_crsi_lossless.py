import unittest

from rUGP.formats.video.crsi import Sequence, parse, rebuild
from rUGP.formats.video.crsi_lossless import encode_rgb


class LosslessCrsiTests(unittest.TestCase):
    def test_matches_native_verified_extreme_color_witness(self):
        # Native PM 0x57b490 decoded this fixture to the exact input, including
        # 255, odd channel values, and consecutive full-range color changes.
        rgb = bytes([0,0,0,255,255,255,255,0,0,0,255,0,0,0,255,
                     1,127,254,254,128,1,255,255,255])
        frame = encode_rgb(rgb, 8, 1)
        self.assertEqual(frame.payload.hex(),
                         'aaa54a80bfff0ffff2fffcbfff7fffbfffcffff5fff8bffdbffe3ffe7fff2ffe8bff97ff80')
        self.assertEqual(frame.mode, 0x03ff)
        self.assertIsNone(frame.parameter)
        header = bytes.fromhex('000101000000000000000800010000000000b80b000000000100')
        parsed = parse(rebuild(Sequence(header, 8, 1, 3000, (frame,)), {}))
        self.assertEqual(parsed.frames[0].payload, frame.payload)
        self.assertEqual(parsed.frames[0].mode, 0x03ff)

    def test_bounds_and_initial_reader_word(self):
        self.assertGreaterEqual(len(encode_rgb(bytes(3), 1, 1).payload), 4)
        for rgb, width, height in [(b'', 1, 1), (bytes(3), 0, 1),
                                   (bytes(1600*3), 1600, 1)]:
            with self.assertRaises(ValueError):
                encode_rgb(rgb, width, height)


if __name__ == '__main__':
    unittest.main()
