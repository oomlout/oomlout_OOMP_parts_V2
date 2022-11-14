
######  Auto translated oomp file

def load(newPart,it):
    oType = "SENS"
    oSize = "LG143050"
    oColor = "X"
    oDesc = "K345"
    oIndex = "01"
    hexID = "SEN345"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['matchSpecial'].append([['ADXL343'], 'SENS-LG143050-X-K345-01'])
    newPart['footprintKicad'].append('FOOTPRINT-kicad-kicad-footprints-Package_LGA-LGA-14_3x5mm_P0.8mm_LayoutBorder1x6y')
    newPart['symbolKicad'].append('SYMBOL-kicad-kicad-symbols-Sensor_Motion-ADXL343')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

