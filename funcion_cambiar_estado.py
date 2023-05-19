import funcion_agregar
from funcion_agregar import agregar

def cambiar_estado(inmuebles):
    print('Cambio del estado de un inmueble: ')
    buscar = agregar()
    for inmueble in inmuebles:
        if inmueble == buscar:
            print(f'Este inmueble coincide con todos los campos.')
            print(inmueble)
            nuevo_estado = input('Ingrese el nuevo estado del inmueble: ')
            inmueble['estado'] = nuevo_estado
            print('El estado del inmueble ha sido actualizado.')
            print(inmueble)
            break
    else:
        print('No se encontró un inmueble que coincida con los datos proporcionados.')