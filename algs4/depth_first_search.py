"""
  Execution:    python depth_first_search.py filename.txt s
  Data files:   https: // algs4.cs.princeton.edu / 41graph / tinyG.txt
                https: // algs4.cs.princeton.edu / 41graph / mediumG.txt

  Run depth first search on an undirected graph.
  Runs in O(E + V) time.

 % python algs4.depth_first_search data/tinyG.txt 0
  0 1 2 3 4 5 6
  NOT connected

 % python algs4.depth_first_search data/tinyG.txt 9
  9 10 11 12
  NOT connected

 """

import sys

from algs4.graph import Graph


class DepthFirstSearch:

    def __init__(self, graph: Graph, source):
        self.marked = [False] * graph.V()
        self.count = 0
        graph.validate_vertex(source)
        self.dfs(graph, source)

    def dfs(self, graph: Graph, vertex):
        self.count += 1
        self.marked[vertex] = True
        for w in graph.adj(vertex):
            if not self.marked[w]:
                self.dfs(graph, w)


if __name__ == '__main__':
    with open(sys.argv[1], encoding='utf8') as f:
        V = int(f.readline())
        E = int(f.readline())
        g = Graph(V)
        for i in range(E):
            v, w = f.readline().split()
            g.add_edge(v, w)
    s = int(sys.argv[2])
    search = DepthFirstSearch(g, s)
    for v in range(g.V()):
        if search.marked[v]:
            print(str(v) + " ")
    if search.count == g.V():
        print("connected")
    else:
        print("NOT connected")


