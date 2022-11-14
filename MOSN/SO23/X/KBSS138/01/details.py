
######  Auto translated oomp file

def load(newPart,it):
    oType = "MOSN"
    oSize = "SO23"
    oColor = "X"
    oDesc = "KBSS138"
    oIndex = "01"
    hexID = "MN2524184A"

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

