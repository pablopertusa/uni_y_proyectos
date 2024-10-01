class SeparateChainingHashTable:
    def __init__(self, initial_table_size = 2**3):
        self._n = 0
        self._table = [[] for i in range(initial_table_size)]

    def __len__(self):
        return self._n

    def _hash_function(self, value):
        return hash(value) % len(self._table)

    def load_factor(self):
        return self._n / len(self._table)
        
    def __getitem__(self, key):
        index = self._hash_function(key)
        bucket_list = self._table[index]
        for (k, v) in bucket_list:
            if k == key:
                return v
        raise KeyError("Key Error: " + repr(key))

    def __contains__(self, key):
        index = self._hash_function(key)
        bucket_list = self._table[index]
        for (k, v) in bucket_list:
            if k == key:
                return True
        return False

    def __setitem__ (self, key, value):
        index = self._hash_function(key)
        bucket_list = self._table[index]
        for i,(k, v) in enumerate(bucket_list):
            if k == key:
                bucket_list[i] = (k, value)
                return
        bucket_list.append((key, value))
        self._n += 1
        if self.load_factor() >= 2:
            self._resize(2 * len(self._table))

    def setdefault(self,key, default):
        index = self._hash_function(key)
        bucket_list = self._table[index]
        for (k, v) in bucket_list:
            if k == key:
                return v
        bucket_list.append((key, default))
        self._n += 1
        if self.load_factor() >= 2:
            self._resize(2 * len(self._table))
        return default

    def __delitem__ (self, key):
        index = self._hash_function(key)
        bucket_list = self._table[index]
        pos = -1
        for i,(k, v) in enumerate(bucket_list):
            if k == key:
                pos = i
                break
        if pos == -1:
            raise KeyError("Key Error: " + repr(key))
        del bucket_list[pos]
        self._n -= 1

    def _resize(self, new_table_size):
        old_table = self._table
        self._table = [[] for i in range(new_table_size)]
        for bucket_list in old_table:
            for (k,v) in bucket_list:
                index = self._hash_function(k)
                self._table[index].append((k,v))

    def __iter__(self):
        for bucket_list in self._table:
            for (k,v) in bucket_list:
                yield k

    def __repr__(self):
        aux = []
        for bucket_list in self._table:
            for (k,v) in bucket_list:
                aux.append(repr(k)+":"+repr(v))
        return "{" + ",".join(aux) + "}"

