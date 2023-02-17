class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    
    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data
    
    def inordertraversal(self,root):
        res=[]
        if root:
            res=self.inordertraversal(root.left)
            res.append(root.data)
            res=res+self.inordertraversal(root.right)
        return res
    def preordertraversal(self,root):
        res1=[]
        if root:
            res1.append(root.data)
            res1=res1+self.preordertraversal(root.left)
            res1=res1+self.preordertraversal(root.right)
        return res1
    def postordertraversal(self,root):
        res2=[]
        if root:
            res2=self.postordertraversal(root.left)
            res2=res2+self.postordertraversal(root.right)
            res2.append(root.data)
        return res2
root=Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.inordertraversal(root))
print(root.preordertraversal(root))
print(root.postordertraversal(root))
