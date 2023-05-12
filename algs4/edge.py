class Edge:

    def __init__(self, v: int, w: int, weight: float):
        self.v = v
        self.w = w
        self.weight = weight

    def either(self):
        return self.v
    
    def other(self, vertext: int):
        if vertext == self.v:
            return self.w
        elif vertext == self.w:
            return self.v
        else:
            raise ValueError('Illegal endpoint')
    
    def __gt__(self, other):
        assert isinstance(other, Edge)
        return self.weight > other.weight

    def __str__(self):
        return f'{self.v}-{self.w} {self.weight:.5f}'
    

if __name__ == '__main__':
    e = Edge(12, 34, 5.67)
    print(e)