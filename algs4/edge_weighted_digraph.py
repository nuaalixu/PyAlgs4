"""
 Execution:    python edge_weighted_graph.py filename.txt
 Data files:   https://algs4.cs.princeton.edu/44sp/tinyEWD.txt
               https://algs4.cs.princeton.edu/44sp/mediumEWD.txt
               https://algs4.cs.princeton.edu/44sp/largeEWD.txt

 An edge-weighted undirected graph, implemented using adjacency lists.
 Parallel edges and self-loops are permitted.

 % python -m algs4.edge_weighted_digraph data/tinyEWD.txt
8 vertices, 15 edges
0: 0->2 0.26000 0->4 0.38000
1: 1->3 0.29000
2: 2->7 0.34000
3: 3->6 0.52000
4: 4->7 0.37000 4->5 0.35000
5: 5->1 0.32000 5->7 0.28000 5->4 0.35000
6: 6->4 0.93000 6->0 0.58000 6->2 0.40000
7: 7->3 0.39000 7->5 0.28000

"""

import sys
from io import TextIOBase

from algs4.link_list import Bag
from algs4.directed_edge import DirectedEdge


class EdgeWeightedDigraph:

    def __init__(self, inp):
        if isinstance(inp, int):
            if inp < 0:
                raise ValueError('number of vertices must be non-negative')
            self._V = inp
            self._E = 0
            self._adj = [Bag() for _ in range(self._V)]
        elif isinstance(inp, TextIOBase):
            self._V = int(inp.readline())
            self._E = 0
            E = int(inp.readline())
            if E < 0:
                raise ValueError('number of edges in a Graph must be non-negative')
            self._adj = [Bag() for _ in range(self._V)]
            for _ in range(E):
                v, w, weight = inp.readline().split()
                v, w = int(v), int(w)
                weight = float(weight)
                e = DirectedEdge(v, w, weight)
                self.add_edge(e)
        else:
            raise ValueError('input error')
    
    def V(self):
        return self._V

    def E(self):
        return self._E

    def add_edge(self, e: DirectedEdge):
        self._adj[e.From()].add(e)
        self._E += 1

    def adj(self, v):
        return self._adj[v]

    def edges(self):
        b = Bag()
        for v in range(self.V()):
            for e in self._adj[v]:
                b.add(e)
        return b

    def __str__(self):
        s = f"{self._V} vertices, {self._E} edges\n"
        for i in range(self._V):
            adjs = " ".join([str(x) for x in self._adj[i]])
            s += f"{i}: {adjs}\n"
        return s
    

if __name__ == "__main__":
    with open(sys.argv[1], encoding='utf8') as f:
        graph = EdgeWeightedDigraph(f)
    print(graph)