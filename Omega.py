import sys
import argparse
import math
import numpy as np 


class Omega:
    def __init__(self,lenstr,dec):
        self.lenstr = lenstr
        self.dec = dec

    def base_montador(self,lenstr):
        self.base = np.empty(lenstr-1,int)
        i = 0
        p = math.factorial(lenstr)
        while i <= lenstr - 2:
            q = math.factorial((lenstr-i))
            r = p // q
            self.base[lenstr-2-i]=r 
            i = i + 1
        return self.base

    def gera_montador(self,dec,basemontador):
        i = 0
        limite = len(basemontador)
        self.montador = np.empty(limite,int)
        while i < limite:
            if dec >= math.factorial(limite + 1):
                print("Limite do digito decimal ultrapasado")
                sys.exit()
            if dec < basemontador[i]:
                self.montador[i]=0
                i = i + 1
            else:
                result = dec // basemontador[i]
                dec = dec % basemontador[i]
                self.montador[i]=result
                i = i + 1
        return self.montador

    def permuta(self,montador,nome):
        i = len(nome) - 1
        while i > 0:
            e = i
            d = e - montador[i - 1]
            nome[e],nome[d]=nome[d],nome[e]
            i = i - 1
        return nome

    def gera_decimal(self,basemontador,montador):
        limite = len(basemontador)
        i = 0
        dec = 0
        while i < limite:
            dec = dec + basemontador[i] * montador[i]
            i = i + 1
        return(dec)



#nome = ["m","a","t","h","e","u","s"]
##nome = sys.argv[1]
##a = Omega(nome, sys.argv[2])
##basemontador = a.base_montador(len(nome))
##montador = a.gera_montador(int(sys.argv[2]),basemontador)
##string = a.permuta(montador,list(nome))
##decimal = a.gera_decimal(basemontador,montador)
##print (basemontador)
##print (montador)
##print (string)
##print (decimal)
#      base = bmont(lenstr)
#      dec = int(sys.argv[2])
#      montador = gmontador(dec, base)
#      string = permuta(montador,list(sys.argv[1]))
#      print(base)
#      print(montador)
#      print(string)
