
######  Auto translated oomp file

def load(newPart,it):
    oType = "TRNP"
    oSize = "SO23"
    oColor = "X"
    oDesc = "KS8550"
    oIndex = "01"
    hexID = "TRNPSO23-KS8550"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C105432', 'partName': 'Basic'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C105432'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Jiangsu Changjing Electronics Technology Co.', 'partID': 'S8550', 'partName': 'S8550'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

