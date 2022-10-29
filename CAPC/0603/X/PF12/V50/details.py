
######  Auto translated oomp file

def load(newPart,it):
    oType = "CAPC"
    oSize = "0603"
    oColor = "X"
    oDesc = "PF12"
    oIndex = "V50"
    hexID = "C063P12"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C38523', 'partName': '50V 12pF C0G ??5% 0603  Multilayer Ceramic Capacitors MLCC - SMD/SMT ROHS'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C38523'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Samsung Electro-Mechanics', 'partID': 'CL10C120JB8NNNC', 'partName': 'CL10C120JB8NNNC'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

