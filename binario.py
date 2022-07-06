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
        i,j,k = 0,8,0
        l = len(string)
        print(b)
        while k < l:
            b[i:(i+4)],b[j:(j-4)]=b[j:(j-4)],b[i:(i+4)]
            i=i+8
            j=j+8
            k=k+1
        return b

string = sys.argv[1]
ba = BinTools(string)
binn = "".join(ba.converte_para_binario())
print(ba.esteira_binaria(list(binn)))
