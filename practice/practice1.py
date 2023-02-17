class Node:
    def __init__ (self,value):
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
    def first_element(self):
        temp=self.head
        print(temp.value)
    def last_element(self):
        pro=self.tail
        print(pro.value)
    def middle_element(self):
        middle=self.length/2
        element=LinkedList[middle]
        print(element)
my_linked_list=LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.print_list()
print("\n")
my_linked_list.first_element()
my_linked_list.last_element()
my_linked_list.middle_element()


