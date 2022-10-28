
######  Auto translated oomp file

def load(newPart,it):
    oType = "VREG"
    oSize = "SO8"
    oColor = "X"
    oDesc = "KAP2112K"
    oIndex = "V25D"
    hexID = "VR2112825"

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

