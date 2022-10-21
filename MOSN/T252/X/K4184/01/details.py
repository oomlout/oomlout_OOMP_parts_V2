
######  Auto translated oomp file

def load(newPart):
    oType = "MOSN"
    oSize = "T252"
    oColor = "X"
    oDesc = "K4184"
    oIndex = "01"
    hexID = "MN2524184A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicad'].append('FOOTPRINT-kicad-kicad-footprints-Package_TO_SOT_SMD-TO-252-3_TabPin2')

    newPart['symbolKicad'].append('SYMBOL-kicad-kicad-symbols-Device-Q_NMOS_GDS')



    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

