'''
Created on 2017-12-26

@author: Titan
'''

class myList(object):
    '''
    class list for chapter 2
    '''

    data = []
    
    def __init__(self, l):
        self.data = l
        
    def display(self):
        print("data is {}".format(self.data))
        
    def union(self, lb):    
        for i in range(len(lb)):
            if(not lb[i] in self.data):
                self.data.append(lb[i])
    
    def merge(self, lb):
        re = []
        ia = 0
        ib = 0
        while ia<len(self.data) and ib<len(lb):
#             print("{}-{} : {}={}".format(ia,ib,self.data[ia],lb[ib]))
            if self.data[ia] >= lb[ib]:
                re.append(lb[ib])
                ib += 1
            else:
                re.append(self.data[ia])
                ia += 1
        if ia < len(self.data):
            for item in self.data[ia:]:
                re.append(item)
        if ib < len(lb):
            for item in lb[ib:]:
                re.append(item)
        return re
    
if __name__ == "__main__":
    a = myList(['gao','zhi',2])
    li = ['tong',3,2]
    a.display()
    print(a.merge(li))