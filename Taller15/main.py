def imprimir_matriz(matriz, n, m):
    for i in range(n):
        for j in range(m):
            print(matriz[i][j], end=" ")
        print()
    return

def imprimir_inversa(matriz, n, m):
    for i in range(n):
        for j in range(n, m):
            print("%.3f " % matriz[i][j], end="")
        print()
    return

def inversa_de_matriz(matriz, orden):
    print("=== Matriz ===")
    imprimir_matriz(matriz, orden, orden)

    for i in range(orden):
        for j in range(2 * orden):
            if j == (i + orden):
                matriz[i][j] = 1

    for i in range(orden - 1, 0, -1):
        if matriz[i - 1][0] < matriz[i][0]:
            fila_temporal = matriz[i]
            matriz[i] = matriz[i - 1]
            matriz[i - 1] = fila_temporal

    for i in range(orden):
        for j in range(orden):
            if j != i:
                temporal = matriz[j][i] / matriz[i][i]
                for k in range(2 * orden):
                    matriz[j][k] -= matriz[i][k] * temporal

    for i in range(orden):
        temporal = matriz[i][i]
        for j in range(2 * orden):
            matriz[i][j] = matriz[i][j] / temporal

    print("\n=== Matriz Inversa ===")
    imprimir_inversa(matriz, orden, 2 * orden)

    return

def main():
    orden = 3

    matriz = [[0 for i in range(20)] for j in range(20)]

    matriz[0][0] = 3
    matriz[0][1] = 2
    matriz[0][2] = 2
    matriz[1][0] = 3
    matriz[1][1] = 1
    matriz[1][2] = -3
    matriz[2][0] = 1
    matriz[2][1] = 0
    matriz[2][2] = -2
  
    ordentwo = 4
    matrix = [[0 for i in range(20)] for j in range(20)]

    matrix[0][0] = 1
    matrix[0][1] = 2
    matrix[0][2] = 0
    matrix[0][3] = 4
    matrix[1][0] = 2
    matrix[1][1] = 0
    matrix[1][2] = -1
    matrix[1][3] = -2
    matrix[2][0] = 1
    matrix[2][1] = 1
    matrix[2][2] = -1
    matrix[2][3] = 0
    matrix[3][0] = 0
    matrix[3][1] = 4
    matrix[3][2] = 1
    matrix[3][3] = 0

    inversa_de_matriz(matriz, orden)
    inversa_de_matriz(matrix, ordentwo)
if __name__ == '__main__':
    main()