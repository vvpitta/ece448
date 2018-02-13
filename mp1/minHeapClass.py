import heapq

'''
MinHeap class:
    This class is designed to replicate a MinHeap using the heapq module.
    The functionality includes:
        isEmpty
        Push
        Pop
'''

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
    
    def pop_tuple(self):
        retval = heapq.heappop(self.data)
        return retval
