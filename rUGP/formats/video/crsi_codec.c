#include "crsi_codec.h"
#include <math.h>
#include <stdlib.h>
#include <string.h>

typedef struct { const uint8_t *p; size_t n, bit; int error; } Bits;
typedef struct { int y, u, v; } Color;
static unsigned get(Bits *b, unsigned n) {
    unsigned v=0;
    if (b->bit+n>b->n*8) { b->error=1; return 0; }
    for (unsigned i=0;i<n;i++,b->bit++)
        v|=((b->p[b->bit/8]>>(b->bit%8))&1U)<<i;
    return v;
}
static unsigned run(Bits *b) {
    if (!get(b,1)) return 1;
    unsigned v=1;
    for (unsigned i=0;i<13;i++) {
        v=v*2+get(b,1);
        if (!get(b,1)) return v;
    }
    b->error=1; return 0;
}
static int signed_code(Bits *b) {
    unsigned sign=get(b,1), more=get(b,1), v=1, used=2;
    while (more && used<13) {
        v=v*2+get(b,1); used++;
        if (used<13) { more=get(b,1); used++; }
    }
    return sign?-(int)v:(int)v;
}
static int clip(int x,int lo,int hi) { return x<lo?lo:x>hi?hi:x; }
/* Arithmetic right shift without implementation-defined signed shifts. */
static int asr(int x,unsigned n) {
    return x>=0?x/(1<<n):-1-((-1-x)/(1<<n));
}
static const int8_t small_delta[24][8]={
    {-32,16,-8,-2,0,2,6,40}, {-32,16,-8,-2,1,3,7,40},
    {-32,16,-7,-1,1,3,8,40}, {-32,16,-7,-1,2,4,8,40},
    {-32,-8,-2,0,2,4,8,40}, {-32,-8,-2,0,3,5,9,40},
    {-32,-8,-2,0,3,5,10,40}, {-32,-8,-2,0,4,6,12,40},
    {-32,-8,-3,1,4,8,16,40}, {-32,-8,-3,1,5,9,17,40},
    {-32,-9,-3,1,5,9,18,40}, {-32,-9,-3,1,6,10,18,40},
    {-32,-10,-3,1,6,12,20,40}, {-32,-10,-3,2,7,12,20,40},
    {-32,-11,-4,2,7,14,23,40}, {-32,-11,-4,2,7,14,23,40},
    {-30,-11,-4,3,8,15,24,40}, {-30,-11,-4,3,8,16,25,40},
    {-29,-12,-4,3,8,17,27,40}, {-29,-12,-4,3,8,17,27,40},
    {-28,-12,-4,4,9,18,28,40}, {-28,-12,-4,4,9,18,29,40},
    {-28,-12,-4,4,9,19,30,40}, {-28,-12,-4,4,9,19,30,40}
};
static int delta_value(int d,unsigned code) {
    if (abs(d)<24) return d<0?-small_delta[-d][code]:small_delta[d][code];
    /* Keep the native SSE2 evaluation order: two otherwise equivalent
     * products round differently at d=-225/code=7 and d=225/code=1. */
    double scale=(10.0/(abs(d)+25)+0.16)*d;
    return (int)floor((code-4.0)*scale+d*0.5+0.5);
}
static int residual(Bits *b,int d) {
    unsigned code;
    if (get(b,1)) code=4;
    else if (get(b,1)) code=get(b,1)?3:5;
    else if (get(b,1)) code=get(b,1)?2:6;
    else { unsigned c=get(b,2); if (!c) return (int)get(b,7)*4-256; code=c==1?1:c==2?0:7; }
    if (d<-256 || d>255) { b->error=1; return 0; }
    return delta_value(d,code);
}
static Color mean(Color a,Color b) {
    Color c={asr(a.y+b.y,1),asr(a.u+b.u,1),asr(a.v+b.v,1)}; return c;
}
static void rgb(Color c,uint8_t p[4]) {
    int b=asr(c.u*29032,16),g=asr(c.u*-5630,16),
        r=asr(c.v*22970,16),q=asr(c.v*-11702,16);
    p[0]=(uint8_t)clip(c.y+b,0,255); p[1]=(uint8_t)clip(c.y+g+q,0,255);
    p[2]=(uint8_t)clip(c.y+r,0,255); p[3]=(uint8_t)clip(c.y+q,0,255);
}
static void put(uint8_t *p,const uint8_t v[4],int independent) {
    for (int k=0;k<4;k++) p[k]=independent?v[k]:(uint8_t)clip((int)p[k]+2*((int)v[k]-128),0,255);
}
int crsi_decode_codec1(const uint8_t *data,size_t size,unsigned width,
                     unsigned height,int independent,unsigned mode,unsigned parameter,
                     uint8_t *out,size_t capacity,size_t *consumed_bits) {
    if (!((mode==0x575 && parameter==8) ||
          ((mode==0x56d || mode==0x52c || mode==0x524) && parameter==32767))) return -1;
    if (!data || !out || !width || !height || (width|height)&1 ||
        width>4096 || height>4096 || capacity<(size_t)width*height*4 ||
        size>16777216 || size<4 || (independent!=0 && independent!=1)) return -1;
    Bits bits={data,size,0,0}; Bits *b=&bits;
    unsigned bbits=(mode&7)+1,gbits=((mode>>3)&7)+1,rbits=((mode>>6)&7)+1;
    int ystep=1<<(8-gbits),ustep=1<<(10-rbits),vstep=1<<(10-bbits);
    Color *above=calloc(width/2,sizeof(*above));
    if (!above) return -2;
    for (unsigned y=0;y<height && !b->error;y+=2) {
        Color state={128,0,0}, prev_top={0,0,0};
        unsigned x=0;
        while (x<width && !b->error) {
            unsigned n=run(b);
            if (!n || n>(width-x)/2) { b->error=1; break; }
            uint8_t last[4]={0};
            for (unsigned i=0;i<n && !b->error;i++,x+=2) {
                Color left=state, up=above[x/2], tr;
                int copy=(int)get(b,1);
                if (copy) state=up;
                else {
                    state.y=asr(clip(state.y+up.y,-32768,32767),1);
                    state.u=asr(clip(state.u+up.u+independent,-32768,32767),1);
                    state.v=asr(clip(state.v+up.v+independent,-32768,32767),1);
                    if (get(b,1)) {
                        int s=signed_code(b);
                        /* The keyframe path uses TWO signed-byte saturating
                         * additions, including the signed-byte wrap first. */
                        int d=independent?(int)(int8_t)(s*(ystep/2))*2:s*ystep;
                        state.y=independent?clip(state.y+d,0,255):state.y+d;
                    }
                    if (independent) state.y&=255;
                    else { state.y=(int16_t)(state.y&(65536-ystep)); state.u=(int16_t)(state.u&(65536-ustep)); state.v=(int16_t)(state.v&(65536-vstep)); }
                    if (get(b,1)) state.v=clip(state.v+signed_code(b)*vstep,-32768,32767);
                    if (get(b,1)) {
                        size_t before=b->bit;
                        int delta=signed_code(b);
                        state.u=clip(state.u+delta*ustep,-32768,32767);
                        /* Native PSLLQ 40 also moves the lookup entry's
                         * length byte into the adjacent V word. At rbits=5,
                         * lengths >=8 add one to V; at rbits=6 it vanishes.
                         * Preserve this observable MMX packing side effect. */
                        state.v=clip(state.v+(int)((b->bit-before)>>(rbits-2)),-32768,32767);
                    }
                }
                int flat=(int)get(b,1), broadcast=0;
                if (!independent) { broadcast=flat; if (!flat) flat=(int)get(b,1); }
                uint8_t pixels[4][4]; /* TL, TR, BL, BR */
                rgb(state,pixels[3]);
                if (flat) {
                    tr=state;
                    for (int p=0;p<3;p++) for (int k=0;k<4;k++) pixels[p][k]=pixels[3][k];
                } else {
                    tr=copy?state:mean(up,state);
                    if (!copy) tr.y=clip(up.y+residual(b,state.y-up.y),0,255);
                    Color bl=mean(left,state); bl.y=left.y+residual(b,state.y-left.y);
                    Color tl=mean(prev_top,tr); tl.y=prev_top.y+residual(b,tr.y-prev_top.y);
                    rgb(tr,pixels[1]); rgb(bl,pixels[2]); rgb(tl,pixels[0]);
                }
                size_t pos=((size_t)y*width+x)*4;
                if (broadcast) {
                    uint8_t base[4]; for (int k=0;k<4;k++) base[k]=out[pos+width*4+4+k];
                    for (int p=0;p<4;p++) {
                        uint8_t *dst=out+pos+(p/2)*width*4+(p%2)*4;
                        for (int k=0;k<4;k++) dst[k]=base[k];
                    }
                }
                for (int p=0;p<4;p++) put(out+pos+(p/2)*width*4+(p%2)*4,pixels[p],independent);
                for (int k=0;k<4;k++) last[k]=pixels[3][k];
                above[x/2]=state; prev_top=tr;
            }
            if (x>=width || b->error) break;
            n=run(b);
            if (!n || n>(width-x)/2) { b->error=1; break; }
            if (independent && n>=parameter) {
                static const int yy[4]={0,1,2,4},cc[4]={-12,-4,0,4};
                unsigned code=get(b,6);
                state.y=clip(state.y+yy[code&3],0,255);
                state.u=clip(state.u+cc[(code>>4)&3],-32768,32767);
                state.v=clip(state.v+cc[(code>>2)&3],-32768,32767);
                rgb(state,last);
            }
            for (unsigned i=0;i<n;i++,x+=2) {
                size_t pos=((size_t)y*width+x)*4;
                for (int p=0;p<4;p++) put(out+pos+(p/2)*width*4+(p%2)*4,last,independent);
                above[x/2]=state;
            }
            prev_top=state;
        }
    }
    free(above);
    if (consumed_bits) *consumed_bits=b->bit;
    return b->error?-3:0;
}

