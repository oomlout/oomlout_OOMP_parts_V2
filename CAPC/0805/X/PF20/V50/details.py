
######  Auto translated oomp file

def load(newPart,it):
    oType = "CAPC"
    oSize = "0805"
    oColor = "X"
    oDesc = "PF20"
    oIndex = "V50"
    hexID = "C085P20"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C107145', 'partName': '50V 220pF X7R ??10% 0805  Multilayer Ceramic Capacitors MLCC - SMD/SMT ROHS'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C107145'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'YAGEO', 'partID': 'CC0805KRX7R9BB221', 'partName': 'CC0805KRX7R9BB221'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

