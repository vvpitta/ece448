import heapq

class MinHeap:
    def __init__(self):
        self.data = []

    def isEmpty(self):
        return len(self.data) == 0

    def push(self, cell, key):
        heapq.heappush(self.data, (key, cell))

    def pop(self):
        retval = heapq.heappop(self.data)
        return retval[1]
