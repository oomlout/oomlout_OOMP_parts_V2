
######  Auto translated oomp file

def load(newPart):
    oType = "RESE"
    oSize = "0402"
    oColor = "X"
    oDesc = "O502"
    oIndex = "01"
    hexID = "R4O502"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C25867', 'partName': '62.5mW Thick Film Resistors 50V ??100ppm/?? ??1% -55??~+155?? 1.5k?? 0402  Chip Resistor - Surface Mount ROHS'})

    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C25867'})

    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'UNI-ROYAL(Uniroyal Elec)', 'partID': '0402WGF1501TCE', 'partName': '0402WGF1501TCE'})



    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

