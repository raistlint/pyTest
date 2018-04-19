# merge sort in chapter 2.3

import insertion
import copy

def mergeSort(A,p=0,r=None):
    if r == None:
        r = len(A)-1
    if p<r:
        q = (p+r)//2
        mergeSort(A,p,q)
        mergeSort(A,q+1,r)
        merge(A,p,q,r)
#         merge2(A,p,q,r)

def merge(A,p,q,r):
    L = copy.copy(A[p:q+1])
    R = copy.copy(A[q+1:r+1])
    L.append('tail')
    R.append('tail')
    i=j=0
    for k in range(p,r+1):
        if L[i] == 'tail':
            A[k] = R[j]
            j+=1
        elif R[j] == 'tail':
            A[k] = L[i]
            i+=1
        elif L[i] <= R[j]:
            A[k] = L[i]
            i+=1
        else:
            A[k] = R[j]
            j+=1
            
def merge2(A,p,q,r):
    n1 = q-p+1
    n2 = r-q
    L = copy.copy(A[p:q+1])
    R = copy.copy(A[q+1:r+1])
    i = j = 0
    k = p
    while i<n1 and j<n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i+=1
        else:
            A[k] = R[j]
            j+=1
        k+=1
    while i<n1:
        A[k] = L[i]
        i+=1
        k+=1
    while j<n2:
        A[k] = R[j]
        j+=1
        k+=1
    
    

########################
# Test section

class TestFunSelection(insertion.TestFun):
    def setUp(self):
        self.f = mergeSort
        self.fd = insertion.insertionSortDecrease
