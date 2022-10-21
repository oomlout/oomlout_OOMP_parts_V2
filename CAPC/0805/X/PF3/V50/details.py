
######  Auto translated oomp file

def load(newPart):
    oType = "CAPC"
    oSize = "0805"
    oColor = "X"
    oDesc = "PF3"
    oIndex = "V50"
    hexID = "C8P3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C107115', 'partName': '50V 33pF NP0 ??5% 0805  Multilayer Ceramic Capacitors MLCC - SMD/SMT ROHS'})

    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C107115'})

    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'YAGEO', 'partID': 'CC0805JRNPO9BN330', 'partName': 'CC0805JRNPO9BN330'})



    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

