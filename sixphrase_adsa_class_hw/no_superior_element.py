class no_superior_elements:
    def find_no_superior_element(self,arr,n):
        nos=0
        max_to_right=float('-inf')
        for i in range(n-1,-1,-1):
            if arr[i]>max_to_right:
                nos+=1
                max_to_right=arr[i]
        return nos
    
if __name__=="__main__":
    testing=no_superior_elements()
    arr1=input("enter the array variables: ")
    arr1=list(map(int,arr1.split()))
    n=len(arr1)
    print(testing.find_no_superior_element(arr1,n))
