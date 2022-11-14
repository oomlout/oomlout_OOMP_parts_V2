
######  Auto translated oomp file

def load(newPart,it):
    oType = "DIOD"
    oSize = "SO236"
    oColor = "X"
    oDesc = "KSRV05X4"
    oIndex = "01"
    hexID = "D34148"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['matchSpecial'].append([['SRV05-4'], 'DIOD-SO236-X-KSRV05X4-01'])
    newPart['footprintKicad'].append('FOOTPRINT-kicad-kicad-footprints-Package_TO_SOT_SMD-SOT-23-6')
    newPart['footprintKicad'].append('FOOTPRINT-kicad-kicad-footprints-Package_TO_SOT_SMD-SOT-23-6_Handsoldering')
    newPart['symbolKicad'].append('SYMBOL-kicad-kicad-symbols-Device-D')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

