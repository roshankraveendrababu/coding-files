# segtree storing the minimum in a index and the no of elements equal to the minimum
# supports set and query operation
class segtree:
    def __init__(self,n):
        self.size=1
        while self.size<n:
            self.size*=2
        self.arr_segtree=[[float("inf"),0] for _ in range(2*self.size)] # each node stores minimum and its cnt

    def build(self,arr):
        self.build_segtree(arr,0,0,self.size)

    def build_segtree(self,arr,x,lx,rx):
        if rx-lx==1:
            if lx<len(arr):
                self.arr_segtree[x]=[arr[lx],1]
            return
        m=(lx+rx)//2
        self.build_segtree(arr,2*x+1,lx,m)
        self.build_segtree(arr,2*x+2,m,rx)
        if self.arr_segtree[2*x+1][0]<self.arr_segtree[2*x+2][0]: # finding the minimum child
            self.arr_segtree[x]=self.arr_segtree[2*x+1].copy()
        elif self.arr_segtree[2*x+1][0]>self.arr_segtree[2*x+2][0]: # finding the minimum child
            self.arr_segtree[x]=self.arr_segtree[2*x+2].copy()
        else: # both child are same , hence the mini cnt will be the sum of them. 
            self.arr_segtree[x]=[self.arr_segtree[2*x+1][0],self.arr_segtree[2*x+1][1]+self.arr_segtree[2*x+2][1]]

    def set(self,i,v):
        self.set_segtree(i,v,0,0,self.size)

    def set_segtree(self,i,v,x,lx,rx):
        if rx-lx==1: # curr node is the leaf node
            self.arr_segtree[x]=[v,1]
            return 
        m=(lx+rx)//2
        if i<m:
            self.set_segtree(i,v,2*x+1,lx,m)
        else:
            self.set_segtree(i,v,2*x+2,m,rx)


        if self.arr_segtree[2*x+1][0]<self.arr_segtree[2*x+2][0]: # finding the minimum child
            self.arr_segtree[x]=self.arr_segtree[2*x+1].copy()
        elif self.arr_segtree[2*x+1][0]>self.arr_segtree[2*x+2][0]: # finding the minimum child
            self.arr_segtree[x]=self.arr_segtree[2*x+2].copy()
        else: # both child are same , hence the mini cnt will be the sum of them. 
            self.arr_segtree[x]=[self.arr_segtree[2*x+1][0],self.arr_segtree[2*x+1][1]+self.arr_segtree[2*x+2][1]]

    def get_min(self,l,r):
        return self.get_min_segtree(l,r,0,0,self.size)
    
    def get_min_segtree(self,l,r,x,lx,rx):
        #lx,rx curr node boundary and l,r is the required boundary
        # 2 base case and 1 recursion case
        if rx<=l or lx>=r:
            return [float("inf"),0] # the base value this can never be the answer for an minimum query
        if lx>=l and rx<=r:
            return self.arr_segtree[x].copy()
        
        # the current node has a part of the answer, get the both answers in a variable and do the same 
        m=(lx+rx)//2
        left_tree=self.get_min_segtree(l,r,2*x+1,lx,m)
        right_tree=self.get_min_segtree(l,r,2*x+2,m,rx)
        if left_tree[0]<right_tree[0]: # finding the minimum child
            return left_tree
        elif left_tree[0]>right_tree[0]: # finding the minimum child
            return right_tree
        else: # both child are same , hence the mini cnt will be the sum of them. 
            return [left_tree[0],right_tree[1]+left_tree[1]]

if __name__=="__main__":
    arr=list(map(int,input().split()))
    t=segtree(len(arr))
    t.build(arr)
    # t.set(4,5)
    # t.set(5,5)
    # t.set(6,5)
    print(t.arr_segtree)
    print(t.get_min(0,11))
    print(t.get_min(7,11))
    print(t.get_min(0,3))

    