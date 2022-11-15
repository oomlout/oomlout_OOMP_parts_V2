
######  Auto translated oomp file

def load(newPart,it):
    oType = "VREG"
    oSize = "SO223"
    oColor = "X"
    oDesc = "KLD1117"
    oIndex = "V25D"
    hexID = "VR111722325D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oompNote'].append('LCSC Part number set in VREG/SO223/X/KLD1117/V5/details2.py')
    newPart['symbolKicad'].append('SYMBOL-kicad-kicad-symbols-Regulator_Linear-AP1117-15')
    newPart['symbolKicad'].append('SYMBOL-kicad-kicad-symbols-Regulator_Linear-LD1117S25TR_SOT223')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

