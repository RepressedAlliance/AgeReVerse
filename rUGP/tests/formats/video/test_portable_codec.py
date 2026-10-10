"""C integration tests: set RUGP_CRSI_LIBRARY to an explicitly built library."""
import ctypes as c
import os
from pathlib import Path
import random
import struct
import unittest
from unittest.mock import patch
import tempfile
from rUGP.formats.video.crsi import Frame, parse
from rUGP.formats.video.crsi_lossless import encode_rgb as reference_lossless
from rUGP.tools.video.portable_codec import Codec, native_to_rgb


@unittest.skipUnless(os.environ.get('RUGP_CRSI_LIBRARY'), 'explicit C library required')
class PortableCodecTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.codec = Codec(Path(os.environ['RUGP_CRSI_LIBRARY']))

    def test_scalar_reference_stream(self):
        rng = random.Random(10575)
        for w,h in [(1,1),(17,9),(32,16)]:
            rgb = rng.randbytes(w*h*3)
            frame = reference_lossless(rgb,w,h)
            decoded, consumed = self.codec.decode(frame,w,h)
            self.assertEqual(native_to_rgb(decoded),rgb)
            self.assertLessEqual(consumed,len(frame.payload)*8)

    def test_scalar_above_and_repeat(self):
        row = bytes(v for x in range(31) for v in ((x//4)*29,255-(x//4)*29,128))
        rgb = row*13
        frame = self.codec.encode_lossless(rgb,31,13)
        decoded,_ = self.codec.decode(frame,31,13)
        self.assertEqual(native_to_rgb(decoded),rgb)
        self.assertEqual(decoded[3::4],bytes([128])*31*13)
        self.assertLess(len(frame.payload),len(rgb)//5)

    def test_codec1_temporal_feedback(self):
        rgb = bytes([255])*32*16*3
        key,surface = self.codec.encode_lossy(rgb,32,16)
        self.assertEqual(native_to_rgb(surface),rgb)
        delta,result = self.codec.encode_lossy(rgb,32,16,surface)
        self.assertFalse(delta.independent)
        decoded,_ = self.codec.decode(delta,32,16,surface)
        self.assertEqual(decoded,result)
        self.assertEqual(native_to_rgb(decoded),rgb)
        with self.assertRaises(ValueError): self.codec.decode(delta,32,16)

    def test_native_mmx_length_byte_spill(self):
        # Independently constructed: one 2x2 flat block, U residual -40.
        # PM native leaves establish these four-byte results for all 4 pixels.
        # Twelve code bits spill +1 into V in the five-bit chroma profiles.
        for mode,param,pixel in [(0x575,8,'00764040'),(0x56d,32767,'00764040'),
                                 (0x52c,32767,'00ac403f'),(0x524,32767,'00ac403f')]:
            frame=Frame(1,0,0,mode,param,bytes.fromhex('70570200'))
            actual,bits=self.codec.decode(frame,2,2)
            self.assertEqual(actual,bytes.fromhex(pixel)*4)
            self.assertEqual(bits,18)
            seed=bytes((30,40,50,128))*4
            dependent=Frame(0,0,0,mode,param,frame.payload)
            actual,_=self.codec.decode(dependent,2,2,seed)
            self.assertEqual(actual,bytes.fromhex('00140000' if mode in (0x575,0x56d) else '00800000')*4)

    def test_c_backend_keeps_dependency_closure(self):
        try:
            import numpy as np
            from rUGP.tools.video.encode_replacement import build
        except ImportError as error:
            self.skipTest(str(error))
        black=np.zeros((2,2,3),dtype=np.uint8)
        white=np.full((2,2,3),255,dtype=np.uint8)
        first,surface=self.codec.encode_lossy(black.tobytes(),2,2)
        dependent,_=self.codec.encode_lossy(black.tobytes(),2,2,surface)
        frames=[first,dependent,first]
        header=bytes.fromhex('00010100000000000000')+struct.pack('<HHIHIH',2,2,0,3000,0,3)
        table,payload=bytearray(),bytearray()
        for f in frames:
            table+=struct.pack('<BIHHHI',f.flags,len(payload),0,f.mode,f.parameter,len(f.payload))
            payload+=f.payload
        class Capture:
            def __init__(self,images): self.images=iter(images)
            def isOpened(self): return True
            def get(self,_): return 30
            def read(self):
                value=next(self.images,None)
                return value is not None,value
            def release(self): pass
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); original=root/'original.crsi'; original.write_bytes(header+table+payload)
            with patch('rUGP.tools.video.encode_replacement.cv2.VideoCapture',side_effect=[Capture([black]*3),Capture([white,black,black])]):
                report=build(original,root/'source.mkv',root/'edited.mkv',root/'out.crsi',root/'report.json',
                             codec_library=Path(os.environ['RUGP_CRSI_LIBRARY']))
            actual=parse((root/'out.crsi').read_bytes())
            self.assertEqual(report['changed_frames'],[0])
            self.assertEqual(report['dependency_closure_frames'],[1])
            self.assertEqual(report['encoder_backend'],'portable-c')
            self.assertIsNone(report['statistics'])
            self.assertEqual(actual.frames[2].payload,first.payload)
            for f,expected in zip(actual.frames,[white,black,black]):
                decoded,_=self.codec.decode(f,2,2)
                self.assertEqual(native_to_rgb(decoded),expected.tobytes())

    def test_truncated_and_invalid_profiles(self):
        rgb = random.Random(43).randbytes(16*8*3)
        for frame in [self.codec.encode_lossless(rgb,16,8),self.codec.encode_lossy(rgb,16,8)[0]]:
            for n in (0,3,len(frame.payload)//2):
                bad = Frame(1,0,0,frame.mode,frame.parameter,frame.payload[:n])
                with self.assertRaises(ValueError): self.codec.decode(bad,16,8)
        for mode,param in [(0x575,7),(0x975,8),(0x16d,None)]:
            with self.assertRaises(ValueError): self.codec.decode(Frame(1,0,0,mode,param,b'\0'*4),2,2)
        with self.assertRaises(ValueError): self.codec.encode_lossy(b'\0'*3,1,1)

    def test_output_bounds(self):
        fn=self.codec.library.crsi_decode_03ff
        frame=self.codec.encode_lossless(b'\xff'*12,2,2)
        target=c.create_string_buffer(b'X'*48,48)
        self.assertNotEqual(fn(frame.payload,len(frame.payload),2,2,c.byref(target,16),15,None),0)
        self.assertEqual(target.raw,b'X'*48)
        self.assertEqual(fn(frame.payload,len(frame.payload),2,2,c.byref(target,16),16,None),0)
        self.assertEqual(target.raw[:16]+target.raw[32:],b'X'*32)
        self.assertEqual(self.codec.library.crsi_encode_03ff(b'\xff'*12,12,2,2,c.byref(target,16),4,c.byref(c.c_size_t())),-3)
        self.assertEqual(target.raw[:16]+target.raw[32:],b'X'*32)

    def test_c_container_mixed_rows(self):
        class Sequence(c.Structure):
            _fields_=[('width',c.c_uint),('height',c.c_uint),('rate',c.c_uint),('count',c.c_uint),
                      ('table_end',c.c_size_t),('data',c.c_void_p),('size',c.c_size_t)]
        class CFrame(c.Structure):
            _fields_=[('independent',c.c_uint),('mode',c.c_uint),('parameter',c.c_uint),
                      ('offset',c.c_uint32),('size',c.c_uint32),('payload',c.c_void_p)]
        fn=self.codec.library.crsi_parse
        fn.argtypes=[c.c_void_p,c.c_size_t,c.POINTER(Sequence),c.c_void_p,c.c_size_t]
        header=bytes.fromhex('00010100000000000000')+struct.pack('<HHIHIH',2,2,0,3000,0,2)
        frames=[self.codec.encode_lossy(bytes(12),2,2)[0],self.codec.encode_lossless(bytes([255])*12,2,2)]
        rows,payload=bytearray(),bytearray()
        for f in frames:
            rows+=struct.pack('<BIHH',f.flags,len(payload),0,f.mode)
            if f.parameter is not None: rows+=struct.pack('<H',f.parameter)
            rows+=struct.pack('<I',len(f.payload));payload+=f.payload
        data=header+rows+payload
        expected=parse(data); actual=Sequence()
        self.assertEqual(fn(data,len(data),c.byref(actual),None,0),0)
        self.assertEqual((actual.width,actual.height,actual.count),(expected.width,expected.height,len(expected.frames)))
        self.assertEqual(actual.table_end,54)
        frame_views=(CFrame*2)()
        self.assertEqual(fn(data,len(data),c.byref(actual),frame_views,2),0)
        write=self.codec.library.crsi_write
        write.argtypes=[c.POINTER(Sequence),c.c_void_p,c.c_size_t,c.c_void_p,c.c_size_t,c.POINTER(c.c_size_t)]
        required=c.c_size_t()
        self.assertEqual(write(c.byref(actual),frame_views,2,None,0,c.byref(required)),0)
        output=c.create_string_buffer(required.value)
        self.assertEqual(write(c.byref(actual),frame_views,2,output,len(output),c.byref(required)),0)
        self.assertEqual(output.raw,data)
        self.assertNotEqual(write(c.byref(actual),frame_views,2,output,len(output)-1,c.byref(required)),0)
        for bad in (data[:-1],data+b'\0',data[:24]+b'\xff\xff'+data[26:],data[:26]+b'\0'+data[27:]):
            self.assertNotEqual(fn(bad,len(bad),c.byref(actual),None,0),0)


if __name__=='__main__': unittest.main()
