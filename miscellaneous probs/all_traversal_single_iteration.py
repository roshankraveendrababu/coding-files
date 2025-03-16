# create an binary tree and print all its three traversal using only one iteration

class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class Tree:
    def insert_root(self,value):
        self.root=Node(value)
        self.populate(self.root)
        self.display(self.root,"")
        self.traversal(self.root)
    def populate(self,node):
        left_child=int(input(f"do you want the left child of {node.value}: "))
        if left_child:
            node.left=Node(int(input(f"enter the value of the left child of {node.value}: ")))
            self.populate(node.left)
        right_child=int(input(f"do you want the right child of {node.value}: "))
        if right_child:
            node.right=Node(int(input(f"enter the value of the right child of {node.value}:")))
            self.populate(node.right)

    def display(self,node,indent):
        if node==None:
            return
        print(indent+str(node.value))
        self.display(node.left,indent+"  ")
        self.display(node.right,indent+"  ")

    def traversal(self,node):
        stack=[]
        inorder=[]
        preorder=[]
        postorder=[]
        if not node:
            print(f"inorder: {inorder}\npreorder: {preorder}\npostorder: {postorder}")
            return 
        stack.append([node,1])
        while stack:
            curr,state=stack.pop()
            if state==1:
                preorder.append(curr.value)
                stack.append([curr,2])
                if curr.left:
                    stack.append([curr.left,1])
            elif state==2:
                inorder.append(curr.value)
                stack.append([curr,3])
                if curr.right:
                    stack.append([curr.right,1])
            else:
                postorder.append(curr.value)

        print(f"inorder: {inorder}\npreorder: {preorder}\npostorder: {postorder}")


if __name__=="__main__":
    t=Tree()
    t.insert_root(3)
