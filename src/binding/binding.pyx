import cython
from libc.stdint cimport uint8_t, uint64_t
from libc.stddef cimport size_t
from libc.stdlib cimport malloc
from libc.string cimport memcpy
from secrets import randbits
from hashlib import sha256

__all__ = ['SHISHUA']

cdef extern from "shishua.h":
    struct prng_state:
        uint64_t state[16]
        uint64_t output[16]
        uint64_t counter[4]

    cdef prng_state prng_init(uint64_t seed[4])
    cdef void prng_gen(prng_state *state, uint8_t *buf, size_t size)

cdef class SHISHUA:
    """
    SHISHUA(seed=None)

    SHISHUA generator

    Fast strong pseudo-random number generator.

    Parameters
    ----------
    seed : {None, int, array_like[ints], str}, optional
        A seed to initialize the PRNG. If None, then fresh,
        unpredictable entropy will be pulled from the OS.
    """
    cdef prng_state rng_state

    def __init__(self, seed=None):
        cdef uint64_t rawseed[4]
        if seed is None:
            for i in range(4):
                rawseed[i] = randbits(64)
        elif isinstance(seed, list):
            rawseed[:] = seed
        elif isinstance(seed, str):
            sha = sha256()
            sha.update(seed.encode("utf-8"))
            h = sha.digest()
            rawseed[0] = int.from_bytes(h[ 0: 4], byteorder='little')
            rawseed[1] = int.from_bytes(h[ 4: 8], byteorder='little')
            rawseed[2] = int.from_bytes(h[ 8:12], byteorder='little')
            rawseed[3] = int.from_bytes(h[12:16], byteorder='little')
        elif isinstance(seed, int):
            rawseed[0] = seed
            rawseed[1] = rawseed[2] = rawseed[3] = 0
        self.rng_state = prng_init(rawseed)

    def random_raw(self, size=1):
        """
        random_raw(self, size=1)

        Return randoms as generated by the underlying BitGenerator

        Parameters
        ----------
        size : int
            Output buffer size, in bytes.

        Returns
        -------
        out : bytes
            Drawn samples.
        """
        # TODO: add buffer for perf + to address
        # sizes that are not multiples of 128 bytes.
        bytesize = size if size % 128 == 0 else size * 128
        buf = bytearray(bytesize)
        cdef prng_state rng_state
        memcpy(&rng_state, &self.rng_state, sizeof(prng_state))
        prng_gen(&rng_state, buf, bytesize)
        return bytes(buf[:size])
