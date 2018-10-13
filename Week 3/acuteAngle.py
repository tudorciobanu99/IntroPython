import numpy as np
import math
def acuteAngle(v1, v2):
    angle = math.acos(np.dot(v1,v2))
    if (angle>(math.pi/2)):
        theta = math.pi - angle
    else:
        theta = angle
    return theta