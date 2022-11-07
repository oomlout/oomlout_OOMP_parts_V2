
######  Auto translated oomp file

def load(newPart,it):
    oType = "TRNN"
    oSize = "T92"
    oColor = "X"
    oDesc = "KC1815"
    oIndex = "01"
    hexID = "TRNN-T92-KC1815"

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

