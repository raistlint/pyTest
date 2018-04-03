import copy
import random

def bubbleSort(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
#             print(i,j)
            if(list[i]>list[j]):
                (list[i],list[j]) = (list[j], list[i])
    return list
        
def test_bubbleSort():
    org = [2,5,1,3,7,6]
    #a = org[:]
    #a = copy.copy(org)
    a = list(org)
    print(org)
    print(bubbleSort(org))
    print(org)
    print("------------")

# quick sort
def partition(list, s, e):
    pass
def quickDo(list, start, end):
    if start<end:
        p = partition(list,start, end)
        quickDo(list, start, p-1)
        quickDo(list, p+1, end)
def sortQuick(list):
    quickDo(list, 0, len(list))
    
    
def random_list(start, stop, length):
    re = []
    for i in range(length):
        re.append(random.randint(start,stop))
    return re
        
def test_sort(f):
    a = []
    if f(a) :
        print("-f-: empty list")
    else:
        print("-p-: enmpty list")
    for _ in range(10):
        start = 0
        end = 100
        length = 20
        a = random_list(start, end, length)
        b = copy.copy(a)
        org = copy.copy(a)
        b.sort()
        f(a)
        for i in range(length):
            if a[i] != b[i]:
                print("-f-: in index {}, re={}, exp={}".format(i, a[i], b[i]))
                print("\torg is", org)
                print("\tre  is", a)
                print("\texp is", b)
                break
#         print("\torg is", org)
#         print("\tre  is", a)
#         print("\texp is", b)
        print("-pass-")
    
if __name__ == "__main__":
#     test_bubbleSort()
    test_sort(bubbleSort)
    print("last line")
