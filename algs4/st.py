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
        if key is None:
            raise ValueError('argument to put() is None')
        if val is None:
            self.delete(key)
            return

    @abstractmethod
    def get(self, key) -> Any:
        if key is None:
            raise ValueError('argument to get() is None')

    @abstractmethod
    def delete(self, key) -> None:
        if key is None:
            raise ValueError('argument to delete() is None')
        if not self.contains(key):
            return

    @abstractmethod
    def contains(self, key) -> bool:
        if key is None:
            raise ValueError('argument to contains() is None')

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
        key = self.cur.key
        self.cur = self.cur.next
        return key
