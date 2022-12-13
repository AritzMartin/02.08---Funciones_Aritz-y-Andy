
def numero(num_entero):
    if num_entero in range(1, 11):
        nombre = 'tabla-' + str(num_entero) + '.txt'
        try:
            file = open(nombre, 'r')
        except FileNotFoundError:
            print('No existe la tabla deseada')
        else:
            print(file.read())
    return


num_entero = int(input('Introduce un número del 1 al 10:\n'))
numero(num_entero)