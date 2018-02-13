'''
BFS uses a queue structure to keep track of the nodes that need to be examined
Starting from s start node it essentially follows this sequence:
    -Deque node
    -Enque neighboring nodes as long as they are not walls and have not been visited already
    -Stop when it reaches the solution/end node
The algorithm also uses a dictionary to keep track of the optimal solution and a list to ensure that nodes that have already been visited are not visited again
BFS gives the optimal path cost, but uses memory poorely as it expands the most number of nodes to reach the desired solution
'''
from maze import *
from mclass import *
from collections import deque

'''
backtrace(parent, start, end):
    Inputs: parent (dictionary keeping track of path), start (startIdx), end (finIdx)
    Output: returns the path in a list

    This function takes in the dictionary that we had been using to keep track of the parent of the current cells.
    We append the end cell to our path list, and then we keep appending the parent of the cell till we hit the start cell.
    We reverse the path to have it in forward order, and then we return the path
'''
def backtrace(parent, start, end):
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse
    return path

maze, cell_list, startIdx, finIdx = getMaze('/inputMazes/openMaze.txt')

print maze

expanded = 0
queue = deque([]) #queue that is used to store the neighboring nodes of the node being examined for later examination
queue.append(startIdx)
marked = []  # List to hold indices of visited cells so we don't visit the same cells twice
marked.append(startIdx)
curr_cell = startIdx
parent = {} #Dict used to keep track of parent cells
while queue:
    curr_cell = queue.popleft() #remove the node whose neighbors we are examining from the queue
    #Check to see if the neighbor is not a wall and the neighbor has not already been visited and the accordinly mark/update the required lists
    expanded += 1

    if cell_list[cell_list[curr_cell].right].isWall == False and cell_list[cell_list[curr_cell].right].idx not in marked:
        # if the neighbor is the solution update the required lists and dictionary for keep track of the baths and exit the while loop
        if cell_list[cell_list[curr_cell].right].isSoln == True:
            right = cell_list[cell_list[curr_cell].right].idx
            parent[right] = curr_cell
            queue.append(right)
            marked.append(right)
            break
        else:
            right = cell_list[cell_list[curr_cell].right].idx
            parent[right] = curr_cell #update the parent dictionary
            queue.append(right) #add the neighboring node to the queue
            marked.append(right) #Mark the cell as visited

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

fin_path = backtrace(parent, startIdx, finIdx)
new_maze = list(maze)

for index in fin_path: #update the maze with the final path
    new_maze[index] = '.'

new_maze[fin_path[-1]] = 'P'
# Path cost is just the number of elements in fin_path. The algorithm considers the final element as part of the path
path_cost = "\n" + "Path cost: " + str(len(fin_path)) + "\n"

# Nodes expanded is just the number of elements popped off the frontier, which in our case is the queue
nodes_expanded = "Nodes expanded: " + str(expanded)
print '\n'
maze_string = ''.join(new_maze)
print maze_string + path_cost + nodes_expanded
maze_string = maze_string + path_cost + nodes_expanded
file = open('bfs_open.txt', 'w')
file.write(maze_string)
