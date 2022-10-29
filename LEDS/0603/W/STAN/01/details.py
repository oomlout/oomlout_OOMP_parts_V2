
######  Auto translated oomp file

def load(newPart,it):
    oType = "LEDS"
    oSize = "0603"
    oColor = "W"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "L063W"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C2290', 'partName': 'White 0603 Light Emitting Diodes (LED) RoHS'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C2290'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Hubei KENTO Elec', 'partID': 'C2290', 'partName': 'C2290'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

