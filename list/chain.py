'''
Created on 20171227

@author: Titan
'''

class lNode(object):
    def __init__(self, value, p=None):
        self.data = value
        self.next = p

class myChain(object):
    '''
    one direction chain list
    '''
    def __init__(self):
        self.head = None
        self.len = 0
        
    def append(self, value):
        n = lNode(value)
        if self.head == None:
            self.head = n
        else:
            p = self.head
            while p.next != None:
                p = p.next
            p.next = n
        self.len += 1
        return True
        
    def insert(self, idx, value):
        if idx>self.len or idx <0:
            return False
        n = lNode(value)
        if self.head == None:
            self.head = n
        elif idx == 0:
            n.next = self.head
            self.head = n
        else:
            p = self.head
            for i in range(idx-1):
                p = p.next
            n.next = p.next
            p.next = n
        self.len += 1
        return True
        
    def get(self, idx):
        if idx>=self.len or idx <0:
            return None
        p=self.head
        for i in range(idx):
            p = p.next
        return p.data
    
    def display(self):
        p = self.head
        tem = []
        while p != None:
            tem.append(p.data)
            p = p.next
        print("chain is -", tem)
        
if __name__ == "__main__":
    a = myChain()
    a.display()
    a.append(1)
    a.append(2)
    a.display()
    a.insert(0, 3)
    a.display()
    print(a.get(2))
    print("last line")
