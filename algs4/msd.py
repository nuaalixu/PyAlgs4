"""
   Execution:  python msd.py < input.txt

   Data files:   https://algs4.cs.princeton.edu/51radix/words3.txt

   % python -m algs4.msd < data/words3.txt
   all
   bad
   bed
   bug
   dad
   ...
   yes
   yet
   zoo

   % python -m algs4.msd < data/shells.txt
   are
   by
   sea
   seashells
   seashells
   sells
   sells
   she
   she
   shells
   shore
   surely
   the
   the
"""


class MSD:
    R = 256
    M = 15

    @classmethod
    def char_at(cls, s: str, d: int):
        if d >= len(s):
            return -1
        return ord(s[d])
        
    @classmethod
    def insertion(cls, a, lo, hi, d):
        for i in range(lo, hi + 1):
            for j in range(i, lo, -1):
                if cls.less(a[j], a[j - 1], d):
                    a[j], a[j - 1] = a[j - 1], a[j]
                else:
                    break
    
    @classmethod
    def less(cls, v: str, w: str, d: int):
        for i in range(min(len(v), len(w))):
            if v[i] > w[i]:
                return False
            if v[i] < w[i]:
                return True
        return len(v) < len(w)

    @classmethod
    def sort(cls, a):
        N = len(a)
        cls.aux = [''] * N
        cls._sort(a, 0, N - 1, 0)

    @classmethod
    def _sort(cls, a, lo, hi, d):
        if hi - lo <= cls.M:
            cls.insertion(a, lo, hi, d)
            return
        count = [0] * (cls.R + 2)
        for i in range(lo, hi + 1):
            count[cls.char_at(a[i], d) + 2] += 1
        for i in range(cls.R + 1):
            count[i + 1] += count[i]
        for i in range(lo, hi + 1):
            cls.aux[count[cls.char_at(a[i], d) + 1]] = a[i]
            count[cls.char_at(a[i], d) + 1] += 1
        for i in range(lo, hi + 1):
            a[i] = cls.aux[i - lo]
        for r in range(0, cls.R):
            if count[r + 1] > count[r]:
                cls._sort(a, lo + count[r], lo + count[r + 1] - 1, d + 1)


if __name__ == '__main__':
    import sys
    words = []
    for line in sys.stdin:
        words.extend(line.split())
    MSD.sort(words)
    for item in words:
        print(item)