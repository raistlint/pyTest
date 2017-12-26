import json
import copy


def test():
    print(bubbleSort([1,2,7,4,6]))
    for i in range(1,10):
        print('{0:2d} {1:3d} {2:4d}'.format(i, i*i, i*i*i))
    str = 'gao\n'
    print("lala {!a}".format(str))
    print("last line")
    x = [1,'gao','zhi']
    with open('log', 'w') as f:
        json.dump(x, f)
    print(json.dumps(x))
    with open('log', 'r') as f:
        a = json.load(f)
    print(json.dumps(a))
    
def test2(list):
    #list = [1,2,3]
    list[1] = 2
    list[2] = 3
    list[3][0] = 4
    print("in -", list)
    #return list

if __name__ == "__main__":
    test_bubbleSort()
    list = [1,1,1, [1]]
    print("bef -", list)
    test2(list)
    print("aft -", list)
    
    