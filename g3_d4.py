'''
Desafío 4: La inmobiliaria
'''
import func_agregar
from func_agregar import agregar
inmuebles = []        #lista con el total de inmuebles

while True:
    print('\nBienvenido/a al sistema de gestión de inmuebles.')
    venta_o_inventario = input('1 - Realizar una venta.\n'
                               '2 - Administrar inventario.\n')
    if venta_o_inventario == '1':
         print()
    elif venta_o_inventario == '2':
        print('Seleccione una opción: ')
        camino = input('1 - Agregar inmueble.\n2 - Editar inmueble.\n'
                       '3 - Eliminar inmueble.\n')
        if camino == '1':
            inmuebles.append(agregar())
            print(inmuebles)

