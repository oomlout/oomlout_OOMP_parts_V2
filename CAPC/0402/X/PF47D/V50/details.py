
######  Auto translated oomp file

def load(newPart,it):
    oType = "CAPC"
    oSize = "0402"
    oColor = "X"
    oDesc = "PF47D"
    oIndex = "V50"
    hexID = "C4P47D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C1569', 'partName': '50V 4.7pF C0G ??0.25pF 0402  Multilayer Ceramic Capacitors MLCC - SMD/SMT ROHS'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C1569'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'FH (Guangdong Fenghua Advanced Tech)', 'partID': '0402CG4R7C500NT', 'partName': '0402CG4R7C500NT'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

