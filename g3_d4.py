'''
Desafío 4: La inmobiliaria
'''
import funcion_agregar
from funcion_agregar import agregar
import inmueble_por_presupuesto
from inmueble_por_presupuesto import buscar_por_presupuesto
import funcion_eliminar
from funcion_eliminar import eliminar
import funcion_cambiar_estado
from funcion_cambiar_estado import cambiar_estado

inmuebles = []        #lista con el total de inmuebles

while True:
    print('\nBienvenido/a al Sistema de Gestión de Inmuebles.')
    eleccion = input('1 - Cambiar estado de un inmueble.\n'
                     '2 - Buscar inmuebles por presupuesto.\n'
                     '3 - Administrar inventario.\n'
                     '4 - Salir del programa.\n')
    if eleccion == '1':
        cambiar_estado(inmuebles)
    elif eleccion == '2':
        precio = int(input('Ingrese el presupuesto disponible: '))
        print(buscar_por_presupuesto(inmuebles, precio))
    elif eleccion == '3':
        print('Seleccione una opción: ')
        inventario = input('1 - Agregar inmueble.\n2 - Editar inmueble.\n'
                           '3 - Eliminar inmueble.\n')
        if inventario == '1':
            seguir = True
            while seguir:
                inmuebles.append(agregar())
                for i in inmuebles:
                    if i == False:
                        inmuebles.pop()
                agregar_otro = input('Desea agregar otro inmueble? s/n: ')
                if agregar_otro == 'n':
                    seguir = False
        elif inventario == '2':
            print('Ingrese los datos del inmueble que desea editar:')
        elif inventario == '3':
            eliminar(inmuebles)
        else:
            print('No ha seleccionado un número válido, inténtelo de nuevo.')
            continue
    elif eleccion == '4':
        print('Gracias por utilizar Sistema de Gestión de Inmuebles.')
        break
    
# INTEGRANTES
# Ibañez, Ana Laura.
# Zalazar, Francisco Ezequiel.
# Messa Torres, María Salomé.
# Bentolila, Isaac.
# Sanchez, Ramon Victor.


