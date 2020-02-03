import webbrowser
from tkinter import *
from tkinter import messagebox

class Application(Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.w1=Text(root,width=40,height=12,bg="gray")
        # 宽度20个字母（10个汉字），高度一个行高
        self.w1.pack()

        self.w1.insert(1.0,"0123456789\nabcdefg\n")
        self.w1.insert(3.0,"锄禾日当午，汗滴禾下土。谁知盘中餐，粒粒皆辛苦。、n")

        Button(self,text="重复插入文本",command=self.insertText).pack(side="left")
        Button(self, text="返回文本文本", command=self.returnText).pack(side="left")
        Button(self, text="添加图片", command=self.addImage).pack(side="left")
        Button(self, text="添加组件", command=self.addWidget).pack(side="left")
        Button(self, text="通过tag精确控制文本", command=self.testTag).pack(side="left")

    def insertText(self):
        # INSERT索引表示在光标出插入
        self.w1.insert(INSERT," redOrange")
        # END表示在索引号最后插入
        self.w1.insert(END," [sxt]")
    def returnText(self):
        # Indexes(索引)是用来指向Text组件中文本的位置，Text的组件索引也是对应实际字符
        # 核心：行号以1开始 列号0开始
        print(self.w1.get(1.2,1.6))
        print("所有文本内容：\n"+self.w1.get(1.0,END))
        messagebox.showinfo("文本",self.w1.get(1.2,1.6))

    def addImage(self):
        # global photo
        self.photo=PhotoImage(file="../imgs/1d7ea11e00290cb565e996bcc3f9d978.gif")
        self.w1.image_create(INSERT,image=self.photo)

    def addWidget(self):
        b1=Button(self.w1,text="爱尚学堂")
        # 在text创建组件的命令
        self.w1.window_create(INSERT,window=b1)
    def testTag(self):
        self.w1.delete(1.0,END)
        self.w1.insert(INSERT,"good good study , day day up !\n 北镜 \n 百战程序员\n百度，搜一下、、、")
        self.w1.tag_add("good",1.0,1.9)
        self.w1.tag_config("good",background="yellow",foreground="red")

        self.w1.tag_add("百度",4.0,4.2)
        self.w1.tag_config("百度",underline=True)
        self.w1.tag_bind("baidu","<Button-1>",self.webshow)

    def webshow(self,event):
        webbrowser.open_new_tab("https://www.baidu.com")

if __name__=="__main__":
    root=Tk()
    root.geometry("600x130+200+300")
    app=Application(master=root)
    root.mainloop()