/* Standalone C inspector/frame exporter. No engine code is loaded. */
#include "../../formats/video/crsi_codec.h"
#include "../../formats/video/crsi_container.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#ifdef _WIN32
#include <wchar.h>
typedef wchar_t Arg;
#define ARG(x) L##x
#define EQ(a,b) (!wcscmp((a),(b)))
#define OPEN _wfopen
#define TOUL wcstoul
#define ENTRY wmain
#else
typedef char Arg;
#define ARG(x) x
#define EQ(a,b) (!strcmp((a),(b)))
#define OPEN fopen
#define TOUL strtoul
#define ENTRY main
#endif

int ENTRY(int argc,Arg **argv) {
    int inspect=argc==3 && EQ(argv[1],ARG("inspect"));
    int decode=argc==5 && EQ(argv[1],ARG("decode"));
    if (!inspect && !decode) {
        fputs("crsi_tool inspect input.crsi\ncrsi_tool decode input.crsi frame-index output.bgrx\n",stderr); return 2;
    }
    FILE *input=OPEN(argv[2],ARG("rb"));
    if (!input) { perror("input"); return 2; }
    if (fseek(input,0,SEEK_END)) { fclose(input); return 2; }
    long length=ftell(input);
    if (length<26 || length>1073741824 || fseek(input,0,SEEK_SET)) { fclose(input); return 2; }
    uint8_t *data=malloc((size_t)length); CrsiSequence s;
    if (!data) { fclose(input); return 2; }
    size_t got=fread(data,1,(size_t)length,input); fclose(input);
    if (got!=(size_t)length || crsi_parse(data,got,&s,NULL,0)) { fputs("unsupported or malformed CRsi\n",stderr); free(data); return 1; }
    CrsiFrame *frames=calloc(s.count,sizeof(*frames));
    if (!frames || crsi_parse(data,got,&s,frames,s.count)) { free(frames); free(data); return 1; }
    unsigned keyframes=0,codec1=0,lossless=0,other=0;
    for (unsigned i=0;i<s.count;i++) {
        keyframes+=frames[i].independent;
        if (((frames[i].mode>>10)&7)==1) codec1++;
        else if (frames[i].mode==0x3ff) lossless++; else other++;
    }
    if (inspect) {
        printf("{\"width\":%u,\"height\":%u,\"rate\":%u,\"frames\":%u,\"keyframes\":%u,\"codec_1\":%u,\"codec_03ff\":%u,\"other\":%u,\"table_end\":%zu}\n",
            s.width,s.height,s.rate,s.count,keyframes,codec1,lossless,other,s.table_end);
        free(frames); free(data); return 0;
    }
    Arg *end; errno=0; unsigned long index=TOUL(argv[3],&end,10);
    if (errno || end==argv[3] || *end || index>=s.count) { fputs("invalid frame index\n",stderr); free(frames); free(data); return 2; }
    unsigned start=(unsigned)index;
    while (start && !frames[start].independent) start--;
    size_t size=(size_t)s.width*s.height*4; uint8_t *pixels=malloc(size); int result=0;
    if (!pixels) result=1;
    for (unsigned i=start;i<=index && !result;i++) {
        CrsiFrame f=frames[i];
        if (((f.mode>>10)&7)==1)
            result=crsi_decode_codec1(f.payload,f.size,s.width,s.height,f.independent,f.mode,f.parameter,pixels,size,NULL);
        else if (f.mode==0x3ff && f.independent)
            result=crsi_decode_03ff(f.payload,f.size,s.width,s.height,pixels,size,NULL);
        else result=1;
    }
    if (!result) {
        /* Exclusive create: never overwrite an existing export. */
        FILE *output=OPEN(argv[4],ARG("wbx"));
        if (!output) { perror("output"); result=1; }
        else { if (fwrite(pixels,1,size,output)!=size) result=1; if (fclose(output)) result=1; }
    }
    if (result) fputs("frame export failed\n",stderr);
    free(pixels); free(frames); free(data); return result?1:0;
}
