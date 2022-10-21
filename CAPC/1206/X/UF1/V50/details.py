
######  Auto translated oomp file

def load(newPart):
    oType = "CAPC"
    oSize = "1206"
    oColor = "X"
    oDesc = "UF1"
    oIndex = "V50"
    hexID = "C12U1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C1848', 'partName': '50V 1uF X7R ??10% 1206  Multilayer Ceramic Capacitors MLCC - SMD/SMT ROHS'})

    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C1848'})

    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Samsung Electro-Mechanics', 'partID': 'CL31B105KBHNNNE', 'partName': 'CL31B105KBHNNNE'})



    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

