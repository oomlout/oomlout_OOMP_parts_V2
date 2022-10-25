
######  Auto translated oomp file

def load(newPart,it):
    oType = "MCUU"
    oSize = "QFN14"
    oColor = "84"
    oDesc = "ATTINY"
    oIndex = "01"
    hexID = "MCAT84QF14"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicad'].append('FOOTPRINT-kicad-kicad-footprints-Package_DFN_QFN-QFN-20-1EP_4x4mm_P0.5mm_EP2.6x2.6mm')
    newPart['symbolKicad'].append('SYMBOL-kicad-kicad-symbols-MCU_Microchip_ATtiny-ATtiny84-20M')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

