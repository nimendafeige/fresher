import tkinter
class showdata:
    def __init__(self):
        self.win=tkinter.Tk()
        self.list=tkinter.Listbox(self.win,width=300,height=300)
        self.list.pack()
    def show(self):
        self.win.mainloop()
    def adddata(self,insertstr):
        self.list.insert(tkinter.END,insertstr)

