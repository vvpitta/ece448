'''
DFS using a stack structure to hold the path.
Starting from the start index, the algorithm will keep trying to go the right space, till it hits a
wall or the solution. If a wall, the algoritm will try a left move. If invalid, the algorithm will try an up move.
Lastly, if invalid again, the algoritm will try a down move. If all four moves are invalid, the algorithm will backtrack
to a cell in which the next move in sequence is valid.
The sequence of moves is: Right till fail or solution, Left till fail or solution, Up till fail or solution, Down till fail or solution

DFS does not give the optimal path almost ever; rather it finds whether a path exists from the start state to the final state.
'''
from mclass import *
from maze import *

maze, cell_list, startIdx, finIdx = getMaze('/inputMazes/bigMaze.txt')

print maze

stack = []                               # Stack to hold indices of cells in the path
stack.append(startIdx)
marked = []                              # List to hold indices of visited cells, so we don't visit cells twice
marked.append(startIdx)
curr_cell = startIdx

while stack != []:                        # Iterate through untill stack is empty (happens when there is no path from beginning to end)

    # Mark the necessary list and stack with the cell neighbor information if the cell neighbor is not a wall and has not been visited yet
    if cell_list[cell_list[curr_cell].right].isWall == False and cell_list[cell_list[curr_cell].right].idx not in marked:
        # If the cell neighbor is the solution, break out of the while loop. This process is repeated for the other three neighbors as well
        if cell_list[cell_list[curr_cell].right].isSoln == True:
            curr_cell = cell_list[cell_list[curr_cell].right].idx
            stack.append(curr_cell)
            marked.append(curr_cell)
            break
        else:
            curr_cell = cell_list[cell_list[curr_cell].right].idx
            stack.append(curr_cell)
            marked.append(curr_cell)

    # DFS, unlike BFS or Greedy, only pushes on one neighbor at a time onto the stack, hence the "elif" instead of "if"
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

    # If none of the moves are valid, pop the cell from the stack and go to the previous cell
    else:
        stack.pop()
        curr_cell = stack[-1]

new_maze = list(maze)

# Update the maze with '.' in the indices of the final path
for index in stack:
    new_maze[index] = '.'

new_maze[stack[0]] = 'P'
new_maze.append('\n')

# Path cost is just the number of elements in the stack. My algoritm counts the final element as part of the path
path_cost = "Path cost: " + str(len(stack)) + "\n"

# Nodes expanded is just the number of elements visited, which is the length of the "marked" list
nodes_expanded = "Nodes expanded: " + str(len(marked))


print '\n'
maze_string = ''.join(new_maze)
maze_string = maze_string + path_cost + nodes_expanded
print maze_string
file = open('dfs_big.txt', 'w')
file.write(maze_string)
