
######  Auto translated oomp file

def load(newPart,it):
    oType = "CAPC"
    oSize = "0805"
    oColor = "X"
    oDesc = "UF7"
    oIndex = "V63D"
    hexID = "C8U763D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C16780', 'partName': '6.3V 47uF X5R ??20% 0805  Multilayer Ceramic Capacitors MLCC - SMD/SMT ROHS'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C16780'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Samsung Electro-Mechanics', 'partID': 'CL21A476MQYNNNE', 'partName': 'CL21A476MQYNNNE'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

