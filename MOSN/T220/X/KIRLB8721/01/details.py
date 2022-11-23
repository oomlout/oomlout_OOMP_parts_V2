
######  Auto translated oomp file

def load(newPart,it):
    oType = "MOSN"
    oSize = "T220"
    oColor = "X"
    oDesc = "KIRLB8721"
    oIndex = "01"
    hexID = "MN8721"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicad'].append('FOOTPRINT-kicad-kicad-footprints-Package_TO_SOT_THT-TO-220-3_Vertical')
    newPart['symbolKicad'].append('SYMBOL-kicad-kicad-symbols-Device-Q_NMOS_GDS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

