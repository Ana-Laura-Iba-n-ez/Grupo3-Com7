'''
Función para eliminar un inmueble de la lista
'''
def eliminar(inmuebles):
    print(inmuebles)
    indice = int(input("Ingrese el índice del inmueble a eliminar: "))
    if indice < 0 or indice >= len(inmuebles):
        print("El índice del inmueble a eliminar no es válido.")
        return
    del inmuebles[indice]
   
    