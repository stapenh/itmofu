AI= "O"
Player= ("X")
    gf =[['_', '_', '_'],
       ['_', '_', '_'],
       ['_', '_', '_']]
def checkGameState(gf):
    i=0
    c='_'
    while(i<3):
        if (gf[i][0]==gf[i][1]==gf[i][2] and gf[i][0]!='_'):
            if(gf[i][0]=='0'):
                return 'AI'
            else :
                return 'Player'
        if (gf[i][0]==gf[i][1]==gf[i][2] and gf[i][0]!='_'):
            if(gf[i][0]=='0'):
                return 'AI'
            else :
                return 'Player'


