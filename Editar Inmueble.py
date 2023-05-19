def editar_inmueble(inmuebles):
    print("Lista de Inmuebles:", inmuebles)
    indice = int(input('Ingrese el numero de indice del inmueble a editar: '))
    inmuebles[indice] = "Atributo"
    print("Los datos han sido añadidos. Verifique que todo este correcto.", inmuebles)