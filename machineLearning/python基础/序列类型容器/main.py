""""
s="John Smith"
print(s.lower())#john smith
print(s.upper())#JOHN SMITH
print(s.find("Smi"))#5
s1="hello World"
print(s1.find("l"),s1.find("l",3))#2 3 find 的第二个函数是从哪里开始找
print(s1.count("l"))#统计出现的次数   3

s=' hello world '
# strip 去掉空格
print(s.strip())#hello world 左右两端空格
print(s.lstrip())#hello world 左边的空格
print(s.rstrip())# hello world右边的空格
#字符串的替换
print(s.replace(" ","*"))#*hello*world*
print(s.replace(" ","**"))#**hello**world**
print(s.replace(" ",""))#helloworld
"""

"""
#列表的操作
t1=[0,1,2,3,4,5]
t1.append(5)
print(t1)#[0, 1, 2, 3, 4, 5, 5]
t1.extend([7,8,9])
print(t1)#[0, 1, 2, 3, 4, 5, 5, 7, 8, 9]
t1.insert(1,9) # insert 的第一个值足够大的时候，相当于append操作
print(t1)#[0, 9, 1, 2, 3, 4, 5, 5, 7, 8, 9]
t1.append([10,11,12])
print(t1)#[0, 9, 1, 2, 3, 4, 5, 5, 7, 8, 9, [10, 11, 12]]
t1.remove(4)#remove删除特定值的操作
print(t1)#[0, 9, 1, 2, 3, 5, 5, 7, 8, 9, [10, 11, 12]]
t1.pop()
print(t1.pop())#9
print(t1.pop(0))#0
print(t1)#[9, 1, 2, 3, 5, 5, 7, 8]
print(t1.index(9))#0 查找元素在列表的特定位置
"""

# p=(1,2,3)
# p[0]=5 #'tuple' object does not support item assignment
# print(p)
# t=[1,2,3]
# p=tuple(t)
# print(p)#(1,2,3)

import random
t=[9,5,8,7,1,3,8,6,8,6]
t.sort()#将数据排序
print(t)
random.shuffle(t)#将数据打乱
print(t)#[9, 7, 1, 5, 6, 8, 3, 6, 8, 8]
random.shuffle(t)
print(t)#[1, 7, 9, 6, 5, 8, 8, 3, 8, 6]
t=['John','Johnson','Mary','Kime']
print(random.choice(t))#随机选择一个元素
print(random.random())#随机生成0~1的数
print(random.randint(1,100))
random.seed(0)#给一个数的初始种子
print(random.randint(1,100))#50
random.seed(0)
print(random.randint(1,100))#50



























