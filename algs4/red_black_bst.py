from algs4.bst import BST


class Node:
    
    def __init__(self, key, val, color, size):
        self.key = key
        self.val = val
        self.size = size
        self.color = color
        self.left, self.right = None, None


class RedBlackBST(BST):
    RED = True
    BLACK = False

    def __init__(self):
        super().__init__()
        self.root = None

    def is_red(self, node):
        if node is None:
            return False
        return node.color == self.RED
    
    def size(self):
        return self._size(self.root)
    
    def _size(self, node):
        if node is None:
            return 0
        return node.size
    
    def is_empty(self):
        return self.root is None
    
    def get(self, key):
        if key is None:
            raise KeyError('argument to get() is None')
        return self._get(self.root, key)
    
    def _get(self, node, key):
        while node:
            if key < node.key:
                node = node.left
            elif key >node.key:
                node = node.right
            else:
                return node.val
        return None
    
    def contains(self, key):
        return self.get(key) is not None
    
    def put(self, key, val):
        if key is None:
            raise KeyError('first argument to put() is None')
        if val is None:
            self.delete(key)
            return
        self.root = self._put(self.root, key, val)
        self.root.color = self.BLACK

    def _put(self, node, key, val):
        if node is None:
            return Node(key, val, self.RED, 1)
        if key < node.key:
            node.left = self._put(node.left, key, val)
        elif key > node.key:
            node.right = self._put(node.right, key, val)
        else:
            node.val = val

        # fix-up any right-leaning links
        if self.is_red(node.right) and not self.is_red(node.left):
            node = self.rotate_left(node)
        if self.is_red(node.left) and self.is_red(node.left.left):
            node = self.rotate_right(node)
        if self.is_red(node.left) and self.is_red(node.right):
            self.flip_colors(node)
        node.size = self._size(node.left) + self._size(node.right) + 1

        return node
    
    def rotate_right(self, node):
        assert node is not None and self.is_red(node.left)
        x = node.left
        node.left = x.right
        x.right =node
        x.color = node.color
        node.color = self.RED
        x.size = node.size
        node.size = self._size(node.left) + self._size(node.right) + 1
        return x

    def rotate_left(self, node):
        assert node is not None and self.is_red(node.right)
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = self.RED
        x.size = node.size
        node.size = self._size(node.left) + self._size(node.right) + 1
        return x

    def flip_colors(self, node):
        node.color = not node.color
        node.left.color = not node.left.color
        node.right.color = not node.right.color

    def delete(self, key):
        ...