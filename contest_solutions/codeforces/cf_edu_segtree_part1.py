# segment tree is one of the most widely used ds for contest and interviews. 
# in these code we try to replicate the codes from cf-edu-pilot-segtree course

# 1) segtree with two operation of sum of an subarray and set an index with an value with build function to build the tree from scratch from an array

# 2) segtree storing minimum and the cnt of elements equal to minimum for each segment

# 3) segtree storing the maximum value subsegment for each segment 
#       this is an awesome approach .. seg=max(seg1,seg2,suf1+pref2)  .. pref=max(pref1,sum1+pref2) .. suf=max(suf2,sum2+suf1) .. sum=sum1+sum2

# 4) segtree to find the index of 1 which is the kth one in the binary array 

# 5) segtree for finding the index of the first element whose value is greater than or equal to x 
        # solves this but updation causes tle in the leetcode qns..
# 5a ) segtree to find the index of the first element whose value is greater than or equal to x after a particular index
#       a[i]>=x and i>=l

# 6) given an array nums return back an array denoting the no of inversion for each element in array.
#    construct an empty array of size len(nums) .. iterate over the nums and find the sum in range (nums[i]+1 to end)  and change 
#    arr[nums[i]] to 1.  this is the set and query operation which both take O(logn) time..

# 7) given an array of no of inversions for an original array . construct the original arr
#    construct an array of all ones , and find the sum from each index to end . this is the initial segtree
#    now iterate over the inversion array from backward , find the index in the segtree which has the value same as in inversion_arr[i]
#    change the value in the segtree to 0 , and construct the tree again
#    operations needed: set and query .. T(c)=O(nlogn)

# 8) given an array of size 2*n containing every element from 1 to n exactly twice . find the no of no of segments present within the 
#    segment [i].. 
#    ex: 5 4 3 2 1 1 2 3 4 5 .. in the the value of 5 is 4 coz the segments of 1,2,3,4 are present within the boundary.
#    xyyx , in this y is an nested segment of x.
#    array of zeros and ones which the left boundary of already visited as 1.. for each element, find the sum from its left to right 
#    boundary which denots the no of inversion.. change the left boundary of this element to 1 so that future elements can use it ..

# 9) same as the above now instead of finding nested segments we need to find intersecting segments.
#    intersecting segment means that only one boundary of an number is present within the end boundaries of the current number .
#    initially all the left boundaries will be 1, now we change it to 0 if its right boundary is within our range ..  
#    traversal type is left to right ..
#    This is done to find the no of intersecting segments whose right boundary is not in range .. we need to do the same for left boundary too.
#    that is done by reversing the array and doing the same process again..
#    sum of these two values is the required value ..
#    after computing the above , we change the left boundary of the current range as also 0, for the next iterations to use them. 

## things learnt from problem 6 to 9:
#   whenver we are dealing with cnt or no's of something , we should construct a segtree of 0's and 1's and manipulate them ..
#   most probably it will be an segtree to find the sum effectively...


# 10) build an segtree supporting two operations
# add(l,r,v)  add v to all elements in the range from l to r  -- only one such operation
# get(i)  get the value in the index i
# we should have TC=O(nlogn), 
# step 1: for the first case we add v to left boundary and subtract v from the right boundary . i.e, set operation
# step 2: we need to find the prefix sum of 0 to i inclusive hence add operation ..
# hence an segtree for sum is used in this case ..
# for second operation , prefix sum from 0 to l have not changed, l to r is +v , r to end is same ..
# hence we avoiding using O(n) for the first task , use tricks and reduce TC. will get it with time ..

# 11) build a segtree supporting two operations  (mass changing operations..)
# add(l,r,v) add v to all elements in the range l to r
# get(i) get value at index i
# initially we will have an array of 0's, if not given an array or an max segtree.
# there will be many type 1 operation , which can be overlapping
# how to do it .. 1) same as the get_sum function in the previous sums, completely inside : add v to curr node 
# the second function , finds the sums of the path from root to i .. this gives us the value at node i ..
# this is a very good technique with wide variety of application..

# when can we use the above method ?? when we do two or more operations , they should be combinable into just 1 ..(commutatitive & associative)
# EX. in the above qn , we can combine 2 or more addition into a single addition..
# other ex: min, max, sum, product, GCD, LCM , &, ||, ^, U, intersection, 

# 12) constructing segtree for an non commutative property .. ( moss non-commutative change operations )
#  now we need to store the order of operations performed on each node..  
# ( leaf has the old operations , root has the new op).. hence when we return from the recursion , we build the answer same way ..(old->new)
# this can be done with a famous cp technique called as lazy propogation.. ( moves operations down the tree )
# we can combine and store operations at each node , so that the upper node becomes empty .. ex: root is x and its left child is y
# now, its left child becomes (y op x) and the root is empty .
# this propogation can be done in constant time , as we can do it in the time of building the tree itself ..
# we should mark the nodes that dont have any op in them ..( we can store some neutral element in them (int_max or int_min))..
# we can push all operations to the leaf node thereby only the leaf nodes will, have any value ..
# make a propogate function and call it at the start of all the recursive function .. (implements the above point).
# ex: assignment operation, matrix multiplication  ..


# solve leetcode weekly 440 q3) -- done

class segtree: # working perfectly hehe
    def __init__(self,n):
        self.size=1
        while self.size<n:
            self.size*=2
        self.seg_arr=[0]*(2*self.size)

    def build(self,arr):
        self.build_segtree(arr,0,0,self.size)

    def build_segtree(self,arr,x,lx,rx):
        if rx-lx==1: # child node
            if lx<len(arr):
                self.seg_arr[x]=arr[lx]
            return
    
        m=(lx+rx)//2
        self.build_segtree(arr,2*x+1,lx,m)
        self.build_segtree(arr,2*x+2,m,rx)

        self.seg_arr[x]=self.seg_arr[2*x+1]+self.seg_arr[2*x+2]

    def set(self,i,v):
        self.set_segtree(i,v,0,0,self.size)

    def set_segtree(self,i,v,x,lx,rx):
        if rx-lx==1: # curr node is the child node
            self.seg_arr[x]=v
            return
        m=(lx+rx)//2
        if i<m: # the index belong the left half
            self.set_segtree(i,v,2*x+1,lx,m)
        else:
            self.set_segtree(i,v,2*x+2,m,rx)
        
        self.seg_arr[x]=self.seg_arr[2*x+1]+self.seg_arr[2*x+2] # we have recalculate the node values of the parent

    def add(self,l,r):
        return self.add_seg(l,r,0,0,self.size)
    
    def add_seg(self,l,r,x,lx,rx):
        # lx and rx are the boundaries of the current node
        # Base Case 1) completely outside the required range
        if rx<=l or lx>=r:
            return 0
        
        # Base Case 2) completely inside the required range
        if lx>=l and rx<=r: 
            return self.seg_arr[x]
        
        m=(lx+rx)//2
        return self.add_seg(l,r,2*x+1,lx,m)+self.add_seg(l,r,2*x+2,m,rx) # we need to return from the recursive call from both childs
    
    def find_seg(self,l,r):
        return self.find_largest_seg(l,r,0,0,self.size)
    
    


if __name__=="__main__":
    
    arr=list(map(int,input().split()))
    t=segtree(len(arr))
    t.build(arr)
    print(t.seg_arr)
    t.set(2,4)
    t.set(5,7)
    print(t.seg_arr)
    print(t.add(2,3))
    print(t.add(1,5))





