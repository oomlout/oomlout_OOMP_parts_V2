
######  Auto translated oomp file

def load(newPart,it):
    oType = "RESE"
    oSize = "0603"
    oColor = "X"
    oDesc = "O511"
    oIndex = ""
    hexID = "R6O511-"

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

