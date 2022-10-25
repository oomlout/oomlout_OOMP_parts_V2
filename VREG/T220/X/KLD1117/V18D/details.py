
######  Auto translated oomp file

def load(newPart,it):
    oType = "VREG"
    oSize = "T220"
    oColor = "X"
    oDesc = "KLD1117"
    oIndex = "V18D"
    hexID = "VR111722018"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['distributorPartNumber'].append({'name': 'LCSC', 'code': 'C-LCSC', 'partID': 'C165948', 'partName': 'C165948', 'partLink': ''})
    newPart['manufacturerPartNumber'].append({'name': 'Korean Hroparts Elec', 'code': 'C-KHRO', 'partID': 'TYPE-C-31-M-12', 'partName': '', 'partLink': ''})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

