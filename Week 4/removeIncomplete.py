import math
import numpy as np
def removeIncomplete(id):
    index = np.array([])
    for i in range(len(id)):
        array = [i]
        expNr = math.floor(id[i])
        if i not in index:
            for j in range(len(id)):
                if (j!=i):
                    if (math.floor(id[j]) == expNr):
                        array = np.append(array, j)
            if (len(array) < 3):
                index = np.append(index, array)
    idComplete = np.delete(id, index)
    return idComplete