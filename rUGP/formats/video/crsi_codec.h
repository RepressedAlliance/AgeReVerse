#ifndef RUGP_CRSI_CODEC_H
#define RUGP_CRSI_CODEC_H
#include <stddef.h>
#include <stdint.h>

/* Observed codec-1 profiles: 0575/8, 056d/32767, 052c/32767, 0524/32767. */
int crsi_decode_codec1(const uint8_t *data,size_t size,unsigned width,
                        unsigned height,int independent,unsigned mode,
                        unsigned parameter,uint8_t *bgrx,size_t surface_size,
                        size_t *consumed_bits);

/* Scoped PM codec 1: mode 0x0575, parameter 8, even-sized full surfaces.
 * Output is top-down native BGRX (X is NOT PNG alpha). For dependent frames
 * the caller supplies the previous decoded surface in the same buffer.
 * No game executable, operating-system API, or Python dependency. */
int crsi_decode_0575(const uint8_t *data, size_t size, unsigned width,
                     unsigned height, int independent, uint8_t *bgrx,
                     size_t surface_size, size_t *consumed_bits);
/* Research codec-1 encoder: lossy 2x2 colour reconstruction, explicit
 * independent/dependent choice, no temporal mode-selection heuristic.
 * previous is required for a dependent frame. reconstructed receives the
 * exact native BGRX result, to use as the next frame's reference.
 * This is not an approved replacement for the lossless subtitle producer. */
size_t crsi_bound_0575(unsigned width,unsigned height);
int crsi_encode_0575(const uint8_t *rgb,size_t rgb_size,unsigned width,
                     unsigned height,int independent,const uint8_t *previous,
                     size_t previous_size,uint8_t *data,size_t capacity,
                     size_t *written,uint8_t *reconstructed,size_t surface_size);
/* Opaque-only mode 0x03ff. Reject transparent input profiles explicitly.
 * Encoder input is top-down RGB; decoder output is native BGR/0x80.
 * The encoder uses the same literal/repeat/above-copy decisions as the
 * existing compact producer. Buffer bound includes row metadata. */
size_t crsi_bound_03ff(unsigned width, unsigned height);
int crsi_encode_03ff(const uint8_t *rgb, size_t rgb_size, unsigned width,
                     unsigned height, uint8_t *data, size_t capacity,
                     size_t *written);
int crsi_decode_03ff(const uint8_t *data, size_t size, unsigned width,
                     unsigned height, uint8_t *bgrx, size_t surface_size,
                     size_t *consumed_bits);
#endif
