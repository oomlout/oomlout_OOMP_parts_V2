
######  Auto translated oomp file

def load(newPart):
    oType = "CAPC"
    oSize = "0603"
    oColor = "X"
    oDesc = "UF2"
    oIndex = "V16"
    hexID = "C6U216"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C23630', 'partName': '16V 2.2uF X5R ??10% 0603  Multilayer Ceramic Capacitors MLCC - SMD/SMT ROHS'})

    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C23630'})

    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Samsung Electro-Mechanics', 'partID': 'CL10A225KO8NNNC', 'partName': 'CL10A225KO8NNNC'})



    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

