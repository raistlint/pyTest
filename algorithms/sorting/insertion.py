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

########################
# Test section

def abs(a):
    if a<0:
        a *= -1
    return a

class TestFun(unittest.TestCase):
    def setUp(self):
        self.f = insertionSort
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

if __name__ == "__main__":
    print("last line - insertion.py")