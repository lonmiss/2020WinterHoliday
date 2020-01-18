## Python内置函数
* sorted(iterable[,key[,reverse]])
* iterable--序列，如字符串，列表，元组等
* key--函数，缺省为空
* reverse--排序规则
* reverse=True降序，reverse=False升序（默认）

#### 表格排序
|姓名|分数|年龄|
|-----|-----|------|
|蒋欣|89|15|
|方鹏|80|14|
|陈珂|85|14|

#### ～
    students=[('蒋欣',89,15),('方鹏',80,14),('陈珂',85,14)]
    # 按年龄从小到大排序
    print(sorted(students,key=lambda s:s[2]))
    # 按成绩从大到小降序
    print(sorted(students,key=lambda s:s[1],reverse=True))
    """
    [('方鹏', 80, 14), ('陈珂', 85, 14), ('蒋欣', 89, 15)]
    [('蒋欣', 89, 15), ('陈珂', 85, 14), ('方鹏', 80, 14)]
    """
   
#### map函数
* map函数根据提供的函数指定序列做映射
* map函数语法：map(function,iterable,...)
* 第一个参数function是对参数序列中的每一个元素调用function函数
，iterable是序列
* 返回值的新列表或迭代器，每个元素是调用function的返回值

        print(list(map(lambda x:x**2,[1,2,3,4,5])))#使用lambda匿名函数
        #[1, 4, 9, 16, 25]
        #提供两个列表，对相同位置的列表数据进行相加
        print(list(map(lambda x,y:x+y,[1,3,5,7,9],[2,4,6,8,10])))
        #[3, 7, 11, 15, 19]
        
#### zip函数
* zip()函数用于讲可迭代的对象作为参数，江对象中的对应的元素打包成一个个元组，然后返回这些元组组成的列表或迭代器
* 如果个迭代器的元素个数不一致，则返回列表长度与最短的对象相同
* zip语法：zip([iterable,....])
** iterable,...两个或多个序列
** 返回值：返回元组列表

        a=[1,2,3]
        b=[4,5,6]
        c=[4,5,6,7,8]
        print(list(zip(a,b)))
        #[(1, 4), (2, 5), (3, 6)]
        print(list(zip(a,c)))#元素个数与最短的列表一致
        #[(1, 4), (2, 5), (3, 6)]
        
#### 字典键值互换
    d={'blue':500,'red':100,'white':300}
    d1=dict(zip(d.values(),d.keys()))
    print(d1)
    #{500: 'blue', 100: 'red', 300: 'white'}
    
#### eval 和 exec函数
* python 是一种动态语言，他包含很多含义。Python变量类型，操作的合法性都在动态运行中检查
运算的代码需要到运行时才能动态确定程序结构也可以动态变化，允许动态加载新模块。这两个函数体现
了这个特点
* eval是计算表达式，返回表达式的值
* exec可运行Python的程序，返回程序的运行结果

        x,y=3,7
        print(eval('x+3*y-4'))#20
        #20
        exec('print("hello world")')
        #hello world  
#### all和any 函数
* all()和any()函数将可迭代的对象作为参数
* all函数参数都为True时，才返回True，否则返回False
* any函数参数只要有一个为True，就返回True,参数全部为False是，返回False


   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    