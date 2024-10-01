class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedQueue:
    def __init__(self):
        self._head = None
        self._last = None

    def isEmpty(self):
        return self._head.next is None
        
    def __len__(self):
        if self._head is None:
            return 0
        size = 1
        siguiente = self._head.next
        while siguiente is not None:
            siguiente = siguiente.next
            size += 1
        return size
        
    def enqueue(self,value):
        newnode = Node(value)
        if self._head is None:
            self._head = newnode
        else:
            self._last.next = newnode
        self._last = newnode
        
    def dequeue(self):
        if self.isEmpty():
            raise IndexError("dequeue from empty queue")
        returned = self._head.value
        self._head = self._head.next
        if self._head is None:
            self._last = None
        return returned
    
    def __repr__(self):
        aux = []
        i = self._head
        while i is not None:
            aux.append(i.value)
            i = i.next
        return 'LinkedQueue('+repr(aux)+')'
    
    def map(self, function):
        if self._head is not None:
            nodo = self._head
            while nodo.next is not None:
                nodo.value = function(nodo.value)
                nodo = nodo.next
            nodo.value = function(nodo.value)
    
def f(x):
    return x%2 == 0
lq = LinkedQueue()
for i in range(10):
    lq.enqueue(i)

print(lq)
lq.map(f)
print(lq)