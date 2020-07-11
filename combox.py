import tkinter
from tkinter import ttk

def go(*arg):
    a=comboxlist.get()
    print(a)

win=tkinter.Tk()
win.geometry("800x600+100+100")
#comvalue=tkinter.StringVar()#窗体自带文本，新建一个值
comboxlist=ttk.Combobox(win)#初始化
comboxlist["values"]=("list","text","table")
comboxlist.current(0)
comboxlist.place(x=100,y=300)#可以代替pack()
comboxlist.bind("<<ComboboxSelected>>",go)#绑定事件“选中”，go处理事件

win.mainloop()

