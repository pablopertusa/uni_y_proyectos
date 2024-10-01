class BST:

    class _Node:
        def __init__(self, key, value, left=None, right=None):
            self._key = key
            self._value = value
            self._left = left
            self._right = right
            
    def __init__(self): # create empty binary tree
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    # VERSION RECURSIVA DE GETITEM, SOLAMENTE SE HA VISTO LA ITERATIVA:
    def __aux_getitem__(self, node, key):
        if node is None:
            raise KeyError("Key Error: " + repr(key))
        elif key == node._key:
            return node._value
        elif key < node._key:
            return self.__aux_getitem__(node._left, key)
        else:
            return self.__aux_getitem__(node._right, key)

    def __getitem__(self, key):
        return self.__aux_getitem__(self._root, key)

    # VERSION ITERATIVA DE GETITEM, LA QUE HEMOS VISTO:
    def __getitem__(self, key):
        node = self._root
        while node is not None:
            if key == node._key:
                return node._value
            elif key < node._key:
                node = node._left
            else:
                node = node._right
        raise KeyError("Key Error: " + repr(key))

    def __contains__(self, key):
        node = self._root
        while node is not None:
            if key == node._key:
                return True
            elif key < node._key:
                node = node._left
            else:
                node = node._right
        return False

    def __setitem__(self, key, value):
        prev, node = None, self._root
        while node is not None:
            prev = node
            if key == node._key:
                node._value = value
                return
            elif key < node._key:
                node = node._left
            else:
                node = node._right
        newchild = BST._Node(key, value)
        self._size += 1
        if prev is None:
            self._root = newchild
        elif key < prev._key:
            prev._left = newchild
        else:
            prev._right = newchild

    def setdefault(self,key, default):
        prev = None
        node = self._root
        while node is not None:
            prev = node
            if key == node._key:
                return node._value
            elif key < node._key:
                node = node._left
            else:
                node = node._right
        newchild = BST._Node(key, default)
        self._size += 1
        if prev is None:
            self._root = newchild
        elif key < prev._key:
            prev._left = newchild
        else:
            prev._root = newchild

    def find_min(self):
        node = self._root
        if node is None:
            return None
        while node._left is not None:
            node = node._left
        return (node._key, node._value)

    def find_max(self):
        node = self._root
        if node is None:
            return None
        while node._right is not None:
            node = node._right
        return (node._key, node._value)

    def _find_lt_rec(self, node, key):
        if node is not None:
            if node._key < key:
                resul = self._find_lt_rec(node._right, key)
                if resul is not None:
                    return resul
                return (node._key, node._value)
            return self._find_lt_rec(node._left, key)
            
    def find_lt(self, key): # predecesor
        return self._find_lt_rec(self._root, key)
    
    def _find_gt_rec(self, node, key):
        if node is not None:
            if node._key > key:
                resul = self._find_gt_rec(node._left, key)
                if resul is not None:
                    return resul
                return (node._key, node._value)
            return self._find_gt_rec(node._right, key)
            
    def find_gt(self, key): # sucesor
        return self._find_gt_rec(self._root, key)
    
    def __delitem__ (self, key):
        prev, node = None, self._root
        while node is not None and node._key != key:
            prev = node
            if key <  node._key:
                node = node._left
            else:
                node = node._right
        if node is None: # key not found
            raise KeyError("Key Error: " + repr(key))
        # key has been found, we have to remove it
        self._size -= 1
        if node._left is None or node._right is None:
             # one child of a leaf
            if node._left is not None:
                replace = node._left
            else:
                replace = node._right
            if prev is None:
                self._root = replace
            elif prev._left == node:
                prev._left = replace
            else:
                prev._right = replace
        else: # two children
            # el mínimo de su subárbol derecho ocupa su lugar:
            parentmin, themin = node, node._right
            while themin._left is not None:
                parentmin, themin = themin, themin._left
            node._key, node._value = themin._key, themin._value
            # remove themin:
            if parentmin._left == themin:
                parentmin._left = themin._right
            else:
                parentmin._right = themin._right

    def _inorder_traversal(self, node):
        if node is not None:
            yield from self._inorder_traversal(node._left)
            yield node
            yield from self._inorder_traversal(node._right)
                
    def __iter__(self): # recorre claves, lo que se ejecuta si iteras self
        for node in self._inorder_traversal(self._root):
            yield node._key
            
    def items(self): # recorre pares (tuplas) clave, valor
        for node in self._inorder_traversal(self._root):
            yield (node._key, node._value)

    # mostrar árbol como diccionario python
    def __repr__(self):
        return "{" + ",".join(repr(k)+':'+repr(v) for k,v in self.items()) + "}"

    
    # mostrar árbol como árbol como nodos y Nones
    # ejemplo: '[15:15]([5:5]([3:3](None,None),[12:12]([10:10]([6:6](None,[7:7](None,None)),None),[13:13](None,None))),[16:16](None,[20:20]([18:18](None,None),[23:23](None,None))))'
    def __aux_repr_tree__(self, node):
        if node is None:
            return 'None'
        return ('['+repr(node._key)+":"+repr(node._value) + '](' +
                self.__aux_repr_tree__(node._left)    + ',' +
                self.__aux_repr_tree__(node._right)   + ')')
    
    # mostrar árbol como árbol mediante parentizado
    # ejemplo: '15(5(3(,),12(10(6(,7(,)),),13(,))),16(,20(18(,),23(,))))'
    def __aux_repr_tree__(self, node):
        if node is None:
            return ''
        return (repr(node._key) + '(' +
                self.__aux_repr_tree__(node._left)    + ',' +
                self.__aux_repr_tree__(node._right)   + ')')
        
    def __repr_tree__(self):
        return self.__aux_repr_tree__(self._root)
    

    #EJERCICIOS
    def search_with_path(self, key):
        if self._root is not None:
            recorrido = []
            nodo = self._root
            while nodo != None and key != nodo._key:
                if nodo._key < key:
                    recorrido.append(nodo._key)
                    nodo = nodo._right
                else:
                    recorrido.append(nodo._key)
                    nodo = nodo._left
            if nodo is None:
                return recorrido
            else:
                recorrido.append(nodo._key)
                return recorrido
        else:
            return []
    def isBST_aux(self, nodo):
        if nodo._left is not None and nodo._right is None:
            izq = nodo._left
            if izq._key > nodo._key:
                return False
            else:
                return self.isBST_aux(izq)
        if nodo._right is not None and nodo._left is None:
            der = nodo._right
            if der._key < nodo._key:
                return False
            else:
                return self.isBST_aux(der)
        if nodo._right is not None and nodo._left is not None:
            izq = nodo._left
            der = nodo._right
            if izq._key > nodo._key or der._key < nodo._key:
                return False
            else:
                return self.isBST_aux(der) and self.isBST_aux(izq)
        if nodo._right is None and nodo._left is None:
            return True
        
    def isBST(self):
        return self.isBST_aux(self._root)
    
    def __eq__(self, otro):
        if isinstance(otro, BST):
            if len(self) == len(otro):
                for (key, value) in self.items():
                    if key in otro:
                        if otro[key] != value:
                            return False
                    else:
                        return False
                return True
            else:
                return False
        else:
            return False

    def identical(self, otro):
        if isinstance(otro, BST):
            return self.preorden() == otro.preorden()
        else:
            return False
        
    def preorden(self):
        return self.preorden_aux(self._root)
    
    def preorden_aux(self, nodo):
        if nodo._left is None and nodo._right is None:
            return [nodo._key]
        if nodo._left is None and nodo._right is not None:
            return [nodo._key] + self.preorden_aux(nodo._right)
        if nodo._left is not None and nodo._right is None:
            return [nodo._key] + self.preorden_aux(nodo._left)
        if nodo._left is not None and nodo._right is not None:
            return [nodo._key] + self.preorden_aux(nodo._left) + self.preorden_aux(nodo._right)
        
    def lca(self, key1, key2):
        recorrido = self.search_node_with_path(key1)
        recorrido = list(reversed(recorrido))
        for nodo in recorrido:
            if self.estaPorDebajo(key2, nodo._right):
                return nodo


    def estaPorDebajo(self, key, nodo):
        node = nodo
        while node is not None:
            if key == node._key:
                return True
            elif key < node._key:
                node = node._left
            else:
                node = node._right
        return False

    def search_node_with_path(self, key):
        if self._root is not None:
            recorrido = []
            nodo = self._root
            while nodo != None and key != nodo._key:
                if nodo._key < key:
                    recorrido.append(nodo)
                    nodo = nodo._right
                else:
                    recorrido.append(nodo)
                    nodo = nodo._left
            if nodo is None:
                return recorrido
            else:
                recorrido.append(nodo)
                return recorrido
        else:
            return []
        
    def countRep(self, nodo):
        return self.countRep_aux(nodo._left, key=nodo._key)
    
    def countRep_aux(self, nodo, key):
        if nodo is None:
            return 0
        else:
            if nodo._left is None and nodo._right is None:
                if nodo._key == key:
                    return 1
                else:
                    return 0
            if nodo._left is None and nodo._right is not None:
                if nodo._key == key:
                    return 1
                else:
                    return 0 + self.countRep_aux(nodo._right, key)
            if nodo._left is not None and nodo._right is None:
                if nodo._key == key:
                    return 1 + self.countRep_aux(nodo._left, key)
                else:
                    return 0 + self.countRep_aux(nodo._left, key)
            if nodo._left is not None and nodo._right is not None:
                if nodo._key == key:
                    return 1 + self.countRep_aux(nodo._left, key)
                else:
                    return 0 + self.countRep_aux(nodo._right, key) + self.countRep_aux(nodo._left, key)

    def caminoQueSuma(self, valor):
        return self.caminoQueSuma_aux(valor, self._root)
    
    def caminoQueSuma_aux(self, valor, nodo, suma=0):
        if nodo is not None:
            if suma == valor:
                return True
            else:
                return self.caminoQueSuma_aux(valor, nodo._left, suma=suma+nodo._key) or self.caminoQueSuma_aux(valor, nodo._right, suma=suma+nodo._key)
        else:
            if suma == valor:
                return True
            else:
                return False
            
    def tamaño(self):
        if self._root is not None:
            return 1 + self.tamaño_aux(self._root)
        else:
            return 0

    def tamaño_aux(self, nodo):
        if nodo._left is not None and nodo._right is None:
            return 1 + self.tamaño_aux(nodo._left)
        if nodo._left is None and nodo._right is None:
            return 0
        if nodo._left is not None and nodo._right is not None:
            return 2 + self.tamaño_aux(nodo._left) + self.tamaño_aux(nodo._right)
        if nodo._left is None and nodo._right is not None:
            return 1 + self.tamaño_aux(nodo._right)
        


    def tallaSubarbol(self, n):
        def contarNodos(nodo):
            if nodo._left == None:
                if nodo._right == None:
                    return 1
                else:
                    return 1 + contarNodos(nodo._right)
            elif nodo._right == None:
                if nodo._left is not None:
                    return 1 + contarNodos(nodo._left)
            elif nodo._right is not None and nodo._left is not None:
                return 1 + contarNodos(nodo._right) + contarNodos(nodo._left)
    
        seguir = True
        nodo = self._root
        while seguir:
            if nodo is None:
                return 0
            elif nodo._key < n:
                nodo = nodo._right
            elif nodo._key > n:
                nodo = nodo._left
            else:
                seguir = False
        return contarNodos(nodo)
    

    def hijosIzq(self):
        lista = []
        def hijosIzq_aux(nodo, lista):
            if nodo._left is not None:
                lista.append(nodo._left._key)
                hijosIzq_aux(nodo._left, lista)
            if nodo._right is not None:
                hijosIzq_aux(nodo._right, lista)
            return lista
        return hijosIzq_aux(self._root, lista)
    
    def imprimirBajadas(self):
        def imprimirBajadas_aux(nodo, izq, der):
            if nodo._left is not None:
                imprimirBajadas_aux(nodo._left, izq+1, der)
            print(izq, der, nodo._key)
            if nodo._right is not None:
                imprimirBajadas_aux(nodo._right, izq, der+1)

        return imprimirBajadas_aux(self._root, 0, 0)
    
    def contarBajadaEquilibrada(self):
        def contarBajadaEquilibrada_aux(nodo, izq, der):
            if nodo is not None:
                if izq == der:
                    return 1 + contarBajadaEquilibrada_aux(nodo._left, izq+1, der) + contarBajadaEquilibrada_aux(nodo._right, izq, der+1)
                else:
                    return contarBajadaEquilibrada_aux(nodo._left, izq+1, der) + contarBajadaEquilibrada_aux(nodo._right, izq, der+1)
            return 0

        return contarBajadaEquilibrada_aux(self._root, 0, 0)
    
    def clasifica(self, hoja, clasificado):
        def buscar(nodo, valor):
            if nodo is not None:
                if nodo._key == valor:
                    return True
                return buscar(nodo._left, valor) or buscar(nodo._right, valor)
            return False

        def clasifica_aux(hoja, clasificado, nodo):
            if nodo._key == clasificado:
                return 'rec'
            if nodo is not None:
                if nodo._key < hoja:
                    if buscar(nodo._left, clasificado):
                        return 'izq'
                    else:
                        return clasifica_aux(hoja, clasificado, nodo._right)
                elif nodo._key > hoja:
                    if buscar(nodo._right, clasificado):
                        return 'der'
                    else:
                        return clasifica_aux(hoja, clasificado, nodo._left)
                else:
                    return 'rec'
        return clasifica_aux(hoja, clasificado, self._root)
    

            
def ordenar(vector):
    if all([isinstance(x,int) for x in vector]):
        arbol = BST()
        ordenado = []
        for i in vector:
            arbol[i] = i
        for x in arbol:
            ordenado.append(x)
        return ordenado
    else:
        return False
    
    



if __name__ == '__main__':
    bst = BST()
    for i in [40, 25, 70, 4, 32, 54, 92, 27, 34, 41, 61, 80, 94, 58]:
        bst[i] = i
    print(bst.clasifica(41, 54))

