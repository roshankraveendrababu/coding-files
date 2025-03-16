class Node:
    def __init__(self,start,end):
        self.value=None  # we need to first create its child before assigning value to it
        self.start=start
        self.end=end
        self.left=None
        self.right=None

class SegmentTree:
    def __init__(self,arr):
        self.root=self._construct_tree(arr,0,len(arr)-1) #creating the root node of the segment tree

    def _construct_tree(self,arr,start,end):
        if start==end: #base case: leaf node
            node= Node(start,end)
            node.value=arr[start]
            return node
        node=Node(start,end) 
        mid=(start+end)//2
        node.left=self._construct_tree(arr,start,mid) #creating the left subtree by calling left child
        node.right=self._construct_tree(arr,mid+1,end) #creating the right subtree by calling right child
        node.value=node.left.value+node.right.value #parent node value= left child value+right child value
        return node #returning the parent node
    
    def display(self):
        self._display_tree(self.root,"root node: ")

    def _display_tree(self,node,details):
        if node==None:
            return
        print(details +str(node.value))
        if node.left is not None:
            self._display_tree(node.left,f"Left child of {node.value} and interval= {node.left.start}-{node.left.end} : ")
        if node.right is not None:
            self._display_tree(node.right,f"Right child of {node.value}and interval= {node.right.start}-{node.right.end} : ")

    def query(self,query_start,query_end):
        return self._query(self.root,query_start,query_end)
    
    def _query(self,node,q_start,q_end):
        if node.start>=q_start and node.end<=q_end:
            return node.value
        if node.start>q_end or node.end<q_start:
            return 0
        return self._query(node.left,q_start,q_end)+self._query(node.right,q_start,q_end)
    
    def update(self,index,value):
        self._update(self.root,index,value)
    
    def _update(self,node,index,value):
        if node.start==node.end==index:
            node.value=value
            return node.value
        if index<node.start or index>node.end:
            return node.value
        else:
            node.value=self._update(node.left,index,value)+self._update(node.right,index,value)
            return node.value
        
if __name__=="__main__":
    arr=[1,2,3,4,5,6,7,8]
    b=SegmentTree(arr)
    #b.display()
    #print(b.query(1,4))
    b.update(2,10)
    b.display()
    print(b.query(1,4))

        

    
    

