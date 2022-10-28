
######  Auto translated oomp file

def load(newPart,it):
    oType = "VREG"
    oSize = "T220"
    oColor = "X"
    oDesc = "KLD1117"
    oIndex = "V5"
    hexID = "VR11172205"

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

