# 测试一个经典的GUI的写法，使用面向对象的方式
from tkinter import *
from tkinter import messagebox

class Application(Frame):
    """一个经典的GUI程序的类的写法"""

    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()

        self.createWidget()

    def createWidget(self):
        """创建组件"""
        self.label01=Label(self,text="百战程序员",width=10,height=2,
                           bg="black",fg="white")
        self.label01.pack()

        self.label02 = Label(self, text="小白", width=10, height=2,
                             bg="blue", fg="white",font=("宋体",30))
        self.label02.pack()

        # 显示图像
        global photo #将photo对象声明成全局变量，如果是局部变量，本方法执行完毕后，图像对象销毁，图像显示不出
        photo=PhotoImage(file="../imgs/1d7ea11e00290cb565e996bcc3f9d978.gif")
        self.label03=Label(self,image=photo)
        self.label03.pack()

        # 显示多行文本
        self.label04=Label(self,text="151ac61ascaspscjs",
                           borderwidth=5,relief="solid",justify="right")
        self.label04.pack()
if __name__=='__main__':
    root = Tk()
    root.geometry("500x540+100+200")
    root.title("一个经典的GUI程序类的测试")
    app=Application(master=root)

    root.mainloop()