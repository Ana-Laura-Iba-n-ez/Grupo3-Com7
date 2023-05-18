'''
Función agregar, sólo sirve para el desafío 4: La Inmobiliaria.
'''
def agregar():
    print('Inserte los datos del inmueble: ')
    inmueble = {}
    inmueble['año'] = input('Año: ')
    inmueble['metros'] = input('Metros: ')
    inmueble['habitaciones'] = input('Habitaciones: ')
    inmueble['garage'] = bool(input('Garage: '))
    inmueble['zona'] = input('Zona: ')
    inmueble['estado'] = input('Estado: ')
    return inmueble
