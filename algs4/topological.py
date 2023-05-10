"""
 Execution:    python topological.py filename.txt delimiter
 Data files:   https://algs4.cs.princeton.edu/42digraph/jobs.txt

 Compute topological ordering of a DAG or edge-weighted DAG.
 Runs in O(E + V) time.

 % python -m algs4.topological data/jobs.txt "/"
 Calculus
 Linear Algebra
 Introduction to CS
 Advanced Programming
 Algorithms
 Theoretical CS
 Artificial Intelligence
 Robotics
 Machine Learning
 Neural Networks
 Databases
 Scientific Computing
 Computational Biology
 *
"""

import sys

from algs4.digraph import Digraph
from algs4.symbol_digraph import SymbolDigraph
from algs4.directed_cycle import DirectedCycle
from algs4.depth_first_order import DepthFirstOrder

class Topological:

    def __init__(self, G: Digraph):
        cycle_finder = DirectedCycle(G)
        if not cycle_finder.has_cycle():
            dfs = DepthFirstOrder(G)
            self.order = dfs.reverse_post

    def is_dag(self):
        return not self.order.is_empty()
    

if __name__ == '__main__':
    filename = sys.argv[1]
    delimiter = sys.argv[2]
    with open(filename) as f:
        sg = SymbolDigraph(f, delimiter)
    topological = Topological(sg.G())
    for v in topological.order:
        print(sg.name(v))