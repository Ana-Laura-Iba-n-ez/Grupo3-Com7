<<<<<<< HEAD
# Función para eliminar un inmueble de la lista

inmuebles = []

=======
'''
Función para eliminar un inmueble de la lista
'''
>>>>>>> 2758dcdb7cbad1ef1bcfec2b9e92d8951b85e27c
def eliminar(inmuebles):
    indice = int(input("Ingrese el índice del inmueble a eliminar: "))

    if indice < 0 or indice >= len(inmuebles):
        print("El índice del inmueble a eliminar no es válido.")
        return
    del inmuebles[indice]
<<<<<<< HEAD
=======


>>>>>>> 2758dcdb7cbad1ef1bcfec2b9e92d8951b85e27c
