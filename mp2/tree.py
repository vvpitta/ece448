'''
tree class
'''

class tree:
    def __init__(self, boardCells, x, y, value):
        self.boardCells = boardCells
        self.children = []
        self.value = value
        self.x = x
        self.y = y


    def children_append(self, child):
        self.children.append(child)

    def set_value(self, value):
        self.value = value
