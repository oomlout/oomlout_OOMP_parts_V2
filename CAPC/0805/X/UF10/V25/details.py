
######  Auto translated oomp file

def load(newPart,it):
    oType = "CAPC"
    oSize = "0805"
    oColor = "X"
    oDesc = "UF10"
    oIndex = "V25"
    hexID = "C8U10"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C15850', 'partName': '25V 10uF X5R ??10% 0805  Multilayer Ceramic Capacitors MLCC - SMD/SMT ROHS'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C15850'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Samsung Electro-Mechanics', 'partID': 'CL21A106KAYNNNE', 'partName': 'CL21A106KAYNNNE'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

