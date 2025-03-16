'''
# arr[]  containing non-negative integers
len(arr)<=10^5 unique states
hence we should use dp coz recursion will fail
if that can be eqally partioned, answer is 0


# divide it into two sets set1 and set2 such that the absolute difference between their sums is minimum
 we can do sum - target to find the sum of remaining elements, which is S2
 now we can place abs(s2-s1) in the table which corresponds to abs(sum-target-target)..
 the values of s1 and s2 get interchanged at the midpoint , hence it that case the min diff stays the same 
 hence we can find the valid values of s1 from range of (0,sum_arr//2), and take the maximum valid value .. coz it gives the mini diff.
 hence our target to calculate for is sum_arr//2 


# minimum difference 
we can run an loop from sum_Arr//2 to 0, and find subset sum for the array, if yes return sum-2*s1 else continue..

'''
# fails for some edge cases negative values..
def minimize_subset_diff(arr):
    sum_arr=sum(arr[:])
    # def recur_subset_diff(i,target):
    #     if i<0:
    #         return abs(sum_arr-(2*target)) # abs diff
        
    #     if arr[i]<=target:
    #         return min(recur_subset_diff(i-1,target-arr[i]),recur_subset_diff(i-1,target))
    #     else:
    #         return recur_subset_diff(i-1,target)
        
    # #return recur_subset_diff(len(arr)-1,sum_arr//2)

    #tabualation
    t=[[False for _ in range(sum_arr+1)] for _ in range(len(arr)+1)]
    for i in range(len(arr)+1):
        t[i][0]=True # first column is one
    for i in range(len(arr)+1):
        for j in range(sum_arr+1):
            if arr[i-1]<=j:
                t[i][j]=t[i-1][j-arr[i-1]] or t[i-1][j]
            else:
                t[i][j]=t[i-1][j]
    min_diff=float("inf")
    for i in range((sum_arr//2)+1):
        if t[len(arr)][i]:
            min_diff=min(min_diff,sum_arr-(2*i))
    return min_diff
        

if __name__=="__main__":
    arr=list(map(int, input().split()))
    print(minimize_subset_diff(arr))
