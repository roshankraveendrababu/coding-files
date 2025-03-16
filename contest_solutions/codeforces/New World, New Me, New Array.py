import math
def is_possible(n,k,p):
    min_operations=math.ceil(abs(k)/abs(p))
    return min_operations if n>=min_operations else -1
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        arr=list(map(int,input().split()))
        n=arr[0]
        k=arr[1]
        p=arr[2]
        print(is_possible(n,k,p))