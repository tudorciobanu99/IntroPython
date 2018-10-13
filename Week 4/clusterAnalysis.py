import math
import numpy as np
def clusterAnalysis(reflectance):
    initialArray = np.ones(len(reflectance), dtype = int)
    s1 = 0
    s2 = 0
    counter = 0
    for i in range(len(reflectance)):
        if (i % 2 == 0):
            s1 += reflectance[i]
        elif (i % 2 != 0):
            initialArray[i] = 2
            s2 += reflectance[i]
            counter += 1
    m1 = s1/(len(reflectance)-counter)
    m2 = s2/counter
    m11 = 0
    m22 = 0
    while ((m1 != m11) and (m2 != m22)):
        m11 = m1
        m22 = m2
        for i in range(len(reflectance)):
            if (abs(m1 - reflectance[i])>abs(m2 - reflectance[i])):
                initialArray[i] = 2
            else:
                initialArray[i] = 1
        s1 = 0
        s2 = 0
        counter = 0
        for j in range(len(initialArray)):
            if (initialArray[j] == 1):
                s1 += reflectance[j]
            elif (initialArray[j] == 2):
                s2 += reflectance[j]
                counter += 1
        m1 = s1/(len(reflectance)-counter)
        m2 = s2/counter
    clusterAssignments = initialArray
    return clusterAssignments