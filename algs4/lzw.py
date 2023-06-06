"""
 *  Execution:    python -m algs4.lzw - < input.txt   (compress)
 *  Execution:    python -m algs4.lzw + < input.txt   (expand)
 *  Data files:   https://algs4.cs.princeton.edu/55compression/abraLZW.txt
 *                https://algs4.cs.princeton.edu/55compression/ababLZW.txt
 *
 *  % python -m algs4.lzw - < data/abraLZW.txt | python -m algs4.lzw +
 *  ABRACADBRACRAACRA
 *
"""

from algs4.binary_stdin import BinaryStdin
from algs4.binary_stdout import BinaryStdout
from algs4.tst import TST


class LZW:
    R = 256  # number of input chars
    L = 4096 # number of codewords = 2^W
    W = 12  # codeword width

    @classmethod
    def compress(cls):
        inp = BinaryStdin.read_str()
        st = TST()

        for i in range(cls.R):
            st.put("" + chr(i), i)

        code = cls.R + 1  # R is codeword for EOF

        while len(inp) > 0:
            s = st.longest_prefix_of(inp)
            BinaryStdout.write_bits(st.get(s), cls.W)
            t = len(s)
            if t < len(inp)  and code < cls.L:
                st.put(inp[:t+1], code)
                code += 1
            inp = inp[t:]
        BinaryStdout.write_bits(cls.R, cls.W)
        BinaryStdout.close()

    @classmethod
    def expand(cls):
        st = [''] * cls.L

        # initialize symbol table with all 1-character strings
        for i in range(cls.R):
            st[i] = '' + chr(i)
        i += 1
        st[i] = ''  # (unused) lookahead for EOF

        codeword = BinaryStdin.read_int_r(cls.W)
        # expanded message is empty string
        if codeword == cls.R:
            return
        val = st[codeword]

        while True:
            BinaryStdout.write_str(val)
            codeword = BinaryStdin.read_int_r(cls.W)
            if codeword == cls.R: break
            s = st[codeword]
            if i == codeword:
                s = val + val[0]  # for special case
            if (i < cls.L):
                st[i] = val + s[0]
                i += 1
            val = s
        BinaryStdout.close()


if __name__ == '__main__':
    import sys
    if sys.argv[1] == '-':
        LZW.compress()
    elif sys.argv[1] == '+':
        LZW.expand()
    else:
        raise ValueError('Illegal command line argument')