
######  Auto translated oomp file

def load(newPart,it):
    oType = "LEDS"
    oSize = "0603"
    oColor = "G"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "L063G"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oplPartNumber'].append({'code': 'C-JLCC', 'name': 'JLC Parts Library', 'partID': 'C72043', 'partName': '20mA 285mcd 3.3V 518nm Colorless transparence -40??~+85?? 520nm~535nm Emerald 120?? 110mW 0603  Light Emitting Diodes (LED) ROHS'})
    newPart['distributorPartNumber'].append({'code': 'C-LCSC', 'name': 'LCSC', 'partID': 'C72043'})
    newPart['manufacturerPartNumber'].append({'code': 'C-XXXX', 'name': 'Everlight Elec', 'partID': '19-217/GHC-YR1S2/3T', 'partName': '19-217/GHC-YR1S2/3T'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

