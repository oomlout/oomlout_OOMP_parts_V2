
######  Auto translated oomp file

def load(newPart,it):
    oType = "LEDS"
    oSize = "0805"
    oColor = "W"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "L8W"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C34499', 'partName': '0805  Light Emitting Diodes (LED) ROHS'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C34499'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Hubei KENTO Elec', 'partID': 'C34499', 'partName': 'C34499'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

