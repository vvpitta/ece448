'''
MazeCell class:
    Keeps track of index, x coordinate, y coordinate, index above, index below, index to the right, and index to the left of the
    current space in the maze.
    Also maintains if the current space is a wall, is a solution, or is a start
'''

class mazeCell:
    def __init__(self, idx,x, y, up, down, left, right, isWall, isSoln, isStart):
        self.idx = idx
        self.x = x
        self.y = y
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.isWall = isWall
        self.isSoln = isSoln
        self.isStart = isStart
