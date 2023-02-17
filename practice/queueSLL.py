from configparser import NoOptionError


class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class queue:
    def __init__(self,value):
        new_node=Node(value)
        self.first=new_node
        self.last=new_node
        self.length=1
    def print(self):
        temp=self.first
        while temp is not None:
            print(temp.value)
            temp=temp.next
    def enqueue(self,value):
        new_node=Node(value)
        if self.first is None:
            self.first=new_node
            self.last=new_node
        else:
            self.last.next=new_node
            self.last=new_node
        self.length+=1
    def dequeue(self):
        if self.length==0:
            return None
        temp=self.first
        if self.first==1:
            self.first==None
            self.last==None
        else:
            self.first=self.first.next
            temp.next=None
        self.length-=1
        return temp
my_queue=queue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.enqueue(5)
my_queue.print()
print("\n")
my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()
my_queue.print()