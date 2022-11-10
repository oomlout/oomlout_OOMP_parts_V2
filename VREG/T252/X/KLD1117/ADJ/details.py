
######  Auto translated oomp file

def load(newPart,it):
    oType = "VREG"
    oSize = "T252"
    oColor = "X"
    oDesc = "KLD1117"
    oIndex = "ADJ"
    hexID = "VR1117252AJ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oompNote'].append('LCSC Part number set in VREG/SO223/X/KLD1117/V33D/details2.py')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart
