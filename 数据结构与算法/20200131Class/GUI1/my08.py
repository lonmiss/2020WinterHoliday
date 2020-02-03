"""测试Canvas组件的基本用法，使用面向对象的方式"""
from tkinter import *
from tkinter import messagebox
import random

class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.canvas=Canvas(self,width=300,height=300,bg="green")
        self.canvas.pack()
        # 画一条直线
        line=self.canvas.create_line(10,10,30,20,40,50)
        #画一个矩形
        rect=self.canvas.create_rectangle(50,50,100,100)
        #画一个椭圆。坐标两双。为椭圆的边界矩形左上角和底部右下角
        oval=self.canvas.create_oval(50,50,100,100)

        global photo
        photo=PhotoImage(file="../imgs/1d7ea11e00290cb565e996bcc3f9d978.gif")
        self.canvas.create_image(300,170,image=photo)

        Button(self,text="hua10个矩形",command=self.draw50Recg).pack(side="left")

    def draw50Recg(self):
        for i in range(0,10):
            x1=random.randrange(int(self.canvas["width"])/2)
            y1=random.randrange(int(self.canvas["height"])/2)
            x2 =x1+ random.randrange(int(self.canvas["width"]) / 2)
            y2 =y1 + random.randrange(int(self.canvas["height"]) / 2)
            self.canvas.create_rectangle(x1,y1,x2,y2)
if __name__=='__main__':
    root = Tk()
    root.geometry("600x400+200+300")
    app = Application(master=root)
    root.mainloop()














