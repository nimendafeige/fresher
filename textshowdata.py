import tkinter
class showdata2:
    def __init__(self):
        self.win=tkinter.Tk()
        self.win.geometry("900x800+0+0")
        self.text=tkinter.Text(self.win,width=300,height=300)
        self.text.pack()
    def show(self):
        self.win.mainloop()

    def adddata(self,insertstr):
        self.text.insert(tkinter.END,insertstr)
