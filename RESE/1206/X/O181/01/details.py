
######  Auto translated oomp file

def load(newPart,it):
    oType = "RESE"
    oSize = "1206"
    oColor = "X"
    oDesc = "O181"
    oIndex = "01"
    hexID = "R12O181"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C17924', 'partName': '250mW Thick Film Resistors 200V ??100ppm/?? ??1% -55??~+155?? 180?? 1206  Chip Resistor - Surface Mount ROHS'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C17924'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'UNI-ROYAL(Uniroyal Elec)', 'partID': '1206W4F1800T5E', 'partName': '1206W4F1800T5E'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

