class Node:
    def __init__(self,value):
        self.value=None
        self.left=None
        self.right=None
class binarysearchtree():
    def __init__(self):
        self.root=None
    def insert(self,value):
        new_node=Node(value)
        if self.root is None:
            self.root=new_node
            return True
        temp=self.root
        while (True):
            if new_node==temp.value:
                return False
            if new_node.value<temp.value:
                if temp.left is None:
                    temp.left=new_node
                    return True
                temp=temp.left
            else:
                if temp.right is None:
                    temp.right=new_node
                    return True
                temp=temp.right
    def contains(self,value):
        if self.root is None:
            return False
        temp=self.root
        while temp is not None:
            if value<temp.value:
                temp=temp.left
            elif value>temp.value:
                temp=temp.right
            else:
                return True
        return False
    def minimum_value(self,current_node):
        while current_node.left is not None:
            current_node=current_node.left
        return current_node
    def bfs(self):
        current_node=self.root
        queue=[]
        results=[]
        queue.append(current_node)
        while len(queue)>0:
            current_node=queue.pop(0)
            results.append(current_node)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
my_tree=binarysearchtree()
my_tree.insert(7)
my_tree.insert(9)
my_tree.insert(10)
my_tree.insert(21)
my_tree.insert(5)
my_tree.insert(3)
my_tree.contains(5)
my_tree.minimum_value()
