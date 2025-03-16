# You are given two integer arrays, nums1 and nums2, both of length n, along with a positive integer k.

# For each index i from 0 to n - 1, perform the following:

# Find all indices j where nums1[j] is less than nums1[i].
# Choose at most k values of nums2[j] at these indices to maximize the total sum.
# Return an array answer of size n, where answer[i] represents the result for the corresponding index i.

#  

# Note: Please do not copy the description during the contest to maintain the integrity of your submissions.

#brute force=O(n^2) . this wont work coz here n =10^5


#Approach used- *sorting to get the index of lower elements along with their index
#               * Min heap to remove the smallest element and keep the k largest elements.
#               * We will keep an single array for heap and do sum operation in O(1) per index
#               * edge case: if the nums1 has duplicate we shouldn't add the same element to heap or total_sum .
            #   * hence we add the same previous output as the current output.
#               *nlogn for sorting and klogk for heap operation
import heapq
class Solution:
    def K_Elements_With_Maximum_Sum(self,nums1,nums2,k):
        nums1_with_index=[[nums1[i],nums2[i],i] for i in range(len(nums1))]
        nums1_with_index.sort(key=lambda x:(x[0],x[1]))
        total_sum=0
        ans=[0]*len(nums1)
        heap=[]
        for i in range(len(nums1_with_index)):
            if i>0 and nums1_with_index[i][0]==nums1_with_index[i-1][0]: # checking for duplicate value
                ans[nums1_with_index[i][2]]=ans[nums1_with_index[i-1][2]] # updating the same value in the final ans array
            else:
                ind=nums1_with_index[i][2]
                ans[ind]=total_sum
                heapq.heappush(heap,nums1_with_index[i][1])
                total_sum+=nums1_with_index[i][1]
                if len(heap)>k:
                    total_sum -= heapq.heappop(heap)  # Ensures we subtract the correct popped element
        return ans
    
if __name__=="__main__":
    weekly_440=Solution()
    k=int(input())
    nums1=list(map(int, input().split()))
    nums2=list(map(int , input().split()))
    print(weekly_440.K_Elements_With_Maximum_Sum(nums1,nums2,k))
