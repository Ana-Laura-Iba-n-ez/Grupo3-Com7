'''
Funcion para que, con un presupuesto dado, se obtenga una lista con los
inmuebles que estén disponibles.
'''
import funcion_calcular_precio
from funcion_calcular_precio import calcular_precio

def buscar_por_presupuesto(inmuebles):
    presupuesto = int(input('Ingrese el monto del presupuesto: '))
    en_presupuesto = []
    for inmueble in inmuebles:
        if (calcular_precio(inmueble) <= presupuesto and 
            inmueble ['estado'] in ['Disponible', 'Reservado']):
         en_presupuesto.append(inmueble)
    return en_presupuesto
