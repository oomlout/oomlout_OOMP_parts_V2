
######  Auto translated oomp file

def load(newPart,it):
    oType = "LEDS"
    oSize = "05"
    oColor = "O"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "L5O"

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

