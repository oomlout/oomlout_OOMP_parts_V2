
######  Put extra tags in this file that will be kept through regeneration

def load(newPart,it):
    oompID = "HEAD-I01-X-PI2X20-01"
    newPart = it[oompID]
    
    ###### Raspberry Pi
    newPart['matchSpecial'].append([["RASPBERRYPI_BPLUS_BONNET_THMSMT"],"HEAD-I01-X-PI2X20-01"]) ###### might also be set elsewhere
    #newPart['footprintKicad'].append('') ###### might also be set elsewhere
    #newPart['symbolKicad'].append('')



