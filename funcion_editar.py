'''
Función para editar un inmueble de la lista
'''
def editar(inmuebles):
    print(inmuebles)
    while True:
        indice = int(input("Ingrese el índice del inmueble a editar: "))
        if indice < 0 or indice >= len(inmuebles):
            print("El índice del inmueble a eliminar no es válido.")
        else:
            print(f'El inmueble seleccionado es el siguiente: \n{inmuebles[indice]}')
        continuar = True
        while continuar:
            clave = input('¿Qué elemento del inmueble desea editar? ')
            valor = inmuebles[indice].get(clave)
            if valor == None:
                print(f'El elemento {clave} no existe en el inmueble.')
            else:
                print(f'El valor actual de {clave} es {valor}.')
                nuevo_valor = input(f'Ingrese el nuevo valor que desea asignarle a {clave}: ')
                inmuebles[indice][clave] = nuevo_valor
            opcion = input('¿Desea modificar otro valor? s/n: ')
            if opcion.lower() != 's':
                continuar = False
        return print(f'El inmueble ha sido modificado correctamente, quedando de la siguiente manera: \n{inmuebles[indice]}')
    

editar([{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
{'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
{'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
{'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
{'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}])