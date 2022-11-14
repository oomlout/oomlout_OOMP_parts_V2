
######  Auto translated oomp file

def load(newPart,it):
    oType = "SENS"
    oSize = "LG163030S"
    oColor = "X"
    oDesc = "KL3GD20"
    oIndex = "01"
    hexID = "MN2524184A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['matchSpecial'].append([['L3GD20H_LGA16L'], 'SENS-LG163030S-X-KL3GD20-01'])
    newPart['symbolKicad'].append('SYMBOL-kicad-kicad-symbols-Sensor_Motion-L3GD20')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

