import numpy as np
def boxArea(boxCorners, area):
    if area == "Box1":
        A = (boxCorners[1]-boxCorners[0])*(boxCorners[5]-boxCorners[4])
    elif area == "Box2":
        A = (boxCorners[3]-boxCorners[2])*(boxCorners[7]-boxCorners[6])
    elif area == "Intersection":
        A = np.dot(np.max([0,min(boxCorners[1],boxCorners[3])-max(boxCorners[0],boxCorners[2])]),np.max([0,min(boxCorners[5],boxCorners[7])-max(boxCorners[4],boxCorners[6])]))
    elif area == "Union":
        A0 = np.dot(np.max([0,min(boxCorners[1],boxCorners[3])-max(boxCorners[0],boxCorners[2])]),np.max([0,min(boxCorners[5],boxCorners[7])-max(boxCorners[4],boxCorners[6])]))
        A1 = (boxCorners[1]-boxCorners[0])*(boxCorners[5]-boxCorners[4])
        A2 = (boxCorners[3]-boxCorners[2])*(boxCorners[7]-boxCorners[6])
        A = (A1 + A2) - A0
    return A