import numpy as np
def computePassesGoalLine(point, directionVector):
    alfa = 0
    if (directionVector[0] > 0):
        alfa = (105 - point[0])/directionVector[0]
    elif (directionVector[0] < 0):
        alfa = -point[0]/directionVector[0]
    ygoal = point[1] + alfa*directionVector[1]
    if (ygoal > 30.34 and ygoal < 37.66):
        score = True
    else:
        score = False
    return score