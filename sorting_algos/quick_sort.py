def partition(arr,low,high):
    pivot=arr[low]
    i=low
    j=high
    while i<j:
        while i<=high-1 and arr[i]<=pivot:
            i+=1
        while j>=low+1 and arr[j]>pivot:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j

def quick_sort(arr,low,high):
    if low<high:
        pindex=partition(arr,low,high)
        quick_sort(arr,low,pindex-1)
        quick_sort(arr,pindex+1,high)

def quick_sort_call(arr,low,high):
    quick_sort(arr,low,high)
    return arr

if __name__=="__main__":
    arr=input("enter the array elements: ")
    arr=list(map(int, arr.split()))
    high=len(arr)-1
    print(quick_sort_call(arr,0,high))