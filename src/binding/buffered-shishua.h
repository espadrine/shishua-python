#ifndef BUFFERED_SHISHUA_H
#define BUFFERED_SHISHUA_H
#include "shishua.h"
#include <stdio.h>
#define BUFSIZE (1 << 17)

typedef struct buffered_shishua_state {
  prng_state state;
  uint8_t buffer[BUFSIZE];
  size_t buf_index;
} buffered_shishua_state;

void buffered_shishua_fill_buffer(buffered_shishua_state *bss) {
  prng_gen(&bss->state, bss->buffer, BUFSIZE);
  bss->buf_index = 0;
}

// Initializes the buffered state.
// Returns a pointer to a newly allocated instance.
buffered_shishua_state *buffered_shishua_new(uint64_t seed[4]) {
  buffered_shishua_state *bss;
  posix_memalign(&bss, 128, sizeof(buffered_shishua_state));
  prng_init(&bss->state, seed);
  buffered_shishua_fill_buffer(bss);
  return bss;
}

void buffered_shishua_delete(buffered_shishua_state *bss) {
  free(bss);
}

// buf: byte buffer.
// size: number of bytes to fill in the buffer.
inline void buffered_shishua_fill(buffered_shishua_state *bss, uint8_t *buf, size_t size) {
  // bl: bytes left to fill.
  // bf: bytes already filled.
  // chunk_size: number of bytes that we fill in a single loop.
  size_t bl = size, bf = 0, chunk_size;
  while (bl > 0) {
    // The number of bytes we add is the min
    // between the available bytes in the internal buffer,
    // and the bytes left to fill.
    chunk_size = BUFSIZE - bss->buf_index;
    if (chunk_size > bl) {
      chunk_size = bl;
    }
    memcpy(&buf[bf], &bss->buffer[bss->buf_index], chunk_size);
    bss->buf_index += chunk_size;
    bf += chunk_size;
    bl -= chunk_size;
    if (bss->buf_index >= BUFSIZE) {
      buffered_shishua_fill_buffer(bss);
    }
  }
}

/* BitGenerator primitives for numpy compatibility. */

uint64_t shishua_next_uint64(void *st) {
  buffered_shishua_state *state = st;
  uint64_t r;
  buffered_shishua_fill(state, (uint8_t *)&r, 8);
  return r;
}

uint32_t shishua_next_uint32(void *st) {
  buffered_shishua_state *state = st;
  uint32_t r;
  buffered_shishua_fill(state, (uint8_t *)&r, 4);
  return r;
}

double shishua_next_double(void *st) {
  return shishua_next_uint64(st) / 0x10000000000000000;
}

#undef BUFSIZE
#endif // BUFFERED_SHISHUA_H
