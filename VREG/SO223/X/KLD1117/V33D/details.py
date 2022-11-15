
######  Auto translated oomp file

def load(newPart,it):
    oType = "VREG"
    oSize = "SO223"
    oColor = "X"
    oDesc = "KLD1117"
    oIndex = "V33D"
    hexID = "VR111722333D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicad'].append('SYMBOL-kicad-kicad-symbols-Regulator_Linear-AP1117-15')
    newPart['symbolKicad'].append('SYMBOL-kicad-kicad-symbols-Regulator_Linear-LD1117S33TR_SOT223')
    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C6186', 'partName': '72dB@(120Hz) 1A 1.3V@(800mA) Fixed 3.3V~3.3V Positive 1 SOT-223  Linear Voltage Regulators (LDO) ROHS'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C6186'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Advanced Monolithic Systems', 'partID': 'AMS1117-3.3', 'partName': 'AMS1117-3.3'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

