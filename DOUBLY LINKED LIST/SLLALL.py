class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class LinkedList:
    
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1
    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
    def append(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
# my_linked_list=LinkedList(1)
# my_linked_list.append(2)
# my_linked_list.append(3)
# my_linked_list.print_list()
    def pop(self):
        if self.length==0:
            return None
        else:
            temp=self.head
            pre=self.head
            while temp.next is not None:
                pre=temp
                temp=temp.next
            self.tail=pre
            self.tail.next=None
            self.length-=1
            if self.length==0:
                self.head=None
                self.tail=None
            return temp
    def prepend(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1

# my_linked_list=LinkedList(1)
# my_linked_list.append(2)
# my_linked_list.append(3)
# my_linked_list.print_list()
# print()
# my_linked_list.pop()
# my_linked_list.print_list()
# print()
# my_linked_list.prepend(0)
# my_linked_list.print_list()
    def pop_first(self):
        if self.length==0:
            return None
        else:
            temp=self.head
            self.head=self.head.next
            temp.next=None
        return temp.value
        self.length-=1
    def get(self,index):
        if index<0 or index>=self.length:
            return None
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp.value
    def set(self,index,value):
        temp=self.get(index)
        if temp is not None:
            temp.value=value
            return True
        return False
my_linked_list=LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.pop_first()
my_linked_list.print_list()
print(my_linked_list.get(0))
  
  