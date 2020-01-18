students=[('蒋欣',89,15),('方鹏',80,14),('陈珂',85,14)]
# 按年龄从小到大排序
print(sorted(students,key=lambda s:s[2]))
# 按成绩从大到小降序
print(sorted(students,key=lambda s:s[1],reverse=True))
"""
[('方鹏', 80, 14), ('陈珂', 85, 14), ('蒋欣', 89, 15)]
[('蒋欣', 89, 15), ('陈珂', 85, 14), ('方鹏', 80, 14)]
"""

print(list(map(lambda x:x**2,[1,2,3,4,5])))#使用lambda匿名函数
#[1, 4, 9, 16, 25]
#提供两个列表，对相同位置的列表数据进行相加
print(list(map(lambda x,y:x+y,[1,3,5,7,9],[2,4,6,8,10])))
#[3, 7, 11, 15, 19]

a=[1,2,3]
b=[4,5,6]
c=[4,5,6,7,8]
print(list(zip(a,b)))
#[(1, 4), (2, 5), (3, 6)]
print(list(zip(a,c)))#元素个数与最短的列表一致
#[(1, 4), (2, 5), (3, 6)]

# 字典键值互换
d={'blue':500,'red':100,'white':300}
d1=dict(zip(d.values(),d.keys()))
print(d1)
#{500: 'blue', 100: 'red', 300: 'white'}


x,y=3,7
print(eval('x+3*y-4'))#20
#20
exec('print("hello world")')
#hello world















