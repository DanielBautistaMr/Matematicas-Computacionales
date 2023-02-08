a = set()
b = set()
c = {1,4,8,10,12,15,18,20}
d = set()

for i in range(5,21):
  a.add(i)

for i in range(1,25):
  if i % 2 == 0:
      b.add(i)
    
for num in range(2, 46):
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
        d.add(num)


def unions(con1, con2):
    return con1.union(con2)
  
  
def intersection(con1, con2):
    return set(value for value in con1 if value in con2)
    
  
def diferencia(con1, con2):
    return con1-con2
    return con2-con1
  
def simetrica(con1, con2):
    return con1^con2


print(intersection(b, simetrica(c, d)))
print(unions(intersection(a, c), b))
print(diferencia(unions(b, d), c))
print(simetrica(diferencia(a,b),intersection(a,d)))