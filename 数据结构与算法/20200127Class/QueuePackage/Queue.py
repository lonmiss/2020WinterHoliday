class Queue:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def enqueue(self,item):
        return self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

# arr=Queue()
# arr.enqueue(1)
# arr.enqueue(2)
# arr.enqueue(3)
# print(arr.items)
# print(arr.dequeue())
# print(arr.items)