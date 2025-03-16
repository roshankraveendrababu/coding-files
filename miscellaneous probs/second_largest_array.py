def find_second_largest(arr):
    largest=arr[0]
    second_largest=0
    for i in range(1,len(arr)):
        if arr[i]>largest:
            second_largest=largest
            largest=arr[i]
        elif arr[i]<largest and arr[i]>second_largest:
            second_largest=arr[i]
    return second_largest
if __name__=="__main__":
    arr=input("enter the array values: ")
    arr=list(map(int,arr.split()))
    print(find_second_largest(arr))

