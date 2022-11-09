
######  Auto translated oomp file

def load(newPart,it):
    oType = "LEDS"
    oSize = "0603"
    oColor = "L"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "L6L"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C72038', 'partName': '20mA 180mcd 2.3V 591nm Colorless transparence -40??~+85?? 585.5nm~591.5nm yellow 120?? 60mW 0603  Light Emitting Diodes (LED) ROHS'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C72038'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Everlight Elec', 'partID': '19-213/Y2C-CQ2R2L/3T(CY)', 'partName': '19-213/Y2C-CQ2R2L/3T(CY)'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

