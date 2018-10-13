def pH2Category(pH):
    if (pH>=0 and pH<3):
        category = "Strongly acidic"
    elif (pH>=3 and pH<6):
        category = "Weakly acidic"
    elif (pH>=6 and pH<8):
        category = "Neutral"
    elif (pH>=8 and pH<11):
        category = "Weakly basic"
    elif (pH>=11 and pH<=14):
        category =  "Strongly basic"
    else:
        category = "pH out of range"
    return category