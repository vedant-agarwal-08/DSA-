class stack(object):
    def __init__(self):
        self.items=[]
    def isfull(self):
        if len(self.items==n):
            return True
    def push(self,item):
        if len(self.items!=n):
            return self.items.append(item)
        else:
            return None
    def isempty(self):
        if len(self.items==0):
            return True
        else:
            return False
    def pop(self):
        if self.items:
            self.items.pop()
        else:
            return None
    def peek(self):
        if self.item:
            return self.item[-1]
        else:
            return None
    def display(self):
        return self.items
    def size(self):
        return len(self.items)
n=5
stack=stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.display()