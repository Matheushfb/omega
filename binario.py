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
    
    def esteira_binaria(self,b):
        i,j,k = 0,4,0
        l = len(b)
        while k < l:
            b[i:j],b[j:(j+j)]=b[j:(j+j)],b[i:j]
            i=i+4
            j=j+4
            k=k+1
        return b

string = sys.argv[1]
ba = BinTools(string)
binn = "".join(ba.converte_para_binario())
print(ba.esteira_binaria(list(binn)))
