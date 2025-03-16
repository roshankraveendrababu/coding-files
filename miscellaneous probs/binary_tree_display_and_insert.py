#code to create an binary tree and display it

class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinaryTree:
    def insert(self):
        root=Node(int(input("Enter the value of the root node: \n")))
        self.populate(root)
        self.display(root,"")
        self.pre_order(root)
        self.post_order(root)  
    def populate(self,value):
        left=int(input(f"do you want a left child for {value.value}: \n"))
        if left:
            value.left=Node(int(input("enter the value of the left child: \n")))
            self.populate(value.left)

        right=int(input(f"do you want a right child for {value.value}: \n"))
        if right:
            value.right=Node(int(input("enter the value of the right child: \n")))
            self.populate(value.right)

    def display(self,node,indent):
        if node==None:
            return 
        print(indent+str(node.value))
        self.display(node.left,indent+"  ")
        self.display(node.right,indent+"  ")

    def pre_order(self,node):
        if node==None:
            return 
        print(node.value)
        self.pre_order(node.left)
        self.pre_order(node.right)

    def post_order(self,node):
        if node==None:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        print(node.value)

if __name__=="__main__":
    b=BinaryTree()
    b.insert()
    

    
        


        