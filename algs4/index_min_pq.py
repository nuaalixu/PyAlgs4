from typing import Any


class IndexMinPQ:

    def __init__(self, n: int):
        self.maxN = n  # maximum number of elements in PQ
        self.pq = []  # binary heap using 0-based indexing
        self.qp = [-1] * n  # inverse of pq
        self.keys = [None] * n  # keys[i] = item of i

    def insert(self, i: int, item: Any):
        self.validate_idx(i)
        if self.contain(i):
            raise ValueError(f'index {i} is already in the priority queue.')
        self.qp[i] = len(self.pq)
        self.pq.append(i)
        self.keys[i] = item
        self.swim(len(self.pq) - 1)

    def change(self, i: int, item: Any):
        self.keys[i] = item
        k = self.qp[i]
        self.swim(k)
        self.sink(k)

    def contain(self, i: int) -> bool:
        return i in self.pq

    def delete(self, i: int) -> None:
        k = self.qp[i]
        self.exch(k, len(self.pq) - 1)
        self.pq.pop()
        self.qp[i] = -1
        self.keys[i] = None
        self.swim(k)
        self.sink(k)

    def validate_idx(self, i: int):
        if i< 0:
            raise ValueError(f'index is negative: {i}')
        if i >= self.maxN:
            raise ValueError(f'index >= capacity: {i}')

    def min(self):
        return self.keys[self.pq[0]]

    def min_index(self):
        return self.pq[0]

    def del_min(self) -> int:
        i = self.pq[0]
        self.exch(0, len(self.pq) - 1)
        self.pq.pop()
        self.qp[i] = -1
        self.keys[i] = None
        self.sink(0)
        return i

    def is_empty(self):
        return not self.pq

    def size(self):
        return len(self.pq)
    
    def greater(self, i: int, j: int) -> bool:
        return self.keys[self.pq[i]] > self.keys[self.pq[j]]

    def exch(self, i: int, j: int):
        self.pq[i], self.pq[j]  = self.pq[j], self.pq[i]
        self.qp[self.pq[i]] = i
        self.qp[self.pq[j]] = j

    def swim(self, k: int):
        while k > 0 and self.greater((k - 1) // 2, k):
            self.exch(k, (k - 1) // 2)
            k = ( k - 1) // 2

    def sink(self, k: int):
        while 2 * k + 1 < len(self.pq):
            j = 2 * k + 1
            if j + 1 < len(self.pq) and self.greater(j, j+1):
                j += 1
            if self.greater(j, k):
                break
            self.exch(k, j)
            k = j

    