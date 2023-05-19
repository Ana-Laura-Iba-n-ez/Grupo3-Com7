'''
Función para calcular el precio de un inmueble en función de la zona
'''
def calcular_precio(inmueble):
    precio_base = inmueble["metros"] * 100 + inmueble["habitaciones"] * 500 + int(inmueble["garaje"]) * 1500
    antiguedad = 2023 - inmueble["año"]
    if inmueble["zona"] == "A":
        precio = precio_base * (1 - antiguedad / 100)
    elif inmueble["zona"] == "B":
        precio = precio_base * (1 - antiguedad / 100) * 1.5
    elif inmueble["zona"] == "C":
        precio = precio_base * (1 - antiguedad / 100) * 2
    return precio

# Isaac