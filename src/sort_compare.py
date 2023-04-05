import sys
import time
import random
from typing import List

from insertion import InsertionSort
from selection import SelectionSort
from shell import ShellSort


class SortClassFactory:
    sort_classes = {
        'insertion': InsertionSort,
        'selection': SelectionSort,
        'shell': ShellSort
    }

    @classmethod
    def create_class(cls, name: str):
        try:
            sort_class = cls.sort_classes[name]
            return sort_class
        except KeyError:
            raise ValueError(f'class {name} is not supported')


class SortCompare:
    @classmethod
    def time(cls, name: str, arr: List):
        sort_class = SortClassFactory.create_class(name.lower())
        st = time.process_time()
        sort_class.sort(arr)
        return time.process_time() - st

    @classmethod
    def time_random_input(cls, name, count: int, length: int):
        total = 0
        for _ in range(count):
            arr = [random.uniform(0, 1)  for _ in range(length)]
            total += cls.time(name, arr)
        return total
    
    @classmethod
    def main(cls):
        try:
            alg1 = sys.argv[1]
            alg2 = sys.argv[2]
            count = int(sys.argv[3])
            length = int(sys.argv[4])
        except IndexError:
            raise ValueError('Usage: this.py <alg1> <alg2> <test-count> <array-length>')

        t1 = cls.time_random_input(alg1, count, length)
        t2 = cls.time_random_input(alg2, count, length)

        print(f'For {count} random Floats\n'
              f'{alg1} is {t2/t1:.2f} times faster than {alg2}')


if __name__ == '__main__':
    SortCompare.main()