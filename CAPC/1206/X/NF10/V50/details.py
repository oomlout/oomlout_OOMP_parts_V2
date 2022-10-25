
######  Auto translated oomp file

def load(newPart,it):
    oType = "CAPC"
    oSize = "1206"
    oColor = "X"
    oDesc = "NF10"
    oIndex = "V50"
    hexID = "C12N10"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C1846', 'partName': '50V 10nF X7R ??10% 1206  Multilayer Ceramic Capacitors MLCC - SMD/SMT ROHS'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C1846'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'FH (Guangdong Fenghua Advanced Tech)', 'partID': '1206B103K500NT', 'partName': '1206B103K500NT'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

