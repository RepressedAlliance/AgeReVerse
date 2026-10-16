"""Public extraction and full-movie workflow checks using synthetic pixels only."""
import json
import os
from pathlib import Path
import shutil
import struct
import subprocess
import tempfile
import unittest
from rUGP.formats.video.crsi import Sequence, rebuild
from rUGP.formats.video.crsi_lossless import encode_rgb
from rUGP.tools.video.crsi_workflow import extract, export


def movie():
    header = bytes.fromhex('00010100000000000000') + struct.pack('<HHIHIH', 2, 2, 0, 3000, 0, 2)
    frames = tuple(encode_rgb(bytes([v])*12, 2, 2) for v in (0, 255))
    return rebuild(Sequence(header, 2, 2, 3000, frames), {})


class WorkflowTests(unittest.TestCase):
    def test_bounded_extract_and_no_overwrite(self):
        data = movie()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source, output = root/'volume', root/'movie.crsi'
            source.write_bytes(b'prefix'+data+b'padding')
            report = extract(source, 6, len(data), output)
            self.assertEqual(output.read_bytes(), data)
            self.assertEqual(report['frames'], 2)
            with self.assertRaises(FileExistsError): extract(source, 6, len(data), output)
            for offset, size in [(-1, 1), (6, len(data)+1), (6, len(data)+100)]:
                with self.assertRaises(ValueError): extract(source, offset, size, root/'bad')
            self.assertFalse((root/'bad').exists())

    @unittest.skipUnless(os.environ.get('RUGP_CRSI_LIBRARY') and shutil.which('ffmpeg'),
                         'explicit C library and FFmpeg required')
    def test_full_ffv1_export_and_failure_report(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source, output, report = root/'input.crsi', root/'proxy.mkv', root/'export.json'
            source.write_bytes(movie())
            result = export(Path(os.environ['RUGP_CRSI_LIBRARY']), source, output, report)
            self.assertEqual(result['decoded_frames'], 2)
            pixels = subprocess.check_output(['ffmpeg', '-v', 'error', '-i', str(output),
                                              '-f', 'rawvideo', '-pix_fmt', 'rgb24', 'pipe:1'])
            self.assertEqual(pixels, bytes(12)+bytes([255])*12)
            with self.assertRaises(FileExistsError):
                export(Path(os.environ['RUGP_CRSI_LIBRARY']), source, output, root/'unused.json')
            with self.assertRaises(FileNotFoundError):
                export(Path(os.environ['RUGP_CRSI_LIBRARY']), source, root/'failed.mkv',
                       root/'failed.json', str(root/'missing-ffmpeg'))
            failed = json.loads((root/'failed.json').read_text())
            self.assertEqual(failed['status'], 'incomplete')
            self.assertEqual(failed['decoded_frames'], 0)


if __name__ == '__main__': unittest.main()
