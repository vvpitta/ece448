class boardCell:
    def __init__(self, idx,x, y, up, down, left, right, up_right, up_left, down_right, down_left, char):
        self.idx = idx
        self.x = x
        self.y = y
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.up_right = up_right
        self.up_left = up_left
        self.down_right = down_right
        self.down_left = down_left
        self.char = char

    def set_char(self, new_char):
        self.char = new_char
