"""开发画图软件的菜单"""
from tkinter import messagebox
from tkinter.filedialog import *
from tkinter.colorchooser import askcolor
import random

# 窗口的宽度和高度
win_width=900
win_height=500

class Applocation(Frame):

    def __init__(self,master=None,bgcolor="#fff"):
        super().__init__(master)
        self.master=master
        self.bgcolor=bgcolor
        self.x=0
        self.y=0
        self.fgcolor="#000"
        self.lastDraw=0 #表示最后的低矮用的id
        self.startDrawFlag=False
        self.penSize=1

        self.pack()
        self.createWidget()

    def createWidget(self):
        # 创建绘图区
        self.drawpad=Canvas(root,width=win_width,height=win_height,bg=self.bgcolor)
        self.drawpad.pack()

        # 创建按钮
        btn_start=Button(root,text="开始",name="start")
        btn_start.pack(side="left",padx="10")
        btn_pen = Button(root, text="画笔", name="pen")
        btn_pen.pack(side="left", padx="10")
        btn_rect = Button(root, text="矩形", name="rect")
        btn_rect.pack(side="left", padx="10")
        btn_clear = Button(root, text="清屏", name="clear")
        btn_clear.pack(side="left", padx="10")
        btn_earsor = Button(root, text="橡皮檫", name="earsor")
        btn_earsor.pack(side="left", padx="10")
        btn_line = Button(root, text="直线", name="line")
        btn_line.pack(side="left", padx="10")
        btn_lineArrow = Button(root, text="箭头直线", name="lineArrow")
        btn_lineArrow.pack(side="left", padx="10")
        btn_color = Button(root, text="颜色", name="color")
        btn_color.pack(side="left", padx="10")
        s1 = Scale(root, from_=1, to=20, length=420, tickinterval=1, orient=HORIZONTAL, command=self.changePenSize)
        s1.pack(side="left", padx="10")

        # 事件处理
        btn_pen.bind_class("Button","<1>",self.eventManager)
        self.drawpad.bind("<ButtonRelease-1>",self.stopDraw)

        # 增加颜色切换的快捷键
        root.bind("<KeyPress-r>",self.kuaijiejian)
        root.bind("<KeyPress-g>", self.kuaijiejian)
        root.bind("<KeyPress-y>", self.kuaijiejian)

    def changePenSize(self,value):
        self.penSize=value

    def eventManager(self,event):

        name=event.widget.winfo_name()
        print(name)
        if name=="line":
            self.drawpad.bind("<B1-Motion>",self.myline)
        elif name== "lineArrow":
            self.drawpad.bind("<B1-Motion>",self.mylineArrow)
        elif name=="rect":
            self.drawpad.bind("<B1-Motion>",self.myRect)
        elif name=="pen":
            self.drawpad.bind("<B1-Motion>",self.myPen)
        elif name=="earsor":
            self.drawpad.bind("<B1-Motion>", self.myEarsor)
        elif name=="clear":
            cnt=messagebox.askquestion("Warning！","是否确认清屏")
            if cnt=="yes":
                self.drawpad.delete("all")
        elif name=="color":
            self.drawpad.bind("<B1-Motion>", self.changeColor)

    def stopDraw(self,event):
        self.startDrawFlag=False
        self.lastDraw=0

    def myline(self,event):
        self.penSize = int(self.penSize)
        self.drawpad.delete(self.lastDraw)

        if not self.startDrawFlag:
            self.startDrawFlag=True
            self.x=event.x
            self.y=event.y

        #self.lastDraw=self.drawpad.create_line(self.x,self.y,event.x,event.y,fill=self.fgcolor)
        self.lastDraw = self.drawpad.create_line(self.x-self.penSize, self.y-self.penSize, event.x+self.penSize, event.y+self.penSize ,fill=self.fgcolor)

    def mylineArrow(self,event):
        self.penSize = int(self.penSize)
        self.drawpad.delete(self.lastDraw)

        if not self.startDrawFlag:
            self.startDrawFlag = True
            self.x = event.x
            self.y = event.y

        # self.lastDraw = self.drawpad.create_line(self.x, self.y, event.x, event.y,arrow=LAST, fill=self.fgcolor)
        self.lastDraw = self.drawpad.create_line(self.x-self.penSize, self.y-self.penSize, event.x+self.penSize, event.y+self.penSize, arrow=LAST, fill=self.fgcolor)

    def myRect(self,event):
        self.drawpad.delete(self.lastDraw)

        if not self.startDrawFlag:
            self.startDrawFlag = True
            self.x = event.x
            self.y = event.y

        self.lastDraw = self.drawpad.create_rectangle(self.x, self.y, event.x, event.y, outline=self.fgcolor) #outline：外边框的颜色

    def myPen(self,event):
        self.drawpad.delete(self.lastDraw)
        self.penSize=int(self.penSize)

        if not self.startDrawFlag:
            self.startDrawFlag = True
            self.x = event.x
            self.y = event.y

        self.drawpad.create_rectangle(self.x-self.penSize, self.y-self.penSize, event.x+self.penSize, event.y+self.penSize, fill=self.fgcolor,outline=self.fgcolor)

        self.x=event.x
        self.y=event.y

    def myEarsor(self,event):
        self.drawpad.delete(self.lastDraw)
        self.penSize = int(self.penSize)
        if not self.startDrawFlag:
            self.startDrawFlag = True
            self.x = event.x
            self.y = event.y

        self.drawpad.create_oval(self.x-self.penSize, self.y-self.penSize, event.x+self.penSize, event.y+self.penSize,fill=self.bgcolor,outline=self.bgcolor)

        self.x = event.x
        self.y = event.y
    def kuaijiejian(self,event):
        if event.char=="r":
            self.fgcolor="#ff0000"
        if event.char=="g":
            self.fgcolor="#00ff00"
        if event.char=="y":
            self.fgcolor="#ffff00"

    def changeColor(self,event):
        nums=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
        a1 = random.choice(nums)
        a2 = random.choice(nums)
        a3 = random.choice(nums)
        a4 = random.choice(nums)
        a5 = random.choice(nums)
        a6 = random.choice(nums)
        self.fgcolor = "#" + a1 + a2 + a3 + a4 + a5 + a6


if __name__=="__main__":
    root=Tk()
    root.geometry(str(win_width+100)+"x"+str(win_height+100)+"+200+300")
    root.title("简易画图软件")
    app=Applocation(master=root)
    root.mainloop()





















