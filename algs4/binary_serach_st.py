import sys

from algs4.st import ST


class BinarySerachST(ST):

    def __init__(self):
        super().__init__()
        self._keys = []
        self._values = []

    def size(self):
        return len(self._keys)

    def get(self, key):
        if self.is_empty():
            return None
        i = self.rank(key)
        if i < len(self._keys) and self._keys[i] == key:
            return self._values[i]
        return None

    def rank(self, key) -> int:
        lo = 0
        hi = len(self._keys) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if self._keys[mid] == key:
                return mid
            elif self._keys[mid] > key:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo
            
    def put(self, key, val):
        i = self.rank(key)
        if i < len(self._keys) and self._keys[i] == key:
            self._values[i] = val
        else:
            self._keys.append(None)
            self._values.append(None)
            for j in range(len(self._keys) - 1, i, -1):
                self._keys[j] = self._keys[j - 1]
                self._values[j]  = self._values[j - 1]
            self._keys[i] = key
            self._values[i] = val

    def delete(self, key):
        if key is None:
            raise ValueError('argument to delete() is None')
        i = self.rank(key)
        if i < len(self._keys) and self._keys[i] == key:
            for j in range(i, len(self._keys) - 1):
                self._keys[j] = self._keys[j + 1]
                self._values[j] = self._values[j + 1]
            self._keys.pop()
            self._values.pop()

    def contains(self, key):
        i = self.rank(key)
        if i < len(self._keys) and self._keys[i] == key:
            return True
        else:
            return False
    
    def keys(self):
        return iter(self._keys)
    
    def min(self):
        return self._keys[0]
    
    def max(self):
        return self._keys[-1]
    
    def select(self, k):
        return self._keys[k]

    def ceiling(self, key):
        i = self.rank(key)
        return self._keys[i]
    
    def floor(self, key):
        i = self.rank(key)
        if self._keys[i] == key:
            return key
        else:
            return self._keys[i - 1]
        
    def del_min(self):
        self._keys.pop(0)
        self._values.pop(0)

    def del_max(self):
        self._keys.pop(-1)
        self._values.pop(-1)

    def is_empty(self):
        return not self._keys
    

if __name__ == '__main__':
    st = BinarySerachST()
    i = 0
    for line in sys.stdin:
        for key in line.split():
            st.put(key, i)
            i += 1

    for key in st.keys():
        print(f'{key} {st.get(key)}')