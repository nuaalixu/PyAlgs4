"""
  Execution:    python directed_cycle.py input.txt
  Data files:   https://algs4.cs.princeton.edu/42digraph/tinyDG.txt
                https://algs4.cs.princeton.edu/42digraph/tinyDAG.txt

  Finds a directed cycle in a digraph.
  Runs in O(E + V) time.

  % python -m directed_cycle data/tinyDG.txt
  Directed cycle: 3 5 4 3

  %  python -m algs4.directed_cycle data/tinyDAG.txt
  No directed cycle
"""

import sys

from algs4.diagraph import Diagraph
from algs4.link_list import Stack


class DirectedCycle:

    def __init__(self, G: Diagraph):
        self.marked = [False] * G.V()
        self.edge_to = [None] * G.V()
        self.on_stack = [False] * G.V()
        self._cycle = None
        for v in range(G.V()):
            if not self.marked[v]:
                self.dfs(G, v)

    def dfs(self, G: Diagraph, v: int):
        self.on_stack[v] = True
        self.marked[v] = True
        for w in G.adj(v):
            # early terminate
            if self.has_cycle():
                return
            if not self.marked[w]:
                self.edge_to[w] = v
                self.dfs(G, w)
            elif self.on_stack[w]:
                self._cycle = Stack()
                x = v
                while x != w:
                    self._cycle.push(x)
                    x = self.edge_to[x]
                self._cycle.push(w)
                self._cycle.push(v)
        self.on_stack[v] = False

    def has_cycle(self):
        return self._cycle is not None

    def cycle(self):
        return self._cycle
    

if __name__ == '__main__':
    with open(sys.argv[1], encoding='utf8') as f:
        g = Diagraph(f)
    finder = DirectedCycle(g)
    if finder.has_cycle():
        print("Directed cycle:", " ".join(str(v) for v in finder.cycle()))    
    else:
        print("No directed cycle")