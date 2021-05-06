import Omega
import sys
import base64

text = open(sys.argv[1],'r')
arquivo = text.encode('ascii') 
base64_bytes = base64.b64encode(arquivo)
o = Omega.Omega(arquivo, sys.argv[2])

for linha in arquivo:
    basemontador = o.base_montador(len(linha))
    montador = o.gera_montador(int(sys.argv[2]),basemontador)
    string = o.permuta(montador,list(linha))
    decimal = o.gera_decimal(basemontador,montador)
    #print (basemontador)
   # print (montador)
    print (''.join(string))
    #print (decimal)
    print(linha)

#o = Omega.Omega(arquivo, sys.argv[2])
#basemontador = o.base_montador(len(arquivo))
#montador = o.gera_montador(int(sys.argv[2]),basemontador)
#string = o.permuta(montador,list(arquivo))
#decimal = o.gera_decimal(basemontador,montador)

#print(basemontador)
#print (basemontador)
#print (montador)
#print (string)
#print (decimal)

