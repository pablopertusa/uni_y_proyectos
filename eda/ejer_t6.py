class DiGraph:
    
    def __init__(self):
        # dict associating a list of adjacent edges to each vertex
        # each edge is a tuple (destiny, weight)
        self._adj = {} # (adj from adjacents)

    def number_of_nodes(self): # |V|
        return len(self._adj)

    def nodes(self): # para iterar sobre los vértices
        return self._adj.keys()

    def out_degree(self, u):
        return len(self._adj[u])

    def in_degree(self, u): # VERY costly!
        #return sum(1 for (w,weight) in lst
                   #for lst in self._adj.values() if w == u)
    
        resul = 0
        for lst in self._adj.values():
            for (v, weight) in lst:
                if v == u:
                    resul += 1
        return resul
    
    def number_of_edges(self): # |A|
        return sum(self.out_degree(u) for u in self.nodes())
    
    def add_node(self, u):
        if u not in self._adj:
            self._adj[u] = []

    def add_edge(self, u, v, weight=1):
        # let's assume there is no edge (u,v)
        self.add_node(u) # just in case
        self.add_node(v) # just in case
        self._adj[u].append((v,weight))

    def weight_edge(self, u, v):
        # returns None if there is no such edge (u,v)
        if u in self._adj:
            for w,weight in self._adj[u]:
                if v == w:
                    return weight
                
    #EJERCICIOS
                
    def __iter__(self):
        for node in self._adj:
            for arista, peso in self._adj[node]:
                yield (node, arista, peso)
    
    def __repr__(self):
        aristas = []
        for arista in self:
            aristas.append(arista)
        return str(aristas)

    def squared(self):
        listaCaminos2 = []
        for node in self._adj:
            for arista, peso in self._adj[node]:
                for arista2, peso2 in self._adj[arista]:
                    listaCaminos2.append((node,arista2, peso*peso2))
        resul = {}
        for camino in listaCaminos2:
            if (camino[0], camino[1]) not in resul:
                resul[(camino[0], camino[1])] = camino[2]
            else:
                resul[(camino[0], camino[1])] += camino[2]
        grafoSquared = DiGraph()
        for camino in resul:
            grafoSquared.add_edge(camino[0], camino[1], resul[camino])
        return grafoSquared

    def aristas_comunes(self, grafo):
        if isinstance(grafo, DiGraph):
            aristasPropias = set()
            aristasOtro = set()
            for inicio,destino,peso in self:
                aristasPropias.add((inicio,destino))
            for inicio,destino,peso in grafo:
                aristasOtro.add((inicio,destino))
            resul = aristasPropias.intersection(aristasOtro)
            return resul
        return False
    
    def filtrar_aristas(self, rinferior, rsuperior):
        resul = DiGraph()
        for nodo in self._adj:
            for destino,peso in self._adj[nodo]:
                if peso >= rinferior and peso <= rsuperior:
                    resul.add_edge(nodo,destino,peso)
        return resul
    
    def quitar_sumideros(self):
        sumideros = []
        aux = self._adj.copy()
        for nodo in aux:
            if len(self._adj[nodo]) == 0:
                sumideros.append(nodo)
                del self._adj[nodo]

        aux = self._adj.copy()
        for nodo in aux:
            cont = 0
            for arista,peso in aux[nodo]:
                if arista in sumideros:
                    del self._adj[nodo][cont]
                cont += 1

import random
grafo = DiGraph()
for u,v in (('A','B'),('A','C'),('A','G'),
                ('B','F'),
                ('F','H'),('F','B'),('F','D'),
                ('C','D'),('D','E'),('D','G')):
        grafo.add_edge(u,v,random.randint(1,30))
print(grafo)
print(grafo._adj)
grafo.quitar_sumideros()
print(grafo)
print(grafo._adj)


#grafo2 = DiGraph()
#for u,v,peso in (('s','r', 5), ('s', 'm', 10), ('r', 't', 5), ('m', 't', 10)):
    #grafo2.add_edge(u,v,peso)
#l = grafo2.squared()
#for arista in l:
    #print(arista)