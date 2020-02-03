from tkinter import *
from tkinter import messagebox

class Application(Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.createWidget()

    def createWidget(self):
        """创建登录界面的组件"""
        self.label01=Label(self,text="用户名")
        self.label01.pack()

        #StringVar变量绑定到指定的组件中
        #StringVar变量的值发生变化，组件内容也变化
        #组件内容发生变化，StringVar变量的值也发生变化
        v1=StringVar()
        self.entry01=Entry(self,textvariable=v1)
        self.entry01.pack()
        v1.set("admin")

        #创建密码框
        self.label02 = Label(self, text="密码")
        self.label02.pack()

        v2 = StringVar()
        self.entry02 = Entry(self, textvariable=v2,show="*")
        self.entry02.pack()

        # self.btn01=Button(self,text="登录",command=self.login)
        # self.btn01.pack()

        Button(self,text="登录",command=self.login).pack()

    def login(self):
        username=self.entry01.get()
        pwd=self.entry02.get()

        print("去数据库对比用户名和密码～")
        print("用户名"+self.entry01.get())
        print("密码" + self.entry02.get())
        # messagebox.showinfo("尚学堂学习系统","登录成功！开始学习！")

        if username=="min" and pwd=="123456":
            messagebox.showinfo("尚学堂学习系统","登录成功！炫音挂开始学习")
        else:
            messagebox.showinfo("尚学堂学习系统","登录失败～用户名或密码错误")

if __name__=="__main__":
    root=Tk()
    root.geometry("400x130+200+300")
    app=Application(master=root)
    root.mainloop()