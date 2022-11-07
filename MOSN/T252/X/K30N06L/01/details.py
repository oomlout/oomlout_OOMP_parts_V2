
######  Auto translated oomp file

def load(newPart,it):
    oType = "MOSN"
    oSize = "T252"
    oColor = "X"
    oDesc = "K30N06L"
    oIndex = "01"
    hexID = "MN30N06D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicad'].append('FOOTPRINT-kicad-kicad-footprints-Package_TO_SOT_SMD-TO-252-2')
    newPart['symbolKicad'].append('SYMBOL-kicad-kicad-symbols-Device-Q_NMOS_GDS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

