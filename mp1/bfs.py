from maze import *
from mclass import *
from collections import deque


def backtrace(parent, start, end):
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse
    return path

maze, cell_list, startIdx, finIdx = getMaze('/openMaze.txt')

print maze

queue = deque([])
queue.append(startIdx)
marked = []
marked.append(startIdx)
curr_cell = startIdx
parent = {}
##print(curr_cell)
##i = 0
while queue:
    curr_cell = queue.popleft()
    ##i = i+1

    ##print (curr_cell)
    ##break
    ##queue.popleft()
    ##curr_cell = queue [-1]
    ##print(cell_list[cell_list[curr_cell].right].isWall)
    if cell_list[cell_list[curr_cell].right].isWall == False and cell_list[cell_list[curr_cell].right].idx not in marked:
        if cell_list[cell_list[curr_cell].right].isSoln == True:
            right = cell_list[cell_list[curr_cell].right].idx
            parent[right] = curr_cell
            queue.append(right)
            marked.append(right)
            break
        else:
            right = cell_list[cell_list[curr_cell].right].idx
            parent[right] = curr_cell
            queue.append(right)
            marked.append(right)
            ##print('reached right')

    if cell_list[cell_list[curr_cell].left].isWall == False and cell_list[cell_list[curr_cell].left].idx not in marked:
        if cell_list[cell_list[curr_cell].left].isSoln == True:
            left = cell_list[cell_list[curr_cell].left].idx
            parent[left] = curr_cell
            queue.append(left)
            marked.append(left)
            break
        else:
            left = cell_list[cell_list[curr_cell].left].idx
            parent[left] = curr_cell
            queue.append(left)
            marked.append(left)
            ##print('reached left')

    if cell_list[cell_list[curr_cell].up].isWall == False and cell_list[cell_list[curr_cell].up].idx not in marked:
        if cell_list[cell_list[curr_cell].up].isSoln == True:
            up = cell_list[cell_list[curr_cell].up].idx
            parent[up] = curr_cell
            queue.append(up)
            marked.append(up)
            break
        else:
            up = cell_list[cell_list[curr_cell].up].idx
            parent[up] = curr_cell
            queue.append(up)
            marked.append(up)
            ##print('reached up')

    if cell_list[cell_list[curr_cell].down].isWall == False and cell_list[cell_list[curr_cell].down].idx not in marked:
        if cell_list[cell_list[curr_cell].down].isSoln == True:
            down = cell_list[cell_list[curr_cell].down].idx
            parent[down] = curr_cell
            queue.append(down)
            marked.append(down)
            break
        else:
            down = cell_list[cell_list[curr_cell].down].idx
            parent[down] = curr_cell
            queue.append(down)
            marked.append(down)
            ##print('reached down')

##print (queue)
fin_path = backtrace(parent, startIdx, finIdx)
new_maze = list(maze)

for index in fin_path:
    new_maze[index] = '.'

new_maze[fin_path[-1]] = 'P'
print '\n'
maze_string = ''.join(new_maze)
print maze_string
file = open('testmazebfs_open.txt', 'w')
file.write(maze_string)
##print(new_maze[marked[len(marked)-1]])
##print(marked[len(marked)-1])
##print(marked)
