
######  Auto translated oomp file

def load(newPart,it):
    oType = "ICIC"
    oSize = "SC16"
    oColor = "X"
    oDesc = "K2003"
    oIndex = "01"
    hexID = "ICIC-SC16-K20301"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C7512', 'partName': 'SOIC-16  Darlington Transistor Arrays ROHS'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C7512'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Texas Instruments', 'partID': 'ULN2003ADR', 'partName': 'ULN2003ADR'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

