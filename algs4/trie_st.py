"""
Execution:    python trie_st.py < words.txt
Dependencies: StdIn.java
Data files:   https://algs4.cs.princeton.edu/52trie/shellsST.txt
 
A string symbol table for extended ASCII strings, implemented
using a 256-way trie.
 
% python -m algs4.trie_st < data/shellsST.txt 
by 4
sea 6
sells 1
she 0
shells 3
shore 7
the 5
 
longestPrefixOf("shellsort"): 
shells 
 
keysWithPrefix("shor"): 
shore 
 
keysThatMatch(".he.l."): 
shells

"""

from typing import Any, Optional

from algs4.link_list import Queue


class Node:
    R = 256

    def __init__(self):
        self.val = None
        self.next = [None] * self.R

class TrieST:

    def __init__(self):
        self._size = 0
        self.root = None

    def get(self, key: str):
        x = self._get(self.root, key, 0)
        if x is None:
            return None
        return x.val
    
    def _get(self, x: Node, key: str, d: int) -> Node:
        if x is None:
            return None
        if d == len(key):
            return x
        c = ord(key[d])
        return self._get(x.next[c], key, d + 1)
    
    def put(self, key: str, val: Any):
        self.root = self._put(self.root, key, val ,0)

    def _put(self, x: Node, key: str, val: Any, d: int) -> Node:
        if x is None:
            x = Node()
        if d == len(key):
            x.val = val
            self._size += 1
            return x
        c = ord(key[d])
        x.next[c] = self._put(x.next[c], key, val, d + 1)
        return x
    
    def collect(self, x: Node, pre: str, q: Queue, pat: Optional[str] = None):
        if x is None:
            return
        if pat is None:
            if x.val is not None:
                q.enqueue(pre)
            for c, node in enumerate(x.next):
                self.collect(node, pre + chr(c), q)
        else:
            if len(pre) == len(pat):
                if x.val is not None:
                    q.enqueue(pre)
                return
            for c, node in enumerate(x.next):
                if pat[len(pre)] == '.' or pat[len(pre)] == chr(c):
                    self.collect(node, pre + chr(c), q, pat)

    def keys_with_prefix(self, pre: str):
        q = Queue()
        x = self._get(self.root, pre, 0)
        self.collect(x, pre, q)
        return q
    
    def keys(self):
        return self.keys_with_prefix('')

    def keys_that_match(self, pat: str):
        q = Queue()
        self.collect(self.root, '', q, pat)
        return q

    def search(self, x: Node, s: str, d: int, length: int) -> int:
        if x is None:
            return length
        if x.val is not None:
            length = d
        if d == len(s):
            return length
        return self.search(x.next[ord(s[d])], s, d + 1, length)

    def longest_prefix_of(self, s: str):
        pre_len = self.search(self.root, s, 0, 0)
        return s[:pre_len]
    
    def delete(self, s: str):
        self.root = self._delete(self.root, s, 0)

    def _delete(self, x: Node, s: str, d: int) -> Optional[Node]:
        if x is None:
            return None
        if d == len(s):
            if x.val is not None:
                self._size -= 1
            x.val = None
        else:
            c = ord(s[d])
            x.next[c] = self._delete(x.next[c], s, d + 1)
        if x.val is not None:
            return x
        for node in x.next:
            if node.val is not None:
                return x
        return None
    
    def size(self):
        return self._size
    
    def contains(self, key):
        return self.get(key) is not None
    
    def empty(self, key):
        return not self._size
    

if __name__ == "__main__":
    import sys
    st = TrieST()
    i = 0
    for line in sys.stdin:
        for key in line.split():
            st.put(key, i)
            i += 1
    if st.size() < 100:
        for key in st.keys():
            print(key, " ", st.get(key))
    print()
    print('longestPrefixOf("shellsort"):')
    print(st.longest_prefix_of("shellsort"))
    print()

    print('longestPrefixOf("quicksort"):')
    print(st.longest_prefix_of("quicksort"))
    print()

    print('keysWithPrefix("shor"):')
    for s in st.keys_with_prefix("shor"):
        print(s)
    print()

    print('keysThatMatch(".he.l."):')
    for s in st.keys_that_match(".he.l."):
        print(s)
