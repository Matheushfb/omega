# -*- coding: cp1252 -*-
import math

en = int(input(" DIGITE O VALOR TAMANHO DA STRING :"))
bmontador = []
matriz = []
j = en
c2 = en - 1
montador2 = []
decimal = []
c4 = en - 2
matrizprimaria = []
c3 = 1


def menu():
    print(" ESCOLHA UM MODO")
    print(" 1 = MONTADOR AVULSO")
    print(" 2 = DECIMAL PARA MONTADOR")
    print(" 3 = GERADOR DE PERMUTAÇÃO")
    print(" DIGITE SUA ESCOLHA: ")
    modo = int(input())
    if modo == 1:
        digmontador(c3)
    elif modo == 2:
        #print
        #"MODO NAO FEITO"
        geramontador()
    elif modo == 3:
        #print
        #"MODO NAO FEITO"
        menu()
    else:
        #print
        #"INISIRA UMA OPCAO VALIDA"
        menu()
        return


# - RECEBE OS DADOS DA MATRIZ E MANDA PARA O GERADOR DE BASE DO DIGITO MONTADOR - #

def geralista():
    c1 = en
    while c1 > 0:
        print("ENTRE COM O ", c1, "º"" ELEMENTO: ")
        x = input('Digite o nome')
        matriz.insert(0, x)
        matrizprimaria.insert(0, x)
        c1 = c1 - 1
        basemontador()
        if c1 == 0:
            print("MATRIZ PRIMARIA ====> ", matriz, "\n")
            del bmontador[-1]
            menu()
            digmontador(c3)
            return


# - GERA BASE DO DIGITO MONTADOR - #

def basemontador():
    global j
    c2 = en
    j = j - 1
    p = math.factorial(c2)
    q = c2 - j + 1
    r = math.factorial(q)
    s = (p // r)
    bmontador.insert(en, s)
    return


# - RECEBE E VALIDA DIGITO MONTADOR - #

def digmontador(c3):
    while c3 < en:
        print("INSIRA O ", c3, "ºDIGITO DO MONTADOR :")
        nm = int(input())
        if nm > c3:
            print('WARNING!!! VOCE INSERIU UM VALOR INVALIDO PARA ESTE CAMPO!!!', "\n")
            return digmontador(c3)
        else:
            permuta(en, nm, c3)
            montador2.append(nm)
            c3 = c3 + 1
        if c3 == en:
            geradecimal(c4, nm)
            return nm


# - GERA O NUMERO DECIMAL - #

def geradecimal(c4, nm):
    while c4 > -1:
        a = bmontador[c4] * montador2[c4]
        decimal.insert(0, a)
        c4 = c4 - 1
        if c4 <= -1:
            print("A BASE DO DIGITO MONTADOR E ===> ", bmontador, "\n")
            print("O MONTADOR E ===>", montador2, "\n")
            print("O NUMERO DECIMAL E ===> ", sum(decimal), "\n")
            print("MATRIZ PRMUTADA", matriz)
            del decimal[0:]
            del montador2[0:]
            menu()


# - GERA PERMUTAÇÃO - #

def permuta(en, nm, c3):
    c2 = c3
    p = c2 - nm
    matriz[p], matriz[c2] = matriz[c2], matriz[p]


# - GERA NUMERO MONTADOR A PARTIR DE UM DECIMAL -#

def geramontador():
    c5 = 0
    while c5 < en - 1:
        print
        bmontador[c5]
        c5 = c5 + 1
        if c5 == en - 1:
            print("DIGITE O NUMERO DECIMAL DE ACORDO COM A STRING")
            menu()


geralista()