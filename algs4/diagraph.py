"""
   Execution:    python digraph.py input.txt
   Dependencies: Bag.java Stack.java In.java StdOut.java
   Data files:   https://algs4.cs.princeton.edu/42digraph/tinyDG.txt
                 https://algs4.cs.princeton.edu/42digraph/mediumDG.txt
                 https://algs4.cs.princeton.edu/42digraph/largeDG.txt
 
   A graph, implemented using an array of sets.
   Parallel edges and self-loops are permitted.
 
   % python -m algs4.diagraph data/tinyDG.txt
   13 vertices, 22 edges
   0: 5 1 
   1: 
   2: 0 3 
   3: 5 2 
   4: 3 2 
   5: 4 
   6: 9 4 8 0 
   7: 6 9
   8: 6 
   9: 11 10 
   10: 12 
   11: 4 12 
   12: 9 
 
 """

import sys
from io import TextIOBase
from typing import Union

from algs4.link_list import Bag


class Diagraph:

    def __init__(self, x: Union[int, TextIOBase]):
        if isinstance(x, int):
            if x < 0:
                raise ValueError('Number of vertices must be non-negative')
            self._V = x
            self._E = 0
            self._adj = [Bag() for _ in range(self._V)]
        elif isinstance(x, TextIOBase):
            self._V = int(x.readline())
            self._E = 0
            E = int(x.readline())
            if E < 0:
                raise ValueError('number of edges in a Graph must be non-negative')
            self._adj = [Bag() for _ in range(self._V)]
            for i in range(E):
                v, w = x.readline().split()
                v, w = int(v), int(w)
                self.add_edge(v, w)

    def V(self):
        return self._V

    def E(self):
        return self._E

    def add_edge(self, v, w):
        self.validate_vertex(v)
        self.validate_vertex(w)
        self._adj[v].add(w)
        self._E += 1

    def adj(self, v):
        self.validate_vertex(v)
        return self._adj[v]

    def reverse(self):
        reverse_g = Diagraph(self._V)
        for v in range(self._V):
            for w in self._adj[v]:
                reverse_g.add_edge(w, v)
        return reverse_g

    def validate_vertex(self, v):
        if v < 0 or v >= self._V:
            raise ValueError(f'vertex {v} is not between 0 and {self._V - 1}')
        
    def degree(self, v):
        return self._adj[v].size()
    
    def __str__(self):
        s = f'{self._V} vertices, {self._E} edges\n'
        for i in range(self._V):
            s += f'{i}: {" ".join(str(w) for w in self._adj[i])}\n'
        return s
    

if __name__ == '__main__':
    with open(sys.argv[1], encoding='utf8') as f:
        g = Diagraph(f)
    print(g)
