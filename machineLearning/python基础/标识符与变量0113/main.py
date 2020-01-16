"""
a="hello"
print(type(a))#<class 'str'>
a=1
print(type(a))#<class 'str'>



a=1
b=1
print(id(a)) # 10914496
print(id(b)) #10914496
a=1000
b=1000
print(id(a))#139931270354864

print(id(b))#139931270354864

"""
# st=input()
# print(st)
#李*民最帅
#李*民最帅

# a=int(input())#1
# print(a+2)#3

# #Python多个输入
# a,b=input().split()#1 2
# print(a,b)# 1 2

# n=int(input("请输入一个整形值N:"))
# print("n:%d"%n)
# """
# 请输入一个整形值N:23
# n:23
# """

# # 输入三角形的三边的长度3,4,5 ； 求这个三角形的面积
# import math #引入数学库
# a=int(input())
# b=int(input())
# c=int(input())
# s=(a+b+c)/2
# area = math.sqrt(s*(s-a)*(s-b)*(s-c))
# print("三角形的边长：",a,b,c,end=" ")
# print("三角形的面积：",area)
# """
# 3
# 4
# 5
# 三角形的边长： 3 4 5 三角形的面积： 6.0
# """

#利用turtle库绘制五角星

# import tkinter as TK
#
# turtle.forward(200)
# turtle.right(144)
# turtle.forward(200)
# turtle.right(144)
# turtle.forward(200)
# turtle.right(144)
# turtle.forward(200)
# turtle.right(144)
# turtle.forward(200)
# turtle.forward(300)
# turtle.done()

for i in range(1,10):
    for j in range(1,i+3):
        print("%d * %d = %d       "%(j,i,j*i),end="")
    print()














