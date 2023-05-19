def editar_inmueble(inmuebles):
    print(f'Lista de Inmuebles:\n{inmuebles}')
    indice = int(input('Ingrese el número de índice del inmueble a editar:  '))
    inmueble = inmuebles[indice]
    while True:
        clave = input('Ingrese el dato a modificar: ').lower
        for a, b in inmueble:
            if a == clave:
                inmueble[clave] = input('Ingrese modificación: ')
                print(inmueble)
        input('Desea modificar otro ')
    print("Los datos han sido añadidos.")