'''
Created on 20180103

@author: Titan
'''
import random

class location(object):
    def __init__(self, x=0, y=0):
        self.x = x 
        self.y = y 
    def __eq__(self, a):
        if a == None:
            return False
        if self.x == a.x and self.y == a.y:
            return True
        return False
    def __ne__(self, a):
        return not self == a
    def __add__(self, di):
        if di == 0:
            return location(self.x, self.y)
        elif di == 1:
            return location(self.x+1, self.y)
        elif di == 2:
            return location(self.x, self.y+1)
        elif di == 3:
            return location(self.x-1, self.y)
        elif di == 4:
            return location(self.x, self.y-1)
    def __sub__(self, pos):
        if self == pos:
            return 0
        elif self.y == pos.y:
            if self.x > pos.x:
                return 1
            else:
                return 3
        elif self.x == pos.x:
            if self.y > pos.y:
                return 2
            else:
                return 4
        return None
        
    
        
class myMap(object):
    gate = 0.3
    path = []
    def __init__(self, size):
        self.size = size
        self.map = []
        self.stepNum = 0
        for i in range(size):
            self.map.append([])
            for _ in range(size):
                a = True
                if random.random() > self.gate:
                    a = False
                self.map[i].append(a)
        self.map[0][0] = self.map[size-1][size-1] = False
        self.entry = location(0,0)
        self.exit = location(size-1, size-1)
        self.path.append(self.entry)
#         self.display()
        
    def display(self):
        print("-" * (self.size +2))
        for i in range(self.size):
            line = "|"
            for j in range(self.size):
                if self.inPath(i, j):
                    line += '*'
                elif self.map[i][j]:
                    line += '+' 
                else:
                    line += ' '
            line += "|"
            print(line)
        print("-" * (self.size +2))
        print("move step is", self.stepNum)
#         print(self.map)

    def inPath(self, x,y):
        if x>=self.size or y >= self.size:
            return False
        for i in range(len(self.path)):
            if self.path[i].x == x and self.path[i].y == y:
                return True
        return False

    def move(self, pos):
        if pos.x >= self.size or pos.y >= self.size  or\
           pos.x <0 or pos.y <0:
            return False
        cur = self.path[-1]
        if pos == cur:
            return False
        if abs(pos.x - cur.x) >1 or abs(pos.y - cur.y) >1:
            return False
        if self.inPath(pos.x, pos.y):
            return False
        if self.map[pos.x][pos.y]:
            return False
        self.path.append(pos)
        self.stepNum += 1
        return True
        
    def back(self):
        if len(self.path) <= 1:
            return None
        cur = self.path.pop()
        return cur
    
    def now(self):
        return self.path[-1]
    
    def findOut(self):
        cur = self.now()
        di = 0
        while cur != self.exit:
            ne = None
            la = None
            for i in range(di+1, 5):
                ne = self.now() +i
                if self.move(ne):
                    cur = self.now()
                    di = 0
                    break
            if cur != ne:
                la = self.back()
                if la == None:
                    print("back to the entry!")
                    break
                cur = self.now()
                di = la - self.now() 
#             self.display()
        if cur == self.exit:
            return True
        return False

        
if __name__ == "__main__":
    m = myMap(20)
    m.display()
    print(m.findOut())
    m.display()
    