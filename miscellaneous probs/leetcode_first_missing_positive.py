def find_missing_positive(arr):
    for i in range(len(arr)):
        if arr[i]<0:
            arr[i]=0
    for i in range(len(arr)):
        val=abs(arr[i])
        if 1<=val<=len(arr):
            if arr[i-1]>0:
                arr[i-1]=-1*arr[i-1]
            else:
                arr[i-1]=-1*(len(arr)+1)
    for i in range(len(arr)):
        if arr[i]>0:
            return i+1
    return len(arr)+1

if __name__=="__main__":
    t=3
    for _ in range(t):
        arr=list(map(int,input().split()))
        print(find_missing_positive(arr))