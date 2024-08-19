def busqueda_binaria(lista, elemento):
    lista.sort()

    izq = 0

    der = len(lista) - 1

    while izq <= der:
        medio = (izq + der) // 2

        if lista[medio] == elemento:
            return medio
        
        elif lista[medio] < elemento:
            izq = medio + 1

        else:
            der = medio - 1 

    return -1

elemento = int(input("Ingrese el Nº que desea buscar:"))
lista = [1,3,45,2,4,5]

resultado = busqueda_binaria(lista, elemento)
print(f"El elemento {elemento} esta en el indice: {resultado}")
