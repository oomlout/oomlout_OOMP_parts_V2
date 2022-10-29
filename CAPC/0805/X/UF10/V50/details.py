
######  Auto translated oomp file

def load(newPart,it):
    oType = "CAPC"
    oSize = "0805"
    oColor = "X"
    oDesc = "UF10"
    oIndex = "V50"
    hexID = "C085U10"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C440198', 'partName': '50V 10uF X5R ??10% 0805  Multilayer Ceramic Capacitors MLCC - SMD/SMT ROHS'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C440198'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Murata Electronics', 'partID': 'GRM21BR61H106KE43L', 'partName': 'GRM21BR61H106KE43L'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

