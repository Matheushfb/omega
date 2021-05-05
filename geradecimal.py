def gdec(basemontador,montador):
    limite = len(basemontador)
    i = 0
    dec = 0
    while i < limite:
        dec = dec + basemontador[i] * montador[i]
        i = i + 1
    return(dec)

#montador = [1,1,1,1]
#basemontador = [60,20,5,1]
gdec(basemontador,montador)
