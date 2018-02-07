from mclass import *
from test import *

maze, cell_list, startIdx = getMaze('/openMaze.txt')

print maze

stack = []
stack.append(startIdx)
marked = []
marked.append(startIdx)
curr_cell = startIdx

while stack != []:
    if cell_list[cell_list[curr_cell].right].isWall == False and cell_list[cell_list[curr_cell].right].idx not in marked:
        if cell_list[cell_list[curr_cell].right].isSoln == True:
            curr_cell = cell_list[cell_list[curr_cell].right].idx
            stack.append(curr_cell)
            marked.append(curr_cell)
            break
        else:
            curr_cell = cell_list[cell_list[curr_cell].right].idx
            stack.append(curr_cell)
            marked.append(curr_cell)

    elif cell_list[cell_list[curr_cell].left].isWall == False and cell_list[cell_list[curr_cell].left].idx not in marked:
        if cell_list[cell_list[curr_cell].left].isSoln == True:
            curr_cell = cell_list[cell_list[curr_cell].left].idx
            stack.append(curr_cell)
            marked.append(curr_cell)
            break
        else:
            curr_cell = cell_list[cell_list[curr_cell].left].idx
            stack.append(curr_cell)
            marked.append(curr_cell)

    elif cell_list[cell_list[curr_cell].up].isWall == False and cell_list[cell_list[curr_cell].up].idx not in marked:
        if cell_list[cell_list[curr_cell].up].isSoln == True:
            curr_cell = cell_list[cell_list[curr_cell].up].idx
            stack.append(curr_cell)
            marked.append(curr_cell)
            break
        else:
            curr_cell = cell_list[cell_list[curr_cell].up].idx
            stack.append(curr_cell)
            marked.append(curr_cell)

    elif cell_list[cell_list[curr_cell].down].isWall == False and cell_list[cell_list[curr_cell].down].idx not in marked:
        if cell_list[cell_list[curr_cell].down].isSoln == True:
            curr_cell = cell_list[cell_list[curr_cell].down].idx
            stack.append(curr_cell)
            marked.append(curr_cell)
            break
        else:
            curr_cell = cell_list[cell_list[curr_cell].down].idx
            stack.append(curr_cell)
            marked.append(curr_cell)

    else:
        stack.pop()
        curr_cell = stack[-1]

new_maze = list(maze)


for index in stack:
    new_maze[index] = '.'

new_maze[stack[0]] = 'P'

print '\n'
maze_string = ''.join(new_maze)
print maze_string
file = open('testmaze_open.txt', 'w')
file.write(maze_string)
