import sys
import math


def gmontador(dec, basemontador):
    i = 0
    limite=len(basemontador)
    montador = []
    while i < limite:
        if dec >= math.factorial(limite+1):
           print("Limite do digito decimal ultrapasado")
           sys.exit()
        if dec < basemontador[i]:
            montador.append(0)
            i = i + 1
        else:
            result = dec // basemontador[i]
            dec = dec % basemontador[i]
            montador.append(result)
            i = i + 1

    return montador
