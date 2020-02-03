from tkinter import *
from tkinter import messagebox

class Application(Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.v=StringVar()
        self.v.set("M")#默认为M

        self.r1=Radiobutton(root,text="男性",value="M",variable=self.v)
        self.r2 = Radiobutton(root, text="女性", value="F", variable=self.v)

        self.r1.pack(side="left")
        self.r2.pack(side="left")

        Button(root,text="确定",command=self.confirm).pack(side="left")

        self.codeHobby=IntVar()
        self.videoHobby=IntVar()

        print(self.codeHobby.get())#默认值为0
        self.c1=Checkbutton(root,text="敲代码",variable=self.codeHobby,
                            onvalue=1,offvalue=0)
        self.c2=Checkbutton(root,text="看视频",variable=self.videoHobby,
                            onvalue=1,offvalue=0)
        self.c1.pack(side="left")
        self.c2.pack(side="left")

        Button(root,text="确定",command=self.confirm).pack(side="left")

    def confirm(self):
        messagebox.showinfo("测试","选择性别："+self.v.get())
if __name__=="__main__":
    root=Tk()
    root.geometry("600x130+200+300")
    app=Application(master=root)
    root.mainloop()