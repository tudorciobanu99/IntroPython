import numpy as np
def letterFrequency(filename):
    filein = open(filename, "r")
    lines = filein.readlines()
    smalltxt = ("".join(lines)).lower()
    alphabet = np.array(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
    freq = np.zeros(26)
    size = 0
    for i in range(len(alphabet)):
        freq[i] = smalltxt.count(alphabet[i])
        size+=freq[i]
    for i in range(len(freq)):
        freq[i] = freq[i]/size*100
    return freq