'''
Función agregar, sólo sirve para el desafío 4: La Inmobiliaria.
Sólo agrega el inmueble si cumple con las las reglas de validación,
de lo contrario devuelve False y un aviso.
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
    if (inmueble['zona'] in ['A', 'B', 'C'] and 
        inmueble['estado'] in ['Disponible', 'Reservado', 'Vendido'] and
        int(inmueble['año']) >= 2000 and int(inmueble['metros']) >= 60 and
        int(inmueble['habitaciones']) >= 2):
        return inmueble
    else:
        print('El inmueble no cumple con las reglas de validación.')
        return False
