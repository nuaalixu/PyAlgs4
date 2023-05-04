import sys

from algs4.st import ST
from algs4.sequential_search_st import SequentialSearchST


class SeparateChaningHashST(ST):

    INIT_CAPACITY = 4
    def __init__(self, m=None):
        super().__init__()
        self.n = 0
        self.m = m or SeparateChaningHashST.INIT_CAPACITY
        self.st = [SequentialSearchST() for _ in range(self.m)]

    def resize(self, chains):
        tmp = SeparateChaningHashST(chains)
        for i in range(self.m):
            for key in self.st[i].keys():
                tmp.put(key, self.st[i].get(key))
        self.m = tmp.m
        self.n = tmp.n
        self.st = tmp.st
    
    def hash(self, key):
        return (hash(key) & 0x7fffffff) % self.m

    def size(self):
        return self.n
    
    def is_empty(self) -> bool:
        return not self.n
    
    def contains(self, key):
        if key is None:
            raise ValueError('argument to contains() is None')
        return self.get(key) is not None
    
    def get(self, key):
        if key is None:
            raise ValueError('argument to get() is None')
        i = self.hash(key)
        return self.st[i].get(key)
    
    def put(self, key, val):
        if key is None:
            raise ValueError('argument to put() is None')
        if val is None:
            self.delete(key)
            return
        if self.n >= 10 * self.m:
            self.resize(2 * self.m)
        i = self.hash(key)
        if not self.contains(key):
            self.n += 1
        self.st[i].put(key, val)
    
    def delete(self, key):
        if key is None:
            raise ValueError('argument to delete() is None')
        i = self.hash(key)
        if self.st[i].contains(key):
            self.n -= 1
        self.st[i].delete(key)

        if (self.m > SeparateChaningHashST.INIT_CAPACITY
            and self.n <= 2 * self.m):
            self.resize(self.m // 2)

    def keys(self):
        keys = []
        for st in self.st:
            for key in st.keys():
                keys.append(key)
        return keys
    

if __name__ == '__main__':
    st = SeparateChaningHashST()
    i = 0
    for line in sys.stdin:
        for key in line.split():
            st.put(key, i)
            i += 1

    for key in st.keys():
        print(f'{key} {st.get(key)}')
