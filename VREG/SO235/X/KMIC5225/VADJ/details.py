
######  Auto translated oomp file

def load(newPart,it):
    oType = "VREG"
    oSize = "SO235"
    oColor = "X"
    oDesc = "KMIC5225"
    oIndex = "VADJ"
    hexID = "VR5225235AJ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicad'].append('SYMBOL-kicad-kicad-symbols-Regulator_Linear-MIC5205AJYM5')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

