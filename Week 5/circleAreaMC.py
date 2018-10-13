import numpy as np
import math
def circleAreaMC(xvals, yvals):
  counter = 0
  for i in range(len(xvals)):
      if (math.sqrt(xvals[i]**2+yvals[i]**2)<1):
            counter+=1
  aShape = 4
  number = len(xvals)
  area = aShape*(counter/number)
  return area