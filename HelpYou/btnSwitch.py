# -*- coding:utf-8 -*-
#作者：陈帅
#实现功能：这个demo实现的btn开始与关闭的切换
from tkinter import *
root=Tk()

def g():
    if b['text']=='开始':
        b['text']='关闭'
        print('开始')
    else:
        b['text']='开始'
        print('结束')
b=Button(root,text='开始',font=('KaiTi',36,'bold'),bg='pink',fg='green',bd=2,width=10,command=g)
print(b)

b.pack()
root.mainloop()
