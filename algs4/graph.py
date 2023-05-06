"""
   Execution:    python graph.py input.txt
   Dependencies: Bag.java Stack.java In.java StdOut.java
   Data files:   https://algs4.cs.princeton.edu/41graph/tinyG.txt
                 https://algs4.cs.princeton.edu/41graph/mediumG.txt
                 https://algs4.cs.princeton.edu/41graph/largeG.txt
 
   A graph, implemented using an array of sets.
   Parallel edges and self-loops allowed.
 
   % python -m algs4.graph < data/tinyG.txt
   13 vertices, 13 edges 
   0: 6 2 1 5 
   1: 0 
   2: 0 
   3: 5 4 
   4: 5 6 3 
   5: 3 4 0 
   6: 0 4 
   7: 8 
   8: 7 
   9: 11 10 12 
   10: 9 
   11: 9 12 
   12: 11 9 
 
   % python -m algs4.graph < data/mediumG.txt 
   250 vertices, 1273 edges 
   0: 225 222 211 209 204 202 191 176 163 160 149 114 97 80 68 59 58 49 44 24 15 
   1: 220 203 200 194 189 164 150 130 107 72 
   2: 141 110 108 86 79 51 42 18 14 
   ...
 """

import sys

from algs4.link_list import Bag


class Graph:

    def __init__(self, V):
        if V < 0:
            raise ValueError('Number of vertices must be non-negative')
        self._V = V
        self._E = 0
        self._adj = [Bag() for _ in range(self._V)]

    def V(self):
        return self._V
    
    def E(self):
        return self._E
    
    def validate_vertex(self, v):
        if v < 0 or v >= self._V:
            raise ValueError(f'vertex {v} is not between 0 and {self._V - 1}')

    def add_edge(self, v, w):
        v, w = int(v), int(w)
        self.validate_vertex(v)
        self.validate_vertex(w)
        self._E += 1
        self._adj[v].add(w)
        self._adj[w].add(v)

    def adj(self, v):
        return self._adj[v]
    
    def degree(self, v):
        return self._adj[v].size()
    
    def __str__(self):
        s = f'{self._V} vertices, {self._E} edges\n'
        for i in range(self._V):
            s += f'{i}: {" ".join(str(w) for w in self._adj[i])}\n'
        return s
    

if __name__ == '__main__':
    V = int(sys.stdin.readline())
    E = int(sys.stdin.readline())
    g = Graph(V)
    for i in range(E):
        v, w = sys.stdin.readline().split()
        g.add_edge(v, w)
    print(g)
