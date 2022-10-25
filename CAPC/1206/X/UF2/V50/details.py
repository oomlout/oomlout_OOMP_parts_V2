
######  Auto translated oomp file

def load(newPart,it):
    oType = "CAPC"
    oSize = "1206"
    oColor = "X"
    oDesc = "UF2"
    oIndex = "V50"
    hexID = "C12U2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C50254', 'partName': '50V 2.2uF X7R ??10% 1206  Multilayer Ceramic Capacitors MLCC - SMD/SMT ROHS'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C50254'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Samsung Electro-Mechanics', 'partID': 'CL31B225KBHNNNE', 'partName': 'CL31B225KBHNNNE'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

