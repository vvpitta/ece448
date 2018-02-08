from mclass import *
from maze import *
import math


def Distance(curr_cell, fin_cell):
    x_squared = math.pow((fin_cell.x - curr_cell.x), 2)
    y_squared = math.pow((fin_cell.y - curr_cell.y), 2)

    dist = math.sqrt(x_squared + y_squared)

    return dist


maze, cell_list, startIdx, finIdx = getMaze('/bigMaze.txt')

print maze
stack = []
stack.append(startIdx)
marked = []
marked.append(startIdx)
curr_cell = startIdx
fin_cell = cell_list[finIdx]

while stack != []:
    curr_cell_right = cell_list[cell_list[curr_cell].right]
    curr_cell_left = cell_list[cell_list[curr_cell].left]
    curr_cell_up = cell_list[cell_list[curr_cell].up]
    curr_cell_down = cell_list[cell_list[curr_cell].down]

    dist_right = Distance(curr_cell_right, fin_cell)
    dist_left = Distance(curr_cell_left, fin_cell)
    dist_up = Distance(curr_cell_up, fin_cell)
    dist_down = Distance(curr_cell_down, fin_cell)

    distances = [(curr_cell_right, dist_right), (curr_cell_left,dist_left), (curr_cell_up,dist_up), (curr_cell_down, dist_down)]
    dist_sorted = sorted(distances, key = lambda x:x[1])
    if curr_cell == 214:
        print distances
        print dist_sorted

    if dist_sorted[0][0].isWall == False and dist_sorted[0][0].idx not in marked:
        if dist_sorted[0][0].isSoln == True:
            curr_cell = dist_sorted[0][0].idx
            stack.append(curr_cell)
            marked.append(curr_cell)
            break
        else:
            curr_cell = dist_sorted[0][0].idx
            stack.append(curr_cell)
            marked.append(curr_cell)

    elif dist_sorted[1][0].isWall == False and dist_sorted[1][0].idx not in marked:
        if dist_sorted[1][0].isSoln == True:
            curr_cell = dist_sorted[1][0].idx
            stack.append(curr_cell)
            marked.append(curr_cell)
            break
        else:
            curr_cell = dist_sorted[1][0].idx
            stack.append(curr_cell)
            marked.append(curr_cell)

    elif dist_sorted[2][0].isWall == False and dist_sorted[2][0].idx not in marked:
        if dist_sorted[2][0].isSoln == True:
            curr_cell = dist_sorted[2][0].idx
            stack.append(curr_cell)
            marked.append(curr_cell)
            break
        else:
            curr_cell = dist_sorted[2][0].idx
            stack.append(curr_cell)
            marked.append(curr_cell)

    elif dist_sorted[3][0].isWall == False and dist_sorted[3][0].idx not in marked:
        if dist_sorted[3][0].isSoln == True:
            curr_cell = dist_sorted[3][0].idx
            stack.append(curr_cell)
            marked.append(curr_cell)
            break
        else:
            curr_cell = dist_sorted[3][0].idx
            stack.append(curr_cell)
            marked.append(curr_cell)
    else:
        stack.pop()
        curr_cell = stack[-1]

new_maze = list(maze)
for index in stack:
    new_maze[index] = '.'

print stack
new_maze[stack[0]] = 'P'

print '\n'
maze_string = ''.join(new_maze)
print maze_string
file = open('testgreedy_big.txt', 'w')
file.write(maze_string)
