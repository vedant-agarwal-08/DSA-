from queue import Empty


class queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,value):
        self.queue.append(value)
    def dequeue(self):
        if len(self.queue)<1:
            return None
        else:
            self.queue.pop(0)
    def display(self):
        print(self.queue)
    def isempty(self):
        if self.queue is Empty:
            return True
        else:
            return False
    def size(self):
        return len(self.queue)

queue=queue()
queue.enqueue(0)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.display()

print(queue.size())

queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.display()

queue.dequeue()

print(queue.isempty())
