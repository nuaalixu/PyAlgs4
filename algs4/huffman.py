"""
 *  Execution:    python -m algs4.huffman - < input.txt   (compress)
 *  Execution:    python -m algs4.huffman + < input.txt   (expand)
 *  Data files:   https://algs4.cs.princeton.edu/55compression/abra.txt
 *                https://algs4.cs.princeton.edu/55compression/tinytinyTale.txt
 *                https://algs4.cs.princeton.edu/55compression/medTale.txt
 *                https://algs4.cs.princeton.edu/55compression/tale.txt
 *
 *  Compress or expand a binary input stream using the Huffman algorithm.
 *
 *  % python -m algs4.huffman - < data/abra.txt | python -m algs4.binary_dump 60
 *  010100000100101000100010010000110100001101010100101010000100
 *  000000000000000000000000000110001111100101101000111110010100
 *  120 bits
 *
 *  % python -m algs4.huffman - < data/abra.txt | python -m algs4.huffman +
 *  ABRACADABRA!
 *
"""

from algs4.min_pq import MinPQ
from algs4.binary_stdin import BinaryStdin
from algs4.binary_stdout import BinaryStdout


class Node:
    
    def __init__(self, ch, freq, left, right):
        self.ch = ch
        self.freq = freq
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None
    
    def __lt__(self, other):
        return self.freq < other.freq
    
    def __gt__(self, other):
        return not self.__lt__(other)
    
    def __str__(self):
        return f'{self.ch} {self.freq}'
    

class Huffman:
    """The class provides class methods for compressing
    and expanding a binary input using Huffman codes over the 8-bit extended
    ASCII alphabet.
    """
    R = 256

    @classmethod
    def compress(cls):
        s = BinaryStdin.read_str()
        freq = [0] * cls.R
        for c in s:
            freq[ord(c)] += 1

        # build huffman trie
        root = cls.build_trie(freq)

        # build code table
        st = [None] * cls.R
        cls.build_code(st, root, '')

        # print trie for decoder
        cls.write_trie(root)

        # print number of bytes in orginial uncompressed message
        BinaryStdout.write_int(len(s))

        # use Huffman code to encode input
        for c in s:
            code = st[ord(c)]
            for b in code:
                if b == '0':
                    BinaryStdout.write_bit(False)
                else:
                    BinaryStdout.write_bit(True)
        BinaryStdout.close()

    @classmethod
    def expand(cls):
        root = cls.read_trie()
        length = BinaryStdin.read_int()
        for _ in range(length):
            x = root
            while not x.is_leaf():
                bit = BinaryStdin.read_bool()
                if bit:
                    x = x.right
                else:
                    x = x.left
            # only applicable for the 8 bit extended ASCII alphabet
            BinaryStdout.write_byte(ord(x.ch))
        BinaryStdout.close()

    @classmethod
    def build_trie(cls, freq):
        pq = MinPQ()
        for c in range(cls.R):
            if freq[c] > 0:
                pq.insert(Node(chr(c), freq[c], None, None))
        while pq.size() > 1:
            left = pq.del_min()
            right = pq.del_min()
            parent = Node(chr(0), left.freq + right.freq, left, right)
            pq.insert(parent)
        return pq.del_min()
    
    @classmethod
    def build_code(cls, st, x, s):
        if x.is_leaf():
            st[ord(x.ch)] = s
        else:
            cls.build_code(st, x.left, s+'0')
            cls.build_code(st, x.right, s+'1')

    @classmethod
    def write_trie(cls, x):
        if x.is_leaf():
            BinaryStdout.write_bit(True)
            BinaryStdout.write_byte(ord(x.ch))
            return
        BinaryStdout.write_bit(False)
        cls.write_trie(x.left)
        cls.write_trie(x.right)

    @classmethod
    def read_trie(cls):
        is_leaf = BinaryStdin.read_bool()
        if is_leaf:
            return Node(chr(BinaryStdin.read_byte()), 0, None, None)
        return Node(chr(0), 0, cls.read_trie(), cls.read_trie())
    

if __name__ == '__main__':
    import sys
    if sys.argv[1] == '-':
        Huffman.compress()
    else:
        Huffman.expand()
