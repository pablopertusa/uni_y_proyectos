import collections

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

    def transpose(self):
        resul = DiGraph()
        for u in self.nodes():
            for v,w in self._adj[u]:
                resul.add_edge(v, u, w)
        return resul
        
    def BFS(self, src):
        dist, pred = { src:0 }, { src:None }
        Q = collections.deque()
        visited = { src } # set
        Q.append(src)
        iter = 1 # para la traza
        while len(Q) > 0:
            print(f'\niter {iter}\nvisited {visited}\npred {pred}\ndist {dist}\nQ {Q}')
            iter += 1
            u = Q.popleft()
            print(f'se selecciona {u}')
            for (v, weight) in self._adj[u]:
                if v not in visited:
                    dist[v] = dist[u] + 1
                    pred[v] = u
                    visited.add(v)
                    Q.append(v)
        return dist, pred

    def DFS(self):
        visited = set()
        pred = {}
        
        def DFS_visit(u, anidamiento=0): # esto es una closure o clausura
            print('  '*anidamiento,f'Entro en DFS_visit({u})',sep='')
            visited.add(u)
            for (v, weight) in self._adj[u]:
                if v not in visited:
                    pred[v] = u
                    DFS_visit(v, anidamiento+1)
            print('  '*anidamiento,f'Salgo de DFS_visit({u})',sep='')
            
        for u in self.nodes():
            if u not in visited:
                pred[u] = None # raíz de un árbol
                DFS_visit(u)
        return pred
                
    def Dijkstra(self, src):
        dist = { src:0 } # asocia una distancia a cada vértice
        pred = {} # para recuperar el camino de menor peso
        fixed = set() # cjt de vértices que ya han sido fijados
        eligible = { src } # cjt con src como elemento inicial
        iter = 1 # para la traza
        while len(eligible)>0:
            d,u = min( (dist[v],v) for v in eligible)
            print(f'Iter: {iter} fijados: {fixed} eligible: {eligible} -> sel. {u}')
            iter += 1
            eligible.remove(u) # lo sacamos de eligible
            fixed.add(u)       # y lo añadimos a fixed
            for v,weight in self._adj[u]: # actualizamos la cota
                if v not in fixed:        # de los adyacentes a v
                    if v not in dist:
                        pred[v], dist[v] = u, dist[u] + weight
                        eligible.add(v)
                    elif dist[v] > dist[u] + weight:
                        pred[v], dist[v] = u, dist[u] + weight
        return dist, pred
        
    def Dijkstra2(self, src):
        fixed = { u:False for u in self._adj }
        dist = { u:float("inf") for u in self._adj }
        dist[src] = 0
        pred = {}
        for i in range(len(self._adj)):
            d,u = min( (dist[v],v) for v in self._adj
                       if not fixed[v] )
            print(f'Iter: {i+1} fijados: {fixed} -> sel. {u}')
            fixed[u] = True
            for v,weight in self._adj[u]:
                if dist[v] > d + weight:
                    pred[v], dist[v] = u, d + weight
        return dist, pred
    
    def camino(self, src, dst, vmin, vmax):
        visitado = set()
        dist = {src:0}
        q = collections.deque()
        q.append(src)
        while len(q) > 0:
            nodo = q.popleft()
            visitado.add(nodo)
            for destino,peso in self._adj[nodo]:
                if destino not in visitado:
                    if peso >= vmin and peso <= vmax:
                        dist[destino] = dist[nodo] + 1
                        q.append(destino)
                        if destino == dst:
                            break
        return dist[dst]


    
if __name__ == '__main__':
    print('-'*80)
    print('Traza de BFS')    
    print('-'*80)    
    grafo = DiGraph()
    for u,v in (('A','B'),('A','C'),('A','G'),
                ('B','F'),
                ('F','H'),('F','B'),('F','D'),
                ('C','D'),('D','E'),('D','G')):
        grafo.add_edge(u,v,1)
    for v in grafo.nodes():
        print(v, grafo._adj[v])
    grafo.BFS('A')

    print()
    print('-'*80)
    print('Traza de DFS')
    print('-'*80)
    grafo = DiGraph()
    for u,v in (('A','B'),('A','C'),('A','G'),
                ('B','F'),
                ('F','H'),('F','B'),('F','D'),
                ('C','D'),('D','E'),('D','G')):
        grafo.add_edge(u,v,1)
    for v in grafo.nodes():
        print(v, grafo._adj[v])
    #print(grafo.BFS('A'))
    pred = grafo.DFS()
    print('pred',pred)

    print()
    print('-'*80)        
    print('Traza de Dijkstra')
    print('-'*80)
    grafo = DiGraph()
    for u,v,w in (('s','u',10),('s','x',5),
                  ('u','v',1),('u','x',2),
                  ('x','u',3),('x','v',9),('x','y',2),
                  ('y','s',7),('y','v',6),
                  ('v','y',4)):
        grafo.add_edge(u,v,w)
    for v in grafo.nodes():
        print(v, grafo._adj[v])
    dist, pred = grafo.Dijkstra('s')
    print("dist:",dist)
    print("pred:",pred)
    print('-'*80)        
    print('Traza de Dijkstra version inf')
    print('-'*80)
    dist, pred = grafo.Dijkstra2('s')
    print("dist:",dist)
    print("pred:",pred)
