from mclass import *
from maze import *
import math
import Queue


def Distance(curr_cell, fin_cell):
    x_squared = math.pow((fin_cell.x - curr_cell.x), 2)
    y_squared = math.pow((fin_cell.y - curr_cell.y), 2)

    dist = math.sqrt(x_squared + y_squared)

    return dist


def backtrace(parent, start, end):
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse
    return path

maze, cell_list, startIdx, finIdx = getMaze('/inputMazes/bigMaze.txt')

print maze
parent = {}
p_q = Queue.PriorityQueue()
dist_to_goal = Distance(cell_list[startIdx], cell_list[finIdx])
p_q.put((dist_to_goal, startIdx))
marked = []
marked.append(startIdx)
curr_cell = startIdx
fin_cell = cell_list[finIdx]
parent = {}


while p_q != []:
    curr_cell = p_q.get()[1]

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


    if dist_sorted[0][0].isWall == False and dist_sorted[0][0].idx not in marked:
        if dist_sorted[0][0].isSoln == True:
            first = dist_sorted[0][0].idx
            parent[first] = curr_cell
            p_q.put((dist_sorted[0][1], first))
            marked.append(first)
            break
        else:
            first = dist_sorted[0][0].idx
            parent[first] = curr_cell
            p_q.put((dist_sorted[0][1], first))
            marked.append(first)

    if dist_sorted[1][0].isWall == False and dist_sorted[1][0].idx not in marked:
        if dist_sorted[1][0].isSoln == True:
            second = dist_sorted[1][0].idx
            parent[second] = curr_cell
            p_q.put((dist_sorted[1][1], second))
            marked.append(second)
            break
        else:
            second = dist_sorted[1][0].idx
            parent[second] = curr_cell
            p_q.put((dist_sorted[1][1], second))
            marked.append(second)

    if dist_sorted[2][0].isWall == False and dist_sorted[2][0].idx not in marked:
        if dist_sorted[2][0].isSoln == True:
            third = dist_sorted[2][0].idx
            parent[third] = curr_cell
            p_q.put((dist_sorted[2][1], third))
            marked.append(third)
            break
        else:
            third = dist_sorted[2][0].idx
            parent[third] = curr_cell
            p_q.put((dist_sorted[2][1], third))
            marked.append(third)

    if dist_sorted[3][0].isWall == False and dist_sorted[3][0].idx not in marked:
        if dist_sorted[3][0].isSoln == True:
            fourth = dist_sorted[3][0].idx
            parent[fourth] = curr_cell
            p_q.put((dist_sorted[3][1], fourth))
            marked.append(fourth)
            break
        else:
            fourth = dist_sorted[3][0].idx
            parent[fourth] = curr_cell
            p_q.put((dist_sorted[3][1], fourth))
            marked.append(fourth)

fin_path = backtrace(parent, startIdx, finIdx)
new_maze = list(maze)
for index in fin_path:
    new_maze[index] = '.'


new_maze[fin_path[-1]] = 'P'

path_cost = "\n" + "Path cost: " + str(len(fin_path)) + "\n"
nodes_expanded = "Nodes expanded: " + str(len(marked))
print '\n'
maze_string = ''.join(new_maze)
print maze_string + path_cost + nodes_expanded
file = open('testgreedy_big.txt', 'w')
file.write(maze_string)
