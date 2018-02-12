from mclass import *
import os
import sys
import requests
import json

sys.dont_write_bytecode = True

'''
getMaze(path):

Input: path (Where the maze is located in our local directory)
Outputs: maze (The maze as a string), cell_list (a list of mazeCells (class that we created)), startIdx (index of 'P'), finIdx (index of '.')

This function takes in the input maze from the text file and creates a mazeCell instance for each block in the maze. The mazeCells are then
used by the algorithms in order to traverse the maze.

This function is used with all the algorithms in part 1.1
'''

def getMaze(path):
    current_path = os.getcwd()

    with open(current_path + path) as infile:
        maze = infile.read()


    i = 0
    while maze[i] != '\n':
        i += 1


    maze_width = i+1           # This is for up/down calculations
    x = 0
    y = 0
    cell_list = []
    for idx in range(len(maze)):
        # 'null values' refer to -1
        # If the character is the newline, then use null values for all options in the mazeCell class
        if maze[idx] == '\n':
            x = 0
            y += 1
            cell = mazeCell(idx, -1, -1, -1, -1, -1, -1, False, False, False)
            cell_list.append(cell)

        # A "person" can never be on a wall cell, therefore set null values for all four sides, and set isWall as True
        elif maze[idx] == '%':
            cell = mazeCell(idx, x, y, -1, -1, -1, -1, True, False, False)
            cell_list.append(cell)
            x += 1

        # Calculated the index of right, left, up and down and set isStart to True
        elif maze[idx] == 'P':
            cell = mazeCell(idx, x, y, idx-maze_width, idx+maze_width, idx-1, idx+1, False, False, True)
            cell_list.append(cell)
            startIdx = idx
            x += 1

        # Calculated the index of right, left, up and down and set isSoln to True
        elif maze[idx] == '.':
            cell = mazeCell(idx, x, y, idx-maze_width, idx+maze_width, idx-1, idx+1, False, True, False)
            cell_list.append(cell)
            finIdx = idx
            x += 1

        # Calculated the index of right, left, up and down. This else statement is for the blank spaces in the maze
        else:
            cell = mazeCell(idx, x, y, idx-maze_width, idx+maze_width, idx-1, idx+1, False, False, False)
            cell_list.append(cell)
            x += 1

    return maze, cell_list, startIdx, finIdx

'''
getMazeWithFinList(path):

Input: path (Where the maze is located in our local directory)
Outputs: maze (The maze as a string), cell_list (a list of mazeCells (class that we created)), startIdx (index of 'P'), fin_list (list of indices of '.')

This function takes in the input maze from the text file and creates a mazeCell instance for each block in the maze. The mazeCells are then
used by the algorithms in order to traverse the maze. The structure of this function is the exact same is above, except all the final indices are put in a list

This function is used with the modified A* algorithm in 1.2
'''
def getMazeWithFinList(path):
    current_path = os.getcwd()

    with open(current_path + path) as infile:
        maze = infile.read()


    i = 0
    while maze[i] != '\n':
        i += 1


    maze_width = i+1           # This is for up/down calculations
    x = 0
    y = 0
    cell_list = []
    fin_list = []
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
            fin_list.append(idx)
            x += 1
        else:
            cell = mazeCell(idx, x, y, idx-maze_width, idx+maze_width, idx-1, idx+1, False, False, False)
            cell_list.append(cell)
            x += 1

    return maze, cell_list, startIdx, fin_list
