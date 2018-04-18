#  selection sort in exercise 2.2-2
import insertion

def selectionSort(A):
    for i in range(0,len(A)-1):
        min = i
        for j in range(i+1,len(A)):
            if A[min] > A[j]:
                min = j
        A[i],A[min] = A[min],A[i]


########################
# Test section

class TestFunSelection(insertion.TestFun):
    def setUp(self):
        self.f = selectionSort
        self.fd = insertion.insertionSortDecrease
