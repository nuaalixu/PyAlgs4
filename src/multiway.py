import sys
from collections import deque

from index_min_pq import IndexMinPQ


class Multiway:

    @classmethod
    def merge(cls, arrs):
        pq = IndexMinPQ(len(arrs))
        for i in range(0, len(arrs)):
            if arrs[i]:
                pq.insert(i, arrs[i].popleft())
        
        while not pq.is_empty():
            print(pq.min())
            i = pq.del_min()
            if arrs[i]:
                pq.insert(i, arrs[i].popleft())


if __name__ == '__main__':
    streams = []
    for file in sys.argv[1:]:
        with open(file, 'r', encoding='utf8') as f:
            streams.append(deque(f.readline().split()))
    Multiway.merge(streams)