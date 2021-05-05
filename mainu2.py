import sys
import argparse
from gerabase import bmont
from geramontador import gmontador
from permuta import permuta


def main():
    lenstr = len(sys.argv[1])
    base = bmont(lenstr)
    dec = int(sys.argv[2])
    montador = gmontador(dec, base)
    string = permuta(montador,list(sys.argv[1]))
#    string = permuta(montador,list(lenstr)
    print(base)
    print(montador)
    print(string)


main()
