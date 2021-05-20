import sys

def dectobin(dec):
    binary = [0]*8
    i = 7
    while i >= 0:
        resto = dec%2
        binary[i]=resto
        dec = dec//2
        i=i-1
    print(binary)

