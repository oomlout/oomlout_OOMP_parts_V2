
######  Auto translated oomp file

def load(newPart,it):
    oType = "HEAD"
    oSize = "I01"
    oColor = "X"
    oDesc = "PI2X06"
    oIndex = "01"
    hexID = "H2X6"

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

