import json


def bubbleSort(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
#             print(i,j)
            if(list[i]>list[j]):
                a = list[i]
                list[i] = list[j]
                list[j] = a
    return list
        

if __name__ == "__main__":
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
    