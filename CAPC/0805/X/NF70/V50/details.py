
######  Auto translated oomp file

def load(newPart,it):
    oType = "CAPC"
    oSize = "0805"
    oColor = "X"
    oDesc = "NF70"
    oIndex = "V50"
    hexID = "C085N70"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C13967', 'partName': '50V 470nF X7R ??10% 0805  Multilayer Ceramic Capacitors MLCC - SMD/SMT ROHS'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C13967'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Samsung Electro-Mechanics', 'partID': 'CL21B474KBFNNNE', 'partName': 'CL21B474KBFNNNE'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

