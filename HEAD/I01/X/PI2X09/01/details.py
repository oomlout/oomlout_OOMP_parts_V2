
######  Auto translated oomp file

def load(newPart,it):
    oType = "HEAD"
    oSize = "I01"
    oColor = "X"
    oDesc = "PI2X09"
    oIndex = "01"
    hexID = "R2X09"

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

