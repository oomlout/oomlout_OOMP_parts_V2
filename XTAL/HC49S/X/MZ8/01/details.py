
######  Auto translated oomp file

def load(newPart,it):
    oType = "XTAL"
    oSize = "HC49S"
    oColor = "X"
    oDesc = "MZ8"
    oIndex = "01"
    hexID = "XTALHC49S-MZ8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C12674', 'partName': '8MHz 49SMD 20pF ??20ppm ??30ppm -20??~+70?? HC-49S/SMD  Crystals ROHS'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C12674'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Yangxing Tech', 'partID': 'X49SM8MSD2SC', 'partName': 'X49SM8MSD2SC'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

