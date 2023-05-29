"""
    Execution:    python directed_dfs.py digraph.txt s
    Data files:   https: // algs4.cs.princeton.edu / 42digraph / tinyDG.txt
                  https://algs4.cs.princeton.edu/42digraph/mediumDG.txt
                  https://algs4.cs.princeton.edu/42digraph/largeDG.txt

    Determine single-source or multiple-source reachability in a digraph
    using depth first search.
    Runs in O(E + V) time.

    % python -m algs4.directed_dfs data/tinyDG.txt 1
    1

    % python -m algs4.directed_dfs data/tinyDG.txt 2
    0 1 2 3 4 5

    % python -m algs4.directed_dfs data/tinyDG.txt 1 2 6
    0 1 2 3 4 5 6 8 9 10 11 12 
"""

import sys

from typing import Tuple

from algs4.digraph import Digraph


class DirectedDFS:

    def __init__(self, graph: Digraph, sources: Tuple):
        self._marked = [False] * graph.V()
        for s in sources:
            s = int(s)
            graph.validate_vertex(s)
            if not self._marked[s]:
                self.dfs(graph, s)

    def dfs(self, graph: Digraph, vertex):
        self._marked[vertex] = True
        for w in graph.adj(vertex):
            if not self._marked[w]:
                self.dfs(graph, w)
    
    def marked(self, v):
        return self._marked[v]


if __name__ == '__main__':
    with open(sys.argv[1], encoding='utf8') as f:
        g = Digraph(f)
    s = int(sys.argv[2])
    reachable = DirectedDFS(g, sys.argv[2:])
    print(" ".join(str(v) for v in range(g.V()) if reachable.marked(v)))