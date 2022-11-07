
######  Auto translated oomp file

def load(newPart,it):
    oType = "MOSN"
    oSize = "SO23"
    oColor = "X"
    oDesc = "K2N7002"
    oIndex = "01"
    hexID = "MOSN-SO23-K2N7002"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C8545', 'partName': 'Basic'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C8545'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Jiangsu Changjing Electronics Technology Co.', 'partID': '2N7002', 'partName': '2N7002'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

