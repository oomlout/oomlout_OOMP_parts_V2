
######  Auto translated oomp file

def load(newPart,it):
    oType = "TRNN"
    oSize = "SO23"
    oColor = "X"
    oDesc = "KMMBT2222A"
    oIndex = "01"
    hexID = "TRNN-SO23-KMMBT2222A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C8512', 'partName': 'Basic'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C8512'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Jiangsu Changjing Electronics Technology Co.', 'partID': 'MMBT2222A 1P', 'partName': 'MMBT2222A 1P'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

