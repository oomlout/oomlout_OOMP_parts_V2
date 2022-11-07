
######  Auto translated oomp file

def load(newPart,it):
    oType = "TRNN"
    oSize = "SO23"
    oColor = "X"
    oDesc = "KS9013"
    oIndex = "01"
    hexID = "TRNN-SO23-KS9013"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C6749', 'partName': 'Basic'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C6749'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Jiangsu Changjing Electronics Technology Co.', 'partID': 'S9013 J3', 'partName': 'S9013 J3'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

