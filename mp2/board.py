'''
board for the 2-player game
'''
from boardClass import *

def initBoard():
    board = []
    boardCells = {}
    x = 0
    y = 6
    row = 0

    for i in range(16):
        if i == 15:
            board.append('\n')
        else:
            if i == 0 or i == 14:
                board.append('|')
            else:
                board.append('-')

    for i in range(16, 224):
        if (i%16) == 15:
            board.append('\n')
            row += 1
            if row%2 == 0:
                y -= 1
                x = 0
        elif row%2 == 1:
            if i%16 == 0 or i%16 == 14:
                board.append('|')
            else:
                board.append('-')
        else:
            if (i%2) != 0:
                board.append(' ')
                if x == 0 or x == 6 or y == 0 or y == 6:
                    if x == 0:
                        left = -1
                        up_left = -1
                        down_left = -1
                        right = (x+1, y)
                        down = (x, y-1)
                        up = (x, y+1)
                        up_right = (x+1, y+1)
                        down_right = (x+1, y-1)

                    if x == 6:
                        right = -1
                        up_right = -1
                        down_right = -1
                        left = (x-1, y)
                        down = (x, y-1)
                        up = (x, y+1)
                        up_left = (x-1, y+1)
                        down_left = (x-1, y-1)

                    if y == 0:
                        down = -1
                        down_right = -1
                        down_left = -1
                        left = (x-1, y)
                        right = (x+1, y)
                        up = (x, y+1)
                        up_right = (x+1, y+1)
                        up_left = (x-1, y+1)

                    if y == 6:
                        up = -1
                        up_right = -1
                        up_left = -1
                        left = (x-1, y)
                        right = (x+1, y)
                        down = (x, y-1)
                        down_right = (x+1, y-1)
                        down_left = (x-1, y-1)

                else:
                    left = (x-1, y)
                    right = (x+1, y)
                    down = (x, y-1)
                    up = (x, y+1)
                    up_right = (x+1, y+1)
                    up_left = (x-1, y+1)
                    down_right = (x+1, y-1)
                    down_left = (x-1, y-1)

                cell = boardCell(i, x, y, up, down, left, right, up_right, up_left, down_right, down_left, '.')
                boardCells[(x,y)] = cell
                x += 1


            else:
                board.append('|')

    for i in range(224, 240):
        if i == 239:
            board.append('\n')
        else:
            if i%16 == 0 or i%16 == 14:
                board.append('|')
            else:
                board.append('-')



    return board, boardCells
