from mclass import *
from test import *

maze, cell_list, startIdx = getMaze('/mediumMaze.txt')

print maze

stack = []
stack.append(startIdx)
curr_cell = startIdx

while stack != []:
    if cell_list[curr_cell].right.isWall
