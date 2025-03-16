# construct a segtree that find the index of the kth user given one in a binary tree
# as it is a binary tree, we can use sum as the method to find the number of ones in a range ..

class segtree:
    def __init__(self,n):
        self.size=1
        while (self.size<n):
            self.size*=2
        self.arr_segtree=[0]*(2*self.size)

    def build(self,arr):
        self._build_segtree(arr,0,0,self.size)
    
    def _build_segtree(self,arr,x,lx,rx):
        if rx-lx==1:
            if lx<len(arr):
                self.arr_segtree[x]=arr[lx]
            return
        
        m=(lx+rx)//2
        self._build_segtree(arr,2*x+1,lx,m)
        self._build_segtree(arr,2*x+2,m,rx)
        #parent node should store the sum of the child nodes
        self.arr_segtree[x]=self.arr_segtree[2*x+1]+self.arr_segtree[2*x+2]

    
    def set(self,ind,val):
        self._set_segtree(ind,val,0,0,self.size)

    def _set_segtree(self,ind,val,x,lx,rx):
        if rx-lx==1:
            self.arr_segtree[x]=val

        #assign the value
        m=(lx+rx)//2
        if ind<m:
            self._set_segtree(ind,val,2*x+1,lx,m)
        else:
            self._set_segtree(ind,val,2*x+2,m,rx)
        
        #change the parent value
        self.arr_segtree[x]=self.arr_segtree[2*x+1]+self.arr_segtree[2*x+2]
