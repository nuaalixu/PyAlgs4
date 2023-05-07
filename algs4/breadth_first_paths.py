"""
 Execution    python bread_first_paths.py G s
 Dependencies: Graph.java Queue.java Stack.java StdOut.java
 Data files:   https://algs4.cs.princeton.edu/41graph/tinyCG.txt
               https://algs4.cs.princeton.edu/41graph/tinyG.txt
               https://algs4.cs.princeton.edu/41graph/mediumG.txt
               https://algs4.cs.princeton.edu/41graph/largeG.txt
 
 Run breadth first search on an undirected graph.
 Runs in O(E + V) time.
 
 %  python -m algs4.graph tinyCG.txt
 6 vertices, 8 edges
 0: 2 1 5 
 1: 0 2 
 2: 0 1 3 4 
 3: 5 4 2 
 4: 3 2 
 5: 3 0 
 
 %  python -m algs4.breadth_first_paths data/tinyCG.txt 0
 0 to 0 (0):  0
 0 to 1 (1):  0-1
 0 to 2 (1):  0-2
 0 to 3 (2):  0-2-3
 0 to 4 (2):  0-2-4
 0 to 5 (1):  0-5

"""

import sys

from typing import Iterable

from algs4.graph import Graph
from algs4.link_list import Queue, Stack


class BreadthFisrtPaths:

    def __init__(self, g: Graph, s: int):
        self.marked = [False] * g.V()
        self.validate_vertex(s)
        self.s = s
        self.edge_to = [None] * g.V()
        self.bfs(g, s)

    def bfs(self, g: Graph, s: int):
        queue = Queue()
        queue.enqueue(s)
        while not queue.is_empty():
            v = queue.dequeue()
            for w in g.adj(v):
                if not self.marked[w]:
                    self.marked[w] = True
                    self.edge_to[w] = v
                    queue.enqueue(w)

    def has_path_to(self, v: int):
        self.validate_vertex(v)
        return self.marked[v]

    def path_to(self, v) -> Iterable:
        if not self.has_path_to(v):
            return None
        path = Stack()
        x = v
        while x != self.s:
            path.push(x)
            x = self.edge_to[x]
        path.push(self.s)
        return path
    
    def validate_vertex(self, v):
        V = len(self.marked)
        if v < 0 or v >= V:
            raise ValueError(f'vertex {v} is not between 0 and {V - 1}')
        

if __name__ == '__main__':
    with open(sys.argv[1], encoding='utf8') as f:
        g = Graph(f)
    s = int(sys.argv[2])
    dfs = BreadthFisrtPaths(g, s)

    for v in range(g.V()):
        if dfs.has_path_to(v):
            print(f'{s} to {v}: {"-".join(str(w) for w in dfs.path_to(v))}')
        else:
            print(f'{s} to {v}: not connected')
