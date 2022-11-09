
######  Auto translated oomp file

def load(newPart,it):
    oType = "LEDS"
    oSize = "0805"
    oColor = "Y"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "L8Y"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C2296', 'partName': 'Yellow 592~594nm 0805 Light Emitting Diodes (LED) RoHS'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C2296'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Hubei KENTO Elec', 'partID': '17-21SUYC/TR8', 'partName': '17-21SUYC/TR8'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

