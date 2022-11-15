
######  Auto translated oomp file

def load(newPart,it):
    oType = "LEDS"
    oSize = "2020"
    oColor = "RGB"
    oDesc = "K102"
    oIndex = "01"
    hexID = "L2020-RGBK102"

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

