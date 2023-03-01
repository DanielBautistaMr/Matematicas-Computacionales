import math

x = -0.85
n = 1
t = 1
r = t
pr = r
ea = 100

while abs(ea) > 0.0001:
    t *= x / n
    pr = r
    r += t
    n += 1
    ea = ((r - pr) / r) * 100

r = 1 / r

print("Aproximación 2:")
print("Valor aproximado: ", round(r, 8))
print("Último error aproximado relativo porcentual: ", round(ea, 8))
print("Número de iteraciones realizadas: ", n-1)