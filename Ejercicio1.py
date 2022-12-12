def numero(num_entero):
    if num_entero in range(1,11):
        file = open('tabla-' + str(num_entero) + '.txt', 'w')
        for tabla in range(1,11):
            respuesta = str(tabla) + "*" + str(num_entero) + "=" + str((tabla * num_entero)) + "\n"
            file.write(respuesta)
    return


num_entero = int(input("numero entero del 1 al 10:\n"))
numero(num_entero)

""""El primer range es para decirle al nu_entero que si su valor esta dentro de ese rango 
(el rango va del 1 al 10, porque el ultimo se lo come) puede hacer la operacion"""
"""El segundo range es para la tabla, hace un bucle del 1 al 10, que son los numeros con los que vas a multiplicar el
num_entero"""
"""Los numeros tienen que convertirse en strings con str(), porque si no no funciona"""