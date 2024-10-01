import collections

class MapReduce:
    def __call__(self, inputdata):
        map_responses = collections.defaultdict(list)
        for (k1,v1) in inputdata:
            for (k2,v2) in self.mapper(k1,v1):
                map_responses[k2].append(v2)
        reduce_responses = collections.defaultdict(list)
        for k2,listv2 in map_responses.items():
            for v2 in self.reducer(k2,listv2):
                reduce_responses[k2].append(v2)
        return reduce_responses


class Bigramas(MapReduce):
    def mapper(self, k1, v1):
        lista = v1.lower().replace('\n', '').split()
        for i in range(len(lista)-1):
            yield(((lista[i],lista[i+1]), 1))

    def reducer(self, k2, lista):
        yield sum(lista)

'''
if __name__ == '__main__':
    with open('datos.txt', 'r') as f:
        w = Bigramas()
        resul = w(enumerate(f))
        for bigrama in resul:
            print(f'{bigrama[0]} {bigrama[1]} {resul[bigrama][0]}')
'''

class MaxLetraPorLinea(MapReduce):
    def mapper(self, k1, v1):
        d = {}
        for letra in v1:
            if letra.isalpha():
                letra = letra.lower()
                if letra not in d:
                    d[letra] = 1
                else:
                    d[letra] += 1
        for letra in d:
            yield (letra, d[letra])

    def reducer(self, k2, lista):
        yield max(lista)


if __name__ == '__main__':
    with open('datos2.txt', 'r') as f:
        w = MaxLetraPorLinea()
        resul = w(enumerate(f))
        l = sorted(resul.items())
        for letra,n in l:
            print(letra, n[0])



class MayorEdadCiudad(MapReduce):
    def mapper(self, k1, v1):
        yield(v1[1], (v1[2], v1[0]))
    def reducer(self, k2, lista):
        max = sorted(lista)[-1]
        return max
        