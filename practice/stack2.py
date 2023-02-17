from operator import truediv


class stack(object):
    def __init__(self):
        self.items=[]
        def push(self,item):
            self.items.append(item)
        def pop(self):
            self.item.pop()
            pass
        def peek(self):
            if self.item:
                return self.item[-1]
            else:
                return None
        def size(self):
            if self.item:
                return len(self.item)
            else:
                return None
        def isempty(self):
            if self.item==[]:
                return True
            else:
                return False

stack=stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

# print(stack)

print("\n")
print(stack.size())
print(stack.peek())

stack.pop()
stack.pop()
stack.pop()

print(stack.size())
print(stack.peek())

print(stack.isempty())