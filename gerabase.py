import math


def bmont(lenstr):
    base = [] 
    i = lenstr - 1
    p = math.factorial(lenstr)
    while i > 0:
        q = math.factorial((lenstr - i) + 1 )
        r = p//q 
        base.append(r)
        i = i - 1
    return(base)
    
#lenstr = 0
#bmont(lenstr)

