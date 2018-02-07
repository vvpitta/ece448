from mclass import *
import os
import sys
import requests
import json

sys.dont_write_bytecode = True

def getMaze(path):
    current_path = os.getcwd()

    with open(current_path + path) as infile:
        maze = infile.read()


    i = 0
    while maze[i] != '\n':
        i += 1

    test = [1,2]
    print test[-1]
    maze_width = i+1           # This is for up/down calculations
    x = 0
    y = 0
    cell_list = []
    for idx in range(len(maze)):
        if maze[idx] == '\n':
            x = 0
            y += 1
            cell = mazeCell(idx, -1, -1, -1, -1, -1, -1, False, False, False)
            cell_list.append(cell)
        elif maze[idx] == '%':
            cell = mazeCell(idx, x, y, -1, -1, -1, -1, True, False, False)
            cell_list.append(cell)
            x += 1
        elif maze[idx] == 'P':
            cell = mazeCell(idx, x, y, idx-maze_width, idx+maze_width, idx-1, idx+1, False, False, True)
            cell_list.append(cell)
            startIdx = idx
            x += 1
        elif maze[idx] == '.':
            cell = mazeCell(idx, x, y, idx-maze_width, idx+maze_width, idx-1, idx+1, False, True, False)
            cell_list.append(cell)
            x += 1
        else:
            cell = mazeCell(idx, x, y, idx-maze_width, idx+maze_width, idx-1, idx+1, False, False, False)
            cell_list.append(cell)
            x += 1

    return maze, cell_list, startIdx
