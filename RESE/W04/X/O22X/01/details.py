
######  Auto translated oomp file

def load(newPart,it):
    oType = "RESE"
    oSize = "W04"
    oColor = "X"
    oDesc = "O22X"
    oIndex = "01"
    hexID = "RW04-O22X"

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

