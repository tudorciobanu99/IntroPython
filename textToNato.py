import numpy as np
def textToNato(plainText):
    plainText = str(plainText).lower()
    natoAlphabet = np.array(["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf",
                             "Hotel", "India", "Juliet", "Kilo", "Lima", "Mike", "November",
                             "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform",
                             "Victor", "Whiskey", "Xray", "Yankee", "Zulu"])
    natoText = ""
    for i in range(len(plainText)):
        for j in range(len(natoAlphabet)):
            if str(plainText[i]) == str(natoAlphabet[j]).lower()[0]:
                if (i == len(plainText)-1):
                    natoText += str(natoAlphabet[j])
                else:
                    natoText += str(natoAlphabet[j]) + "-"
    return natoText
