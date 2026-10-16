import struct
import unittest

from rUGP.formats.video.crsi import Frame, Sequence, parse, rebuild
from rUGP.formats.video.crsi_literal import encode_rgb


def fixture():
    header = bytearray.fromhex('000101000000000000000004580200000000b80b000000000400')
    frames = tuple(Frame(flag, 0, 0, 0x575, 8, bytes([i])*4) for i, flag in enumerate((1, 0, 0, 1)))
    return Sequence(bytes(header), 1024, 600, 3000, frames)


class CrsiTests(unittest.TestCase):
    def test_mixed_variable_rows_and_exact_roundtrip(self):
        source = fixture()
        original = rebuild(source, {})
        self.assertEqual(rebuild(parse(original), {}), original)
        replacement = Frame(1, 0, 0, 0x16d, None, b'abcdef')
        mixed = rebuild(source, {2: replacement})
        parsed = parse(mixed)
        self.assertEqual(parsed.header, source.header)
        self.assertEqual(len(mixed), len(original))  # payload +2, row -2
        self.assertEqual(parsed.frames[2].payload, b'abcdef')
        self.assertIsNone(parsed.frames[2].parameter)
        self.assertEqual(parsed.frames[3].payload, source.frames[3].payload)

    def test_dependency_closure(self):
        replacement = Frame(1, 0, 0, 0x16d, None, b'1234')
        with self.assertRaisesRegex(ValueError, 'dependent frame 2'):
            rebuild(fixture(), {1: replacement})
        self.assertEqual(len(parse(rebuild(fixture(), {1: replacement, 2: replacement})).frames), 4)

    def test_reject_corrupt_extents_and_extra_bytes(self):
        original = rebuild(fixture(), {})
        for data in (original[:25], original[:-1], original+b'\0'):
            with self.assertRaises(ValueError):
                parse(data)
        data = bytearray(original)
        struct.pack_into('<I', data, 27, 1)
        with self.assertRaisesRegex(ValueError, 'contiguous'):
            parse(data)

    def test_literal_quantizer_and_input_rejection(self):
        frame, expected = encode_rgb(bytes((255, 17, 2, 0, 255, 255)), 2, 1)
        self.assertEqual(expected, bytes((252, 16, 0, 0, 252, 252)))
        self.assertEqual(frame.mode, 0x16d)
        self.assertTrue(frame.independent)
        with self.assertRaises(ValueError):
            encode_rgb(b'123', 2, 1)


if __name__ == '__main__':
    unittest.main()
