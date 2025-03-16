def build_a(n,b):
    arr=[1]
    for i in range(len(b)):
        val=arr[-1]
        if b[i]==1:            
            arr.append(val)
        else:
            arr.append(val+1)
    return arr

def is_possible(n,b):
    for i in range(1,len(b)-1):
        if b[i-1]==1 and b[i+1]==1 and b[i]==0:
            return "Not Possible"
    return build_a(n,b)

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        b=list(map(int,input().split()))
        print(is_possible(n,b))

