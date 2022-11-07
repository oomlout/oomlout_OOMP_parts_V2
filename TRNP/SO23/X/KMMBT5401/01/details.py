
######  Auto translated oomp file

def load(newPart,it):
    oType = "TRNP"
    oSize = "SO23"
    oColor = "X"
    oDesc = "KMMBT5401"
    oIndex = "01"
    hexID = "TRNPSO23-KMMBT5401"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C8326', 'partName': 'Basic'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C8326'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Jiangsu Changjing Electronics Technology Co.', 'partID': 'MMBT5401', 'partName': 'MMBT5401'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

