import sys
def converte_para_binario(string):
    d,b=[],[]
    for i in string:
        d.append(ord(i))
    for i in d:
        b.append(format(i,'08b'))
    return (b)

string = sys.argv[1]

print(list(converte_para_binario(string)[0]))
