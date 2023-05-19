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
import inmueble_por_presupuesto
from inmueble_por_presupuesto import buscar_por_presupuesto
import funcion_eliminar
from funcion_eliminar import eliminar

inmuebles = []        #lista con el total de inmuebles
inmuebles = [{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
{'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
{'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
{'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
{'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}] 

while True:
    print('\nBienvenido/a al Sistema de Gestión de Inmuebles.')
    eleccion = input('1 - Cambiar estado de un inmueble.\n'
                     '2 - Buscar inmuebles por presupuesto.\n'
                     '3 - Administrar inventario.\n'
                     '4 - Salir del programa.\n')
    if eleccion == '1':
        print('Cambio del estado de un inmueble: ')
        buscar = agregar()
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
    elif eleccion == '2':
        buscar_por_presupuesto(inmuebles)
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
            eliminar(inmuebles)
        else:
            print('No ha seleccionado un número válido, inténtelo de nuevo.')
            continue
    elif eleccion == '4':
        print('Gracias por utilizar Sistema de Gestión de Inmuebles.')
        break
    


