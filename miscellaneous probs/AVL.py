#create an avl tree that gets first 100 elements and updates the self balancing binary tree



class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        self.height=1
    
class AVL:
    def __init__(self):
        self.root=None

    def height(self,node):
        if node==None:
            return 0
        return node.height
    

    def insert(self,value):
        self.root=self.insert_node(value,self.root)

    def insert_node(self,value,node):
        if node==None:
            return Node(value)
        if value<node.value:
            node.left=self.insert_node(value,node.left)

        else:
            node.right=self.insert_node(value,node.right)

        node.height=1+max(self.height(node.left),self.height(node.right))
        return self.rotate(node)
    
    def rotate(self,node):
        if self.height(node.left)-self.height(node.right)>1:
            if self.height(node.left.left)-self.height(node.left.right)>=0:
                #left left case
                return self.rightRotate(node)
            else:
                node.left=self.leftRotate(node.left)
                return self.rightRotate(node)
        if self.height(node.right)-self.height(node.left)>1:
            if self.height(node.right.right)-self.height(node.right.left)>=0:
                return self.leftRotate(node)
            else:
                node.right=self.rightRotate(node.right)
                return self.leftRotate(node)
        return node
    
    def rightRotate(self,node):
        c=node.left
        t=c.right

        c.right=node
        node.left=t

        c.height=1+max(self.height(c.left),self.height(c.right))
        node.height=1+max(self.height(node.left),self.height(node.right))
        return c
    
    def leftRotate(self,node):
        c=node.right
        t=c.left

        c.left=node
        node.right=t

        c.height=1+max(self.height(c.left),self.height(c.right))
        node.height=1+max(self.height(node.left),self.height(node.right))
        return c


    
    def populate(self,arr):
        self.populate_sorted(arr,0,len(arr)-1)
    
    def populate_sorted(self,arr,start,end):
        if start>end:
            return 
        mid=(start+end)//2
        self.insert(arr[mid])
        self.populate_sorted(arr,start,mid-1)
        self.populate_sorted(arr,mid+1,end)

    def display(self):
        self.display_tree(self.root,"root node: ")

    def display_tree(self,node,details):
        if node==None:
            return 
        print(details +str(node.value))
        self.display_tree(node.left,f"left child of {node.value}: ")
        self.display_tree(node.right,f"right child of {node.value}: ")

    

if __name__=="__main__":
    b=AVL()
    arr=list(range(1,11))
    for ele in arr:
        b.insert(ele)
    
    b.display()

