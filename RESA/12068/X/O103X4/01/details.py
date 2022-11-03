
######  Auto translated oomp file

def load(newPart,it):
    oType = "RESA"
    oSize = "12068"
    oColor = "X"
    oDesc = "O103X4"
    oIndex = "01"
    hexID = "RA12103"

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

