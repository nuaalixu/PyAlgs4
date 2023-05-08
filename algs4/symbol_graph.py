"""
   Execution:    python symbol_graph.py filename.txt delimiter
   Data files:   https://algs4.cs.princeton.edu/41graph/routes.txt
                 https://algs4.cs.princeton.edu/41graph/movies.txt
                 https://algs4.cs.princeton.edu/41graph/moviestiny.txt
                 https://algs4.cs.princeton.edu/41graph/moviesG.txt
                 https://algs4.cs.princeton.edu/41graph/moviestopGrossing.txt

   %  python -m algs4.symbol_graph.py data/routes.txt " "
   JFK
      MCO
      ATL
      ORD
   LAX
      PHX
      LAS

   % python -m algs4.symbol_graph.py data/movies.txt "/"
   Tin Men (1987)
      Hershey, Barbara
      Geppi, Cindy
      Jones, Kathy (II)
      Herr, Marcia
      ...
      Blumenfeld, Alan
      DeBoy, David
   Bacon, Kevin
      Woodsman, The (2004)
      Wild Things (1998)
      Where the Truth Lies (2005)
      Tremors (1990)
      ...
      Apollo 13 (1995)
      Animal House (1978)


   Assumes that input file is encoded using UTF-8.
   % iconv -f ISO-8859-1 -t UTF-8 movies-iso8859.txt > movies.txt

 """

import sys
from io import TextIOBase
from collections import OrderedDict

from algs4.graph import Graph


class SymbolGraph:

    def __init__(self, file_obj: TextIOBase, delim: str):
        self.st = OrderedDict()
        for line in file_obj:
            for key in line.rstrip().split(delim):
                if key not in self.st:
                    self.st[key] = len(self.st)
        self.keys = list(self.st.keys())
        self.g = Graph(len(self.keys))
        file_obj.seek(0, 0)
        for line in file_obj:
            a = line.rstrip().split(delim)
            v = self.st[a[0]]
            for i in range(1, len(a)):
                self.g.add_edge(v, self.st[a[i]])

    def contains(self, key: str):
        return key in self.st

    def index(self, key: str) -> int:
        return self.st[key]

    def name(self, v: int) -> str:
        return self.keys[v]

    def G(self) -> Graph:
        return self.g
    

if __name__ == "__main__":
    filename, delimiter = sys.argv[1], sys.argv[2]
    with open(filename, encoding='utf8') as f:
        sg = SymbolGraph(f, delimiter)
    graph = sg.G()

    for line in sys.stdin:
        source = line.strip()
        if sg.contains(source):
            s = sg.index(source)
            for v in graph.adj(s):
                print("  ", sg.name(v))
        else:
            print("input not contains source: ", source)
