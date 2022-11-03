
######  Auto translated oomp file

def load(newPart,it):
    oType = "HEAD"
    oSize = "JSTXH"
    oColor = "X"
    oDesc = "PI19"
    oIndex = "01"
    hexID = "RXH19"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['manufacturerPartNumber'].append({'partLink': 'https://www.jst.co.uk/productSeries.php?pid=136'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

