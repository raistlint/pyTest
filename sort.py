import copy

def bubbleSort(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
#             print(i,j)
            if(list[i]>list[j]):
                a = list[i]
                list[i] = list[j]
                list[j] = a
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
    
if __name__ == "__main__":
    test_bubbleSort()
