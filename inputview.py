import tkinter
import search.bigdatafind
import search.listshowdata

class view:
    def __init__(self):
        self.win=tkinter.Tk()
        self.win.geometry("800x800+300+0")
        self.entry=tkinter.Entry(self.win)
        self.entry.place(x=0,y=0)
        self.button=tkinter.Button(self.win,text="search",command=self.search)
        self.button.place(x=200,y=0)
        self.Find=search.bigdatafind.datafind()
    def show(self):
        self.win.mainloop()
    def search(self):
        str = self.entry.get()
        print("start search")
        self.Find.find(str)
        self.Find.show()

begin=view()
begin.show()