"""
 Execution:    python edge_weighted_graph.py filename.txt
 Data files:   https://algs4.cs.princeton.edu/43mst/tinyEWG.txt
               https://algs4.cs.princeton.edu/43mst/mediumEWG.txt
               https://algs4.cs.princeton.edu/43mst/largeEWG.txt

 An edge-weighted undirected graph, implemented using adjacency lists.
 Parallel edges and self-loops are permitted.

 % python -m algs4.edge_weighted_graph data/tinyEWG.txt
 8 vertices, 16 edges
 0: 6-0 0.58000  0-2 0.26000  0-4 0.38000  0-7 0.16000
 1: 1-3 0.29000  1-2 0.36000  1-7 0.19000  1-5 0.32000
 2: 6-2 0.40000  2-7 0.34000  1-2 0.36000  0-2 0.26000  2-3 0.17000
 3: 3-6 0.52000  1-3 0.29000  2-3 0.17000
 4: 6-4 0.93000  0-4 0.38000  4-7 0.37000  4-5 0.35000
 5: 1-5 0.32000  5-7 0.28000  4-5 0.35000
 6: 6-4 0.93000  6-0 0.58000  3-6 0.52000  6-2 0.40000
 7: 2-7 0.34000  1-7 0.19000  0-7 0.16000  5-7 0.28000  4-7 0.37000

"""

import sys
from io import TextIOBase

from algs4.link_list import Bag
from algs4.edge import Edge


class EdgeWeightedGraph:

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
                e = Edge(v, w, weight)
                self.add_edge(e)
        else:
            raise ValueError('input error')
    
    def V(self):
        return self._V

    def E(self):
        return self._E

    def add_edge(self, e: Edge):
        v = e.either()
        w = e.other(v)
        # for self-loop
        if v != w:
            self._adj[v].add(e)
        self._adj[w].add(e)
        self._E += 1

    def adj(self, v):
        return self._adj[v]

    def edges(self):
        b = Bag()
        for v in range(self.V()):
            for e in self._adj[v]:
                if e.other(v) >= v:
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
        graph = EdgeWeightedGraph(f)
    print(graph)