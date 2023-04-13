class MinPQ:
    def __init__(self):
        self.__pq = []

    def is_empty(self):
        return len(self.__pq) == 0
    
    def size(self):
        return len(self.__pq)
    
    def insert(self, v):
        self.__pq.append(v)
        self.swim(len(self.__pq) - 1)

    def del_min(self) -> int:
        m = self.__pq[0]
        self.__pq[0] = self.__pq[-1]
        self.__pq.pop()
        self.sink(0)
        return m
    
    def swim(self, k):
        while k > 0 and self.__pq[k] < self.__pq[(k - 1) // 2]:
            self.__pq[k], self.__pq[(k - 1) // 2] = self.__pq[(k - 1) // 2], self.__pq[k]
            k = (k - 1) // 2

    def sink(self, k):
        while 2 * k + 1 < len(self.__pq):
            j = 2 * k + 1
            if j + 1 < len(self.__pq) and self.__pq[j] > self.__pq[j + 1]:
                j += 1
            if self.__pq[k] < self.__pq[j]:
                break
            self.__pq[k], self.__pq[j] = self.__pq[j], self.__pq[k]
            k = j
