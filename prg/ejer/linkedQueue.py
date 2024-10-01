class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedQueue:
    def __init__(self):
        self._head = None
        self._last = None
        self._size = 0

    def isEmpty(self):
        return self._size == 0
        
    def enqueue(self,value):
        newnode = Node(value)
        if self._head is None:
            self._head = newnode
        else:
            self._last.next = newnode
        self._last = newnode
        self._size += 1
        
    def dequeue(self):
        if self.isEmpty():
            raise IndexError("dequeue from empty queue")
        returned = self._head.value
        self._head = self._head.next
        if self._head is None:
            self._last = None
        self._size -= 1
        return returned
    
    def __repr__(self):
        aux = []
        i = self._head
        while i is not None:
            aux.append(i.value)
            i = i.next
        return 'LinkedQueue('+repr(aux)+')'
    
    def str(self):
        cont = []
        if self._size == 0:
            return ''
        nodo = self._head
        for i in range(self._size):
            cont.append(str(nodo.value))
            nodo = nodo.next
        return ','.join(cont)
    
    def map(self, function):
        if self._size != 0:
            nodo = self._head
            for i in range(self._size):
                nodo.value = function(nodo.value)
                nodo = nodo.next

    def filter(self, function):
        if self._size != 0:
            aux = []
            nodo = self._head
            if function(nodo.value):
                aux.append(nodo.value)
            while nodo.next is not None:
                nodo = nodo.next
                if function(nodo.value):
                    aux.append(nodo.value)
            self._head, self._last, = None,None
            self._size = 0
            for i in aux:
                self.enqueue(i)

    def extend(self, other):
        size = other._size
        nodo = other._head
        self.enqueue(nodo.value)
        while nodo.next is not None:
            nodo = nodo.next
            self.enqueue(nodo.value)

    def __eq__(self, other):
        if self._size != other._size:
            return False
        if self._head.value != other._head.value:
            return False
        nodo1 = self._head
        nodo2 = other._head
        for i in range(self._size - 1):
            nodo1 = nodo1.next
            nodo2 = nodo2.next
            if nodo1.value != nodo2.value:
                return False
        return True
    
    def __getitem__(self, index):
        if index >= self._size:
            raise IndexError('LinkedQueue index out of range')
        else:
            pos = 0
            nodo = self._head
            while pos != index:
                nodo = nodo.next
                pos += 1
            return nodo.value
        
    def take(self, n):
        aux = LinkedQueue()
        list = []
        if n >= self._size:
            nodo = self._head
            list.append(nodo.value)
            for i in range(self._size-1):
                nodo = nodo.next
                list.append(nodo.value)
        else:
            nodo = self._head
            list.append(nodo.value)
            for i in range(n-1):
                nodo = nodo.next
                list.append(nodo.value)

        for i in list:
            aux.enqueue(i)

        return aux
    
    def drop(self, n, inplace=True):
        if inplace == True:
            if n >= self._size:
                self.__init__()

            else:
                nodo = self._head
                for i in range(n):
                    nodo = nodo.next
                self._head = nodo

        else:
            if n >= self._size:
                return LinkedQueue()

            else:
                aux = LinkedQueue()
                nodo = self._head
                for i in range(self._size):
                    if i >= n:
                        aux.enqueue(nodo.value)
                    nodo = nodo.next
                return aux
                








            
def f(x):
    return x%2 != 0
lq = LinkedQueue()
for i in range(10):
    lq.enqueue(i)

print(lq)

q2 = lq.drop(5, False)
print(lq)
print(q2)
