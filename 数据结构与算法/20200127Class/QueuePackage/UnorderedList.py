from Node import Node
class UnorderedList:

    def __init__(self):
        self.head=None

    #头插法
    def add(self,item):
        temp=Node(item)
        temp.setNext(self.head)
        self.head=temp

    #size:从链表头head开始遍历到表同时用变量累加经过的节点个数
    def size(self):
        current=self.head
        count=0
        while current!=None:
            count+=1
            current=current.getNext()

        return count
    # search:从链表头head开始遍历到表尾，同时判断当前节点的数据项是否为目标
    def search(self,item):
        current=self.head
        found=False
        while current !=None and not found:
            if(current.getData()==item):
                found=True
            else:
                current=current.getNext()
        return found

    #remove(item):首先找到item,这个过程跟search一样，但删除节点时，需要特别的技巧
    def remove_me(self,item):
        current=self.head
        if (current.getData()==item):
            current.setNext(current.getNext())
        else:
            while current.getNext().getData()!=item:
                current=current.getNext()
            current.setNext(current.getNext().getNext())

    def remove(self,item):
        current=self.head
        previous=None
        found=False
        while not found:
            if(current.getData()==item):
                found=True
            else:
                previous=current
                current=current.getNext()

        if(previous==None):
            self.head=current.getNext()
        else:
            previous.setNext(current.getNext())