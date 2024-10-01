class MinHeap:
    def __init__(self, initial=()):
        self._data = [v for v in initial]
        self._buildheap()

    def __len__(self):
        return len(self._data)

    def _heapify(self, pos):
        d = self._data # para simplificar la escritura
        size = len(d)  # para simplificar la escritura
        child_pos = 2*pos + 1 # posición del hijo izquierdo
        if child_pos < size: # existe hijo izquierdo
            # determinar el menor de los hijos:
            if child_pos+1 < size and d[child_pos+1] < d[child_pos]:
                # usaremos la posición del hijo derecho
                child_pos += 1
            # child_pos tiene la posición del menor de los hijos
            if d[pos] > d[child_pos]:
                # intercambiamos con el hijo
                d[pos],d[child_pos] = d[child_pos],d[pos]
                self._heapify(child_pos)

    def _buildheap(self):
        # se trata de ir aplicando _heapify a cada elemento desde el
        # último que tenga hijos hacia atrás hasta llegar a la raíz:
        if len(self._data) > 1: # no hace falta en otro caso
            ultimo_indice = len(self._data)-1
            padre_ultimo = (ultimo_indice-1)//2
            for pos in range(padre_ultimo, -1, -1): # hacia atras hasta 0
                self._heapify(pos)

    def min(self):
        if len(self._data) == 0:
            raise KeyError('MinHeap is empty.')
        return self._data[0]
    
    def remove_min(self):
        if len(self._data) == 0:
            raise KeyError('MinHeap is empty.')
        themin = self._data[0] # el que vamos a devolver
        last = self._data.pop() # quitamos el último
        if len(self._data) > 0: # si había > 1
            self._data[0] = last # sustituimos el 1º por el último
            self._heapify(0) # restaurar propiedad de heap
        return themin # devolvemos el mínimo
    


    def add(self, value):
        d = self._data # para simplificar la escritura:
        d.append(value) # añadimos el nuevo elemento
        pos = len(d)-1 # índice del nuevo elemento
        parent_pos = (pos-1)//2 # índice de su padre
        while (pos > 0 and d[pos] < d[parent_pos]):
            # los intercambiamos:
            d[pos], d[parent_pos] = d[parent_pos], d[pos]
            # y subimos
            pos = parent_pos
            parent_pos = (pos-1)//2 # índice de su padre
            

    def __repr__(self):
        return repr(self._data)


    #EJERCICIOS
    def isHeap(self):
        d = self._data
        padre_ult = (len(d)-2)//2
        for pos in range(padre_ult, -1, -1):
            if d[2*pos+1] < d[pos]:
                    return False
            if 2*pos+2 <= len(d)-1:
                if d[2*pos+2] < d[pos]:
                    return False
                
        return True
    
    def maxValue(self):
        if len(self._data) > 0:
            primer_padre = ((len(self._data)-1)-1)//2
            resul = max(self._data[primer_padre+1:])
            return resul
        else:
            return None


    def _refloat(self, pos): # supone 0<=pos<len(self._data)
        d = self._data # para simplificar la escritura:
        parent_pos = (pos-1)//2 # índice de su padre
        while (pos > 0 and d[pos] < d[parent_pos]):
        # los intercambiamos:
            d[pos], d[parent_pos] = d[parent_pos], d[pos]
            # y subimos
            pos = parent_pos
            parent_pos = (pos-1)//2 # índice de su padre

    def remove_max(self):
        pos = ((len(self._data)-1)-1)//2
        max = self.maxValue()
        pos_max = 0
        while pos <= len(self._data)-1:
            if self._data[pos] == max:
                pos_max = pos
            pos += 1
        if pos_max == len(self._data)-1:
            self._data.pop()
        else:
            self._data[pos_max] = self._data[-1]
            last = self._data.pop()
            self._refloat(pos_max)
        return max
    
    def count(self, x):
        def count_aux(pos, x):
            if pos < len(self._data)-1:
                if self._data[pos] == x:
                    return 1 + count_aux(2*pos+1, x) + count_aux(2*pos+2, x)
                elif self._data[pos] > x:
                    return 0
                else:
                    return count_aux(2*pos+1, x) + count_aux(2*pos+2, x)
            return 0


        return count_aux(0,x)
    
    def __contains__(self, x):
        def contains_aux(pos, x):
            if pos <= len(self._data)-1:
                if self._data[pos] == x:
                    return True
                elif self._data[pos] > x:
                    return False
                else:
                    return contains_aux(2*pos+1, x) or contains_aux(2*pos+2, x)

        return contains_aux(0, x)
    
    def rangoValido(self, pos):
        if len(self) == 0 or len(self) == 1:
            return (None, None)
        else:
            if pos < 0 or pos > len(self)-1:
                return (None, None)
            else:
                if (pos-1)//2 < 0:
                    limiteInf = None
                else:
                    limiteInf = self._data[(pos-1)//2]
                if 2*pos+1 > len(self)-1:
                    limiteSup = None
                else:
                    if 2*pos+2 <= len(self)-1:
                        limiteSup = min(self._data[2*pos+1], self._data[2*pos+2])
                    else:
                        limiteSup = self._data[2*pos+1]
            return (limiteInf, limiteSup)


    def caminoMenorHoja(self):
        if len(self) > 1:
            min = self._data[-1]
            pos = -1
            resul = []
            for i in range((len(self)-1)//2+1, len(self)):
                if self._data[i] < min:
                    min = self._data[i]
                    pos = i

            while pos >= 0:
                resul.append(self._data[pos])
                pos = (pos-1)//2
            resul = list(reversed(resul))
            return resul
            

        else:
            if len(self) == 1:
                return self._data[0]
            else:
                return None
            
    def hermano(self, pos):
        if pos > 0:
            padre = (pos-1)//2
            if 2*padre+1 == pos:
                if 2*padre+2 <= len(self)-1:
                    return 2*padre+2
                else:
                    return None
            else:
                return 2*pos+2
        else:
            return None
        
    def modifica(self, indice, valor):
        if indice >= 0 and indice < len(self._data):
            padre = (indice-1)//2
            if self._data[padre] > valor:
                return False
            hijoIzq = 2*indice+1
            hijoDer = 2*indice+2
            if hijoIzq < len(self._data):
                if self._data[hijoIzq] < valor:
                    return False
            if hijoDer < len(self._data):
                if self._data[hijoDer] < valor:
                    return False
            self._data[indice] = valor
            return True
        return False
                


def nMayores(v, n):
    minheap = MinHeap()
    cont = 0
    for i in v:
        if cont < n:
            minheap.add(i)
            cont += 1
        else:
            if minheap.min() < i:
                minheap.remove_min()
                minheap.add(i)
    resul = minheap._data
    return resul



v = [1,2,10,10,5,17,56,7,8,9,10,45]
minheap = MinHeap(v)
print(minheap)
print(minheap.caminoMenorHoja())