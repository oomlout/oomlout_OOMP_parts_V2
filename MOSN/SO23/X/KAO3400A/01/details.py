
######  Auto translated oomp file

def load(newPart,it):
    oType = "MOSN"
    oSize = "SO23"
    oColor = "X"
    oDesc = "KAO3400A"
    oIndex = "01"
    hexID = "MOSN-SO23-KAO3400A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C20917', 'partName': '30V 5.7A 26.5m??@10V'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C20917'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Alpha & Omega Semicon', 'partID': 'AO3400A', 'partName': 'AO3400A'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

