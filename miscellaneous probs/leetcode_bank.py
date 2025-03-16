import math
class Solution:
    def totalMoney(self, n: int) -> int:
        ans=0
        weeks=math.ceil(n/7)
        for week in range(weeks):
            days=min(7,n)
            curr_cnt=((days+week)*(days+week+1))//2
            remainder=((week)*(week+1))//2
            ans=ans+curr_cnt-remainder
            n-=7
        return ans
    
if __name__=="__main__":
    cnt=Solution()
    print(cnt.totalMoney(20000000))

        
        

        
        