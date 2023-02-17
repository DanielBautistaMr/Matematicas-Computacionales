def run():
    def subconjuntos(i):
        conjunto_potencia = [[]]
        for element in i:
            for sub_conjunto in conjunto_potencia:
                conjunto_potencia = conjunto_potencia + [list(sub_conjunto) + [element]]
        return conjunto_potencia
    

    i = [1,7,14,66,411]
    number = len(i)
    Pa = 2**number

    print('el cojunto tiene ' + str(Pa) + ' subconjuntos')
    print(subconjuntos(i))

if __name__ == '__main__':
    run()
    


