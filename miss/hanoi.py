'''
Created on 20180104

@author: Titan
'''

class hanoi(object):
    def __init__(self, level):
        self.x = [i for i in range(level,0,-1)]
        self.y = []
        self.z = []
        self.level = level
        
    def move(self, f, t):
        if len(f) > 0:
            t.append(f.pop())
            self.display()
    
    def display(self):
        print(self.x)
        print(self.y)
        print(self.z)
        print('-'*35)
    
    def start(self):
        self.go(self.level, self.x, self.y, self.z)
        
    def go(self, n, x,y,z):
        if n == 1:
            self.move(x, z)
        else:
            self.go(n-1, x,z,y)
            self.move(x, z)
            self.go(n-1, y,x,z)

if __name__ == '__main__':
    h = hanoi(10)
    h.display()
    h.start()