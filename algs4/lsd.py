"""
   Execution:  python lsd.py < input.txt

   Data files:   https://algs4.cs.princeton.edu/51radix/words3.txt

   % python -m algs4.lsd < data/words3.txt
   all
   bad
   bed
   bug
   dad
   ...
   yes
   yet
   zoo
"""

from typing import List

class LSD:
    R = 256  # alphabet

    @classmethod
    def sort(cls, a: List[str], W: int):
        N = len(a)
        aux = [''] * N
        if W > N:
            W = N
        for d in range(W - 1, -1, -1):
            count = [0] * (cls.R + 1)
            for s in a:
                count[ord(s[d]) + 1] += 1
            for i in range(cls.R):
                count[i + 1] += count[i]
            for s in a:
                aux[count[ord(s[d])]] = s
                count[ord(s[d])] += 1
            for i, s in enumerate(aux):
                a[i] = s
        return a
    

if __name__ == '__main__':
    import sys
    words = []
    for line in sys.stdin:
        words.extend(line.split())
    LSD.sort(words, len(words[0]))
    for item in words:
        print(item)