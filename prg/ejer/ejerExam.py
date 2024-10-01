def cantidad_primos(desde, hasta):
    if desde > hasta:
        return 0
    else:
        if es_primo(desde):
            return 1+cantidad_primos(desde+1, hasta)
        else:
            return cantidad_primos(desde+1, hasta)
        
def es_primo(x):
    pass
        
def paratodos(lista, funcion, ini=0):
    if ini >= len(lista):
        return True
    else:
        if funcion(lista[ini]):
            return paratodos(lista, funcion, ini+1)
        else:
            return False

def esPar(x):
    return x%2 == 0

lista = [0,0,2,4,6,8]
print(paratodos(lista, esPar))