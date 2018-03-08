# This class will be used to implement priority queue

import heapq

class MinHeap:
    def __init__(self):
        self.data = []

    def isEmpty(self):
        return len(self.data) == 0

    def push(self, state, key):
        heapq.heappush(self.data, (key, state))

    def pop(self):
        return heapq.heappop(self.data)[1]
