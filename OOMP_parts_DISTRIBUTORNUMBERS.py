######  File for adding LCSC part numbers to parts easily in a central location

def load(it):
    pass
    ###### empty dict
    distributors = ["C-DIGK","C-LCSC","C-MOUS","C-FARN"]

    
    distDict = {}
    current = "C-DIGK"
    distDict[current] = {}
    distDict[current]["CODE"] = current
    distDict[current]["NAME"] = "Digikey"
    distDict[current]["LINK"] = "https://www.digikey.com/en/products/detail/"
    distDict[current]["LINKEND"] = ""
    current = "C-LCSC"
    distDict[current] = {}
    distDict[current]["CODE"] = current
    distDict[current]["NAME"] = "LCSC"
    distDict[current]["LINK"] = "https://www.lcsc.com/product-detail/"
    distDict[current]["LINKEND"] = ".html"
    current = "C-MOUS"
    distDict[current] = {}
    distDict[current]["CODE"] = current
    distDict[current]["NAME"] = "Mouser"
    distDict[current]["LINK"] = "https://www.mouser.co.uk/c/?q="
    distDict[current]["LINKEND"] = ""
    current = "C-FARN"
    distDict[current] = {}
    distDict[current]["CODE"] = current
    distDict[current]["NAME"] = "Farnell"
    distDict[current]["LINK"] = "https://www.mouser.co.uk/c/?q="
    distDict[current]["LINKEND"] = ""
    
    
    
    ######setup Base
    base  = {}
    base["oompID"] = ""
    for d in distributors:
        base[d] = ""

    list = []
    
    item = base.copy()
    item["oompID"] = "MCUU-SC14-84-ATTINY-01"
    item["MPN"] = "C-MICROC-ATtiny84-20SSU"
    item["C-DIGK"] = "microchip-technology/ATTINY84A-SSU/3046522"
    item["C-LCSC"] = "C1337153"
    item["C-FARN"] = "1972173"
    item["C-MOUS"] = "556-ATTINY84-20SSUR"    
    ######ITEM END
    list.append(item)
    
    

    for l in list:
        oompID = l["oompID"]
        newPart = it[oompID]    
        for d in distributors:
            pNum = l[d]
            link = distDict[d]["LINK"] + pNum + distDict[d]["LINKEND"]
            newPart['distributorPartNumber'].append(
                {'dpnKey': 'DPN-' + d + '-' + pNum, 
                'DISTRIBUTOR': distDict[d]["NAME"], 
                'DISTRCODE': distDict[d]["CODE"], 
                'DPN': pNum, 'MPN': '', 
                'TAGS': [], 
                'LINK': link, 
                'OOMPID': oompID})