class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class DoublyLinkedList:
    
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1
    def append(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1
    def pop(self):
        if self.length==0:
            return None
        else:
            temp=self.tail
            self.tail=self.tail.prev
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
            self.head.prev=new_node
            self.head=new_node
        self.length+=1
        return True
    def pop_first(self):
        if self.length==0:
            return None
        temp=self.head
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            self.head.prev=None
            temp.next=None
        self.length-=1
        return temp
    def get(self,index):
        if index<0 and index>=self.length:
            return None
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp
        
        

