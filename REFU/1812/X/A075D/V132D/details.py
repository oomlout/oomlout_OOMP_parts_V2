
######  Auto translated oomp file

def load(newPart,it):
    oType = "REFU"
    oSize = "1812"
    oColor = "X"
    oDesc = "A075D"
    oIndex = "V132D"
    hexID = "RF18075D"

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

