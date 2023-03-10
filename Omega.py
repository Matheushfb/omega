import sys
import argparse
import math

class Omega:
    def __init__(self,string,dec):
        self.string = string
        self.dec = dec

    def base_montador(self,string):
        self.base = []
        i = string - 1
        p = math.factorial(string)
        while i > 0:
            q = math.factorial((string - i) + 1)
            r = p // q
            self.base.append(r)
            i = i - 1
        return self.base

    def gera_montador(self,dec,basemontador):
        i = 0
        limite = len(basemontador)
        self.montador = []
        while i < limite:
            if dec >= math.factorial(limite + 1):
                print("Limite do digito decimal ultrapasado")
                sys.exit()
            if dec < basemontador[i]:
                self.montador.append(0)
                i = i + 1
            else:
                result = dec // basemontador[i]
                dec = dec % basemontador[i]
                self.montador.append(result)
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


    def depermuta(self,montador,nome):
        i = 0
        while i < len(nome)-1:
            e = i + 1
            d = e - montador[i]
            nome[e],nome[d]=nome[d],nome[e]
            i = i + 1
        return nome

    def gera_decimal(self,basemontador,montador):
        limite = len(basemontador)
        i = 0
        dec = 0
        while i < limite:
            dec = dec + basemontador[i] * montador[i]
            i = i + 1
        return(dec)

if __name__ == '__main__':
    nome = sys.argv[1]
    a = Omega(nome, 0)
    i = 0
    conta = 0

    basemontador = a.base_montador(len(nome))

    while i < math.factorial(len(nome)):
        montador = a.gera_montador(i,basemontador)
        string = a.permuta(montador,list(nome))
        decimal = a.gera_decimal(basemontador,montador)
        i = i + 1
        j = 0
        while j < len(nome)-1:
            if string[j] == nome[j]:
              #print("is not chaotique!")
                break
            else:
                j = j + 1
            if j == len(nome)-1:
                conta = conta + 1
                print (conta,decimal,string)
