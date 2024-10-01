def ejer1(vector):
    def ejer1_aux(vector, inicio, final):
        puntoMedio = (inicio + final)//2
        if vector[puntoMedio-1] < vector[puntoMedio] > vector[puntoMedio+1]:
            return puntoMedio
        elif vector[puntoMedio-1] < vector[puntoMedio] < vector[puntoMedio+1]:
            return ejer1_aux(vector, puntoMedio, final)
        elif vector[puntoMedio-1] > vector[puntoMedio] > vector[puntoMedio+1]:
            return ejer1_aux(vector, inicio, puntoMedio)
        else:
            return 'vector mal hecho'
        
    
    return ejer1_aux(vector, 0, len(vector)-1)


def ejer2(vector, e):
    def ejer2_aux(vector, e, inicio, final):
        puntoMedio = (inicio + final)//2
        if inicio == final:
            if e > vector[final]:
                return None
            elif e < vector[inicio]:
                return vector[inicio]
        if vector[puntoMedio] < e:
            if vector[puntoMedio+1] > e:
                return vector[puntoMedio+1]
            else:
                return ejer2_aux(vector, e, puntoMedio+1, final)
            
        else:
            if vector[puntoMedio-1] < e:
                return vector[puntoMedio]
            else:
                return ejer2_aux(vector, e, inicio, puntoMedio-1)

    return ejer2_aux(vector, e, 0, len(vector)-1)


def ejer3(vector, x):
    
    def ejer3_aux_izq(vector, x, inicio, final):
        puntoMedio = (inicio + final)//2
        if vector[puntoMedio] == x:
            if vector[puntoMedio-1] != x:
                return puntoMedio
            else:
                return ejer3_aux_izq(vector, x, inicio, puntoMedio-1)
        elif vector[puntoMedio] > x:
            return ejer3_aux_izq(vector, x, inicio, puntoMedio)
        elif vector[puntoMedio] < x:
            return ejer3_aux_izq(vector, x, puntoMedio, final)
            

    def ejer3_aux_der(vector, x, inicio, final):
        puntoMedio = (inicio + final)//2
        if vector[puntoMedio] == x:
            if vector[puntoMedio+1] != x:
                return puntoMedio
            else:
                return ejer3_aux_der(vector, x, puntoMedio+1, final)
        elif vector[puntoMedio] > x:
            return ejer3_aux_der(vector, x, inicio, puntoMedio)
        elif vector[puntoMedio] < x:
            return ejer3_aux_der(vector, x, puntoMedio, final)

    if x not in vector:
        return 0
    
    return ejer3_aux_der(vector, x, 0, len(vector)-1) - ejer3_aux_izq(vector, x, 0, len(vector)-1) + 1



def balanza(vector, i, j, r, s):
    pass

def buscarMoneda(vector):
    def buscarMoneda_aux(vector, inicio, final):
        if len(vector) == 1:
            return inicio
        if len(vector) == 2:
            if balanza(vector, inicio, inicio, final, final) == -1:
                return inicio
            elif balanza(vector, inicio, inicio, final, final) == 1:
                return final
            else:
                return 'algo mal has hecho jefe'
        if len(vector)%2 == 0:
            puntoMedio = (inicio + final)//2
            i, j, r, s = inicio, puntoMedio, puntoMedio+1, final
            if balanza(vector, i, j, r, s) == -1:
                return buscarMoneda_aux(vector, inicio, puntoMedio)
            else:
                return buscarMoneda_aux(vector, puntoMedio, final)
            
        else:
            puntoMedio = (inicio + final)//2
            if balanza(vector, inicio, puntoMedio-1, puntoMedio+1, final) == 0:
                return puntoMedio
            elif balanza(vector, inicio, puntoMedio-1, puntoMedio+1, final) == -1:
                return buscarMoneda_aux(vector, inicio, puntoMedio-1)
            else:
                return buscarMoneda_aux(vector, puntoMedio+1, final)


    return buscarMoneda_aux(vector, 0, len(vector)-1)


def posicionAdicionalRecursiva(a, b, inicio, fin):
    if fin - inicio == 1:
        if a[fin] != b[fin]:
            return inicio
        else:
            return fin
    mitad = (inicio + fin)//2
    if a[mitad] == b[mitad]:
        return posicionAdicionalRecursiva(a, b, mitad, fin)
    else:
        return posicionAdicionalRecursiva(a, b, inicio, mitad)



def posicionAdicional(a, b):
    res = len(a)-1
    if a[-2] != b[-1]:
        return posicionAdicionalRecursiva(a, b, 0, len(b)-1)+1
    return res


def contarDyV(vector):
    d = {}
    def contarDyV_aux(vector, inicio, fin, d):
        if inicio == fin:
            if vector[inicio] in d:
                d[vector[inicio]] += 1
            else:
                d[vector[inicio]] = 1
        elif vector[inicio] == vector[fin]:
            if vector[inicio] in d:
                d[vector[inicio]] += fin-inicio+1
            else:
                d[vector[inicio]] = fin-inicio+1

        else:
            puntoMedio = (inicio+fin)//2
            contarDyV_aux(vector, inicio, puntoMedio, d)
            contarDyV_aux(vector, puntoMedio+1, fin, d)


                
    contarDyV_aux(vector, 0, len(vector)-1, d)
    return d

def contar(creci, decre):
    def contar_aux(creci, decre, inicio, final):
        if inicio == final:
            if creci[inicio] == decre[inicio]:
                return 1
            return 0
        else:
            puntoMedio = (inicio+final)//2
            if creci[puntoMedio] < decre[puntoMedio]:
                return contar_aux(creci, decre, puntoMedio+1, final)
            elif creci[puntoMedio] > decre[puntoMedio]:
                return contar_aux(creci, decre, inicio, puntoMedio-1)
            else:
                return 1 + contar_aux(creci, decre, inicio, puntoMedio-1) + contar_aux(creci, decre, puntoMedio+1, final)


    return contar_aux(creci, decre, 0, len(creci)-1)


def localizar(vector):
    if vector[0] != 'PAR':
        return 0
    elif vector[-1] != 'IMPAR':
        return len(vector)-1
    
    
    def localizar_aux(vector, inicio, fin):
        if inicio == fin - 1:
            return inicio + 1
        puntoMedio = (inicio + fin)//2
        if puntoMedio % 2 == 0:
            if vector[puntoMedio] == 'PAR':
                return localizar_aux(vector, puntoMedio, fin)
            else:
                return localizar_aux(vector, inicio, puntoMedio)
        else:
            if vector[puntoMedio] == 'IMPAR':
                return localizar_aux(vector, puntoMedio, fin)
            else:
                return localizar_aux(vector, inicio, puntoMedio)

    return localizar_aux(vector, 0, len(vector)-1)




print(localizar(['PAR', 'IMPAR', 'PAR', 'IMPAR', 'PAR', 'IMPAR', 'PAR']))
