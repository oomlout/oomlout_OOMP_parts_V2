
######  Auto translated oomp file

def load(newPart,it):
    oType = "TRNP"
    oSize = "T92"
    oColor = "X"
    oDesc = "KBC327"
    oIndex = "01"
    hexID = "TRNPT92-KBC327"

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

