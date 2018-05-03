# the maximum subarray in chapter 4.1
import unittest

def findMaxCrossing(A,low,mid,high):
    ls = -99999
    sum = 0
    ml = mid
    for i in range(mid, low-1, -1):
        sum += A[i]
        if sum > ls:
            ls = sum
            ml = i
    rs = -99999
    sum = 0
    mr = mid
    for i in range(mid+1, high+1):
        sum += A[i]
        if sum > rs:
            rs = sum
            mr = i
    return (ml, mr, ls+rs)

def findMaximum(A,low=None,high=None):
    if low == None:
        low = 0
    if high == None:
        high = len(A)-1
    if low == high:
        return (low,high,A[low])
    elif low < high:
        mid = (low + high)//2
        (ll, lh, ls) = findMaximum(A, low, mid)
        (rl, rh, rs) = findMaximum(A, mid+1, high)
        (cl, ch, cs) = findMaxCrossing(A, low, mid, high)
        if ls >= rs and ls >= cs:
            return (ll, lh, ls)
        elif rs >= ls and rs >= cs:
            return (rl, rh, rs)
        else:
            return (cl, ch, cs)
        
def findMaximumBrute(A):
    ''' exercise 4.1-2
    '''
    l=r=-1
    max = -99999
    for i in range(len(A)-1):
        sum = 0
        for j in range(i, len(A)):
            sum += A[j]
            if sum >= max:
                max = sum
                l = i
                r = j
    return (l,r,max)

def findMaximumDyn(A):
    """ exercise 4.1-5
    """
    max = -9999
    sum = 0
    for i in range(len(A)):
        if sum <0:
            sum = A[i]
        else:
            sum += A[i]
        if sum >max:
            max = sum
    return max

def findMaximumLinear(A):
    """ exercise 4.1-5
    """
    max = -9999
    sum = 0
    l = r = cur =0
    for i in range(len(A)):
        sum += A[i]
        if sum > max:
            max = sum
            l = cur
            r = i
        if sum <0:
            sum = 0
            cur = i+1
    return (l,r,max)
    
########################
# Test section

class TestFunSelection(unittest.TestCase):
    def setUp(self):
#         self.f = findMaximum
#         self.f = findMaximumBrute
        self.f = findMaximumLinear
        self.f2 = findMaximumDyn
    def tearDown(self):
        pass
    
    def test_f2(self):
        a = [-1,2,4,-7,10]
        self.assertEqual(self.f2(a), 10)
        a = [-1,2,4,-5,10, -5]
        self.assertEqual(self.f2(a), 11)
    def test_fun(self):
        a = [x for x in range(10)]
        self.assertTupleEqual(self.f(a), (0,9,45), "0-9 case")
        a[3] = -10
        self.assertTupleEqual(self.f(a), (4,9,39), "4-9 case")
        a = [1, -4, 3, -4]
        self.assertTupleEqual(self.f(a), (2,2,3), "normal case")
        a = [-x for x in range(10)]
        self.assertTupleEqual(self.f(a), (0,0,0), "0- -9 case")
        
