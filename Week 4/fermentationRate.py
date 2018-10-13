import numpy as np
def fermentationRate(measuredRate, lowerBound, upperBound):
    sum = 0
    counter = 0
    for i in range(0, len(measuredRate)):
        if (measuredRate[i] > lowerBound and measuredRate[i] < upperBound):
            sum += measuredRate[i]
            counter += 1
    averageRate = sum/counter
    return averageRate