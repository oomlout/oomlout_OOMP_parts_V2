
######  Auto translated oomp file

def load(newPart,it):
    oType = "LEDS"
    oSize = "0805"
    oColor = "L"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "L8L"

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

