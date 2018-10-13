def gravitationalPull(x):
    R = 6.371e6
    g0 = 9.82
    if (x>=R):
        g = g0*(R**2)/(x**2)
    elif (x>=0 and x<R):
        g = g0*x/R
    return g