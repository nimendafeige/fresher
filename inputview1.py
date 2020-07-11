import tkinter
from tkinter import ttk
import search.bigdatafind
import search.listshowdata
import search.textshowdata
import search.tableshowdata
import search.savedatafind
import search.datamailsend

class view:
    def __init__(self):
        self.win=tkinter.Tk(baseName="search")
        self.win.geometry("800x300+500+200")
        self.photo = tkinter.PhotoImage(file=r"C:\Users\nimendafeige\PycharmProjects\untitled\1.gif")
        self.label = tkinter.Label(self.win,text="shao",image=self.photo)
        self.label.pack()

        self.label1 = tkinter.Label(self.win, text="  Help    Yourself ", font=("华文彩云", 15), fg="SaddleBrown", bg="LightGreen")
        self.label1.place(x=0, y=160)
        self.stringvar1=tkinter.StringVar()
        self.stringvar1.set("please entry keywords")
        self.entry1=tkinter.Entry(self.win,textvariable=self.stringvar1)
        self.entry1.place(x=150,y=160)
        self.button1=tkinter.Button(self.win,text="search",command=self.search,bg="LightGreen")
        self.button1.place(x=300,y=160)
        self.button3 = tkinter.Button(self.win, text="e-mail",command=self.send,bg="LightGreen")
        self.button3.place(x=450, y=160)

        self.label4 = tkinter.Label(self.win, text="Choices of Show",font=("华文彩云",15),fg="red",bg="PowderBlue")
        self.label4.place(x=0, y=110)
        self.comvalue = tkinter.StringVar()
        self.comboxlist = ttk.Combobox(self.win,textvariable=self.comvalue,width=68)
        self.comboxlist["values"] = ("listshowdata", "textshowdata", "tableshowdata")
        self.comboxlist.current(0)
        self.comboxlist.bind("<<ComboboxSelected>>", self.go)
        self.comboxlist.place(x=150,y=110)
        self.howtoshow="listshowdata"

        self.label5 = tkinter.Label(self.win, text="Choices of Addr",font=("华文彩云",15),fg="red",bg="white")
        self.label5.place(x=0, y=10)
        self.comvaluef = tkinter.StringVar()
        self.comboxlistf = ttk.Combobox(self.win, textvariable=self.comvaluef,width=68)
        self.comboxlistf["values"] = (r"演示示例1.txt",
                                       r"演示示例2.txt",
                                       r"演示示例3.txt")
        #self.comboxlistf.current(0)
        self.comboxlistf.bind("<<ComboboxSelected>>", self.gof)
        self.comboxlistf.place(x=150, y=10)
        self.howtoshowf = r"演示示例1.txt"

        self.label2 = tkinter.Label(self.win, text="Input Otheraddr",font=("华文彩云",15),fg="LimeGreen",bg="yellow")
        self.label2.place(x=0, y=60)
        self.entry2=tkinter.Entry(self.win,width=70)
        self.entry2.place(x=150,y=60)

        self.button3 = tkinter.Button(self.win, text="save", command=self.save,bg="LightGreen")
        self.button3.place(x=650, y=210)
        self.label3 = tkinter.Label(self.win, text="Where   to   Save ", font=("华文彩云", 15), fg="blue", bg="pink")
        self.label3.place(x=0, y=210)
        self.stringvar3 = tkinter.StringVar()
        self.stringvar3.set("save.txt")
        self.entry3 = tkinter.Entry(self.win, width=70,textvariable=self.stringvar3)
        self.entry3.place(x=150, y=210)

    def go(self,*arg):
        self.howtoshow=self.comvalue.get()#保存选中值
        print(self.comboxlist.get())#选中当前值

    def gof(self,*arg):
        self.howtoshowf=self.comboxlistf.get()#保存选中值
        print(self.comboxlistf.get())#选中当前值

    def show(self):
        self.win.mainloop()

    def search(self):
        if self.entry2.get()!='':
            self.howtoshowf=self.entry2.get()
        Find = search.bigdatafind.datafind(self.howtoshowf, self.howtoshow,0)
        print("start search")
        Find.find(self.stringvar1.get(),0)
        Find.show()

    def save(self):
        Save=search.bigdatafind.datafind(self.howtoshowf, self.howtoshow,1)
        Save.find(self.stringvar1.get(),1)
        Save.save(self.stringvar3.get())

    def send(self):
        Send=search.bigdatafind.datafind(self.howtoshowf, self.howtoshow,1)
        Send.find(self.stringvar1.get(),1)
        Send.send()
        pass


begin=view()
begin.show()