
######  Auto translated oomp file

def load(newPart,it):
    oType = "XTAL"
    oSize = "5032"
    oColor = "X"
    oDesc = "MZ8"
    oIndex = "01"
    hexID = "XTAL5032-MZ8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C115962', 'partName': '8MHz SMD Crystal Resonator 20pF ??10ppm ??50ppm -40??~+85?? SMD5032-2P  Crystals ROHS'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C115962'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Yangxing Tech', 'partID': 'X50328MSB2GI', 'partName': 'X50328MSB2GI'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

