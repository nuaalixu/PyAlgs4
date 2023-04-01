import sys
import abc
from typing import List


class Sort(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def sort(cls, arr: List):
        ...

    @classmethod
    def is_sorted(cls, arr: List):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                return False
        else:
              return True
    
    @classmethod
    def show(cls, arr: List):
        print(" ".join(arr))
    
    @classmethod
    def main(cls):
        items = []
        for line in sys.stdin:
            items.extend(line.split())
        arr = cls.sort(items)
        assert cls.is_sorted(arr)
        cls.show(arr)
