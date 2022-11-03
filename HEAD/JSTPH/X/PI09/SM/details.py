
######  Auto translated oomp file

def load(newPart,it):
    oType = "HEAD"
    oSize = "JSTPH"
    oColor = "X"
    oDesc = "PI09"
    oIndex = "SM"
    hexID = "RPH09S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['manufacturerPartNumber'].append({'partLink': 'https://www.jst.co.uk/productSeries.php?pid=6626'})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

