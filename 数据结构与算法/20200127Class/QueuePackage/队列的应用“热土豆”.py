""" 热土豆问题（约瑟夫问题）
* “击鼓传花”的土豆版本
* 传递烫手的热土豆，鼓声停的时候，手里有土豆的小孩就要出列
* 传说犹太人反叛罗马人，落入困境，约瑟夫和39人决定殉难，做成一圈，报数1~7，报道7的人由旁边杀死，结果
约瑟夫给自己安排了一个位置结果自己活了下来
"""
'''
* 模拟程序采用队列来存放所有参加游戏的人名，按照传递土豆方向从对首排到对尾
* 模拟游戏开始，只需要将对首的人出队，随即在到对尾入队，就算土豆的一次传递
* 传递了num次后，将对首的人移除，不在入队，如此反复，直到队列中只剩1人

'''

from Queue import Queue

def hotPotato(namelist,num):
    simqueue=Queue()
    for name in (namelist):
        simqueue.enqueue(name)

    while simqueue.size()>1:
        for i in range(1,num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()
        print(simqueue.items)

    return simqueue.dequeue()

list=[]
for i in range(1,42):
    list.append(i)
print(list)
print(hotPotato(list,3))
