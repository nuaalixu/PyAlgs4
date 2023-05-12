class DirectedEdge:

    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def From(self):
        return self.v
    
    def To(self):
        return self.w

    def __str__(self):
        return f"{self.v}->{self.w} {self.weight:.5f}"
    
    def __gt__(self, other):
        return self.weight > other.weight
    

if __name__ == '__main__':
    e = DirectedEdge(12, 34, 5.67)
    print(e)
