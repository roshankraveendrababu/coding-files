# segtree storing the maximum sum sub-segment for every segment
# approach we need to store sum,prefix,suffix and max segment
# parent node will be max_seg=max(max_seg1,max(max_seg2,suff1+pref2))
# pref=max(pref1,sum1+pref2)
# suff=max(suff2,sum2+suff1)
# sum=sum1+sum2

class segtree:
    def __init__(self,n):
        self.size=1
        while self.size<n:
            self.size*=2
        self.arr_segtree=[[0,0,0,0] for _ in range(2*self.size)] # store max_Seg,prefix, suffix , sum
    
    def create_node(self,x):
        left_val=self.arr_segtree[2*x+1]
        right_val=self.arr_segtree[2*x+2]
        max_seg=max(left_val[0],max(right_val[0],left_val[2]+right_val[1]))
        pref=max(left_val[1],left_val[3]+right_val[1])
        suff=max(right_val[2],right_val[3]+left_val[2])
        sum_val=right_val[3]+left_val[3]
        return [max_seg,pref,suff,sum_val]


    def build(self,arr):
        self.build_segtree(arr,0,0,self.size)

    def build_segtree(self,arr,x,lx,rx):
        if rx-lx==1:
            if lx<len(arr):
                self.arr_segtree[x]=[max(0,arr[lx]),max(0,arr[lx]),max(0,arr[lx]),arr[lx]] # for leaf node all the values will be the same ..
            return
        
        m=(lx+rx)//2
        self.build_segtree(arr,2*x+1,lx,m)
        self.build_segtree(arr,2*x+2,m,rx)
        # we will give the node formation form scratch to a function
        self.arr_segtree[x]=self.create_node(x)

    def set(self,i,v):
        self.set_segtree(i,v,0,0,self.size)

    def set_segtree(self,i,v,x,lx,rx):
        if rx-lx==1: # child node 
            self.arr_segtree[x]=[max(0,v),max(0,v),max(0,v),v]
            return
        m=(lx+rx)//2
        if i<m:
            self.set_segtree(i,v,2*x+1,lx,m)
        else:
            self.set_segtree(i,v,2*x+2,m,rx)
        
        self.arr_segtree[x]=self.create_node(x)

    def max_segtree(self,l,r):
        return self.get_max_segtree(l,r,0,0,self.size)
    
    def get_max_segtree(self,l,r,x,lx,rx):
        # if rx<=l or lx>=r:
        #     return float("-inf")
        # if lx>=l and rx<=r:
        #     val=self.arr_segtree[x]
        #     return val[0]
        # m=(lx+rx)//2
        # left_val=self.get_max_segtree(l,r,2*x+1,lx,m)
        # right_val=self.get_max_segtree(l,r,2*x+2,m,rx)
        # return max(left_val,right_val)
        val=self.arr_segtree[0]
        return val[0]
    
if __name__=="__main__":
    nm=list(map(int,input().split()))
    n,m=nm[0],nm[1]
    t=segtree(n)
    arr=list(map(int,input().split()))
    t.build(arr)
    print(t.max_segtree(0,n))
    for i in range(m):
        iv=list(map(int,input().split()))
        i,v=iv[0],iv[1]
        t.set(i,v)
        print(t.max_segtree(0,n))

    