"""通用消息框"""
from tkinter import *
from tkinter.messagebox import *

root=Tk()
root.geometry("400x200")

a1=showinfo(title="尚学堂",message="Python~")
print(a1)

root.mainloop()