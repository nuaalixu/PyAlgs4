import sys

from algs4.graph import Graph
from algs4.link_list import Stack


class DepthFirstPaths:

    def __init__(self, g: Graph, s: int):
        self.s = s
        self.edge_to = [None] * g.V()
        self.marked = [False] * g.V()
        self.validate_vertex(s)
        self.dfs(g, s)

    def dfs(self, g: Graph, v: int):
        """depth first search from v"""
        self.marked[v] = True
        for w in g.adj(v):
            if not self.marked[w]:
                self.edge_to[w] = v
                self.dfs(g, w)

    def has_path_to(self, v: int):
        self.validate_vertex(v)
        return self.marked[v]
    
    def path_to(self, v: int):
        if not self.has_path_to(v):
            return None
        path = Stack()
        while v != self.s:
            path.push(v)
            v = self.edge_to[v]
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
    dfs = DepthFirstPaths(g, s)

    for v in range(g.V()):
        if dfs.has_path_to(v):
            print(f'{s} to {v}: {"-".join(str(w) for w in dfs.path_to(v))}')
        else:
            print(f'{s} to {v}: not connected')
