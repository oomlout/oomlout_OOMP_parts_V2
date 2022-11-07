
######  Auto translated oomp file

def load(newPart,it):
    oType = "TRNN"
    oSize = "SO23"
    oColor = "X"
    oDesc = "KMMBT3904"
    oIndex = "01"
    hexID = "TRNN-SO23-KMMBT3904"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C20526', 'partName': 'Basic'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C20526'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Jiangsu Changjing Electronics Technology Co.', 'partID': 'MMBT3904', 'partName': 'MMBT3904'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

