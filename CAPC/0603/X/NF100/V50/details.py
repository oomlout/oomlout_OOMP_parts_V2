
######  Auto translated oomp file

def load(newPart,it):
    oType = "CAPC"
    oSize = "0603"
    oColor = "X"
    oDesc = "NF100"
    oIndex = "V50"
    hexID = "C063N100"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C14663', 'partName': '50V 100nF X7R ??10% 0603  Multilayer Ceramic Capacitors MLCC - SMD/SMT ROHS'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C14663'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'YAGEO', 'partID': 'CC0603KRX7R9BB104', 'partName': 'CC0603KRX7R9BB104'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

