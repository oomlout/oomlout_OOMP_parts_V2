
######  Put extra tags in this file that will be kept through regeneration

def load(newPart,it):
    oompID = "TRNN-SO23-X-KS8050-01"
    newPart = it[oompID]
    
    #newPart['matchSpecial'].append([["ADXL345"],"SENS-LG14-X-K345-01"]) ###### might also be set elsewhere
    newPart['footprintKicad'].append('FOOTPRINT-kicad-kicad-footprints-Package_TO_SOT_SMD-SOT-23') ###### might also be set elsewhere
    newPart['symbolKicad'].append('SYMBOL-kicad-kicad-symbols-Device-Q_NPN_BEC')



