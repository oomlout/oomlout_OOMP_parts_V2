
######  Auto translated oomp file

def load(newPart,it):
    oType = "CAPC"
    oSize = "0402"
    oColor = "X"
    oDesc = "UF1"
    oIndex = "V25"
    hexID = "C4U1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C52923', 'partName': '25V 1uF X5R ??10% 0402  Multilayer Ceramic Capacitors MLCC - SMD/SMT ROHS'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C52923'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Samsung Electro-Mechanics', 'partID': 'CL05A105KA5NQNC', 'partName': 'CL05A105KA5NQNC'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

