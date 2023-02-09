listaV = []


def ordenar(lista):
    for i in range(len(lista)):
        menor_indice = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[menor_indice]:
                menor_indice = j
        lista[i], lista[menor_indice] = lista[menor_indice], lista[i]
    return lista


for n in range(5):
    texto = str(input('Digite uma fruta: '))
    listaV.append(texto)
    ordenar(listaV)
print(listaV)
