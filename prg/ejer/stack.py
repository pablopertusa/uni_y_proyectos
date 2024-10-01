class Stack:
    def __init__(self):
        self.items = []
    def apilar(self, elem):
        self.items.append(elem)
    def desapilar(self):
        if not self.esVacia():
            return self.items.pop()
        else:
            return False
    def esVacia(self):
        return (len(self.items) == 0)
    

def bienParentizada(cadena):
    abrir = ['(','[','{']
    cerrar = [')',']','}']
    pila = Stack()
    for elem in cadena:
        if elem in abrir:
            pila.apilar(elem)
        if elem in cerrar:
            if elem == ')':
                a = pila.desapilar()
                if a != '(':
                    return False
            if elem == ']':
                a = pila.desapilar() 
                if a != '[':
                    return False
            if elem == '}':
                a = pila.desapilar() 
                if a != '{':
                    return False
    return pila.esVacia()

class colaCircular:
    def __init__(self, inicio = 10):
        self._items = [None]*inicio
        self._first = 0
        self._size = 0

    def esVacia(self):
        return self._size == 0
    
    def encolar(self, elem):
        pos_next = (self._first  + self._size) % len(self._items)
        self.items[pos_next] = elem
        self._size += 1
    
    def desencolar(self):
        valor = self._items[self._first]
        self._items[self._first] = None
        self._size -= 1
        self._first = (self._first + 1) % len(self._items)
        return valor

                