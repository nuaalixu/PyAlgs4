
class Node:

    def __init__(self, item, next_node):
        self.item = item
        self.next = next_node


class LinkIterator:

    def __init__(self, current):
        self.current = current

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current is None:
            raise StopIteration()
        else:
            item = self.current.item
            self.current = self.current.next
            return item


class Bag:

    def __init__(self):
        self.first = None
        self.n = 0

    def __str__(self):
        return " ".join(str(i) for i in self)

    def __iter__(self):
        return LinkIterator(self.first)

    def size(self):
        return self.n

    def is_empty(self):
        return self.first is None

    def add(self, item):
        oldfirst = self.first
        self.first = Node(item, oldfirst)
        self.n += 1


class Stack:

    def __init__(self):
        self.first = None
        self.n = 0

    def __str__(self):
        return " ".join(i for i in self)

    def __iter__(self):
        return LinkIterator(self.first)

    def size(self):
        return self.n

    def is_empty(self):
        return self.first is None

    def push(self, item):
        oldfirst = self.first
        self.first = Node(item, oldfirst)
        self.n += 1

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack underflow")
        else:
            item = self.first.item
            self.first = self.first.next
            self.n -= 1
            return item
        

class Queue:

    def __init__(self):
        self.first = None
        self.last = None
        self.n = 0

    def __str__(self):
        return " ".join(i for i in self)

    def __iter__(self):
        return LinkIterator(self.first)

    def size(self):
        return self.n

    def is_empty(self):
        return self.first is None

    def enqueue(self, item):
        oldlast = self.last
        self.last = Node(item, None)
        if self.is_empty():
            self.first = self.last
        else:
            oldlast.next = self.last
        self.n += 1

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue empty")
        else:
            item = self.first.item
            self.first = self.first.next
            if self.is_empty():
                self.last = None
            self.n -= 1
            return item
