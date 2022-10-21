
######  Auto translated oomp file

def load(newPart):
    oType = "CAPC"
    oSize = "1206"
    oColor = "X"
    oDesc = "UF10"
    oIndex = "V50"
    hexID = "C12U10"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C13585', 'partName': '50V 10uF X5R ??10% 1206  Multilayer Ceramic Capacitors MLCC - SMD/SMT ROHS'})

    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C13585'})

    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Samsung Electro-Mechanics', 'partID': 'CL31A106KBHNNNE', 'partName': 'CL31A106KBHNNNE'})



    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

