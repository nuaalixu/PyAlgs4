from abc import ABC, abstractmethod
from typing import Any, Iterator


class Node:

    def __init__(self, key, val, next_node):
        self.key = key
        self.val = val
        self.next = next_node


class ST(ABC):
    
    @abstractmethod
    def put(self, key, val) -> None:
        ...

    @abstractmethod
    def get(self, key) -> Any:
        ...

    def delete(self, key) -> None:
        self.put(key, None)

    @abstractmethod
    def contains(self, key) -> bool:
        ...

    @abstractmethod
    def is_empty(self) -> bool:
        ...

    @abstractmethod
    def size(self) -> int:
        ...

    @abstractmethod
    def keys(self) -> Iterator:
        ...


class STKeyIterator:

    def __init__(self, cur):
        self.cur = cur

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.cur is None:
            raise StopIteration()
        else:
            key = self.cur.key
            self.cur = self.cur.next
            return key
        