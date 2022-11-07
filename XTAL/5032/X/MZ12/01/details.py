
######  Auto translated oomp file

def load(newPart,it):
    oType = "XTAL"
    oSize = "5032"
    oColor = "X"
    oDesc = "MZ12"
    oIndex = "01"
    hexID = "XTAL5032-MZ12"

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

