# This file will be used to determine the class representation of a state

class StateNode:
    def __init__(self):
        self.widget1 = [0,0,0,0,0]
        self.widget2 = [0,0,0,0,0]
        self.widget3 = [0,0,0,0,0]
        self.widget4 = [0,0,0,0,0]
        self.widget5 = [0,0,0,0,0]

    def getw1(self):
        return self.widget1

    def getw2(self):
        return self.widget2

    def getw3(self):
        return self.widget3

    def getw4(self):
        return self.widget4

    def getw5(self):
        return self.widget5

    def printState(self):
        print "W1:", self.widget1
        print "W2:", self.widget2
        print "W3:", self.widget3
        print "W4:", self.widget4
        print "W5:", self.widget5
        return

    def updateWidgets(self, city):
        widget1global = [0, 4, 3, 2, 0]
        widget2global = [1, 4, 0, 2, 3]
        widget3global = [1, 0, 1, 2, 4]
        widget4global = [3, 0 ,3, 1, 3]
        widget5global = [1, 4, 2, 1, 3]

        for componentIdx in range(len(self.widget1)):
            if self.widget1[componentIdx] == 0:
                if widget1global[componentIdx] == city:
                    self.widget1[componentIdx] = 1
                    break
                else:
                    break

        for componentIdx in range(len(self.widget2)):
            if self.widget2[componentIdx] == 0:
                if widget2global[componentIdx] == city:
                    self.widget2[componentIdx] = 1
                    break
                else:
                    break

        for componentIdx in range(len(self.widget3)):
            if self.widget3[componentIdx] == 0:
                if widget3global[componentIdx] == city:
                    self.widget3[componentIdx] = 1
                    break
                else:
                    break

        for componentIdx in range(len(self.widget4)):
            if self.widget4[componentIdx] == 0:
                if widget4global[componentIdx] == city:
                    self.widget4[componentIdx] = 1
                    break
                else:
                    break

        for componentIdx in range(len(self.widget5)):
            if self.widget5[componentIdx] == 0:
                if widget5global[componentIdx] == city:
                    self.widget5[componentIdx] = 1
                    break
                else:
                    break

        return
