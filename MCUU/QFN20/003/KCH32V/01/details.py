
######  Auto translated oomp file

def load(newPart,it):
    oType = "MCUU"
    oSize = "QFN20"
    oColor = "003"
    oDesc = "KCH32V"
    oIndex = "01"
    hexID = "MCK323T20"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicad'].append('FOOTPRINT-kicad-kicad-footprints-Package_DFN_QFN-QFN-20-1EP_3x3mm_P0.4mm_EP1.65x1.65mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

