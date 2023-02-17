class Node:
    def __init__(self,sname,regno,mark1,mark2,mark3):
        self.sname=sname
        self.regno=regno
        self.mark1=mark1
        self.mark2=mark2
        self.mark3.mark3
class Student:
    def __init__(self,sname,regno,mark1,mark2,mark3):
        new_node=Node(sname,regno,mark1,mark2,mark3)
        self.head=new_node
        self.tail=new_node
        self.length=1
    def print(self):
        temp=self.head
        while temp:
            print(temp.value)
            temp=temp.next
my_student=Student("vedant",21,90,98,99)
my_student.print()