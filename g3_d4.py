'''
Desafío 4: La inmobiliaria
'''
inmuebles = []        #tupla con el total de inmuebles

while True:
    print('Bienvenido/a al sistema de gestión de inmuebles.')
    venta_o_inventario = input('1 - Realizar una venta.\n'
                               '2 - Administrar inventario.\n')
    if venta_o_inventario == '1':
         print()
    elif venta_o_inventario == '2':
        print('Seleccione una opción: ')
        camino = input('1 - Agregar inmueble.\n2 - Editar inmueble.\n'
                       '3 - Eliminar inmueble.\n')

