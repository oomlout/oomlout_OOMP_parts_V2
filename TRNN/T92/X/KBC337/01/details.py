
######  Auto translated oomp file

def load(newPart,it):
    oType = "TRNN"
    oSize = "T92"
    oColor = "X"
    oDesc = "KBC337"
    oIndex = "01"
    hexID = "TRNN-T92-KBC337"

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

