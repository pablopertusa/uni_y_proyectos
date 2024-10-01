def heapify(v, pos, size): # de un max-heap!!!!
    child_pos = 2*pos + 1
    if child_pos < size:
        if (child_pos+1 < size and
            v[child_pos+1] > v[child_pos]):
            child_pos += 1
        if v[pos] < v[child_pos]:
            v[pos],v[child_pos] = v[child_pos],v[pos]
            heapify(v, child_pos, size)
            
def heapsort(v):
    # en primer lugar aplicamos buildheap:
    sz = len(v)
    for pos in range(sz//2 -1, -1, -1):
        heapify(v, pos, sz)
    # a continuación, vamos quitando el mayor y lo ponemos al final:
    while sz > 1:
        v[sz-1],v[0] = v[0],v[sz-1]
        sz += -1
        heapify(v, 0, sz)
    return v

def heapsort(v):
    # en primer lugar aplicamos buildheap:
    sz = len(v)
    for pos in range(sz//2 -1, -1, -1):
        heapify(v, pos, sz)
    print(f"{v} (tras buildheap)")
    # a continuación, vamos quitando el mayor y lo ponemos al final:
    while sz > 1:
        print(f"{v} (antes de intercambiar, sz {sz:>2})")
        v[sz-1],v[0] = v[0],v[sz-1]
        sz += -1
        heapify(v, 0, sz)
        print(f"{v} (tras heapify, sz {sz:>2})")
    return v

heapsort([5,13,2,25,7,17,20,8,4])
