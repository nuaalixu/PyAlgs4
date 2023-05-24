"""
 *  Execution:    python kmp.py pattern text
 *
 *  Reads in two strings, the pattern and the input text, and
 *  searches for the pattern in the input text using the
 *  KMP algorithm.
 *
 *  % python -m algs4.kmp abracadabra abacadabrabracabracadabrabrabracad
 *  text:    abacadabrabracabracadabrabrabracad
 *  pattern:               abracadabra
 *
 *  % python -m algs4.kmp rab abacadabrabracabracadabrabrabracad
 *  text:    abacadabrabracabracadabrabrabracad
 *  pattern:         rab
 *
 *  % python -m algs4.kmp bcara abacadabrabracabracadabrabrabracad
 *  text:    abacadabrabracabracadabrabrabracad
 *  pattern:                                   bcara
 *
 *  % python -m algs4.kmp rabrabracad abacadabrabracabracadabrabrabracad
 *  text:    abacadabrabracabracadabrabrabracad
 *  pattern:                        rabrabracad
 *
 *  % python -m algs4.kmp abacad abacadabrabracabracadabrabrabracad
 *  text:    abacadabrabracabracadabrabrabracad
 *  pattern: abacad
 *
"""

class KMP:
    R = 256  # size of alphabet

    def __init__(self, pat):
        # construct dfa
        self.pat = pat
        self.dfa = [[0] * len(pat) for _ in range(self.R)]
        self.dfa[ord(pat[0])][0] = 1
        X = 0
        M = len(pat)
        for j in range(1, M):
            for c in range(self.R):
                self.dfa[c][j] = self.dfa[c][X]
            self.dfa[ord(pat[j])][j] = j + 1
            X = self.dfa[ord(pat[j])][X]

    def search(self, txt):
        """return a offset."""
        j = 0
        M = len(self.pat)
        for i, c in enumerate(txt):
            j = self.dfa[ord(c)][j]
            if j == M:
                return i - M + 1
        return len(txt)
    

if __name__ == "__main__":
    import sys
    pat, txt = sys.argv[1], sys.argv[2]
    kmp = KMP(pat)
    offset = kmp.search(txt)
    print("text:    " + txt)
    print("pattern: ", end="")
    for i in range(offset):
        print(" ", end="")
    print(pat)