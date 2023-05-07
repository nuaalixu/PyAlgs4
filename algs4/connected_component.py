"""
  Execution:    python cc.py filename.txt
  Data files:   https://algs4.cs.princeton.edu/41graph/tinyG.txt
                https://algs4.cs.princeton.edu/41graph/mediumG.txt
                https://algs4.cs.princeton.edu/41graph/largeG.txt

  Compute connected components using nonrecurisve depth first search.
  Runs in O(E + V) time.

  % python -m algs4.connected_component tinyG.txt
  3 components
  0 1 2 3 4 5 6
  7 8
  9 10 11 12

  % python -m algs4.connected_component mediumG.txt
  1 components
  0 1 2 3 4 5 6 7 8 9 10 ...

"""

import sys

from algs4.graph import Graph
from algs4.link_list import Stack, Bag

class ConnectedComponent:

    def __init__(self, g: Graph):
        self.marked = [False] * g.V()
        self.ids = [None] * g.V()
        self._count = 0
        for v in range(len(self.marked)):
            if not self.marked[v]:
                self.dfs(g, v)
                self._count += 1

    def dfs(self, g: Graph, v: int):
        stack = Stack()
        stack.push(v)
        while not stack.is_empty():
            v = stack.pop()
            for w in g.adj(v):
                if not self.marked[w]:
                    self.marked[w] = True
                    self.ids[w] = self._count
                    stack.push(w)

    def connected(self, v: int ,w: int):
        return self.ids[v] == self.ids[w]
    
    def id(self, v: int):
        return self.ids[v]

    def count(self):
        return self._count
    

if __name__ == "__main__":
    with open(sys.argv[1], encoding='utf8') as f:
        V = int(f.readline())
        E = int(f.readline())
        g = Graph(V)
        for i in range(E):
            v, w = f.readline().split()
            g.add_edge(v, w)

    cc = ConnectedComponent(g)
    print(cc.count(), " components")
    components = []
    for i in range(cc.count()):
        components.append(Bag())

    for v in range(g.V()):
        components[cc.id(v)].add(v)

    for i in range(cc.count()):
        for v in components[i]:
            print(v, " ", end='')
        print()