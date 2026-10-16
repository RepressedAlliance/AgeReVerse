import random
import unittest

from rUGP.formats.images.crip008_decode import (
    Crip008Header, decode_crip008_kind3_native,
)

try:
    from rUGP.tools.video.compact_encoder import encode_rgb
except ModuleNotFoundError as error:
    if error.name not in ('numpy', 'numba'):
        raise
    encode_rgb = None


@unittest.skipIf(encode_rgb is None, 'optional NumPy/Numba producer dependencies')
class CompactCrsiTests(unittest.TestCase):
    def check_roundtrip(self, rgb, width, height):
        frame, counts = encode_rgb(rgb, width, height)
        header = Crip008Header(width, height, 0, 0, width, height, 3, 3,
                              0, 2, 8, 8, 8, False, True, False, False,
                              False, 0, len(frame.payload))
        native = decode_crip008_kind3_native(frame.payload, header)
        actual = bytearray(width * height * 3)
        actual[0::3], actual[1::3], actual[2::3] = native[2::4], native[1::4], native[0::4]
        self.assertEqual(actual, rgb)
        self.assertEqual(set(native[3::4]), {128})
        self.assertEqual(sum(counts.values()), width * height)
        return frame, counts

    def test_native_verified_run_and_above_row_transitions(self):
        rgb = (bytes([1,127,254])*4 + bytes([255,0,0])*3 + bytes([0,255,255])*5)*3
        frame, counts = self.check_roundtrip(rgb, 12, 3)
        self.assertEqual(frame.payload.hex(),
                         'aaa742fff5ffefff98fffdfffafffd0bfff3fffd4aaa74731a5553a398d0')
        self.assertGreater(counts['above_pixels'], 0)
        self.assertGreater(counts['repeat_pixels'], 0)

    def test_predictor_resets_and_odd_row_lengths(self):
        rng = random.Random(20261010)
        for width in (1, 2, 3, 17, 1599):
            row = rng.randbytes(width*3)
            # Literal-to-copy transitions, single-pixel repeats, row changes.
            rgb = row + row + bytes([255,0,255])*width + rng.randbytes(width*3)
            with self.subTest(width=width):
                self.check_roundtrip(rgb, width, 4)

    def test_bounds_and_reader_initial_word(self):
        # The CRsi reader always fetches an initial uint32. Its required extra
        # byte exceeds the image decoder's <=7-bit padding rule for this case.
        from rUGP.formats.video.crsi_lossless import encode_rgb as literal
        frame, _ = encode_rgb(bytes(3), 1, 1)
        self.assertEqual(frame.payload, literal(bytes(3), 1, 1).payload)
        self.assertGreaterEqual(len(frame.payload), 4)
        for rgb, width, height in ((b'', 1, 1), (bytes(3), 0, 1),
                                   (bytes(4800), 1600, 1), (b'', 1, 4097)):
            with self.assertRaises(ValueError):
                encode_rgb(rgb, width, height)


if __name__ == '__main__':
    unittest.main()
