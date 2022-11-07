
######  Auto translated oomp file

def load(newPart,it):
    oType = "TRNN"
    oSize = "SO23"
    oColor = "X"
    oDesc = "KD882"
    oIndex = "01"
    hexID = "TRNN-SO23-KD882"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C9634', 'partName': 'Basic'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C9634'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Jiangsu Changjing Electronics Technology Co.', 'partID': 'C9634', 'partName': 'C9634'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

