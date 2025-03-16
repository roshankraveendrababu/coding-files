#creating an binary search tree and inserting value from an sorted array and make it non skewed

class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
    
class BST:
    def __init__(self):
        self.root=None
    def insert(self,value):
        self.root=self.insert_node(value,self.root)

    def insert_node(self,value,root):
        if root==None:
            return Node(value)
        if value<root.value:
            root.left=self.insert_node(value,root.left)

        else:
            root.right=self.insert_node(value,root.right)
        return root
    
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

    def in_order(self,node):
        if node==None:
            return
        self.in_order(node.left)
        print(node.value)
        self.in_order(node.right)

    def find_min(self,node):
        if node.left==None:
            return node.value
        return self.find_min(node.left)
    
    def search_element(self,root,value):
        if root==None: # base case :the required element is not in the binary tree
            return False
        if root.value==value:
            return True
        if value<root.value: #value is smaller than the current value and hence it will be in the left subtree
            return self.search_element(root.left,value)
        else: #value is greater than the current value and hence it will be in the right subtree
            return self.search_element(root.right,value)
        

    def remove_ele(self,val,node):
        if not node:#the element is not present in the binary tree
            return None
        if val<node.value:
            node.left=self.remove_ele(val,node.left) #everytime we are returning a node hence we should assign it to a node
        elif val>node.value:
            node.right=self.remove_ele(val,node.right)
        else: 
            if not node.left: #for case 1: if there is no left child , the right child can be null or have an value which will be the child of the parent of the node to be removed
                return node.right
            elif not node.right: #same for the right child
                return node.left
            else: # case 2 where the node to be removed has both left and right child
                min_val=self.find_min(node.right)  #find the minimum value in the right subtree of the node to be removed
                node.value=min_val  #replace the value of the node to be removed with the minimum value in the right subtree
                node.right=self.remove_ele(min_val,node.right) #now remove the minimum value from the right subtree
        return node  #returning the node after removing the element or just the default case

if __name__=="__main__":
    b=BST()
    arr=[1,2,3,4,5,6,7,8,9]
    b.populate(arr)
    #b.display()
    #print(b.find_min(b.root))
    #print(b.search_element(b.root,15))
    b.remove_ele(5,b.root)
    b.display()

