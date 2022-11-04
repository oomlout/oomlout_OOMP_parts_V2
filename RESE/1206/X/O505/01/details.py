
######  Auto translated oomp file

def load(newPart,it):
    oType = "RESE"
    oSize = "1206"
    oColor = "X"
    oDesc = "O505"
    oIndex = "01"
    hexID = "R12O5501"

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

