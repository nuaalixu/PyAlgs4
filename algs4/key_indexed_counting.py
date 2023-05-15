from typing import List
from algs4.sort import Sort


class Node:

    def __init__(self, key: int, val: str):
        self.key = key
        self.val = val

    def __str__(self):
        return f'{self.val}\t{self.key}'

class KeyIndexedCounting:
    
    def __init__(self, R):
        self.R = R

    def sort(self, arr: List[Node]) -> List:
        count = [0] * (self.R + 1)
        aux = [None] * len(arr)
        for node in arr:
            count[node.key + 1] += 1
        
        for i in range(self.R):
            count[i + 1] += count[i]

        for node in arr:
            aux[count[node.key]] = node
            count[node.key] += 1
        
        # demonstrate intentionally.
        for i in range(len(arr)):
            arr[i] = aux[i]
        
        return arr


if __name__ == '__main__':
    arr = [
        Node(2, 'Anderson'),
        Node(3, 'Brown'),
        Node(3, 'Davis'),
        Node(4, 'Garcia'),
        Node(1, 'Harris'),
        Node(3, 'Jackson')
    ]
    kic = KeyIndexedCounting(5)
    print("name\tgroup")
    print('\n'.join(str(node) for node in arr))
    arr = kic.sort(arr)
    print("name\tgroup")
    print('\n'.join(str(node) for node in arr))