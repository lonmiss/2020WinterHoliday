## 2020.1.13 night

#### 标识符
* 标识符是指来标识某个实体的一个符号，在不同的应用环境下有不同的含义
* 标识符有字母、下划线和数字组成，且不能以数字开头
* 标识符区分大小写
#### 常亮和变量
* 常量就是不能改变的量
* 变量就是值可以改变的量，变量名则是程序为了方便地引用内存中的值而为它取的名称
* Python变量名是大小写敏感的

         a="hello"
         print(type(a))#<class 'str'>
         a=1
         print(type(a))#<class 'str'>

##### 用del()回收函数
#### id函数
* Python变量有一个非常重要的性质：变量是将名字和对象进行关联
* 赋值操作并不会实际复制值，他只是微数据对象取个相关的名字
* id()是Python的内置函数，可以显示对象的地址
* python 会为1~255分配独立的内存实现效率高
        a=1
        b=1
        print(id(a)) # 10914496
        print(id(b)) #10914496
        a=1000
        b=1000
        print(id(a))#139931270354864
        print(id(b))#139931270354864
 
 ## Python的输入输出
 
 #### 输入函数input()
 * input函数在Python中的一个内建函数，可以实现从标准输入（键盘）中读入一个字符串
 
        st=input()
        print(st)
        #李*民最帅
        #李*民最帅
        
        a=int(input())#1
        print(a+2)#3
        
        #Python多个输入
        a,b=input().split()#1 2
        print(a,b)# 1 2
        
        #python 带有提示的输入
        n=int(input("请输入一个整形值N:"))
        print("n:%d"%n)
        """
        请输入一个整形值N:23
        n:23
        """
#### Python输出
* print(a)
* print(a,b) 1 2
* for i in range(5):
    print(i)
    0
    1
    2
    3
    4
* for i in range(5):
    print(i,end=" ")0 1 2 3 4
    
        
            # 输入三角形的三边的长度3,4,5 ； 求这个三角形的面积
            import math #引入数学库
            a=int(input())
            b=int(input())
            c=int(input())
            s=(a+b+c)/2
            area = math.sqrt(s*(s-a)*(s-b)*(s-c))
            print("三角形的边长：",a,b,c,end=" ")
            print("三角形的面积：",area)
            """
            3
            4
            5
            三角形的边长： 3 4 5 三角形的面积： 6.0
            """






















