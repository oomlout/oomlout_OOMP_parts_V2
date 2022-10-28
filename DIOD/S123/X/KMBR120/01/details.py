
######  Auto translated oomp file

def load(newPart,it):
    oType = "DIOD"
    oSize = "S123"
    oColor = "X"
    oDesc = "KMBR120"
    oIndex = "01"
    hexID = "D34148"

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

