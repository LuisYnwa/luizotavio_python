def sequencial (*args):
    multiplafinal = 1
    for n in args:
       multiplafinal *= n
    return multiplafinal

aaa = sequencial(3, 4, 2, 5, 8, 2)
#print(aaa)

def ehpar (pi):
    final = pi % 2 == 0
    if final:
        return True
    else:
        return False
    
parouimpar = ehpar(45)
print(parouimpar)
        

