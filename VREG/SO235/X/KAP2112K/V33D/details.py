
######  Auto translated oomp file

def load(newPart,it):
    oType = "VREG"
    oSize = "SO235"
    oColor = "X"
    oDesc = "KAP2112K"
    oIndex = "V33D"
    hexID = "VR211223533"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicad'].append('SYMBOL-kicad-kicad-symbols-Regulator_Linear-AP2112K-3.0-3.0')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

