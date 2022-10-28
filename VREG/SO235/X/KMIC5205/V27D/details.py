
######  Auto translated oomp file

def load(newPart,it):
    oType = "VREG"
    oSize = "SO235"
    oColor = "X"
    oDesc = "KMIC5205"
    oIndex = "V27D"
    hexID = "VR522523527"

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

