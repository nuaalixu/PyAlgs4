"""
 Execution:    python depth_first_order.py digraph.txt
 Data files:   https://algs4.cs.princeton.edu/42digraph/tinyDAG.txt
               https://algs4.cs.princeton.edu/42digraph/tinyDG.txt

 Compute preorder and postorder for a digraph or edge-weighted digraph.
 Runs in O(E + V) time.

 % python -m algs4.depth_first_order data/tinyDAG.txt
 Preorder:  0 5 4 1 6 9 11 12 10 2 3 7 8
 Postorder: 4 5 1 12 11 10 9 6 0 3 2 7 8
 Reverse postorder: 8 7 2 3 0 6 9 10 11 12 1 5 4

"""

import sys

from algs4.diagraph import Diagraph
from algs4.link_list import Queue, Stack


class DepthFirstOrder:

    def __init__(self, G: Diagraph):
        self.marked = [False] * G.V()
        self.pre = Queue()
        self.post = Queue()
        self.reverse_post = Stack()
        for v in range(G.V()):
            if not self.marked[v]:
                self.dfs(G, v)
    
    def dfs(self, G: Diagraph, v: int):
        self.pre.enqueue(v)
        self.marked[v] = True
        for w in G.adj(v):
            if not self.marked[w]:
                self.dfs(G, w)
        self.post.enqueue(v)
        self.reverse_post.push(v)


if __name__ == '__main__':
    with open(sys.argv[1], encoding='utf8') as f:
        g = Diagraph(f)
    bfs = DepthFirstOrder(g)
    print("Preorder:", bfs.pre)
    print("Postorder:", bfs.post)
    print("Reverse postorder:", bfs.reverse_post)