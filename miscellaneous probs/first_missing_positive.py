def first_missing(arr):
    for i in range(len(arr)):
        if arr[i]<0:
            arr[i]=0

    for i in range(len(arr)):
        val=abs(arr[i])
        if 1<=val<=len(arr):
            if arr[val-1]>0:
                arr[val-1]*=-1
            elif arr[val-1]==0:
                arr[val-1]=-1*(len(arr)+1)
    for i in range(1,len(arr)+1):
        if arr[i-1]>=0:
            return i
    return len(arr)+1

def first_missing_sort_brute(arr):
    n=len(arr)
    for i in range(n):
        if arr[i]<=0:
            arr[i]=n+2
    arr.sort()
    j=1
    for num in arr:
        if num==j:
            j+=1
        else:
            break
    return j

if __name__=="__main__":
    arr=input("enter the array to find the first missing positive: ")
    arr=list(map(int, arr.split()))
    print(first_missing_sort_brute(arr))
