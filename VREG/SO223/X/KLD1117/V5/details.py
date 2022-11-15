
######  Auto translated oomp file

def load(newPart,it):
    oType = "VREG"
    oSize = "SO223"
    oColor = "X"
    oDesc = "KLD1117"
    oIndex = "V5"
    hexID = "VR11172235"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicad'].append('SYMBOL-kicad-kicad-symbols-Regulator_Linear-AP1117-15')
    newPart['symbolKicad'].append('SYMBOL-kicad-kicad-symbols-Regulator_Linear-LD1117S50TR_SOT223')
    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C6187', 'partName': '68dB@(120Hz) 1A 1.3V@(1A) Fixed 5V~5V Positive 1 15V SOT-223  Linear Voltage Regulators (LDO) ROHS'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C6187'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Advanced Monolithic Systems', 'partID': 'AMS1117-5.0', 'partName': 'AMS1117-5.0'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

