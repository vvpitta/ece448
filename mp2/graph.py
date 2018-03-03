import numpy as np

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

def stepsGraph():

    retVal = np.zeros((5, 5))

    retVal[0][1] = retVal[1][0] = 1
    retVal[0][2] = retVal[2][0] = 1
    retVal[0][3] = retVal[3][0] = 1
    retVal[0][4] = retVal[4][0] = 1
    retVal[1][2] = retVal[2][1] = 1
    retVal[1][3] = retVal[3][1] = 1
    retVal[1][4] = retVal[4][1] = 1
    retVal[2][3] = retVal[3][2] = 1
    retVal[2][4] = retVal[4][2] = 1
    retVal[3][4] = retVal[4][3] = 1

    return retVal
