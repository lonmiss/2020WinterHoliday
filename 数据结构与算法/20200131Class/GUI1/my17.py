"""文件对话框获取文件"""

from tkinter import *
from tkinter.filedialog import *

root=Tk()
root.geometry("400x100")

def test1():
    f=askopenfilename(title="上传文件",initialdir="f",filetypes=[("视频文件",".mp4")])

    # show["text"]=f

