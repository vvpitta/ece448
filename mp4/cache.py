# This file will be used to do part 2 of the MP

'''
    These classes are used in the storage of elements in the forward
    and backward propagation for the four layer neural net
'''
class AffineCache:

    def __init__(self, A, W, b):
        self.A = A
        self.W = W
        self.b = b

    def getAll(self):
        return self.A, self.W, self.b


class ReLUCache:

    def __init__(self, Z, Zchange):
        self.Z = Z
        self.Zchange = Zchange

    def getAll(self):
        return self.Z, self.Zchange
