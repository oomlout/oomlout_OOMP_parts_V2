
######  Auto translated oomp file

def load(newPart,it):
    oType = "XTAL"
    oSize = "HC49"
    oColor = "X"
    oDesc = "MZ8"
    oIndex = "01"
    hexID = "XTALHC49-MZ8"

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

