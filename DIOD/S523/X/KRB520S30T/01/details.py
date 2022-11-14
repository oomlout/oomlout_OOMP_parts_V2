
######  Auto translated oomp file

def load(newPart,it):
    oType = "DIOD"
    oSize = "S523"
    oColor = "X"
    oDesc = "KRB520S30T"
    oIndex = "01"
    hexID = "D34148"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['matchSpecial'].append([['RB520S30T1G'], 'DIOD-S523-X-KRB520S30T-01'])
    newPart['footprintKicad'].append('FOOTPRINT-kicad-kicad-footprints-Diode_SMD-D_SOD-523')
    newPart['symbolKicad'].append('SYMBOL-kicad-kicad-symbols-Device-D')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

