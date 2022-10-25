
######  Auto translated oomp file

def load(newPart,it):
    oType = "CAPC"
    oSize = "0402"
    oColor = "X"
    oDesc = "NF20"
    oIndex = "V16"
    hexID = "C4N2016"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C16772', 'partName': '16V 220nF X7R ??10% 0402  Multilayer Ceramic Capacitors MLCC - SMD/SMT ROHS'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C16772'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Samsung Electro-Mechanics', 'partID': 'CL05B224KO5NNNC', 'partName': 'CL05B224KO5NNNC'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

