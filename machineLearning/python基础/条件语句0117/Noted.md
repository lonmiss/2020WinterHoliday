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


   
#### open函数
* fileobj=open(filename,mode)
* fileobj是open()返回文件对象
* filename是该文件的文件名
* mode是指明文件类型和操作的字符串
* mode的第一个字母表明对其的操作。mode的第二个字母是文件类型；
t（可省略）代表文本类型文件；b代表二进制类型文件，后面的文件处理操作均
以文本类型；b代表二进制类型文件。后面文件处理操作均为文本类型为例
    
#### 文件打开模式
|文件打开模式|含义|
|:----------:|:------------------------------:|
|r|只读模式（默认）|
|w|覆盖写模式（不存在则新创建；存在则重写新内容）| 
|a|追加模式（不存在则新创建；存在则只追加内容）|
|x|创建写模式（不存在则新创建；存在则出错）|
|+|与r/w/a/x一起使用，增加读写内容|
|t|文本类型|
|b|二进制类型|   

#### 文件读写函数
|名称|含义|
|--------|------------------------------------|
|open()|打开文件|
|read(size)|从文件读取长度size的字符串，如果未给定或负则读取所有的内容|
|readline()|读取整行，返回字符串|
|readlines()|读取所有行并返回列表|
|write(s)|吧字符串s的内容写入文件|
|writelines(s)|向文件写入一个元素为字符串的列表，如果需要换行则要自己加入每行的换行符|
|seek(off,whence=0)|设置文件的当前位置|
|tell()|返回文件读写的当前位置|
|close()|关闭文件，关闭后，关闭文件不能在进行读写操作|
    
#### 多行文件读写
* 用readlines()读写多行文件

    f=open("score.txt","r")
    for line in f.readlines():
        print(line)#处理行
    f.close()   
 
 * 可用嵌套列表存放多行内容
 
 
   
### Python 的模块函数分为三个层次
* 内置函数
*** 不用import语句引入，它里面的函数可直接调用
* 标准模块函数
*** 用import语句引入后调用，但不必安装，如math库
* 第三个模块函数
*** 需要先安装，在用import语句后引入模块后才能调用里面的函数，如Pandas模块
    
    
#### Pandas模块
* Pandas是Python的一个数据分析包
* pandas是最初被作为金融数据分析工具二开发出来的
* pandas为时间序列分析提供了很好的支持
* pandas是基于NumPy的一种工具
* Pandas纳入了大量函数和一些标准的数据模型，提供了高效操作大型所需的工具
，提供了大量能使我们快速便捷地处理数据的函数和方法，让Python成为强大而高效的数据分析环境

#### Plotly模块
* plotly是一个基于javascript的动态绘图模块。plotly的绘图效果与我们在网页上看到
的动态交互式绘图结果是一样的，其默认的绘图结果是一个HTML网页文件，通过浏览器皆可以查看
* plotly是基于javascript的绘图库，所以其绘图结果可以与web应用无缝集成
* plotly最初是一款商业化的绘图软件，自plotly.js开源之后，我们可以使用本地
离线模式进行绘图，不依赖于官方的服务器，使得绘图速度更快，而绘图效果与在线绘图一样
* 离线模式：form plotly.offline import plot

    
#### DataFrame 数据类型
* DataFrame是Pandas库的一种数据类型。DataFrame是一个行和列具有标签的表格
，它与Excel电子表格并无不同
* DataFrame使用非常方便，当你在处理二维表格数据时，都应该使用他们。DataFrame
可由元组、列表、字典或另一个DataFrame构造出来


#### Web应用程序的运行过程
* 运行用Python编写的服务程序
* 用户在浏览器输入URL访问某个资源
* Flask接受用户请求分析URL
* 为这个URL找到相应的处理函数
* 执行函数并生成响应，返回给浏览器
* 浏览器接受病解析响应，讲信息显示在页面中

#### Web应用框架
* Flask是一个使用Python编写的轻量级Web应用框架。其WSGL工具箱采用Werkzeug,
模板引擎则使用Jinja2.Flask使用BSD授权。
* Flask也称为“miscroframework”,因为它使用简单的核心，采用拓展增加其他功能。
* Flash是第三方模块，需要先安装才能使用
* 使用Flask0.12版本
    
    
#### HTTP协议常用请求
* get：从服务器程序获取信息
* post:通常用作项服务器程序发送数据，一般用表单实现
** post请求可能会导致新的资源的建立和/或已有资源的修改


#### 浏览器和服务起程序交互
* 浏览器和服务器程序交互可以通过get和post方法实现
* 在装饰器上可以加http方法，常用的是get和post方法，缺省的是get方法
* @app.route("/")就等同于
  @app.route("/",methods=["get"])
* 如需要用两个方法，可写成：
    @app.route("/",methods=["get","post"])
* get和post是站在浏览器角度看的
      
    
    
    
    
    
    
    