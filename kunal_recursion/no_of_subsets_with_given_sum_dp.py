'''
find the number of subsets whose sum is equal to target
given an target and array -- hence it is a knapsack problem
we use pick and not pick method
as we have to cnt we return 1/0 in base case
we use cnt variable to find cnt 
'''
# this is the recursive code having complexity of 2^len(arr)..
def cnt_subsets(arr,target):
    def no_of_subsets(i,target):
        if target==0:
            return 1
        if i<0: # array is exhausted but the target is remaining..
            return 0
        cnt=0
        if arr[i]<=target:
            cnt+=no_of_subsets(i-1,target-arr[i])
            cnt+=no_of_subsets(i-1,target)
        else:
            cnt=no_of_subsets(i-1,target)
        return cnt
    return no_of_subsets(len(arr)-1,target)


# we will write the tabulation code.. the values changing ar len(arr) and target
def cnt_subsets_tabulation(arr,target):
    t=[[0 for _ in range(target+1)] for _  in range(len(arr)+1)]
    for i in range(len(arr)+1):
        t[i][0]=1
    for i in range(1,len(arr)+1):
        for j in range(1,target+1):
            if arr[i-1]<=j:
                t[i][j]=t[i-1][j-arr[i-1]]+t[i-1][j]
            else:
                t[i][j]=t[i-1][j]
    return t[len(arr)][target]


if __name__=="__main__":
    arr=list(map(int, input().split()))
    target=int(input())
    print(cnt_subsets_tabulation(arr,target))