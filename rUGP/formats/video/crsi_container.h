#ifndef RUGP_CRSI_CONTAINER_H
#define RUGP_CRSI_CONTAINER_H
#include <stdint.h>
#include <stddef.h>
typedef struct {
    unsigned independent, mode, parameter;
    uint32_t offset, size;
    const uint8_t *payload;
} CrsiFrame;
typedef struct {
    unsigned width,height,rate,count;
    size_t table_end;
    const uint8_t *data;
    size_t size;
} CrsiSequence;
/* Views borrow the caller's immutable file buffer. Scoped schema-1 parent;
 * codec-0/1 rows only. frame_capacity must cover count, obtained from header.
 * Passing frames=NULL validates the full container and returns metadata. */
int crsi_parse(const uint8_t *data,size_t size,CrsiSequence *sequence,
               CrsiFrame *frames,size_t frame_capacity);
/* Serialize a COMPLETE frame plan against the validated parent's unchanged
 * header/count/timing. Caller owns prediction consistency for changed frames.
 * Returns required bytes through written when output=NULL. Input and output
 * storage must not overlap. Offsets are recomputed; placement padding is not
 * part of the record. Unsupported flags/codecs fail before writing. */
int crsi_write(const CrsiSequence *sequence,const CrsiFrame *frames,size_t count,
               uint8_t *output,size_t capacity,size_t *written);
#endif
