def bacteriaGrowth(n0, alpha, K, N):
    tN = 0
    n = n0
    while (not (n > N   )):
        n = (1 + alpha*(1-n/K))*n
        tN+=1
    return tN