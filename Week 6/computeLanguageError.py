import numpy as np
import pandas as pd
def computeLanguageError(freq):
    E = np.array([])
    languageFreq = pd.read_csv("letter_frequencies.csv")
    for i in range(1,16):
        languageLetters = np.array(languageFreq.iloc[:,i])
        individualError = 0
        for j in range(len(languageLetters)):
            individualError += (freq[j] - languageLetters[j])**2
        E = np.append(E, individualError)
    return E