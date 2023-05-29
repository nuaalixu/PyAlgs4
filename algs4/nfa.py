"""
 *  Execution:    python nfa.py regexp text
 *
 *  % python -m algs4.nfa "(A*B|AC)D" AAAABD
 *  true
 *
 *  % python -m algs4.nfa  "(A*B|AC)D" AAAAC
 *  false
 *
 *  % python -m algs4.nfa  "(a|(bc)*d)*" abcbcd
 *  true
 *
 *  % python -m algs4.nfa  "(a|(bc)*d)*" abcbcbcdaaaabcbcdaaaddd
 *  true
 *
 *  Remarks
 *  -----------
 *  The following features are not supported:
 *    - The + operator
 *    - Multiway or
 *    - Metacharacters in the text
 *    - Character classes.
 *
"""

from algs4.digraph import Digraph
from algs4.directed_dfs import DirectedDFS
from algs4.link_list import Stack, Bag


class NFA:

    def __init__(self, regexp):
        self.regexp = regexp
        self.graph = Digraph(len(regexp) + 1)
        ops = Stack()

        for i, c in enumerate(regexp):
            lp = i

            # add '(' and '|' in stack
            if c in ('(', '|'):
                ops.push(i)
            elif c == ')':
                or_op = ops.pop()

                # 2-way or operator
                if regexp[or_op] == '|':
                    lp = ops.pop()
                    self.graph.add_edge(lp, or_op + 1)
                    self.graph.add_edge(or_op, i)
                elif regexp[or_op] == '(':
                    lp = or_op
                else:
                    raise ValueError('Invalid regular expression')

            # closure operator (uses 1-character lookahead)
            if i < len(regexp)-1 and regexp[i+1] == '*':
                self.graph.add_edge(lp, i+1)
                self.graph.add_edge(i+1, lp)
            if regexp[i] in ('(', '*', ')'):
                self.graph.add_edge(i, i+1)
        if  ops.size() != 0:
            raise ValueError('Invalid regular expression')
        
    def recognizes(self, txt: str) -> bool:
        dfs = DirectedDFS(self.graph, (0,))
        pc = Bag()
        # collect states from start
        for v in range(self.graph.V()):
            if dfs.marked(v):
                pc.add(v)
        # compute possible NFA states for txt[i+1]
        for i, c in enumerate(txt):
            if c in ('(', ')', '*', '|'):
                raise ValueError(f'text contains the metacharacter "{c}"')
            match = Bag()
            for v in pc:
                if v == len(self.regexp):
                    continue
                if self.regexp[v] in (c, '.'):
                    match.add(v+1)
            if match.is_empty():
                continue
            dfs = DirectedDFS(self.graph, match)
            pc = Bag()
            for v in range(self.graph.V()):
                if dfs.marked(v):
                    pc.add(v)
            # stop earlier
            if pc.size() == 0:
                return False
            
        # check for accept state
        for v in pc:
            if v == len(self.regexp):
                return True
        return False
    

if __name__ == '__main__':
    import sys
    regexp = '(' + sys.argv[1] + ')'
    txt = sys.argv[2]
    nfa = NFA(regexp)
    print(nfa.recognizes(txt))