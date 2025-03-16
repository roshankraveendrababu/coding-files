class Solution:
    def candy(self,ratings):
        # using slope based greedy approach
        n=len(ratings)
        ans=n
        i=1
        while i<n:
            if ratings[i]==ratings[i-1]:
                i+=1  # we alredy counted 1 for this child in the final answer
                continue
            inc=0 # we start at 0 coz the first occurence of increase is 1 which is already counted
            while i<n and ratings[i]>ratings[i-1]:
                inc+=1
                ans+=inc
                i+=1
            dec=0
            while i<n and ratings[i]<ratings[i-1]:
                dec+=1
                ans+=dec
                i+=1
            ans-=min(inc,dec) # we added the peak element twice for both iteration hence we subtract the lower half one
        return ans

if __name__=="__main__":
    ans=Solution()
    t=3
    for _ in range(t):
        ratings=list(map(int, input().split()))
        print(ans.candy(ratings))