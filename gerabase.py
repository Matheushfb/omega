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
    print (base)
    return(base)
    
lenstr = 5
bmont(lenstr)

