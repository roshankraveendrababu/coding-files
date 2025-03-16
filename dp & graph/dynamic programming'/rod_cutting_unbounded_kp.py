'''
this is an unbounded knapsack problem wherein we have to maximise the rod price.
parameters: rod length, ind, arr , curr price
choices: pick : rod length-arr[ind],ind,arr if arr[ind]<=rod length
         not pick : rod length, ind-1,arr

         we will use max of them.
    
base case:
    if ind<0: return cur price
'''


def find_max_price(length_arr,price_arr,rod_length):
    #tabulation method changed from knapsack problem
    t=[[0 for _ in range(rod_length+1)] for _ in range(len(price_arr)+1)]
    for i in range(1,len(arr)+1):
        for j in range(1,rod_length+1):
            if length_arr[i-1]<=j:
                t[i][j]=max(price_arr[i-1]+t[i][j-length_arr[i-1]],t[i-1][j])
            else:
                t[i][j]=t[i-1][j]
    return t[len(price_arr)][rod_length]
    
    
if __name__=="__main__":
    arr=list(map(int,input().split()))
    length_arr=[i+1 for i in range(len(arr))]
    rod_length=len(arr)
    print(find_max_price(length_arr,arr,rod_length))