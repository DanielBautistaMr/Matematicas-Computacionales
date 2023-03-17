import math

a = math.comb(6, 1) * math.comb(5, 1) * math.comb(4, 1) * math.comb(3, 1)
print("a. Número de formas posibles sin María ni Pedro:", a)

b = math.comb(1, 1) * math.comb(6, 1) * math.comb(5, 1) * math.comb(4, 1)
print("b. Número de formas posibles con María en el comité:", b)

c = math.comb(2, 1) * math.comb(6, 1) * math.comb(5, 1) * math.comb(4, 1)
print("c. Número de formas posibles con María y Pedro en el comité:", c)

d = (math.comb(1, 1) * math.comb(6, 1) * math.comb(5, 1) * math.comb(4, 1)) + (math.comb(1, 1) * math.comb(1, 1) * math.comb(5, 1) * math.comb(4, 1))
print("d. Número de formas posibles con María o Pedro como director:", d)