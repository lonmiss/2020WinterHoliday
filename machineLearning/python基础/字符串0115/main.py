s='abcdefgh'
print(s[0],s[-1]) #a h

# x=float(input())
# if(x<=15):
#     y=4*x/3
# else:
#     y=2.5*x-17.5
# print("%.2lf"%y)
# print("{:.2f}".format(y))


for i in [1,2,3,4]:
    print(i,end=" ")

a=list(range(10))
print()
print(a)

# print("求n! ， 输入 n: \n")
# n=int(input())
# s=1
# for i in range(1,n+1):
#     s*=i
# print(s)

n1=[2*number for number in [1,2,3,4,5]]
print(n1)#[2, 4, 6, 8, 10]

n2=[number for number in range(1,8) if number %2==1]
print(n2)#[1, 3, 5, 7]

# 求1+1/2+1/3+...+1/20之和
a=sum([1/i for i in range(1,21)])
print(a)#3.597739657143682

# # 求1-1/2+1/3-1/4+...之前n项和（n>=10)
# n=int(input())
# a=sum([1/i if i%2==1 else -1/i for i in range(1,n+1)])
# print(a)
# # 求6+66+666+...+666...666
# print(sum([int('6'*i) for i in range(1,1+n)]))

""" 华氏-摄氏温度转换表
    输入2个正整数lower和upper(lower<upper<100),输出一张取值范围【lower,upper]
    \且每次增加2华氏度的华氏-摄氏温度转换表，结果小数部分保留一位
    温度转换的计算公式
            C=5*(F-32)/9
    其中：C表示摄氏温度，F表示华氏温度
"""
print()
# me
# min1,max1=input().split()
# min1,max1=int(min1),int(max1)
# cList=[]
# fList=[]
# for i in range(min1,max1+1,2):
#     f=i
#     c=5*(f-32)/9
#     fList.append(f)
#     cList.append(c)
# print(fList)
# print(cList)
#
# lower,upper=input().split()
# lower,upper=int(lower),int(upper)
# for i in range(lower,upper+1,2):
#     print(i,"{:.1f}".format(5*(i-32)/9))



""" 求交错序列前N项和
    输入正整数N，输出序列和，结果保留三位小数
    1-2/3+3/5-4/7+5/9-6/11+...前N项
"""
n=int(input())
s=1
for i in range(2,n+1):
    if(i%2==0):
        s-=i/(2*i-1)
    else:
        s+=i/(2*i-1)
print("{:.3f}".format(s))

result=sum([i/(2*i-1) if(i%2==1) else (i/(2*i-1))*-1 for i in range(1,n+1)])
print("{:.3f}".format(result))