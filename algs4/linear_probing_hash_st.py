import sys

from algs4.st import ST


class LinearProbingHashST(ST):
    INIT_CAPACITY = 4

    def __init__(self, m=None):
        self.n = 0
        self.m = m or LinearProbingHashST.INIT_CAPACITY
        self._keys = [None] * self.m
        self._vals = [None] * self.m

    def size(self):
        return self.n
    
    def is_empty(self):
        return not self.n
    
    def contains(self, key):
        super().contains(key)
        return self.get(key) is not None
    
    def hash(self, key):
        return (hash(key) & 0x7FFFFFFF) % self.m
    
    def resize(self, capacity):
        tmp = LinearProbingHashST(capacity)
        for i in range(self.m):
            if self._keys[i] is not None:
                tmp.put(self._keys[i], self._vals[i])
        self._keys = tmp._keys
        self._vals = tmp._vals
        self.m = tmp.m

    def put(self, key, val):
        super().put(key, val)
        if self.n >= self.m // 2:
            self.resize(2 * self.m)
        i = self.hash(key)
        while self._keys[i] is not None:
            if self._keys[i] == key:
                self._vals[i] = val
                return
            i = (i + 1) % self.m
        self._keys[i] = key
        self._vals[i] = val
        self.n += 1

    def get(self, key):
        super().get(key)
        i = self.hash(key)
        while self._keys[i] is not None:
            if self._keys[i] == key:
                return self._vals[i]
            i = (i + 1) % self.m
        return None
    
    def delete(self, key):
        super().delete(key)
        i = hash(key)
        while self._keys[i] != key:
            i = (i + 1) % self.m
        self._keys[i] = None
        self._vals[i] = None

        i = (i + 1) % self.m
        while self._keys[i] != None:
            key = self._keys[i]
            val = self._vals[i]
            self._keys[i] = None
            self._vals[i] = None
            self.n -= 1
            self.put(key, val)
            i = (i + 1) % self.m

        self.n -= 1

        if self.n > LinearProbingHashST.INIT_CAPACITY and self.n <= self.m // 8:
            self.resize(self.m // 2)

    def keys(self):
        queue = []
        for key in self._keys:
            if key is not None:
                queue.append(key)
        return queue
    

if __name__ == '__main__':
    st = LinearProbingHashST()
    i = 0
    for line in sys.stdin:
        for key in line.split():
            st.put(key, i)
            i += 1

    for key in sorted(st.keys()):
        print(f'{key} {st.get(key)}')