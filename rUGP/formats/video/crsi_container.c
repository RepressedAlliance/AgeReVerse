#include "crsi_container.h"
#include <string.h>
static unsigned u16(const uint8_t *p) { return p[0]|(unsigned)p[1]<<8; }
static uint32_t u32(const uint8_t *p) { return u16(p)|(uint32_t)u16(p+2)<<16; }
int crsi_parse(const uint8_t *data,size_t size,CrsiSequence *s,CrsiFrame *frames,size_t capacity) {
    static const uint8_t signature[10]={0,1,1,0,0,0,0,0,0,0};
    if (!data || !s || size<26 || memcmp(data,signature,10) || u32(data+14) || u32(data+20)) return -1;
    unsigned w=u16(data+10),h=u16(data+12),rate=u16(data+18),count=u16(data+24);
    if (!w || !h || w>4096 || h>4096 || !rate || !count || count==65535 || (frames && capacity<count)) return -1;
    size_t pos=26,end=0;
    for (unsigned i=0;i<count;i++) {
        if (size-pos<9) return -2;
        unsigned flags=data[pos],mode=u16(data+pos+7),codec=(mode>>10)&7,param=0;
        uint32_t offset=u32(data+pos+1);
        if (flags>1 || (!i && !flags) || u16(data+pos+5) ||
            (mode!=0x03ff && ((mode&~0x05ff) || codec>1))) return -3;
        pos+=9;
        if (codec==1) { if (size-pos<2) return -2; param=u16(data+pos); pos+=2; }
        if (size-pos<4) return -2;
        uint32_t n=u32(data+pos); pos+=4;
        if (!n || n>16777216 || offset!=end || n>size-end) return -3;
        end+=n;
        if (frames) frames[i]=(CrsiFrame){flags,mode,param,offset,n,NULL};
    }
    if (end!=size-pos) return -3;
    if (frames) for (unsigned i=0;i<count;i++) frames[i].payload=data+pos+frames[i].offset;
    *s=(CrsiSequence){w,h,rate,count,pos,data,size}; return 0;
}
static void put16(uint8_t *p,unsigned v) { p[0]=(uint8_t)v;p[1]=(uint8_t)(v>>8); }
static void put32(uint8_t *p,uint32_t v) { put16(p,v&65535);put16(p+2,v>>16); }
int crsi_write(const CrsiSequence *s,const CrsiFrame *frames,size_t count,uint8_t *out,size_t capacity,size_t *written) {
    CrsiSequence validated;
    if (!s || !frames || !written || crsi_parse(s->data,s->size,&validated,NULL,0) || count!=validated.count) return -1;
    uint64_t table=26,payload=0;
    for (size_t i=0;i<count;i++) {
        CrsiFrame f=frames[i]; unsigned codec=(f.mode>>10)&7;
        if (f.independent>1 || (!i && !f.independent) || !f.payload || !f.size || f.size>16777216 ||
            (f.mode!=0x3ff && ((f.mode&~0x5ff) || codec>1)) || (!codec && f.parameter) || f.parameter>65535) return -1;
        table+=codec==1?15:13;payload+=f.size;
    }
    if (payload>UINT32_MAX || table+payload>SIZE_MAX) return -1;
    *written=(size_t)(table+payload);
    if (!out) return 0;
    if (capacity<*written) return -2;
    memcpy(out,s->data,26);size_t pos=26,offset=0;
    for (size_t i=0;i<count;i++) {
        CrsiFrame f=frames[i];out[pos++]=(uint8_t)f.independent;
        put32(out+pos,(uint32_t)offset);pos+=4;put16(out+pos,0);pos+=2;
        put16(out+pos,f.mode);pos+=2;
        if (((f.mode>>10)&7)==1) { put16(out+pos,f.parameter);pos+=2; }
        put32(out+pos,f.size);pos+=4;
        memcpy(out+(size_t)table+offset,f.payload,f.size);offset+=f.size;
    }
    return 0;
}
