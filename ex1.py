def ordenar(lista):
    for i in range(len(lista)):
        menor_indice = i
        for j in range(i + 1, len(lista)):
            if lista[j] > lista[menor_indice]:
                menor_indice = j
        lista[i], lista[menor_indice] = lista[menor_indice], lista[i]
    return lista

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ordenar(lista)
print(lista)
