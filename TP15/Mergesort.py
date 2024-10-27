def mergesort(lista):
    if len(lista) <= 1:
        return lista

    medio = len(lista) // 2
    izquierda = lista[:medio]
    derecha = lista[medio:]

    izquierda = mergesort(izquierda)
    derecha = mergesort(derecha)

    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    res = []
    i = 0
    j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            res.append(izquierda[i])
            i += 1
        else:
            res.append(derecha[j])
            j += 1

    res.extend(izquierda[i:])
    res.extend(derecha[j:])
    return res

lista = [4, 7, 2, 8, 1, 3, 5]
print("La lista ordenada es:", mergesort(lista))