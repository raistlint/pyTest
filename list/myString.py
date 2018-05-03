
def index1(s,t,p=0):
    i = p
    j = 0
    print(len(s), len(t))
    while(i<len(s) and j<len(t)):
        print("i = {}, j = {}".format(i,j))
        if(s[i]==t[j]):
            print("--")
            i += 1
            j += 1
        else:
            print("**")
            i = i - j +1
            j = 0
    if j >= len(t):
        return i - j 
    else:
        return None
    

if __name__ == "__main__":
    print(index1("gao zhi tong", "zhi"))
    print("last line")