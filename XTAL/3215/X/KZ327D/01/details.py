
######  Auto translated oomp file

def load(newPart,it):
    oType = "XTAL"
    oSize = "3215"
    oColor = "X"
    oDesc = "KZ327D"
    oIndex = "01"
    hexID = "XTAL3215-KZ327D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C32346', 'partName': '32.768kHz SMD Crystal Resonator 12.5pF 70k?? ??20ppm -40??~+85?? SMD3215-2P  Crystals ROHS'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C32346'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Seiko Epson', 'partID': 'Q13FC1350000400', 'partName': 'Q13FC1350000400'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

