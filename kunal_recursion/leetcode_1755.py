# this is a meet in the middle algorithm
'''
this is the blueprint for any problem with subset sum & minimize difference with a integer goal.. 
step 1) make two arrays by splitting in half
step 2) generate all subsets of each half 
step 3) sort the second half and apply lower bound of every element in first half in second half
step 4) maintain a global minimum variable and keep on updating it ..
'''

class meet_in_middle:

    def lower_bound(self,arr,val):
        l,r=0,len(arr)
        while l<r:
            m=(l+r)//2
            if arr[m]<val:
                l=m+1
            else:
                r=m
        return l 

    def split_half(self,arr):
        if len(arr)%2==0:
            first_half=arr[:len(arr)//2]
            second_half=arr[len(arr)//2:]
        else:
            first_half=arr[:len(arr)//2+1]
            second_half=arr[len(arr)//2+1:]
        return [first_half,second_half]
    
    def generate_subsets(self,arr,ind,curr_subs,total_subs):
        if ind<0:
            total_subs.add(curr_subs)
            return
        self.generate_subsets(arr,ind-1,curr_subs+(arr[ind]),total_subs) #pick and move
        self.generate_subsets(arr,ind-1,curr_subs,total_subs) # not pick and move

    def closest_subs_sum(self,subs1,subs2,goal):
        sub2_list=sorted(list(subs2))
        ans=float("inf")
        for subs1_ele in subs1:
            needed_ele=goal-subs1_ele
            lb=self.lower_bound(sub2_list,needed_ele)  # index of the first element greater or equal to goal
            if lb<len(sub2_list): # in case where sums1[i]+sums2[i]>=goal but near to goal
                lb_val= sub2_list[lb]
                ans=min(ans,abs(goal-(subs1_ele+lb_val)))
            if lb>0:  # in case where sums1[i]+sums2[i]<goal but near to goal.
                lb_val_1= sub2_list[lb-1]
                ans=min(ans,abs(goal-(subs1_ele+lb_val_1)))
        return ans

if __name__=="__main__":   
    t=meet_in_middle()
    arr=list(map(int,input().split()))
    goal=int(input())
    first_half,second_half=t.split_half(arr)
    subs1,subs2=set(),set()
    t.generate_subsets(first_half,len(first_half)-1,0,subs1)
    t.generate_subsets(second_half,len(second_half)-1,0,subs2)
    print(t.closest_subs_sum(subs1,subs2,goal))
