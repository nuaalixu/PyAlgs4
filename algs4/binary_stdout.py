import sys


class BinaryStdout:
    buffer = 0
    n = 0

    @classmethod
    def write_byte(cls, b):
        for i in range(8):
            bit = ((b >> (8 - i - 1)) & 1) == 1
            cls.write_bit(bit)

    @classmethod
    def write_int(cls, x):
        """write in big endian byte ordering."""
        cls.write_byte((x >> 24) & 0xff)
        cls.write_byte((x >> 16) & 0xff)
        cls.write_byte((x >> 8) & 0xff)
        cls.write_byte(x & 0xff)

    @classmethod
    def write_bit(cls, bit):
        cls.buffer <<= 1
        if bit:
            cls.buffer |= 1
        cls.n += 1
        if cls.n == 8:
            cls.clear_buffer()

    @classmethod
    def clear_buffer(cls):
        if cls.n == 0:
            return
        if cls.n > 0:
            cls.buffer <<= (8 - cls.n)
        sys.stdout.buffer.write(bytes([cls.buffer]))
        cls.n = 0
        cls.buffer = 0

    @classmethod
    def close(cls):
        cls.clear_buffer()