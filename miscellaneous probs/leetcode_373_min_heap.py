import heapq
def find_k_smallest_pairs(nums1,nums2,k):
    arr=[]
    ans=[]
    for i in range(len(nums1)):
        arr.append([nums1[i]+nums2[0],nums1[i],nums2[0],0]) # store sum , value from nums1 and nums2 and index at nums2
    heapq.heapify(arr)
    while k:
        k-=1
        sum_val,nums1_val,nums2_val,nums2_ind=heapq.heappop(arr)
        ans.append([nums1_val,nums2_val])
        if nums2_ind==len(nums2)-1:
            continue
        heapq.heappush(arr,[nums1_val+nums2[nums2_ind+1],nums1_val,nums2[nums2_ind+1],nums2_ind+1])
    return ans

if __name__=="__main__":
    k=int(input())
    nums1=list(map(int,input().split()))
    nums2=list(map(int,input().split()))
    print(find_k_smallest_pairs(nums1,nums2,k))