'''
we need to find two subsets of an array such that subset1-subset2=diff
we know that subset1+subset2=total

by adding them both , we get 2*subset1=diff+total
subset1=diff+total//2

for positive values of subset needed, we can use tabulation method 
otherwise, we have to use memoization

we can also use meet in the middle algo , wherein we add map the subsets .. and try to find its corresponding and increase cnt ..

'''
class cnt_diff_meet_middle:
    def split_half(self,arr):
        if len(arr)%2==0:
            first_half=arr[:len(arr)//2]
            second_half=arr[len(arr)//2:]
        else:
            first_half=arr[:len(arr)//2+1]
            second_half=arr[len(arr)//2+1:]
        return [first_half,second_half]
    
    def generate_subsets(self,arr,i,curr_sum,total_subs):
        if i<0:
            if curr_sum in total_subs:
                total_subs[curr_sum]+=1
            else:
                total_subs[curr_sum]=1
            return
        #pick and not pick 
        self.generate_subsets(arr,i-1,curr_sum+arr[i],total_subs)
        self.generate_subsets(arr,i-1,curr_sum,total_subs)

    def find_cnt(self,subs1,subs2,goal):
        cnt=0
        for i in range(goal+1):
            if i in subs1:
                needed=goal-i
                if needed in subs2:
                    cnt+=(subs1[i]*subs2[needed])
        return cnt


    
#tabulation:
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

def meet_in_the_middle(arr,diff):
    #split,generate subsets and store in a map and iterate over one map and find the total cnt ..
    t=cnt_diff_meet_middle()
    sum_arr=sum(arr[:])
    target=(sum_arr+diff)//2
    first_half,second_half=t.split_half(arr)
    subsets_of_1,subsets_of_2={},{}
    t.generate_subsets(first_half,len(first_half)-1,0,subsets_of_1)
    t.generate_subsets(second_half,len(second_half)-1,0,subsets_of_2)
    return t.find_cnt(subsets_of_1,subsets_of_2,target)

if __name__=="__main__":
    arr=list(map(int, input().split()))
    diff=int(input())
    print(meet_in_the_middle(arr,diff))