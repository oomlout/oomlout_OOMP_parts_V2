
######  Auto translated oomp file

def load(newPart,it):
    oType = "CAPC"
    oSize = "0603"
    oColor = "X"
    oDesc = "NF70"
    oIndex = "V25"
    hexID = "C063N70"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C1623', 'partName': '25V 470nF X7R ??10% 0603  Multilayer Ceramic Capacitors MLCC - SMD/SMT ROHS'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C1623'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Samsung Electro-Mechanics', 'partID': 'CL10B474KA8NNNC', 'partName': 'CL10B474KA8NNNC'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

