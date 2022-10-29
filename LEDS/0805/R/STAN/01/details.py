
######  Auto translated oomp file

def load(newPart,it):
    oType = "LEDS"
    oSize = "0805"
    oColor = "R"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "L085R"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C84256', 'partName': 'Red 0805  Light Emitting Diodes (LED) ROHS'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C84256'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Foshan NationStar Optoelectronics', 'partID': 'NCD0805R1', 'partName': 'NCD0805R1'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

