
######  Auto translated oomp file

def load(newPart,it):
    oType = "MOSP"
    oSize = "SO23"
    oColor = "X"
    oDesc = "KAO3401A"
    oIndex = "01"
    hexID = "MOSPSO23-KAO3401A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C15127', 'partName': '30V 4A 44m??@10V'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C15127'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Alpha & Omega Semicon', 'partID': 'AO3401A', 'partName': 'AO3401A'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

