import math

a = 0.45
x = 0.455
h = x - a

fx = 0
fxa = 0
e = math.e

for i in range(16):
    if i % 2 == 0:
        fa = e ** a
    else:
        fa = e ** (-a)

    fx += (fa * (h ** i)) / math.factorial(i)

    if i > 0:
        ea = abs((fx - fxa) / fx) * 100
        print('orden ', i, 'valor de la serie ', fx, 'error ', ea)
        print('---------------------------------')

