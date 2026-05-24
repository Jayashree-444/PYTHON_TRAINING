class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class Binarytree:
    def __init__(self):
        self.root=None
    def insertNode(self,data):
        self.root=self.insert(self.root,data);
        
# inserted here
    def insert(self,root,data):
        if root is None:
            return Node(data)
        
        if data<root.data:
            root.left=self.insert(root.left,data)
            
        if data>root.data:
            root.right=self.insert(root.right,data)
        return root
# finding of maximum element in the tree
# DFS using Stack
# BFS using Queue

    def findTheMaximun(self):
        if self.root is None:
            return None
        return self.findMax(self.root)
            
    def findMax(self,root):
        if root is None:
            return float('-inf')
        leftMax=self.findMax(root.left)
        rightMax=self.findMax(root.right)
        return max(root.data,leftMax,rightMax)
    
    # main
tree=Binarytree()
n=int(input("enter the number of section: "))
for  i in range(n):
    value=int(input("enter the value: "))
    tree.insertNode(value)
print("maximum item quantity: ",tree.findTheMaximun())
    
     

        
        
        