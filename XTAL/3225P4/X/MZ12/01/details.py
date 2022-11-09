
######  Auto translated oomp file

def load(newPart,it):
    oType = "XTAL"
    oSize = "3225P4"
    oColor = "X"
    oDesc = "MZ12"
    oIndex = "01"
    hexID = "XTAL3225P4-MZ12"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C9002', 'partName': '12MHz SMD Crystal Resonator 20pF ??10ppm ??30ppm -40??~+85?? SMD3225-4P  Crystals ROHS'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C9002'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Yangxing Tech', 'partID': 'X322512MSB4SI', 'partName': 'X322512MSB4SI'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

