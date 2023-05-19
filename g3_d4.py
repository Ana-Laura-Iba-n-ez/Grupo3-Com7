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
import func_agregar
from func_agregar import agregar
inmuebles = []        #lista con el total de inmuebles

while True:
    print('\nBienvenido/a al Sistema de Gestión de Inmuebles.')
    eleccion = input('1 - Realizar una venta.\n'
                     '2 - Administrar inventario.\n'
                     '3 - Salir del programa.\n')
    if eleccion == '1':
         print()
    elif eleccion == '2':
        print('Seleccione una opción: ')
        inventario = input('1 - Agregar inmueble.\n2 - Editar inmueble.\n'
                           '3 - Eliminar inmueble.\n')
        if inventario == '1':
            inmuebles.append(agregar())
            print(inmuebles)
            for i in inmuebles:
                if i == False:
                    inmuebles.pop()
                    print(inmuebles)
        elif inventario == '2':
            print('Ingrese los datos del inmueble que desea editar:')
        elif inventario == '3':
            print('Ingrese los datos del objeto que desea eliminar:')
        else:
            print('No ha seleccionado un número válido, inténtelo de nuevo.')
            continue
    elif eleccion == '3':
        print('Gracias por utilizar Sistema de Gestión de Inmuebles.')
        break
    


