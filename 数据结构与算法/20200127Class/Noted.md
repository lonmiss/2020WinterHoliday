### 队列抽象数据类型及Python实现
#### 队列
* 队列是一种有次序的数据集合，其特征是：新数据项添加总发生在一段，而数据的移除总发生在另一端
* 当数据项加入队列，首先出现在对尾，随着对首数据项的移除，它逐渐接近对尾
#### 抽象数据类型Queue由如下操作定义：
* Queue():创建一个空队列对象，返回值为Queue对象
* enqueue(item):将数据item添加到对尾，无返回值；
* dequeue():从队尾移除数据项，返回值为对首数据项，队列被修改
* size():返回队列中数据项的个数

#### 模拟算法：打印任务
##### 一个具体的实例配置如下
* 一个实验室，在任一个小时内，大约有10名左右学生在场
* 在这一小时中，每个人会发起2次左右的打印，每次1~20页
##### 打印机的性能是：
* 以草稿模式打印的话，每分钟10页
* 已正常模式打印的话，打印质量好，但速度下降，为每分钟5页
####### 问题是：怎样设定打印机的模式，让大家都不会等太久的前提下尽量提高导引质量

#### 双端队列Deque
###### 双端队列Deque是一种有次序的数据集，跟队列相似，其两端可以称为“首”，“尾”端，但
deque中的数据项既可以从对首加入，也可以从对尾加入；数据项也可以从两端移除
* 某种意义上说，爽端队列集成了栈和队列的能力

#### deque定义操作如下
* Deque():创建一个空的双端队列
* addFront(item):将item加入对首
* addRear(item):将item加入对尾
* removeFront():从对首移除数据项，返回值为移除的数据项
* removeRear():从对尾移除数据项，返回值为移除的数据项
* isEmpty():返回deque是否为空
* size():返回deque中包含的数据项的个数


### 无序表抽象数据类型
#### 列表List是一种简单强大的数据集结构，提供了丰富的操作接口
* 但不是所有的编程语言都提供了List数据类型，有时候需要程序员自己实现
* 一种数据项按照相对位置存放的数据集
##### 无序表List的操作如下：
* List():创建一个空列表
* add(item):添加一个数据项到列表中，假如item原先不存在于列表中
* remove(item):从列表中移除item,列表被修改，item原先赢在与表中
* search(item):在列表中查找item,返回布尔类型值
* isEmpty():返回列表是否为空
* size():返回值表包含了多少数据项
* append(item):添加一个数据项到表末尾，假设item原先不存在于列表中
* index(item):返回数据项在表中的位置
* insert(pos,item):将数据项插入到位置pos,假如item原先不存在与列表中，同时原列表具有足够
多个数据项，能让item占据位置pos
* pop():从列表末尾移除数据项，假设元列表至少一个数据项
* pop(pos):移除位置pos的数据项，假设原列表存在位置pos

#### 采用链表实现无序表
* 为了实现无序表数据结构，可以采用链接表的方案
* 虽然列表数据结构要求保持数据项的前后相对位置，但这种前后的保持，并不要求数据项依次存放在连续的存储空间
* 数据项存放位置并没有规则，但如果在数据项之间建立链接指向，就可以保持前后相对位置
##### 链表实现：节点Node
* 每个节点至少包含2个信息：数据项本身，以及指向下一个节点的引用信息
* 注意next为None的意义是没有下一个节点了，这个很重要
##### 链表实现：无序表UnorderedList
* 可以采用链接节点的方式构建数据集来实现无序表
* 链表的第一个和最后一个节点最重要
** 如果想要访问到链表中的所有节点，就必须从第一个节点开始沿着链接遍历下去

##### 链表实现：无序表UnorderedList
    
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
#### 抽象数据类型：有序表OrderedList
* 有序表是一种数据项依照其某可比性质(如整数大小、字母表先后)来决定在列表中的位置
* 越小的数据项越靠近列表的头，越靠前















