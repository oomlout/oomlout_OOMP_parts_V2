
######  Auto translated oomp file

def load(newPart,it):
    oType = "LEDS"
    oSize = "0603"
    oColor = "R"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "L6R"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C2286', 'partName': 'Red 615~630nm 1.9~2.2V 0603 Light Emitting Diodes (LED) RoHS'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C2286'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Hubei KENTO Elec', 'partID': 'KT-0603R', 'partName': 'KT-0603R'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

