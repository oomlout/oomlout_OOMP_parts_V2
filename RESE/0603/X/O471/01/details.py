
######  Auto translated oomp file

def load(newPart,it):
    oType = "RESE"
    oSize = "0603"
    oColor = "X"
    oDesc = "O471"
    oIndex = "01"
    hexID = "R6O471"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C23179', 'partName': '100mW Thick Film Resistors 75V ??100ppm/?? ??1% -55??~+155?? 470?? 0603  Chip Resistor - Surface Mount ROHS'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C23179'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'UNI-ROYAL(Uniroyal Elec)', 'partID': '0603WAF4700T5E', 'partName': '0603WAF4700T5E'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

