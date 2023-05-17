"""
   Execution:  python msd.py < input.txt

   Data files:   https://algs4.cs.princeton.edu/51radix/words3.txt

   % python -m algs4.quick_three_string < data/words3.txt
   all
   bad
   bed
   bug
   dad
   ...
   yes
   yet
   zoo

   % python -m algs4.quick_three_string < data/shells.txt
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

import random

class Quick3String:
    CUTOFF = 15
    @classmethod
    def sort(cls, a):
        random.shuffle(a)
        cls._sort(a, 0, len(a) - 1, 0)

    @classmethod
    def _sort(cls, a, lo, hi, d):
        if hi - lo <= cls.CUTOFF:
            cls.insertion(a, lo, hi, d)
            return
        lt = lo
        gt = hi
        v = cls.char_at(a[lo], d)
        i = lo + 1
        while i <= gt:
            t = cls.char_at(a[i], d)
            if  t < v:
                a[lt], a[i] = a[i], a[lt]
                lt += 1
                i += 1
            elif t > v:
                a[i], a[gt] = a[gt], a[i]
                gt -= 1
            else:
                i += 1
        cls._sort(a, lo, lt - 1, d)
        if v >= 0:
            cls._sort(a, lt, gt - 1, d + 1)
        cls._sort(a, gt, hi, d)
        

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
        for i in range(d, min(len(v), len(w))):
            if v[i] > w[i]:
                return False
            if v[i] < w[i]:
                return True
        return len(v) < len(w)


if __name__ == '__main__':
    import sys
    words = []
    for line in sys.stdin:
        words.extend(line.split())
    Quick3String.sort(words)
    for item in words:
        print(item)