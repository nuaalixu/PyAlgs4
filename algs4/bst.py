import sys

from algs4.st import ST


class Node:
    
    def __init__(self, key, val, N):
        self.key = key
        self.val = val
        self.N = N
        self.left, self.right = None, None

    def size(self):
        return self.N
    
    def __repr__(self):
        return f'{self.__class__.__qualname__}({self.key}, {self.val}, {self.N})'


class BST(ST):
    
    def __init__(self):
        super().__init__()
        self.root = None

    def is_empty(self):
        return self.root is None

    def size(self):
        return self._size(self.root)
    
    def _size(self, node):
        if node is None:
            return 0
        return node.size()
    
    def contains(self, key):
        if key is None:
            raise KeyError('argument to contains() is None')
        return self.get(key) is not None

    def get(self, key):
        if key is None:
            raise KeyError('calls get() with a None key')
        node = self._get(self.root, key)
        if node is None:
            return None
        return node.val
    
    def _get(self, node, key):
        if node is None:
            return None
        if node.key == key:
            return node
        elif node.key < key:
            return self._get(node.right, key)
        else:
            return self._get(node.left, key)
        
    def put(self, key, val):
        if key is None:
            raise KeyError('calls put() with a None key')
        if val is None:
            self.delete(key)
            return
        self.root = self._put(self.root, key, val)
    
    def _put(self, node, key, val):
        if node is None:
            return Node(key, val, 1)
        if node.key < key:
            node.right = self._put(node.right, key, val)
        elif node.key > key:
            node.left = self._put(node.left, key, val)
        else:
            node.val = val
        node.N = self._size(node.left) + self._size(node.right) + 1
        return node

    def min(self):
        if self.is_empty():
            raise ValueError('calls min() with empty symbol table')
        return self._min(self.root).key
    
    def _min(self, node):
        if node.left is None:
            return node
        return self._min(node.left)
    
    def max(self):
        if self.is_empty():
            raise ValueError('calls max() with empty symbol table')
        return self._max(self.root).key
    
    def _max(self, node):
        if node.right is None:
            return node
        return self._max(node.right)

    def floor(self, key):
        if key is None:
            raise ValueError('argument to floor() is None')
        if self.is_empty():
            raise ValueError('calls floor() with empty symbol table')
        node = self._floor(self.root, key)
        if node is None:
            raise ValueError('argument to floor() is too small')
        return node.key

    def _floor(self, node, key):
        if node is None:
            return None
        if node.key == key:
            return node
        if node.key > key:
            return self._floor(node.left, key)
        t = self._floor(node.right, key)
        if t is None:
            return node
        return t

    def ceiling(self, key):
        if key is None:
            raise ValueError('argument to ceiling() is None')
        if self.is_empty():
            raise ValueError('calls ceiling() with empty symbol table')
        node =  self._ceiling(self.root, key)
        if node is None:
            raise ValueError('argument to ceiling() is too large')
        return node.key

    def _ceiling(self, node, key):
        if node is None:
            return None
        if node.key == key:
            return node
        if node.key < key:
            return self._ceiling(node.right, key)
        t = self._ceiling(node.left, key)
        if t is None:
            return node
        return t
    
    def select(self, k):
        if k < 0 or k >= self.size():
            raise ValueError('argument to select() is invalid')
        return self._select(self.root, k).key
    
    def _select(self, node ,k):
        if node is None:
            return None
        ls = self._size(node.left)
        if ls == k:
            return node
        elif ls > k:
            return self._select(node.left, k)
        else:
            return self._select(node.right, k - ls - 1)
    
    def rank(self, key):
        if key is None:
            raise  ValueError('argument to rank() is null')
        return self._rank(self.root, key)
    
    def _rank(self, node, key):
        if node is None:
            return 0
        if node.key == key:
            return self._size(node.left)
        elif node.key > key:
            return self._rank(node.left, key)
        else:
            return self._size(node.left) + 1 + self._rank(node.right, key)
        
    def del_min(self):
        if self.is_empty():
            raise IndexError('Symbol table underflow')
        self.root = self._del_min(self.root)

    def _del_min(self, node):
        if node.left is None:
            return node.right
        node.left = self._del_min(node.left)
        node.N = self._size(node.left) + self._size(node.right) + 1
        return node

    def del_max(self):
        if self.is_empty():
            raise IndexError('Symbol table underflow')
        self.root = self._del_max(self.root)

    def _del_max(self, node):
        if node.right is None:
            return node.left
        node.right = self._del_max(node.right)
        node.N = self._size(node.left) + self._size(node.right) + 1
        return node

    def delete(self ,key):
        if key is None:
            raise KeyError('calls delete() with a null key')
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key >node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            tgt = node
            node = self._min(tgt.right)
            node.right = self._del_min(tgt.right)
            node.left = tgt.left
        node.N = self._size(node.left) + self._size(node.right)  + 1
        return node
    
    def keys(self):
        if self.is_empty():
            return []
        keys = []
        self._keys(self.root, keys, self.min(), self.max())
        return keys

    def _keys(self, node, queue, lo, hi):
        if node is None:
            return
        if node.key > lo:
            self._keys(node.left, queue, lo, hi)
        if node.key >= lo and node.key <= hi:
            queue.append(node.key)
        if node.key < hi:
            self._keys(node.right, queue, lo, hi)

    def height(self):
        return self._height(self.root)
    
    def _height(self, node):
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

    def level_order(self):
        """Return the keys in the BST in level order."""
        keys = []
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node is None:
                continue
            keys.append(node.key)
            queue.append(node.left)
            queue.append(node.right)
        return keys

    def __str__(self):
        keys = self.level_order()
        return str(keys)



if __name__ == '__main__':
    st = BST()
    i = 0
    for line in sys.stdin:
        for key in line.split():
            st.put(key, i)
            i += 1

    for key in st.keys():
        print(f'{key} {st.get(key)}')
