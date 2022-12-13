def numero(num_entero, linea):
    if num_entero in range(1, 11):
        nombre = 'tabla-' + str(num_entero) + '.txt'
        try:
            with open(nombre, 'r') as file:
                lineas = file.readlines()
            print(lineas[linea - 1])
        except FileNotFoundError:
            print('No existe la tabla')
    return

num_entero = int(input('Seleccione un número entre el 1 y el 10:\n'))
linea = int(input('Elija una línea entre el 1 y el 10:\n'))
numero(num_entero, linea)