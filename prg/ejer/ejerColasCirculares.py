class CircularQueue:
    def __init__(self, initialsize=10):
        self._first = 0 # index of first in content
        self._size = 0  # number of elements
        self._items = [None]*initialsize

    def enqueue(self, value):
        if self._size == len(self._items):
            self._resize()
        pos_next = (self._first + self._size) % len(self._items)
        self._items[pos_next] = value
        self._size += 1

    def push(self, value):
        if self._size == len(self._items):
            self._resize()
        self._first = (self._first -1) % len(self._items)
        self._items[self._first] = value
        self._size += 1

    def map(self, function):
        for i in range(self._size):
            pos = (self._first + i) % len(self._items)
            self._items[pos] = function(self._items[pos])

    def filter(self, function):
        escribo = self._first
        new_size = 0
        for i in range(self._size):
            pos = (self._first + i) % len(self._items)
            if function(self._items[pos]):
                    self._items[escribo] = self._items[pos]
                    escribo = (escribo + 1) % len(self._items)
                    new_size += 1
        for i in range((len(self._items) - new_size)):
            pos = (escribo + i) % len(self._items)
            self._items[pos] = None
        self._size = new_size

    def __eq__(self, otra):
        if not isinstance(otra, CircularQueue):
            return False
        if self._size != otra._size:
            return False
        for i in range(self._size):
            if self._items[(self._first + i) % len(self._items)] != otra._items[(otra._first + i) % len(otra._items)]:
                return False
        return True

    def _resize(self):
        aux = [None]*len(self._items)*2
        for i in range(self._size):
            aux[i] = self._items[(self._first+i)]%len(self._items)
        self._items = aux
        self._first = 0	

    def isEmpty(self):
        return self._size == 0

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("dequeue from empty CircularQueue")
        value = self._items[self._first]
        self._items[self._first] = None # why? (garbage collection)
        self._first = (self._first + 1) % len(self._items)
        self._size -= 1
        return value

    def __repr__(self):
        return f'first {self._first}, size {self._size} content {self._items}'
    


def f(x):
    return x > 5


c = CircularQueue()
for i in range(9):
    c.enqueue(i)
c.enqueue(12)
c.enqueue(12)
print(c)