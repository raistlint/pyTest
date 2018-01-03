'''
Created on 20180103

@author: Titan
'''
import random

class myMap(object):
    gate = 0.25
    def __init__(self, size):
        self.size = size
        self.map = []
        for i in range(size):
            self.map.append([])
            for _ in range(size):
                a = True
                if random.random() > self.gate:
                    a = False
                self.map[i].append(a)
        self.display()
        
    def display(self):
        print("-" * (self.size +2))
        for i in range(self.size):
            line = "|"
            for j in range(self.size):
                if self.map[i][j]:
                    line += '+' 
                else:
                    line += ' '
            line += "|"
            print(line)
        print("-" * (self.size +2))
#         print(self.map)

class dog(object):
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
        pass        
        
        
if __name__ == "__main__":
    m = myMap(8)