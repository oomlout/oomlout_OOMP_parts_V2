
######  Auto translated oomp file

def load(newPart,it):
    oType = "CAPC"
    oSize = "0603"
    oColor = "X"
    oDesc = "PF7"
    oIndex = "V50"
    hexID = "C063P7"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C107045', 'partName': '50V 27pF NP0 ??5% 0603  Multilayer Ceramic Capacitors MLCC - SMD/SMT ROHS'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C107045'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'YAGEO', 'partID': 'CC0603JRNPO9BN270', 'partName': 'CC0603JRNPO9BN270'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

