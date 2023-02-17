# 1
# class Node:
#     def __init__(self,sname,regno,mark1,mark2,mark3):
#         self.sname=sname
#         self.regno=regno
#         self.mark1=mark1
#         self.mark2=mark2
#         self.mark3.mark3
#         self.next=None
# class Student:
#     def __init__(self,sname,regno,mark1,mark2,mark3):
#         new_node=Node(sname,regno,mark1,mark2,mark3)
#         self.head=new_node
#         self.tail=new_node
#         self.length=1
#     def print(self):
#         temp=self.head
#         while temp:
#             print(temp.value)
#             temp=temp.next
# my_student=Student("vedant","21BIT0189",90,98,99)
# my_student.print()

#2
# class Node:
#     def __init__(self,value):
#         self.value=value
#         self.next=None
# class Student:
#     def __init__(self,value):
#         new_node=Node(value)
#         self.head=new_node
#         self.tail=new_node
#         self.length=1
#     def print(self):
#         temp=self.head
#         while temp:
#             print(temp.value,"->",end=" ")
#             temp=temp.next
#         print("None")
#     def prependmark2(self,value):
#         new_node=Node(value)
#         if self.length==0:
#             self.head=new_node
#             self.tail=new_node
#         else:
#             new_node.next=self.head
#             self.head=new_node
#         self.length+=1
#         return True
#     def prependmark1(self,value):
#         new_node=Node(value)
#         if self.length==0:
#             self.head=new_node
#             self.tail=new_node
#         else:
#             new_node.next=self.head
#             self.head=new_node
#         self.length+=1
#         return True
#     def prependregno(self,value):
#         new_node=Node(value)
#         if self.length==0:
#             self.head=new_node
#             self.tail=new_node
#         else:
#             new_node.next=self.head
#             self.head=new_node
#         self.length+=1
#         return True
#     def prependsname(self,value):
#         new_node=Node(value)
#         if self.length==0:
#             self.head=new_node
#             self.tail=new_node
#         else:
#             new_node.next=self.head
#             self.head=new_node
#         self.length+=1
#         return True
    # total=int(mark1+mark2+mark3)
    # def appendtotal(self):
    #     value=int(mark1+mark2+mark3)
    #     new_node=Node(value)
        
    #     self.tail.next=new_node
    #     self.tail=new_node
    #     self.length+=1
#     #     return True
# my_student=Student(90)
# my_student.prependmark2(89)
# my_student.prependmark1(88)
# my_student.prependregno("21BIT0189")
# my_student.prependsname("Vedant")
# # my_student.appendtotal()
# my_student.print()


#3
# class Node1:
#     def __init__(self,mark3):
#         self.mark3=mark3
#         self.next=None
# class Node2:
#     def __init__(self,mark2):
#         self.mark2=mark2
#         self.next=Node1
# class Node3:
#     def __init__(self,mark1):
#         self.mark1=mark1
#         self.next=Node2
# class Node4:
#     def __init__(self,regno):
#         self.regno=regno
#         self.next=Node3
# class Node5:
#     def __init__(self,sname):
#         self.sname=sname
#         self.next=Node4
# class Student:
#     def __init__(self,value):
#         new_node=Node(value)
                        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
