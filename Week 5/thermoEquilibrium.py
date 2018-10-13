import numpy as np
def thermoEquilibrium(N, r):
    Nl = int(N)
    Nr = 0
    t = 0
    i = 0
    while (not(Nr == Nl) and i < len(r)):
        pLr = Nl/N
        if (r[i] <= pLr):
            Nr+=1
            Nl-=1
        elif (r[i] > pLr):
            Nr-=1
            Nl+=1
        if (Nr == Nl):
            t = i+1
        i+=1
    return t