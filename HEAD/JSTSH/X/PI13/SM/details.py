
######  Auto translated oomp file

def load(newPart):
    oType = "HEAD"
    oSize = "JSTSH"
    oColor = "X"
    oDesc = "PI13"
    oIndex = "SM"
    hexID = "HSH13"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['manufacturerPartNumber'].append({'partLink': 'https://www.jst.co.uk/productSeries.php?pid=93'})



    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

