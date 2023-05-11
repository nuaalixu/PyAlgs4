"""
 Execution:    python kosaraju_scc.py filename.txt
 Data files:   https://algs4.cs.princeton.edu/42digraph/tinyDG.txt
               https://algs4.cs.princeton.edu/42digraph/mediumDG.txt
               https://algs4.cs.princeton.edu/42digraph/largeDG.txt
 
 Compute the strongly-connected components of a digraph using the
 Kosaraju-Sharir algorithm.
 
 Runs in O(E + V) time.
 
 % python kosaraju_scc.py tinyDG.txt
 5 strong components
 1
 0 2 3 4 5
 9 10 11 12
 6 8
 7
 
 % python -m algs4.kosaraju_scc data/mediumDG.txt
 10 strong components
 21
 2 5 6 8 9 11 12 13 15 16 18 19 22 23 25 26 28 29 30 31 32 33 34 35 37 38 39 40 42 43 44 46 47 48 49
 14
 3 4 17 20 24 27 36
 41
 7
 45
 1
 0
 10
 
"""

import sys

from algs4.link_list import Queue
from algs4.digraph import Digraph
from algs4.depth_first_order import DepthFirstOrder


class KosarajuSCC:

    def __init__(self, G: Digraph):
        self.marked = [False] * G.V()
        self.ids = [None] * G.V()
        self._count = 0
        order = DepthFirstOrder(G.reverse())
        for s in order.reverse_post:
            if not self.marked[s]:
                self.dfs(G, s)
                self._count += 1

    def dfs(self, G: Digraph, v: int):
        self.marked[v] = True
        self.ids[v] = self._count
        for w in G.adj(v):
            if not self.marked[w]:
                self.dfs(G, w)

    def id(self, v: int):
        return self.ids[v]
    
    def count(self):
        return self._count
    
    def strongly_connected(self, v, w):
        return self.ids[v] == self.ids[w]
    

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        g = Digraph(f)
    scc = KosarajuSCC(g)
    m = scc.count()
    print(m, "strong components")
    components = []
    for i in range(m):
        components.append(Queue())
    for v in range(g.V()):
        components[scc.id(v)].enqueue(v)

    for i in range(m):
        print(components[i])
    