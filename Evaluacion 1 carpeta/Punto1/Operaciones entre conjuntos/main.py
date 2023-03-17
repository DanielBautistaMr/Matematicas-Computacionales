A = {7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}
B = {2, 5, 7, 9, 15, 22, 33}
C = {4, 7, 10, 13, 16, 19, 22, 25, 28}


def unions(con1, con2):
    return con1.union(con2)
    
def intersection(con1, con2):
    return set(value for value in con1 if value in con2)
    
def diferencia(con1, con2):
    return con1-con2
    return con2-con1
  
def simetrica(con1, con2):
    return con1^con2


#La primera Union
print(unions(intersection(A, C), simetrica(A,B)))

#simplificar la intersecion 2
un = unions(A,C)
sim = simetrica(un, B)
dif = diferencia(A,B)

print(intersection(sim, dif))

#simplificar la intersecion 3

int = intersection(A, C)
diferen = diferencia(un, int)
uni = unions(un, C)

print(intersection(diferen, uni))




