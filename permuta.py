def permuta(montador,string_orig):
    i=len(string_orig) -1 
    while i > 0:
        e = i
        d = e - montador[i-1] 
        string_orig[e],string_orig[d] = string_orig[d],string_orig[e]
        i = i - 1
    return(string_orig)

#string_orig = list(input("DIGITE UMA STRING: "))
#strng = strg[:]
#montador = [0,0,0,0,0,6]
#permuta(montador,string_orig)
