import Omega
import sys
import base64
import dectobin

text = open(sys.argv[1],'rb')
arquivo = text.read() 
#base64_bytes = base64.b64encode(arquivo)
o = Omega.Omega(text, sys.argv[2])

#for linha in arquivo:
basemontador = o.base_montador(len(arquivo))
montador = o.gera_montador(int(sys.argv[2]),basemontador)
string = o.permuta(montador,list(arquivo))
decimal = o.gera_decimal(basemontador,montador)
#print(text)
print(string)


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

