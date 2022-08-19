from tkinter import *
root = Tk()
def create():
#创建一个顶级弹窗
    top = Toplevel()
    top.title('我的弹窗')
    msg = Message(top,text = '类似于弹出窗口，具有独立的窗口属性。',width = 150)
    msg.pack()
Button(root,text = '创建一个顶级窗口',command = create).pack(padx = 20,pady = 50)
mainloop()