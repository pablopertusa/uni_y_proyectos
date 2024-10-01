def secuencia_es_BST(lista):
    if len(lista) > 1:
        if lista[1] >= lista[0]:
            if all([x>=lista[0] for x in lista]):
                return secuencia_es_BST(lista[1:])
            else:
                return False
        else:
            if all([x<=lista[0] for x in lista]):
                return secuencia_es_BST(lista[1:])
            else:
                return False
    else:
        return True

lista = [935, 278, 347, 621, 299, 392, 358, 363]
print(secuencia_es_BST(lista))