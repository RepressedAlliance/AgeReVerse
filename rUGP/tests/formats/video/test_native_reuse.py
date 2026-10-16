from dataclasses import replace

import unittest

from rUGP.formats.video.crsi import Frame, Sequence
from rUGP.tools.video.verify_replacement import reusable_indices


def sequence(*frames):
    return Sequence(b'unchanged header', 2, 2, 3000, frames)


class NativeReuseTests(unittest.TestCase):
    def test_reuse_allows_relocated_identical_frames_after_independent_reset(self):
        key = Frame(1, 0, 0, 0x03ff, None, b'key')
        delta = Frame(0, 3, 0, 0x575, 8, b'delta')
        before = sequence(key, key, delta)
        after = sequence(replace(key, payload=b'new'), replace(key, offset=9), replace(delta, offset=12))
        self.assertEqual(reusable_indices(before, after, ['a', 'b', 'c'], ['new', 'b', 'c']), {1, 2})


    def test_reuse_rejects_dependent_surface_after_changed_key(self):
        key = Frame(1, 0, 0, 0x03ff, None, b'key')
        delta = Frame(0, 3, 0, 0x575, 8, b'delta')
        with self.assertRaisesRegex(ValueError, 'altered dependency'):
            reusable_indices(sequence(key, delta), sequence(replace(key, payload=b'new'), delta), ['a','b'], ['new','b'])
        with self.assertRaisesRegex(ValueError, 'requires full replay'):
            reusable_indices(sequence(key, delta), sequence(key, replace(delta, payload=b'changed')), ['a','b'], ['a','new'])


    def test_reuse_rejects_rgb_claim_or_header_drift(self):
        key = Frame(1, 0, 0, 0x03ff, None, b'key')
        original = sequence(key)
        with self.assertRaisesRegex(ValueError, 'different target RGB'):
            reusable_indices(original, original, ['a'], ['b'])
        with self.assertRaisesRegex(ValueError, 'header'):
            reusable_indices(original, replace(original, header=b'changed'), ['a'], ['a'])
