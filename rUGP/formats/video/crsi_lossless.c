#include "crsi_codec.h"
#include <string.h>

typedef struct { const uint8_t *src; uint8_t *dst; size_t size,bit; int error; } Stream;
static unsigned read_bit(Stream *s) {
    if (s->bit>=s->size*8) { s->error=1; return 0; }
    size_t p=s->bit++; return (s->src[p/8]>>(7-p%8))&1;
}
static void write_bit(Stream *s,unsigned bit) {
    if (s->bit>=s->size*8) { s->error=1; return; }
    size_t p=s->bit++; s->dst[p/8]|=(uint8_t)(bit<<(7-p%8));
}
static unsigned read_uint(Stream *s) {
    unsigned v=1;
    while (read_bit(s)) {
        if (v>32767) { s->error=1; return 0; }
        v=v*2+read_bit(s);
    }
    return v;
}
static int read_signed(Stream *s) {
    if (!read_bit(s)) return 0;
    int sign=(int)read_bit(s),v=(int)read_uint(s);
    return sign?-v:v;
}
static void write_uint(Stream *s,unsigned v) {
    unsigned k=0; for (unsigned n=v;n>1;n>>=1) k++;
    while (k) { k--; write_bit(s,1); write_bit(s,(v>>k)&1); }
    write_bit(s,0);
}
static void write_signed(Stream *s,int v) {
    write_bit(s,v!=0);
    if (v) { write_bit(s,v<0); write_uint(s,(unsigned)(v<0?-v:v)); }
}
static int rel(int delta,int base) { return delta<-base?-base:delta>255-base?255-base:delta; }
static int dimensions(unsigned w,unsigned h) { return w>0 && w<1600 && h>0 && h<=4096 && (size_t)w*h<=2097152; }
static int same(const uint8_t *a,const uint8_t *b) { return a[0]==b[0] && a[1]==b[1] && a[2]==b[2]; }
size_t crsi_bound_03ff(unsigned w,unsigned h) { return dimensions(w,h)?(size_t)w*h*12+h*128+64:0; }
int crsi_encode_03ff(const uint8_t *rgb,size_t rgb_size,unsigned w,unsigned h,
                     uint8_t *data,size_t capacity,size_t *written) {
    if (!rgb || !data || !written || !dimensions(w,h) || rgb_size!=(size_t)w*h*3 || capacity<4 || capacity>SIZE_MAX/8) return -1;
    memset(data,0,capacity); Stream s={NULL,data,capacity,0,0};
    for (unsigned y=0;y<h && !s.error;y++) {
        write_signed(&s,32); write_uint(&s,w);
        unsigned x=0; int r=0,g=0,b=0;
        while (x<w && !s.error) {
            unsigned start=x++;
            while (x<w && !same(rgb+((size_t)y*w+x)*3,rgb+((size_t)y*w+x-1)*3)) x++;
            write_uint(&s,x-start); int acc=0;
            for (unsigned xx=start;xx<x;xx++) {
                const uint8_t *p=rgb+((size_t)y*w+xx)*3;
                if (y && same(p,p-w*3)) { write_bit(&s,1); acc=0; }
                else {
                    int green=(int)p[1]-g;
                    write_bit(&s,0); write_signed(&s,green-rel(acc,g));
                    write_signed(&s,(int)p[2]-b-rel(green,b));
                    write_signed(&s,(int)p[0]-r-rel(green,r)); acc=green;
                }
                r=p[0]; g=p[1]; b=p[2];
            }
            if (x<w) {
                start=x;
                while (x<w && same(rgb+((size_t)y*w+x)*3,rgb+((size_t)y*w+x-1)*3)) x++;
                write_uint(&s,x-start);
            }
        }
    }
    *written=(s.bit+7)/8; if (*written<4) *written=4;
    return s.error?-3:0;
}
int crsi_decode_03ff(const uint8_t *data,size_t size,unsigned w,unsigned h,
                     uint8_t *out,size_t capacity,size_t *consumed) {
    if (!data || !out || !dimensions(w,h) || size<4 || size>16777216 || capacity<(size_t)w*h*4) return -1;
    Stream s={data,NULL,size,0,0};
    for (unsigned y=0;y<h && !s.error;y++) {
        if (read_signed(&s)!=32 || read_uint(&s)!=w) { s.error=1; break; }
        unsigned x=0; int b=0,g=0,r=0,repeat=0;
        while (x<w && !s.error) {
            unsigned n=read_uint(&s); int acc=0;
            if (!n || n>w-x) { s.error=1; break; }
            for (unsigned i=0;i<n;i++,x++) {
                uint8_t *p=out+((size_t)y*w+x)*4;
                if (!repeat) {
                    if (read_bit(&s)) {
                        if (!y) { s.error=1; break; }
                        b=p[-(ptrdiff_t)w*4]; g=p[-(ptrdiff_t)w*4+1]; r=p[-(ptrdiff_t)w*4+2]; acc=0;
                    } else {
                        int green=read_signed(&s)+rel(acc,g);
                        int blue=read_signed(&s),red=read_signed(&s);
                        b+=rel(green,b)+blue; r+=rel(green,r)+red; g+=green; acc=green;
                        if (b<0 || b>255 || g<0 || g>255 || r<0 || r>255) { s.error=1; break; }
                    }
                }
                p[0]=(uint8_t)b; p[1]=(uint8_t)g; p[2]=(uint8_t)r; p[3]=128;
            }
            repeat=!repeat;
        }
    }
    if (consumed) *consumed=s.bit;
    return s.error?-3:0;
}
