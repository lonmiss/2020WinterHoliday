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




textFile=open("123.txt","rt")#以文本方式打开
t=textFile.readline()
print(t)
textFile.close()
binFile=open("123.txt","rb")#以二进制方式打开
b=binFile.readline()
print(b)
binFile.close()
"""
欢迎来到文件读写～688

b'\xe6\xac\xa2\xe8\xbf\x8e\xe6\x9d\xa5\xe5\x88\xb0\xe6\x96\x87\xe4\xbb\xb6\xe8\xaf\xbb\xe5\x86\x99\xef\xbd\x9e688\n'

"""

# # 多行文件读写
#
# f=open("score.txt","r")
# for line in f.readlines():
#     print(line)#处理行
# f.close()

"""
计算总分
总评=笔试*50%+平时*25%+实验*25%
"""
f=open("score.txt","r")
l1=[]
s=f.readlines()
for i in  s:
    l=i.split(" ")
    l2=[]
    for j in l:
        if(j!=" " and j!=""):
            l2.append(j)
    l1.append(l2)
print(len(l1))
for i in range(1,len(l1)):
    #['001', '詹艳峰', '计算机', '65', '85', '76\n']
    score=int(l1[i][3])*0.5+int(l1[i][4])*0.25+int(l1[i][5][:2])*0.25
    print(l1[i][0]+"  "+l1[i][1]+"  "+str(score))






