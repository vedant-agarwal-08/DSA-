from operator import truediv


class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class linkedlist:
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
    def pop(self):
        if self.length==0:
            return None
        temp=self.head
        pre=self.head
        while temp is not None:
            pre=temp
            temp=temp.next
        self.tail=pre
        self.tail.next-None
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
        return True
    def pop_first(self):
        if self.length==0:
            return None
        temp=self.head
        
        self.head=self.head.next
        temp.next=None
        self.length-=1
        if self.length==0:
            self.tail=None
        return temp.value
    def addInMid(self, value):  
        #Create a new node  
        new_node = Node(value);  
          
        #Checks if the list is empty  
        if(self.head == None):  
            #If list is empty, both head and tail would point to new node  
            self.head = new_node;  
            self.tail = new_node;  
        else:  
            #Store the mid position of the list  
            count = (self.size//2) if(self.size % 2 == 0) else ((self.size+1)//2) 
            #Node temp will point to head  
            temp = self.head;  
            current = None;  
            for i in range(0, count):  
                #Node current will point to temp  
                current = temp;  
                #Node temp will point to node next to it.  
                temp = temp.next;  
              
            #current will point to new node  
            current.next = new_node;  
            #new node will point to temp  
            new_node.next = temp;  
        self.size = self.size + 1;  

    def get(self,index):
        if index<0 or index>=self.length:
            return None
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp




            
