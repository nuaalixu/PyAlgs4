"""
 *  Execution:    python dijkstra_sp.py input.txt s
 *  Data files:   https://algs4.cs.princeton.edu/44sp/tinyEWD.txt
 *                https://algs4.cs.princeton.edu/44sp/mediumEWD.txt
 *                https://algs4.cs.princeton.edu/44sp/largeEWD.txt
 *
 *  Dijkstra's algorithm. Computes the shortest path tree.
 *  Assumes all weights are nonnegative.
 *
 *  % python -m algs4.dijkstra_sp data/tinyEWD.txt 0
 *  0 to 0 (0.00)
 *  0 to 1 (1.05)  0->4  0.38   4->5  0.35   5->1  0.32
 *  0 to 2 (0.26)  0->2  0.26
 *  0 to 3 (0.99)  0->2  0.26   2->7  0.34   7->3  0.39
 *  0 to 4 (0.38)  0->4  0.38
 *  0 to 5 (0.73)  0->4  0.38   4->5  0.35
 *  0 to 6 (1.51)  0->2  0.26   2->7  0.34   7->3  0.39   3->6  0.52
 *  0 to 7 (0.60)  0->2  0.26   2->7  0.34
 *
 *  % python -m algs4.dijkstra_sp data/mediumEWD.txt 0
 *  0 to 0 (0.00)
 *  0 to 1 (0.71)  0->44  0.06   44->93  0.07   ...  107->1  0.07
 *  0 to 2 (0.65)  0->44  0.06   44->231  0.10  ...  42->2  0.11
 *  0 to 3 (0.46)  0->97  0.08   97->248  0.09  ...  45->3  0.12
 *  0 to 4 (0.42)  0->44  0.06   44->93  0.07   ...  77->4  0.11
 *  ...
 *
"""

import sys

from algs4.link_list import Stack
from algs4.index_min_pq import IndexMinPQ
from algs4.edge_weighted_digraph import EdgeWeightedDigraph


class DijkstraSP:

    def __init__(self, G: EdgeWeightedDigraph, s: int):
        self._dist_to = [float('inf')] * G.V()
        self._dist_to[s] = 0
        self._edge_to = [None] * G.V()
        self._pq = IndexMinPQ(G.V())
        self._pq.insert(s, 0.0)
        while not self._pq.is_empty():
            self.relax(G, self._pq.del_min())

    def dist_to(self, v: int):
        return self._dist_to[v]

    def has_path_to(self, v: int):
        return self._dist_to[v] < float('inf')

    def path_to(self, v: int):
        if not self.has_path_to(v):
            return None
        path = Stack()
        e = self._edge_to[v]
        while e is not None:
            path.push(e)
            e = self._edge_to[e.From()]
        return path

    def relax(self, G, v):
        for e in G.adj(v):
            w = e.To()
            if self._dist_to[w] > self._dist_to[v] + e.weight:
                self._dist_to[w] = self._dist_to[v] + e.weight
                self._edge_to[w] = e
                if self._pq.contain(w):
                    self._pq.change(w, self._dist_to[w])
                else:
                    self._pq.insert(w, self._dist_to[w])


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        g = EdgeWeightedDigraph(f)
    s = int(sys.argv[2])
    sp = DijkstraSP(g, s)

    for t in range(g.V()):
        print(f'{s} to {t}', end=' ')
        print(f'{sp.dist_to(t):4.2f}:', end=' ')
        if sp.has_path_to(t):
            print(" ".join(str(e) for e in sp.path_to(t)))
