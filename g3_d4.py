'''
Desafío 4: La inmobiliaria
'''
import func_agregar
from func_agregar import agregar
inmuebles = []        #lista con el total de inmuebles

while True:
    print('\nBienvenido/a al sistema de gestión de inmuebles.')
    eleccion = input('1 - Realizar una venta.\n'
                     '2 - Administrar inventario.\n'
                     '3 - Salir del programa.')
    if eleccion == '1':
         print()
    elif eleccion == '2':
        print('Seleccione una opción: ')
        camino = input('1 - Agregar inmueble.\n2 - Editar inmueble.\n'
                       '3 - Eliminar inmueble.\n')
        if camino == '1':
            inmuebles.append(agregar())
            print(inmuebles)
        elif camino == '2':
            print('Ingrese los datos del inmueble que desea editar:')
        elif camino == '3':
            print('Ingrese los datos del objeto que desea eliminar:')
        else:
            print('No ha seleccionado un número válido, inténtelo de nuevo.')
            continue
    elif eleccion == '3':
        print('Gracias por utilizar Sistema de Gestión de Inmuebles.')
        break
    


