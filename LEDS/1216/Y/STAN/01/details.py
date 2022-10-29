
######  Auto translated oomp file

def load(newPart,it):
    oType = "LEDS"
    oSize = "1216"
    oColor = "Y"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "L12YY"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)



    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

