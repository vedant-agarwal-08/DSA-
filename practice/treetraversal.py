class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
class binarysearchtree:
    def __init__(self,value):
        new_node=Node(value)
        self.root=new_node
    def insert(self,value):
        new_node=Node(value)
        if self.root ==None:
            self.root=new_node
            return True
        temp=self.root
        while(True):
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
    # def contains(self,value):
    #         if self.root is None:
    #             return False
    #         temp=self.root
    #         while temp is not None:
    #             if value<temp.value:
    #                 temp=temp.left
    #             elif value>temp.value:
    #                 temp=temp.right
    #             else:
    #                 return True
    #         return False
    # def min_value(self,current_node):
    #     while current_node.left is not None:
    #         current_node=current_node.left
    #     return current_node.value
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

my_tree=binarysearchtree()
root=my_tree.insert(27)
my_tree.insert(14)
my_tree.insert(35)
my_tree.insert(10)
my_tree.insert(19)
my_tree.insert(31)
my_tree.insert(42)
# root = Node(27)
# root.insert(14)
# root.insert(35)
# root.insert(10)
# root.insert(19)
# root.insert(31)
# root.insert(42)
print(root.inorderTraversal(root))
print(root.inordertraversal(root))
# print(my_tree.min_value(my_tree.root))
# print(my_tree.contains(3))
# print(my_tree.root.value)
# print(my_tree.root.left.value)
# print(my_tree.root.left.value)
# print(my_tree.root.right.value)
# print(my_tree.root.right.right.value)
