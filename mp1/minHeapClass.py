import heapq

class minHeap:
    def __init__(self):
        self.priorityQueue = []

    def push(self, cell, heuristicPriority):
        heapq.heappush(self.priorityQueue, (heuristicPriority, cell))

    def pop(self):
        retval = heapq.heappop(self.priorityQueue)
        return retval[1]

    def isEmpty(self):
        return len(self.priorityQueue) == 0
