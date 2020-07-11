import tkinter
from tkinter import ttk
class showdata3:
    def __init__(self):
        self.win=tkinter.Tk()
        self.tree=ttk.Treeview(self.win,height=300)
        self.idnum=0
        self.tree["columns"]=("name","idnum")
        self.tree.column("name",width=200)
        self.tree.column("idnum",width=200)

        self.tree.heading("name",text="Name")
        self.tree.heading("idnum",text="IDnum")
        self.tree.pack()
    def show(self):
        self.win.mainloop()

    def adddata(self,insertstr):
        datalist=insertstr.split(" ")
        if len(datalist)==2:
            self.tree.insert("",self.idnum,text="line"+str(self.idnum+1),values=(datalist[0],datalist[1]))
            self.idnum+=1

