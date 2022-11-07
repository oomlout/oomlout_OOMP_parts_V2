
######  Auto translated oomp file

def load(newPart,it):
    oType = "ICIC"
    oSize = "SC18W"
    oColor = "X"
    oDesc = "K2803"
    oIndex = "01"
    hexID = "ICIC-SC18WK28301"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C9683', 'partName': 'SOIC-18_300mil  Darlington Transistor Arrays ROHS'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C9683'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Texas Instruments', 'partID': 'ULN2803ADWR', 'partName': 'ULN2803ADWR'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

