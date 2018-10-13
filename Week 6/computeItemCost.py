import numpy as np
def computeItemCost(resourceItemMatrix, resourceCost):
    itemCost = np.array([])
    columns = np.size(resourceItemMatrix,1)
    for i in range(columns):
        cost = np.dot(resourceItemMatrix[:,i], resourceCost)
        itemCost = np.append(itemCost, cost)
    return itemCost