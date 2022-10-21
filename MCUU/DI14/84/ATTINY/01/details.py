
######  Auto translated oomp file

def load(newPart):
    oType = "MCUU"
    oSize = "DI14"
    oColor = "84"
    oDesc = "ATTINY"
    oIndex = "01"
    hexID = "MCAT84DI14"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicad'].append('FOOTPRINT-kicad-kicad-footprints-Package_DIP-DIP-14_W7.62mm')

    newPart['symbolKicad'].append('SYMBOL-kicad-kicad-symbols-MCU_Microchip_ATtiny-ATtiny84-20P')



    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

