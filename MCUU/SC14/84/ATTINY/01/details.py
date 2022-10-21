
######  Auto translated oomp file

def load(newPart):
    oType = "MCUU"
    oSize = "SC14"
    oColor = "84"
    oDesc = "ATTINY"
    oIndex = "01"
    hexID = "MCAT84SC14"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicad'].append('FOOTPRINT-kicad-kicad-footprints-Package_SO-SOIC-14_3.9x8.7mm_P1.27mm')

    newPart['symbolKicad'].append('SYMBOL-kicad-kicad-symbols-MCU_Microchip_ATtiny-ATtiny20-SS')



    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

