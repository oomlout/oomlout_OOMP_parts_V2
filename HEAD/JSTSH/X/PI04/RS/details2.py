
######  Put extra tags in this file that will be kept through regeneration

def load(newPart,it):
    oompID = "HEAD-JSTSH-X-PI04-RS"
    newPart = it[oompID]
    
    ###### QWIIC Connector
    newPart['matchSpecial'].append([["JST_SH_SM04B-SRSS-TB_1x04-1MP_P1.00mm_Horizontal","STEMMA_I2C","QWIIC","I2C_STANDARDJS-1MM"],"HEAD-JSTSH-X-PI04-RS"]) ###### might also be set elsewhere
    #newPart['footprintKicad'].append('') ###### might also be set elsewhere
    #newPart['symbolKicad'].append('')



