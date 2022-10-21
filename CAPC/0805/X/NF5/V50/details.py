
######  Auto translated oomp file

def load(newPart):
    oType = "CAPC"
    oSize = "0805"
    oColor = "X"
    oDesc = "NF5"
    oIndex = "V50"
    hexID = "C8N5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C1717', 'partName': '50V 1.5nF X7R ??10% 0805  Multilayer Ceramic Capacitors MLCC - SMD/SMT ROHS'})

    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C1717'})

    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'FH (Guangdong Fenghua Advanced Tech)', 'partID': '0805B152K500NT', 'partName': '0805B152K500NT'})



    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

