
######  Auto translated oomp file

def load(newPart,it):
    oType = "CAPC"
    oSize = "0402"
    oColor = "X"
    oDesc = "NF70"
    oIndex = "V10"
    hexID = "C4N7010"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C47339', 'partName': '10V 470nF X5R ??10% 0402  Multilayer Ceramic Capacitors MLCC - SMD/SMT ROHS'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C47339'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Samsung Electro-Mechanics', 'partID': 'CL05A474KP5NNNC', 'partName': 'CL05A474KP5NNNC'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

