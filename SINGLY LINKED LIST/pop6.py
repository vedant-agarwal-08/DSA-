class Node:   #creating a node
    def __init__(self, value): 
        self.value = value
        self.next = None
        

class LinkedList:  #creating a class named linked list
    def __init__(self, value): #creating a constructor
        new_node = Node(value)  #calling the above class
        self.head = new_node  
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:  #if there is no node
            self.head = new_node
            self.tail = new_node
        else:          #if there 
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:  #if there is no node
            return None
        temp = self.head
        pre = self.head
        while temp.next is not None: #if there are more than two nodes
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1  #if there is only one node 
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value


my_linked_list = LinkedList(1)
my_linked_list.append(2)

# (2) Items - Returns 2 Node
print(my_linked_list.pop())
# (1) Item -  Returns 1 Node
print(my_linked_list.pop())
# (0) Items - Returns None
print(my_linked_list.pop())


