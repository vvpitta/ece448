'''
Greedy Best First Search using a euclidean distance heuristic.
Euclidean distance is implemented in the Distance() function
    - distance = sqrt((X2-X1)^2 + (Y2-Y1)^2)
A priority queue is used to maintain organize the queue in ascending order by distance to
the goal
Starting from the start index, the algorithm will push on indices of the current cell's neighbors in order of
distance to the goal state (smallest distance to goal pushed on first)
The algorithm will then pop off the neighbor with the smallest distance to the goal first, and then push on its
neighbors in a similar fashion. The path is kept track with the parent dictionary, which is useful in the backtrace() function.
Once the algorithm recognizes the goal state cell, it breaks from the loop and calls on backtrace to highlight the path.
'''

from mclass import *
from maze import *
import math
import Queue

'''
Distance(curr_cell, fin_cell):
    Inputs : mazeCell instances of current_cell and goal state cell
    Output: Distance to goal state cell

    This function implements the euclidean distance, which is the heuristic we used for the best first search
'''
def Distance(curr_cell, fin_cell):
    x_squared = math.pow((fin_cell.x - curr_cell.x), 2)
    y_squared = math.pow((fin_cell.y - curr_cell.y), 2)

    dist = math.sqrt(x_squared + y_squared)

    return dist

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

maze, cell_list, startIdx, finIdx = getMaze('/inputMazes/mediumMaze.txt')

print maze
parent = {}                                                         # Dict used to keep track of parent cells
p_q = Queue.PriorityQueue()                                         # Priority Queue that will be used to pick neighboring cells closest to the final cell
dist_to_goal = Distance(cell_list[startIdx], cell_list[finIdx])     # Getting distance to the goal from the start cell to the final cell
p_q.put((dist_to_goal, startIdx))                                   # Our priority queue holds a tuple of (distance_to_goal, index of curr_cell)
marked = []                                                         # Marked is a list which holds the indices of the cells we have already visited, so that we don't visit them again
marked.append(startIdx)
curr_cell = startIdx
fin_cell = cell_list[finIdx]
expanded = 0

while p_q != []:
    curr_cell = p_q.get()[1]                                         # Index of the cell with the closest distance to the goal
    expanded += 1

    curr_cell_right = cell_list[cell_list[curr_cell].right]
    curr_cell_left = cell_list[cell_list[curr_cell].left]
    curr_cell_up = cell_list[cell_list[curr_cell].up]
    curr_cell_down = cell_list[cell_list[curr_cell].down]

    # Figure out the distance to goal for each of the curr_cells neighbors
    dist_right = Distance(curr_cell_right, fin_cell)
    dist_left = Distance(curr_cell_left, fin_cell)
    dist_up = Distance(curr_cell_up, fin_cell)
    dist_down = Distance(curr_cell_down, fin_cell)

    # Create a list of tuples with the neighboring cell and corresponding distance to goal and sort it according to distance in ascending order
    distances = [(curr_cell_right, dist_right), (curr_cell_left,dist_left), (curr_cell_up,dist_up), (curr_cell_down, dist_down)]
    dist_sorted = sorted(distances, key = lambda x:x[1])

    # Mark the necessary list, priority queue and dictionary with the cell neighbor information if the cell neighbor is not a wall and has not been visited yet
    if dist_sorted[0][0].isWall == False and dist_sorted[0][0].idx not in marked:
        # If the cell neighbor is the solution, break out of the while loop. This process is repeated for the other three neighbors as well
        if dist_sorted[0][0].isSoln == True:
            first = dist_sorted[0][0].idx
            parent[first] = curr_cell
            p_q.put((dist_sorted[0][1], first))
            marked.append(first)
            break
        else:
            first = dist_sorted[0][0].idx
            parent[first] = curr_cell                                    # update the parent dictionary
            p_q.put((dist_sorted[0][1], first))                          # Push the tuple containing the distance to goal and the cell index
            marked.append(first)                                         # Mark the cell as visited
                                                                         # The previous three lines are repeated for all four neighbors

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
for index in fin_path:                     # Update the maze with the final path
    new_maze[index] = '.'


new_maze[fin_path[-1]] = 'P'

# Path cost is just the number of elements in fin_path. My algorithm considers the final element as part of the path
path_cost = "\n" + "Path cost: " + str(len(fin_path)) + "\n"

# Nodes expanded is just the number of elements pushed off the frontier, which in our case is the priority queue
nodes_expanded = "Nodes expanded: " + str(expanded)
print '\n'
maze_string = ''.join(new_maze)
print maze_string + path_cost + nodes_expanded
maze_string = maze_string + path_cost + nodes_expanded
file = open('greedy_medium.txt', 'w')
file.write(maze_string)
