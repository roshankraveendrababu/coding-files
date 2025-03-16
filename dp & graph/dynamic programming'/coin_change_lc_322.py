def find_min_coins(coins,amount):
    ans=coin_change_1(coins,len(coins)-1,amount)
    return ans if ans!=float("inf") else -1

def coin_change_1(arr,ind,amount):
    if ind<0:
        if amount==0:
            return 0
        return float("inf")
    if arr[ind]<=amount:
        return min(1+coin_change_1(arr,ind,amount-arr[ind]),coin_change_1(arr,ind-1,amount))
    else:
        return coin_change_1(arr,ind-1,amount)
    
def coin_change_tabulation(arr,amount):
    t=[[0 for _ in range(amount+1)] for _ in range(len(arr)+1)]
    for i in range(amount+1):
        t[0][i]=float("inf")
    for i in range(1,len(arr)+1):
        for j in range(1,amount+1):
            if arr[i-1]<=j:
                t[i][j]=min(1+t[i][j-arr[i-1]],t[i-1][j])
            else:
                t[i][j]=t[i-1][j]
    ans=t[len(arr)][amount]
    return ans if ans!=float("inf") else -1
    
if __name__=="__main__":
    arr=list(map(int,input().split()))
    amount=int(input())
    print(coin_change_tabulation(arr,amount))