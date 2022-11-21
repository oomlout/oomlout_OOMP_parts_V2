
######  Auto translated oomp file

def load(newPart,it):
    oType = "MCUU"
    oSize = "SP16"
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

    newPart['footprintKicad'].append('FOOTPRINT-kicad-kicad-footprints-Package_SO-SOP-16_3.9x9.9mm_P1.27mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

