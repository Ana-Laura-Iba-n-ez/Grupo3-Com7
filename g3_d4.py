'''
Desafío 4: La inmobiliaria
FALTAN:
Modificar la funcion agregar para que sólo acepte un mueble si cuenta con las
reglas de validación.
Función editar.
Función eliminar.
acciones para vender.
funcion calcular precio.
Lo que falte de las consignas.
'''
import funcion_agregar
from funcion_agregar import agregar
inmuebles = []        #lista con el total de inmuebles

while True:
    print('\nBienvenido/a al Sistema de Gestión de Inmuebles.')
    eleccion = input('1 - Cambiar estado de un inmueble.\n'
                     '2 - Buscar inmuebles por presupuesto.\n'
                     '2 - Administrar inventario.\n'
                     '3 - Salir del programa.\n')
    if eleccion == '1':
        print('Cambio del estado de un inmueble: ')
        print('Inserte los datos del inmueble: ')
        buscar = agregar()
<<<<<<< HEAD
        for i in inmuebles:
            if i in buscar:
                print(f'El inmueble numero{inmuebles.index(buscar)}'
                      'coincide con todos los campos')
                vender = input('Desea cambiar el estado a "vendido"? s/n: ')
                

=======
        indice = None
        for i, inmueble in enumerate(inmuebles):
            if inmueble == buscar:
                print(f'El inmueble número {i} coincide con todos los campos.')
                nuevo_estado = input('Ingrese el nuevo estado del inmueble: ')
                inmuebles[i]['estado'] = nuevo_estado
                print('El estado del inmueble ha sido actualizado.')
                indice = i
                break
        if indice is None:
            print('No se encontró un inmueble que coincida con los datos proporcionados.')
>>>>>>> 2758dcdb7cbad1ef1bcfec2b9e92d8951b85e27c
    elif eleccion == '2':
        print()
    elif eleccion == '3':
        print('Seleccione una opción: ')
        inventario = input('1 - Agregar inmueble.\n2 - Editar inmueble.\n'
                           '3 - Eliminar inmueble.\n')
        if inventario == '1':
            inmuebles.append(agregar())
            for i in inmuebles:
                if i == False:
                    inmuebles.pop()
        elif inventario == '2':
            print('Ingrese los datos del inmueble que desea editar:')
        elif inventario == '3':
            print('Ingrese los datos del objeto que desea eliminar:')
        else:
            print('No ha seleccionado un número válido, inténtelo de nuevo.')
            continue
    elif eleccion == '4':
        print('Gracias por utilizar Sistema de Gestión de Inmuebles.')
        break
    


