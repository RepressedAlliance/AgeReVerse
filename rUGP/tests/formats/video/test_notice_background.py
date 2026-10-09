import importlib.util
import unittest


@unittest.skipUnless(importlib.util.find_spec('numpy'), 'optional NumPy video processing dependency')
class NoticeBackgroundTests(unittest.TestCase):
    def test_reconstructs_known_bilinear_field_and_preserves_exterior(self):
        import numpy as np
        from rUGP.tools.video.notice_background import coons_fill

        y, x = np.mgrid[:32, :48]
        original = np.stack((x+2*y, 2*x+y, 3*x+2*y), axis=2).astype(np.uint8)
        damaged = original.copy()
        box = (8, 5, 35, 25)
        damaged[5:25, 8:35] = [255, 0, 255]
        repaired = coons_fill(damaged, box)
        np.testing.assert_array_equal(repaired, original)


if __name__ == '__main__':
    unittest.main()
