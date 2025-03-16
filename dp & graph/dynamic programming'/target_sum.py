'''
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

recursion -->tabulation
parameters for recursion -- arr, index, sum
as we require cnt , we should return 1 or 0 in base case
we should pick each number , but the two cases should be +i and -i..

we can find two subsets whose diff is target ..
hence , subs1-subs2=diff
subs1+subs2=total
2*subs1=diff+total
subs1=diff+total//2


'''
def find_cnt(arr,diff):
    arr_sum=sum(arr[:])
    subs1_sum=(diff+arr_sum)//2
    return tabu_find_cnt(arr,subs1_sum)

def tabu_find_cnt(arr,target):
    t=[[0 for _ in range(target+1)] for _ in range(len(arr)+1)]
    for i in range(len(arr)+1):
        t[i][0]=1
    for i in range(1,len(arr)+1):
        for j in range(1,target+1):
            if arr[i-1]<=j:
                t[i][j]=t[i-1][j]+t[i-1][j-arr[i-1]]
            else:
                t[i][j]=t[i-1][j]
    return t[len(arr)][target]


if __name__=="__main__":
    arr=list(map(int, input().split()))
    target=int(input())
    print(find_cnt(arr,target))