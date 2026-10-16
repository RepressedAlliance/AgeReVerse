"""Optional NumPy/Numba producer for opaque, lossless CRsi mode 0x03ff.

Uses the audited scalar kind-3 grammar: alternating literal/repeat segments,
above-row copies, and predictive RGB deltas. No runtime patch dependency.
"""
from __future__ import annotations

import numpy as np
from numba import njit

from rUGP.formats.video.crsi import Frame


def _unsigned_code(value: int) -> tuple[int, int]:
    code, bits = 0, 0
    for digit in bin(value)[3:]:
        code = (code << 2) | 2 | (digit == '1')
        bits += 2
    return code << 1, bits + 1


@njit(cache=True, inline='always')
def _put(out, pos, current, used, code, bits):
    current = (current << bits) | code
    used += bits
    while used >= 8:
        used -= 8
        out[pos] = (current >> used) & 255
        pos += 1
    current &= (1 << used) - 1
    return pos, current, used


@njit(cache=True, inline='always')
def _same(rgb, a, b):
    return rgb[a] == rgb[b] and rgb[a+1] == rgb[b+1] and rgb[a+2] == rgb[b+2]


@njit(cache=True)
def _encode(rgb, width, height, sc, sb, uc, ub):
    # A literal pixel needs at most 58 bits. The extra row capacity covers
    # alpha and segment headers even when every segment contains one pixel.
    out = np.zeros(width*height*12 + height*128 + 64, dtype=np.uint8)
    pos = current = used = 0
    copies = repeated = literals = 0
    for y in range(height):
        pos,current,used = _put(out,pos,current,used,sc[542],sb[542])  # opaque alpha: +32
        pos,current,used = _put(out,pos,current,used,uc[width],ub[width])
        r = g = b = 0
        x = 0
        while x < width:
            start = x
            x += 1
            while x < width and not _same(rgb,(y*width+x)*3,(y*width+x-1)*3):
                x += 1
            length = x-start
            pos,current,used = _put(out,pos,current,used,uc[length],ub[length])
            green_acc = 0
            for xx in range(start,x):
                p = (y*width+xx)*3
                tr,tg,tb = int(rgb[p]),int(rgb[p+1]),int(rgb[p+2])
                if y > 0 and _same(rgb,p,p-width*3):
                    pos,current,used = _put(out,pos,current,used,1,1)
                    green_acc = 0
                    copies += 1
                else:
                    green = tg-g
                    raw_g = green-max(-g,min(255-g,green_acc))
                    b_inc = tb-b-max(-b,min(255-b,green))
                    r_inc = tr-r-max(-r,min(255-r,green))
                    pos,current,used = _put(out,pos,current,used,0,1)
                    for value in (raw_g,b_inc,r_inc):
                        pos,current,used = _put(out,pos,current,used,sc[value+510],sb[value+510])
                    green_acc = green
                    literals += 1
                r,g,b = tr,tg,tb
            if x < width:
                start = x
                while x < width and _same(rgb,(y*width+x)*3,(y*width+x-1)*3):
                    x += 1
                length = x-start
                pos,current,used = _put(out,pos,current,used,uc[length],ub[length])
                repeated += length
    if used:
        out[pos] = current << (8-used)
        pos += 1
    return out[:max(4,pos)], copies, repeated, literals


def encode_rgb(rgb: bytes, width: int, height: int) -> tuple[Frame, dict]:
    if not (0 < width < 1600 and 0 < height <= 4096 and width*height <= 2_097_152):
        raise ValueError('dimensions exceed the verified scalar CRsi profile')
    if len(rgb) != width*height*3:
        raise ValueError('RGB buffer does not match CRsi dimensions')
    uc = np.zeros(width+1,dtype=np.int64)
    ub = np.zeros(width+1,dtype=np.int64)
    for value in range(1,width+1):
        uc[value],ub[value] = _unsigned_code(value)
    sc = np.zeros(1021,dtype=np.int64)
    sb = np.ones(1021,dtype=np.int64)
    for value in range(-510,511):
        if value:
            code,bits = _unsigned_code(abs(value))
            sc[value+510] = ((2 | (value<0)) << bits) | code
            sb[value+510] = bits+2
    payload,copies,repeated,literals = _encode(np.frombuffer(rgb,dtype=np.uint8),width,height,sc,sb,uc,ub)
    return Frame(1,0,0,0x03ff,None,payload.tobytes()), dict(above_pixels=copies,repeat_pixels=repeated,literal_pixels=literals)
