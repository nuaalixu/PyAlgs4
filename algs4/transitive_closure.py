'''
 Compilation:  javac TransitiveClosure.java
 Execution:    java TransitiveClosure filename.txt
 Dependencies: Digraph.java DepthFirstDirectedPaths.java In.java StdOut.java
 Data files:   https://algs4.cs.princeton.edu/42digraph/tinyDG.txt

 Compute transitive closure of a digraph and support
 reachability queries.

 Preprocessing time: O(V(E + V)) time.
 Query time: O(1).
 Space: O(V^2).

 % python -m algs4.transitive_closure data/tinyDG.txt
        0  1  2  3  4  5  6  7  8  9 10 11 12
 --------------------------------------------
   0:   T  T  T  T  T  T
   1:      T
   2:   T  T  T  T  T  T
   3:   T  T  T  T  T  T
   4:   T  T  T  T  T  T
   5:   T  T  T  T  T  T
   6:   T  T  T  T  T  T  T     T  T  T  T  T
   7:   T  T  T  T  T  T  T  T  T  T  T  T  T
   8:   T  T  T  T  T  T  T  T  T  T  T  T  T
   9:   T  T  T  T  T  T           T  T  T  T
  10:   T  T  T  T  T  T           T  T  T  T
  11:   T  T  T  T  T  T           T  T  T  T
  12:   T  T  T  T  T  T           T  T  T  T
'''

import sys

from algs4.digraph import Digraph
from algs4.directed_dfs import DirectedDFS


class TransitiveClosure:

    def __init__(self, G: Digraph):
        self.all = [DirectedDFS(G, [v]) for v in range(G.V())]

    def reachable(self, v, w):
        return self.all[v].marked(w)
    

if __name__ == '__main__':
    with open(sys.argv[1], encoding='utf8') as f:
        g = Digraph(f)
    tc = TransitiveClosure(g)
    print("   ", "".join(f'{v:3d}' for v in range(g.V())))
    print("_" * 3 * (g.V() + 1))
    for v in range(g.V()):
        print(f'{v:3d}:', end='')
        for w in range(g.V()):
            if tc.reachable(v, w):
                print('  T', end='')
            else:
                print('   ', end='')
        print()