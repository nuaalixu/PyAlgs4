import sys

from algs4.st import Node, ST, STKeyIterator


class SequentialSearchST(ST):

    def __init__(self):
        self.n = 0
        self.first: Node = None

    def size(self) -> int:
        return self.n

    def is_empty(self) -> bool:
        return self.size() == 0

    def contains(self, key) -> bool:
        if key is None:
            raise ValueError('argument to contains() is None')
        return self.get(key) is not None

    def get(self, key):
        if key is None:
            raise ValueError('argument to get() is None')
        x = self.first
        while x:
            if key == x.key:
                return x.val
            x = x.next
        return None

    def put(self, key, val):
        if key is None:
            raise ValueError('argument to put() is None')
        x = self.first
        while x:
            if key == x.key:
                x.val = val
                return
            x = x.next
        self.first = Node(key, val, self.first)
        self.n += 1

    def delete(self, key):
        if key is None:
            raise ValueError('argument to delete() is None')
        last: Node = None
        x = self.first
        while x:
            if key == x.key:
                self.n -= 1
                if last:
                    last.next = x.next
                else:
                    self.first = x.next
                return
            last = x
            x = x.next

    def keys(self):
        return STKeyIterator(self.first)


if __name__ == '__main__':
    st = SequentialSearchST()
    i = 0
    for line in sys.stdin:
        for key in line.split():
            st.put(key, i)
            i += 1

    for key in st.keys():
        print(f'{key} {st.get(key)}')
        