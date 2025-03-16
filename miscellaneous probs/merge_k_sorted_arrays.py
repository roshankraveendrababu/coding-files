# this solution has an space complexity of O(k)
import heapq
def merge_k_sorted_arrays(karrays,k):
    arr=[]
    for i in range(k):
        arr.append([karrays[i][0],0,i])
    heapq.heapify(arr)
    ans=[]
    while arr:
        ele,ele_ind,list_num=heapq.heappop(arr)
        ans.append(ele)
        if ele_ind+1<len(karrays[list_num]):
            heapq.heappush(arr,[karrays[list_num][ele_ind+1],ele_ind+1,list_num])
    return ans 

if __name__=="__main__":
    k=int(input())
    karrays=[]
    for _ in range(k):
        karrays.append(list(map(int,input().split())))
    print(merge_k_sorted_arrays(karrays,k))