
######  Auto translated oomp file

def load(newPart,it):
    oType = "RESE"
    oSize = "0805"
    oColor = "X"
    oDesc = "O753"
    oIndex = "01"
    hexID = "R8O753"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C17819', 'partName': '125mW Thick Film Resistors 150V ??100ppm/?? ??1% -55??~+155?? 75k?? 0805  Chip Resistor - Surface Mount ROHS'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C17819'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'UNI-ROYAL(Uniroyal Elec)', 'partID': '0805W8F7502T5E', 'partName': '0805W8F7502T5E'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

