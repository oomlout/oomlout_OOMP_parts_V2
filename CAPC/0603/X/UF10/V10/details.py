
######  Auto translated oomp file

def load(newPart,it):
    oType = "CAPC"
    oSize = "0603"
    oColor = "X"
    oDesc = "UF10"
    oIndex = "V10"
    hexID = "C063U1010"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C19702', 'partName': '10V 10uF X5R ??10% 0603  Multilayer Ceramic Capacitors MLCC - SMD/SMT ROHS'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C19702'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Samsung Electro-Mechanics', 'partID': 'CL10A106KP8NNNC', 'partName': 'CL10A106KP8NNNC'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

