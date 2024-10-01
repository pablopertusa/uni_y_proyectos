######################################################################
# POP ELEMENTS FROM A LIST UNTIL IT IS EMPTY
######################################################################

def empty_front(vec):
    while len(vec)>0:
        vec.pop(0)
        
def empty_ending(vec):
    while len(vec)>0:
        vec.pop()
        

######################################################################
# SORTING ALGORITHMS
######################################################################

def insertionSort(lis):
    for index in range(1,len(lis)):
        key = lis[index]
        pos = index
        while pos>0 and lis[pos-1]>key:
            lis[pos]=lis[pos-1]
            pos = pos-1
        lis[pos]=key

def merge(vect, izqA, izqB, derB):
    i,j,derA,k,aux = izqA,izqB,izqB-1,0,[]
    while i<=derA and j<=derB:
        if vect[i]<vect[j]:
            aux.append(vect[i])
            i += 1
        else:
            aux.append(vect[j])
            j += 1
    for r in range(i,derA+1): # copiar resto parte izq.
        aux.append(vect[r])
    for r in range(j,derB+1): # copiar resto parte der.
        aux.append(vect[r])
    k = 0
    for r in range(izqA,derB+1): # copiar al vector orig.
        vect[r] = aux[k]
        k += 1

def mergesort_aux(vect, izq, der):
    if izq < der:
        mitad = (izq+der)//2
        mergesort_aux(vect, izq, mitad)
        mergesort_aux(vect, mitad+1, der)
        merge(vect, izq, mitad+1, der)
    
def mergeSort(vect):
    mergesort_aux(vect, 0, len(vect)-1)

def nativeSort(vect):
    vect.sort()

