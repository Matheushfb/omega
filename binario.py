import sys

class BinTools:
    def __init__(self, string):
        self.string = string

    def converte_para_binario(self):
        d,self.b=[],[]
        for i in self.string:
            d.append(ord(i))
        for i in d:
            self.b.append(format(i,'08b'))
        return self.b
    
string = sys.argv[1]
ba = BinTools(string)
binn = "".join(ba.converte_para_binario())
print(binn)
