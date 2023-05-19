'''
Función agregar, sólo sirve para el desafío 4: La Inmobiliaria.
Sólo agrega el inmueble si cumple con las las reglas de validación,
de lo contrario devuelve False y un aviso.
'''
def agregar():
    print('Inserte los datos del inmueble: ')
    inmueble = {}
    inmueble['año'] = int(input('Año: '))
    inmueble['metros'] = int(input('Metros: '))
    inmueble['habitaciones'] = int(input('Habitaciones: '))
    inmueble['garage'] = bool(input('Garage: '))
    inmueble['zona'] = input('Zona: ')
    inmueble['estado'] = input('Estado: ')
    if (inmueble['zona'] in ['A', 'B', 'C'] and 
        inmueble['estado'] in ['Disponible', 'Reservado', 'Vendido'] and
        inmueble['año'] >= 2000 and inmueble['metros'] >= 60 and
        inmueble['habitaciones'] >= 2):
        return inmueble
    else:
        print('El inmueble no cumple con las reglas de validación.')
        return False
