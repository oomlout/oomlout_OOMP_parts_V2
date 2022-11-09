
######  Auto translated oomp file

def load(newPart,it):
    oType = "XTAL"
    oSize = "3225P4"
    oColor = "X"
    oDesc = "MZ16"
    oIndex = "01"
    hexID = "XTAL3225P4-MZ16"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C13738', 'partName': '16MHz SMD Crystal Resonator 9pF ??10ppm ??30ppm -40??~+85?? SMD3225-4P  Crystals ROHS'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C13738'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Yangxing Tech', 'partID': 'X322516MLB4SI', 'partName': 'X322516MLB4SI'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

