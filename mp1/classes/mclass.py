

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
    
