class make_all_equal:
    def move_apples(self,n,arr):
        sum=0
        for arr_val in arr:
            sum+=arr_val
        mean_value=sum//n
        no_of_movement=0
        for arr_value in arr:
            if mean_value>arr_value:
                no_of_movement+=mean_value-arr_value
        return no_of_movement
    
if __name__=="__main__":
    first_try=make_all_equal()
    arr=input("enter the no of apples in each box: ")
    arr=list(map(int,arr.split()))
    n=len(arr)
    print(first_try.move_apples(n,arr))
