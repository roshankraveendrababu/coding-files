def merge(arr,low,mid,high):
    l=low
    r=mid+1
    temp=[]
    while l<=mid and r<=high:
        if arr[l]<=arr[r]:
            temp.append(arr[l])
            l+=1
        else:
            temp.append(arr[r])
            r+=1
    while l<=mid:
        temp.append(arr[l])
        l+=1
    while r<=high:
        temp.append(arr[r])
        r+=1
    for i in range(low,high+1):
        arr[i]=temp[i-low]

def merge_sort(arr,low,high):
    if low>=high:
        return 
    mid=(low+high)//2
    merge_sort(arr,low,mid)
    merge_sort(arr,mid+1,high)
    merge(arr,low,mid,high)
    return arr
    

if __name__=="__main__":
    arr=input("enter the array element in space seperated format: ")
    arr=list(map(int,arr.split()))
    n=len(arr)
    print(merge_sort(arr,0,n-1))
    #print(arr)