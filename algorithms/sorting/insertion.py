# INSERTION SORT in chapter 2.1
import unittest
import copy
import random

def insertionSort(A):
    for j in range(1,len(A)):
        tmp = A[j]
        i = j-1
        while i>=0 and A[i]> tmp:
            A[i],A[i+1] = A[i+1],A[i]
            i-=1
        A[i+1] = tmp
        
def insertionSortDecrease(A):
    """ exercise 2.1-2
    """
    for j in range(1,len(A)):
        tmp = A[j]
        i=j-1
        while i>=0 and A[i] <tmp:
            A[i],A[i+1] = A[i+1],A[i]
            i-=1
        A[i+1] = tmp
def addBinary(A,B):
    """ exercise 2.1-4
    """
    carry = 0
    c = []
    for i in range(len(A)-1,-1,-1):
        c.insert(0,(A[i]+B[i]+carry)%2)
        carry = (A[i]+B[i]+carry)>>1
    c.insert(0,carry)
    return c

def insertionSortRecursive(A, k=None):
    """ exercise 2.3-4
    """
    if(k == None):
        k=len(A)
    if k>1:
        insertionSortRecursive(A, k-1)
        tmp = A[k-1]
        i=k-2
        while i>=0 and A[i] > tmp:
            A[i+1] = A[i]
            i-=1
        A[i+1] = tmp

########################
# Test section

def abs(a):
    if a<0:
        a *= -1
    return a

class TestFun(unittest.TestCase):
    def setUp(self):
#         self.f = insertionSort
        self.f = insertionSortRecursive
        self.fd = insertionSortDecrease
    def tearDown(self):
        pass
    def random_list(self, start, stop, length):
        re = []
        for i in range(length):
            re.append(random.randint(start,stop))
        return re
        
    def test_abs(self):
        self.assertEqual(abs(-1), 1, "first case")
        self.assertEqual(abs(1), 1, "second case")
        
    def test_sort(self):
        a = [2,5,3,1,4,8,7,6]
        b = copy.copy(a)
        self.f(a)
        b.sort()
        self.assertListEqual(a,b,"sort list")
        self.f(a)
        self.assertListEqual(a,b,"already sort list")
        a.reverse()
        self.f(a)
        self.assertListEqual(a,b,"reverse list")
    def test_sort_null(self):
        a = []
        self.f(a)
        self.assertListEqual(a,[])
    def test_sort_stress(self):
        for _ in range(10):
            start = 0
            end = 100
            length = 20
            a = self.random_list(start, end, length)
            b = copy.copy(a)
            org = copy.copy(a)
            b.sort()
            self.f(a)
            self.assertListEqual(a,b,"ori is {}".format(org))
    def test_sort_dec(self):
        a = [2,5,3,1,4,8,7,6]
        b = copy.copy(a)
        self.fd(a)
        b.sort()
        b.reverse()
        self.assertListEqual(a,b,"dec sort list")
        self.fd(a)
        self.assertListEqual(a,b,"dec already sort list")
        a.reverse()
        self.fd(a)
        self.assertListEqual(a,b,"dec reverse list")
    def test_addBinary(self):
        a = [1,1,0,1,1,1]
        b = [1,1,0,1,1,1]
        c = addBinary(a, b)
        self.assertListEqual(c,[1,1,0,1,1,1,0])
        a = [1,1,1]
        self.assertListEqual(addBinary(a, a), [1,1,1,0])

if __name__ == "__main__":
    print("last line - insertion.py")