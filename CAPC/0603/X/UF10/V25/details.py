
######  Auto translated oomp file

def load(newPart,it):
    oType = "CAPC"
    oSize = "0603"
    oColor = "X"
    oDesc = "UF10"
    oIndex = "V25"
    hexID = "C6U10"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C96446', 'partName': '25V 10uF X5R ??20% 0603  Multilayer Ceramic Capacitors MLCC - SMD/SMT ROHS'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C96446'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Samsung Electro-Mechanics', 'partID': 'CL10A106MA8NRNC', 'partName': 'CL10A106MA8NRNC'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

