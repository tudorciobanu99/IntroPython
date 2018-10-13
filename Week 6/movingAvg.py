import numpy as np
def movingAvg(y):
    rows = 5
    columns = len(y)
    matrix = np.zeros((rows,columns))
    limit = 0
    for i in range(rows):
        if (i == 0):
            limit = columns-2
            for j in range(limit):
                matrix[i,j] = y[j+2]
        if (i == 1):
            limit = columns-1
            for j in range(limit):
                matrix[i,j] = 2*y[j+1]
        if (i == 2):
            matrix[i,:] = 3*y
        if (i == 3):
            limit = 1
            for j in range(limit,columns):
                matrix[i,j] = 2*y[j-1]
        if (i == 4):
            limit = 2
            for j in range(limit,columns):
                matrix[i,j] = y[j-2]
    ysmooth = np.array([])
    for i in range(columns):
        sumOf = sum(matrix[:, i])/9
        ysmooth = np.append(ysmooth,sumOf)
    return ysmooth