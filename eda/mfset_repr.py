class MFset:
    def __init__(self):
        self._p = {}

    def find(self, x):
        while x in self._p:
            x = self._p[x]
        return x
    
    def merge(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            self._p[rx] = ry

    def __repr__(self):
        h = {} # a cada padre una lista de sus hijos
        for x,px in self._p.items():
            h.setdefault(px,[]).append(x)
        # los representantes son padres que no son hijos de nadie:
        r = [x for x in h if x not in self._p]
        # resultado final:
        def aux(x): # función auxiliar recursiva
            resul = repr(x) # representación de x como cadena
            if x in h: # si tiene hijos los añadimos:
                resul += "(" + ",".join(aux(y) for y in h[x]) + ")"
            return resul
        return 'MFset('+" ".join(aux(x) for x in r)+')'
    
    def getPartition(self, x):
        l = []
        rx = self.find(x)
        for i in self._p.keys():
            if self.find(i) == rx:
                l.append(i)
        l.append(rx)
        return l
    
    def hojasParticion(self, x):
        if x not in self._p:
            return 0
        rx = self.find(x)
        resul = []
        for i in self._p:
            if self.find(i) == rx:
                cont = 0
                while i != rx:
                    i = self._p[i]
                    cont += 1
                resul.append(cont)
        return max(resul)
    
    
def transitividad(amigos, enemigos):
    mfset = MFset()
    for x,y in amigos:
        mfset.merge(x,y)
    for x,y in enemigos:
        if mfset.find(x) == mfset.find(y):
            return f'{x} y {y} deberían ser amigos y son enemigos'
    return 'los amigos de mis amigos son mis amigos'


def toMFset(v):
    d = {}
    mf = MFset()
    for i in range(len(v)):
        if v[i] not in d:
            d[v[i]] = i
        else:
            x = d[v[i]]
            mf.find(x)
            mf.merge(x,i)
    return mf

    


mf = MFset()
mf.merge(9,4)
mf.merge(4,0)
mf.merge(1,0)
mf.merge(2,0)
print(mf.hojasParticion(2))





