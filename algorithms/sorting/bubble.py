import insertion

def bubbleSort(A):
    for i in range(len(A)-1):
        for j in range(len(A)-1, i,-1):
            if A[j] < A[j-1]:
                A[j],A[j-1] = A[j-1],A[j]


########################
# Test section

class TestFunSelection(insertion.TestFun):
    def setUp(self):
        self.f = bubbleSort
        self.fd = insertion.insertionSortDecrease
