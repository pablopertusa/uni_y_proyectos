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

    def _resize(self):
        aux = [None]*len(self._items)*2
        for i in range(self._size):
            aux[i] = self._items[(self._first+i)%len(self._items)]
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
    
if __name__ == '__main__':
    d = CircularQueue()
    print(repr(d))
    for i in range(7):
        d.enqueue(i)
    print(repr(d))
    while not d.isEmpty():
        print(d.dequeue(),end=' ')
    print()
    print(repr(d))
    for i in range(15):
        d.enqueue(i)
    for i in range(5):
        print(d.dequeue(),end=' ')
    print()
    print(repr(d))
    while not d.isEmpty():
        print(d.dequeue(),end=' ')

