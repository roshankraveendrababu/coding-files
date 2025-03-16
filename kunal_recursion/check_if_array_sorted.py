def is_sorted(arr,pos):
    if pos==len(arr)-1:
        return True
    return arr[pos]<arr[pos+1] and is_sorted(arr,pos+1)

if __name__=="__main__":
    arr=input("enter the values in space seperated format: ")
    arr=list(map(int,arr.split()))
    print(is_sorted(arr,0))