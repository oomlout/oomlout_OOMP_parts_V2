
######  Auto translated oomp file

def load(newPart,it):
    oType = "VREG"
    oSize = "SO235"
    oColor = "X"
    oDesc = "KMIC5225"
    oIndex = "V18D"
    hexID = "VR522523518"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicad'].append('SYMBOL-kicad-kicad-symbols-Regulator_Linear-AP131-15')
    newPart['symbolKicad'].append('SYMBOL-kicad-kicad-symbols-Regulator_Linear-MIC520518YM5')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

