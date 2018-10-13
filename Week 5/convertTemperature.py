def convertTemperature(T, unitFrom, unitTo):
    if (str(unitFrom) == 'Celsius'):
        if (str(unitTo) == 'Fahrenheit'):
            T = 1.8*T+32
        elif (str(unitTo) == 'Kelvin'):
            T = T + 273.15
    elif (str(unitFrom) == 'Fahrenheit'):
        if (str(unitTo) == 'Celsius'):
            T = (T-32)/1.8
        elif (str(unitTo) == 'Kelvin'):
            T = (T + 459.67)/1.8
    elif (str(unitFrom) == 'Kelvin'):
        if (str(unitTo) == 'Fahrenheit'):
            T = 1.8*T-459.67
        elif (str(unitTo) == 'Celsius'):
            T = T - 273.15
    else:
        T = 0
    return T