import Omega
import sys
import base64
import dectobin
import binascii

name = sys.argv[1]
o = Omega.Omega(name,sys.argv[2])
    
message = name
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')
teste = dectobin(base64_message)

print(teste)

#for linha in arquivo:
basemontador = o.base_montador(len(name))
montador = o.gera_montador(int(sys.argv[2]),basemontador)
string = o.permuta(montador,list(name))
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

