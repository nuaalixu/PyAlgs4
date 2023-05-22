"""
Execution:    python tst.py < words.txt
Dependencies: StdIn.java
Data files:   https://algs4.cs.princeton.edu/52trie/shellsST.txt
 
A string symbol table for extended ASCII strings, implemented
using a 256-way trie.
 
% python -m algs4.tst < data/shellsST.txt
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

from algs4.link_list import Queue


class Node:
    
    def __init__(self):
        self.c = None
        self.val = None
        self.left = self.mid = self.right = None


class TST:
    
    def __init__(self):
        self.root = None
        self._size = 0

    def get(self, key):
        assert isinstance(key, str)
        if key == '':
            raise ValueError('key must have length >= 1')
        x = self._get(self.root, key, 0)
        if x is None:
            return None
        return x.val

    def _get(self, x, key, d):
        if x is None:
            return None
        c = key[d]
        if c > x.c:
            return self._get(x.right, key, d)
        elif c < x.c:
            return self._get(x.left, key , d)
        elif d < len(key) - 1:
            return self._get(x.mid, key, d + 1)
        else:
            return x
        
    def contains(self, key):
        return self.get(key) is not None
    
    def put(self, key, val):
        if not self.contains(key):
            self._size += 1
        elif val is None:
            self._size -= 1
        self.root = self._put(self.root, key, val, 0)

    def _put(self, x, key, val, d):
        c =key[d]
        if x is None:
            x = Node()
            x.c = c
        if c < x.c:
            x.left = self._put(x.left, key, val, d)
        elif c >x.c:
            x.right = self._put(x.right, key, val, d)
        elif d < len(key) - 1:
            x.mid = self._put(x.mid, key, val, d + 1)
        else:
            x.val = val
        return x
    
    def longest_prefix_of(self, s: str):
        length = self.search(self.root, s, 0, 0)
        return s[:length]

    def search(self, x, s, d, length):
        if x is None or d == len(s):
            return length
        c = s[d]
        if c < x.c:
            return self.search(x.left, s, d, length)
        elif c > x.c:
            return self.search(x.right, s, d, length)
        else: 
            if x.val is not None:
                length = d + 1
            return self.search(x.mid, s, d + 1, length)
        
    def keys_with_prefix(self, prefix):
        queue = Queue()
        node = self._get(self.root, prefix, 0)
        if node is None:
            return queue
        if node.val is not None:
            queue.enqueue(prefix)
        self.collect(node.mid, prefix, queue)
        return queue

    def collect(self, node, prefix, queue, pattern=None):
        if node is None:
            return
        if pattern is None:
            if node.val is not None:
                queue.enqueue(prefix + node.c)
            self.collect(node.left, prefix, queue)
            self.collect(node.mid, prefix + node.c, queue)
            self.collect(node.right, prefix, queue)
        else:
            if len(prefix) == len(pattern):
                return
            c = pattern[len(prefix)]
            if c == '.' or c < node.c:
                self.collect(node.left, prefix, queue, pattern)
            if c == '.' or c == node.c:
                if len(prefix) == len(pattern) - 1 and node.val is not None:
                    queue.enqueue(prefix + node.c)
                self.collect(node.mid , prefix + node.c, queue, pattern)
            if c == '.' or c > node.c:
                self.collect(node.right, prefix, queue, pattern)
            
    def keys(self):
        queue = Queue()
        self.collect(self.root, '', queue)
        return queue
    
    def keys_that_match(self, pattern):
        queue = Queue()
        self.collect(self.root, '', queue, pattern)
        return queue
    
    def delete(self, key):
        self.put(key, None)

    def size(self):
        return self._size

if __name__ == "__main__":
    import sys
    st = TST()
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

    print('longestPrefixOf("shell"):')
    print(st.longest_prefix_of("shell"))
    print()

    print('keysWithPrefix("shor"):')
    for s in st.keys_with_prefix("shor"):
        print(s)
    print()

    print('keysThatMatch(".he.l."):')
    for s in st.keys_that_match(".he.l."):
        print(s)