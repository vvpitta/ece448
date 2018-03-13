'''
tree class
'''

class tree:
    def __init__(self, boardCells, x, y, value, depth, nodes_expanded):
        self.boardCells = boardCells
        self.children = []
        self.value = value
        self.x = x
        self.y = y
        self.nodes_expanded = nodes_expanded
        self.depth = depth

    def children_append(self, child):
        self.children.append(child)

    def set_value(self, value):
        self.value = value

    def set_nodes_expanded(self, nodes_expanded):
        self.nodes_expanded = nodes_expanded
