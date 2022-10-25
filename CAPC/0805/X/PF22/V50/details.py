
######  Auto translated oomp file

def load(newPart,it):
    oType = "CAPC"
    oSize = "0805"
    oColor = "X"
    oDesc = "PF22"
    oIndex = "V50"
    hexID = "C8P22"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C1804', 'partName': '50V 22pF C0G ??5% 0805  Multilayer Ceramic Capacitors MLCC - SMD/SMT ROHS'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C1804'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Samsung Electro-Mechanics', 'partID': 'CL21C220JBANNNC', 'partName': 'CL21C220JBANNNC'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

