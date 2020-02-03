from tkinter import *
from tkinter import messagebox


root = Tk()

root.title("我第一个GUI程序")
root.geometry("500x300+100+200")  # 宽度  高度   距离左边多少像素 距离上边多少像素

# 加组件
btn01 = Button(root)
btn01["text"] = "点下我就送花"

btn01.pack()
# 压缩

def songhua(e):
    #e 就是事件对象
    messagebox.showinfo("Message", "送你一朵玫瑰花，亲亲我吧")
    print("送你99朵玫瑰花")

#绑定函数
btn01.bind("<Button-1>",songhua)

root.mainloop() # 调用组件的mainloop()方法进入循环

