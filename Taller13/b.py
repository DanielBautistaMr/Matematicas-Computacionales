import numpy as np

fil = int(input('Ingrese el numero de filas de la matriz A y B: '))
col = int(input('Ingrese el numero de columnas de la matriz A y B: '))

print('---------------------------------------------------------------------')

a = []
for i in range(fil):
    fila = []
    for j in range(col):
        if j % 2 == 0:
            valor = input('Ingrese el valor para la posición [{},{}] matriz A: '.format(i, j))
            fila.append(int(valor))
        else:
            valor = input('Ingrese el valor para la posición [{},{}] matriz A: '.format(i, j))
            fila.append(int(valor))
    a.append(fila)

matrizA = np.array(a)

print('---------------------------------------------------------------------')

b = []
for i in range(fil):
    fila = []
    for j in range(col):
        if j % 2 == 0:
            valor = input('Ingrese el valor para la posición [{},{}] de la matriz B: '.format(i, j))
            fila.append(int(valor))
        else:
            valor = input('Ingrese el valor para la posición [{},{}] de la matriz B: '.format(i, j))
            fila.append(int(valor))
    b.append(fila)

matrizB = np.array(b)

print('---------------------------------------------------------------------')

print("Matriz A:")
print(matrizA)

print("Matriz B:")
print(matrizB)

print('---------------------------------------------------------------------')


tresA = 3 * matrizA
print("3A:")
print(tresA)


cuatroB = 4 * matrizB
print("4B:")
print(cuatroB)


sumaAB = matrizA + matrizB
print("A + B:")
print(sumaAB)


productoBA = np.matmul(matrizB, matrizA)
print("B x A:")
print(productoBA)
