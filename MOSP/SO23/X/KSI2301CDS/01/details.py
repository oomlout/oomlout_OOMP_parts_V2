
######  Auto translated oomp file

def load(newPart,it):
    oType = "MOSP"
    oSize = "SO23"
    oColor = "X"
    oDesc = "KSI2301CDS"
    oIndex = "01"
    hexID = "MOSPSO23-KSI2301CDS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C8492', 'partName': '50V 130mA 225mW 10??@5V'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C8492'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'LRC', 'partID': 'LBSS84LT1G', 'partName': 'LBSS84LT1G'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

