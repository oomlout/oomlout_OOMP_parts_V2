
######  Auto translated oomp file

def load(newPart,it):
    oType = "TERS"
    oSize = "35D"
    oColor = "L"
    oDesc = "PI01"
    oIndex = "01"
    hexID = "T35L1"

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