int crsi_decode_0575(const uint8_t *data,size_t size,unsigned width,unsigned height,
                     int independent,uint8_t *out,size_t capacity,size_t *consumed_bits) {
    return crsi_decode_codec1(data,size,width,height,independent,0x575,8,out,capacity,consumed_bits);
}

typedef struct { uint8_t *p; size_t n,bit; int error; } Writer;
static void write_bits(Writer *w,unsigned v,unsigned n) {
    if (w->bit+n>w->n*8) { w->error=1; return; }
    for (unsigned i=0;i<n;i++,w->bit++) w->p[w->bit/8]|=(uint8_t)(((v>>i)&1)<<(w->bit%8));
}
static unsigned log2u(unsigned v) { unsigned n=0; while (v>1) { v>>=1; n++; } return n; }
static void write_run(Writer *w,unsigned v) {
    write_bits(w,v!=1,1);
    unsigned k=log2u(v);
    while (k) { k--; write_bits(w,(v>>k)&1,1); write_bits(w,k!=0,1); }
}
static void write_delta(Writer *w,int v) {
    write_bits(w,v!=0,1);
    if (!v) return;
    if (abs(v)>127) { w->error=1; return; }
    write_bits(w,v<0,1);
    unsigned mag=(unsigned)abs(v),k=log2u(mag);
    while (k) { k--; write_bits(w,1,1); write_bits(w,(mag>>k)&1,1); }
    if (mag<64) write_bits(w,0,1);
}
static unsigned pixel_error(Color c,const uint8_t target[3]) {
    uint8_t p[4]; rgb(c,p); unsigned error=0;
    for (int k=0;k<3;k++) { int d=(int)p[k]-target[k]; error+=(unsigned)(d*d); }
    return error;
}
static int round_div(int v,int divisor) { return v<0?-((-v+divisor/2)/divisor):(v+divisor/2)/divisor; }
static Color choose_base(Color predictor,const uint8_t target[3],int independent,int steps[3]) {
    /* Initial RGB->Y/Cb/Cr estimate, then search the representable lattice.
     * Actual scoring uses the native fixed-point inverse and clipping. */
    int y=(299*(int)target[2]+587*(int)target[1]+114*(int)target[0]+500)/1000;
    int u=round_div(((int)target[0]-y)*65536,29032);
    int v=round_div(((int)target[2]-y)*65536,22970);
    int sy=round_div(y-predictor.y,2),su=round_div(u-predictor.u,16),sv=round_div(v-predictor.v,16);
    unsigned best=~0U; Color result=predictor;
    for (int a=-1;a<=1;a++) for (int b=-1;b<=1;b++) for (int c=-1;c<=1;c++) {
        int dy=clip(sy+a,-127,127),du=clip(su+b,-127,127),dv=clip(sv+c,-127,127);
        if (!independent && (predictor.y+dy*2<0 || predictor.y+dy*2>254)) continue;
        Color value={clip(predictor.y+dy*2,0,255),predictor.u+du*16,predictor.v+dv*16};
        if (!independent) value.y&=254;
        unsigned err=pixel_error(value,target);
        if (err<best) { best=err; result=value; steps[0]=dy; steps[1]=dv; steps[2]=du; }
    }
    return result;
}
static Color encode_detail(Writer *w,Color base,Color end,const uint8_t target[3],int clip_y) {
    static const unsigned codes[8]={16,8,12,6,1,2,4,24},lengths[8]={5,5,4,3,1,3,4,5};
    Color chroma=mean(base,end),best=chroma;
    int d=end.y-base.y; unsigned err_best=~0U,choice=0;
    for (unsigned i=0;i<136;i++) {
        int delta=i<8?delta_value(d,i):((int)i-8)*4-256;
        Color value=chroma; value.y=base.y+delta;
        if (clip_y) value.y=clip(value.y,0,255);
        unsigned err=pixel_error(value,target);
        if (err<err_best) { err_best=err; choice=i; best=value; }
    }
    if (choice<8) write_bits(w,codes[choice],lengths[choice]);
    else { write_bits(w,0,5); write_bits(w,choice-8,7); }
    return best;
}
size_t crsi_bound_0575(unsigned w,unsigned h) {
    return w && h && !((w|h)&1) && w<=4096 && h<=4096?(size_t)w*h*16+h*64+64:0;
}
int crsi_encode_0575(const uint8_t *input,size_t input_size,unsigned w,unsigned h,
                     int independent,const uint8_t *previous,size_t previous_size,
                     uint8_t *data,size_t capacity,size_t *written,uint8_t *reconstructed,size_t surface_size) {
    size_t bound=crsi_bound_0575(w,h),pixels=(size_t)w*h;
    if (!bound || !input || !data || !written || !reconstructed || input_size!=pixels*3 ||
        capacity<4 || capacity>SIZE_MAX/8 || surface_size<pixels*4 ||
        (independent!=0 && independent!=1) || (!independent && (!previous || previous_size<pixels*4))) return -1;
    Color *above=calloc(w/2,sizeof(*above)); if (!above) return -2;
    memset(data,0,capacity); Writer writer={data,capacity,0,0};
    for (unsigned y=0;y<h && !writer.error;y+=2) {
        Color state={128,0,0},prev_top={0,0,0};
        write_run(&writer,w/2);
        for (unsigned x=0;x<w && !writer.error;x+=2) {
            uint8_t target[4][3];
            for (unsigned p=0;p<4;p++) {
                size_t pos=(size_t)(y+p/2)*w+x+p%2;
                for (unsigned k=0;k<3;k++) {
                    int v=input[pos*3+2-k];
                    if (!independent) v=128+round_div(v-previous[pos*4+k],2);
                    target[p][k]=(uint8_t)clip(v,0,255);
                }
            }
            Color left=state,up=above[x/2],predictor=mean(left,up);
            if (independent) {
                predictor.u=asr(left.u+up.u+1,1); predictor.v=asr(left.v+up.v+1,1);
            } else { predictor.u=(int16_t)(predictor.u&65520); predictor.v=(int16_t)(predictor.v&65520); }
            int steps[3]; state=choose_base(predictor,target[3],independent,steps);
            write_bits(&writer,0,1); /* update the spatial predictor */
            for (int k=0;k<3;k++) write_delta(&writer,steps[k]);
            write_bits(&writer,0,independent?1:2); /* four-pixel detail */
            Color tr=encode_detail(&writer,up,state,target[1],1);
            (void)encode_detail(&writer,left,state,target[2],0);
            (void)encode_detail(&writer,prev_top,tr,target[0],0);
            above[x/2]=state; prev_top=tr;
        }
    }
    free(above);
    *written=((writer.bit+15)/16)*2; if (*written<4) *written=4;
    if (writer.error || *written>capacity) return -3;
    if (!independent) memmove(reconstructed,previous,pixels*4);
    return crsi_decode_0575(data,*written,w,h,independent,reconstructed,surface_size,NULL);
}
