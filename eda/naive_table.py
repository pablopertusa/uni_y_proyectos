class NaiveTable:
    def __init__(self):
        self._table = []

    def __len__(self):
        return len(self._table)

    def __getitem__(self, key):
        for (k, v) in self._table:
            if k == key:
                return v
        raise KeyError("Key Error: " + repr(k))

    def __contains__(self, key):
        for (k, v) in self._table:
            if k == key:
                return True
        return False

    def __setitem__ (self, key, value):
        for i,(k, v) in enumerate(self._table):
            if k == key:
                self._table[i] = (k, value)
                return
        self._table.append((key, value))

    def setdefault(self,key, default):
        for (k, v) in self._table:
            if k == key:
                return v
        self._table.append((key, default))
        return default

    def __delitem__ (self, key):
        for i,(k, v) in enumerate(self._table):
            if k == key:
                del self._table[i]
                return
        raise KeyError("Key Error: " + repr(k))

    def __iter__(self):
        for (k,v) in self._table:
            yield k

    def __repr__(self):
        aux = []
        for (k,v) in self._table:
            aux.append(repr(k)+":"+repr(v))
        return "{" + ", ".join(aux) + "}"

