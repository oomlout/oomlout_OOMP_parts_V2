
######  Auto translated oomp file

def load(newPart):
    oType = "CAPC"
    oSize = "1206"
    oColor = "X"
    oDesc = "UF7"
    oIndex = "V10"
    hexID = "C12U710"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C96123', 'partName': '10V 47uF X5R ??20% 1206  Multilayer Ceramic Capacitors MLCC - SMD/SMT ROHS'})

    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C96123'})

    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Samsung Electro-Mechanics', 'partID': 'CL31A476MPHNNNE', 'partName': 'CL31A476MPHNNNE'})



    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

