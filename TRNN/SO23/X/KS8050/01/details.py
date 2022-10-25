
######  Auto translated oomp file

def load(newPart,it):
    oType = "TRNN"
    oSize = "SO23"
    oColor = "X"
    oDesc = "KS8050"
    oIndex = "01"
    hexID = "TNS248050"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicad'].append('FOOTPRINT-kicad-kicad-footprints-Package_TO_SOT_SMD-SOT-23')
    newPart['symbolKicad'].append('SYMBOL-kicad-kicad-symbols-Device-Q_NPN_BEC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

