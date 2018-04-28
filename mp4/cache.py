# This file will be used to do part 2 of the MP

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
