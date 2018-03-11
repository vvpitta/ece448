import numpy as np
from minHeapClass import *

def milesGraph():

    retVal = np.zeros((5, 5))

    retVal[0][1] = retVal[1][0] = 1064
    retVal[0][2] = retVal[2][0] = 673
    retVal[0][3] = retVal[3][0] = 1401
    retVal[0][4] = retVal[4][0] = 277
    retVal[1][2] = retVal[2][1] = 958
    retVal[1][3] = retVal[3][1] = 1934
    retVal[1][4] = retVal[4][1] = 337
    retVal[2][3] = retVal[3][2] = 1001
    retVal[2][4] = retVal[4][2] = 399
    retVal[3][4] = retVal[4][3] = 387

    return retVal

def shortestGraphChildren(current):

    children = []
    for i in range(5):
        if i == current:
            continue
        children.append(i)

    return children

def dijkstra(start, goal):

    distances = milesGraph()
    openList = MinHeap()
    gn = {}
    path = {}

    openList.push(start, 0)
    gn[start] = 0
    path[start] = None

    while not openList.isEmpty():
        current = openList.pop()

        if current == goal:
            break

        successors = shortestGraphChildren(current)
        for child in successors:
            newG = gn[current] + distances[current][child]
            if child not in gn or newG < gn[child]:
                gn[child] = newG
                path[child] = current
                fn = newG + 0
                openList.push(child, fn)

    reversePath = []
    current = goal
    while current != start:
        reversePath.append(current)
        current = path[current]
    reversePath = reversePath[::-1]

    minDist = 0
    i = 0
    minDist += distances[start][reversePath[0]]
    while (i+1 != len(reversePath)):
        minDist += distances[reversePath[i]][reversePath[i+1]]
        i += 1

    return minDist, reversePath

def shortestGraph():

    distances = milesGraph()
    actualPaths = {}

    for x in range(distances.shape[0]):
        for y in range(distances.shape[1]):
            if x == y:
                continue
            dijkPath, path = dijkstra(x, y)
            actualPaths[(x, y)] = path
            if dijkPath < distances[x][y]:
                distances[x][y] = dijkPath

    return distances, actualPaths
