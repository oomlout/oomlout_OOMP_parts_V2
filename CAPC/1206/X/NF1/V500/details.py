
######  Auto translated oomp file

def load(newPart,it):
    oType = "CAPC"
    oSize = "1206"
    oColor = "X"
    oDesc = "NF1"
    oIndex = "V500"
    hexID = "C12N10"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C35216', 'partName': '500V 1nF X7R ??10% 1206  Multilayer Ceramic Capacitors MLCC - SMD/SMT ROHS'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C35216'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Samsung Electro-Mechanics', 'partID': 'CL31B102KGFNNNE', 'partName': 'CL31B102KGFNNNE'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

