import tkinter
class savedata:
    def __init__(self,loadpath):
        self.loadpath = loadpath
    def save(self,findlist):
        load = open(self.loadpath, "wb")
        load.write(("检索数据如下\n").encode("utf-8"))
        for line in findlist:
            load.write((line+"\n").encode("utf-8"))
        load.close()

        win = tkinter.Tk()
        win.geometry("150x50+800+400")
        attention = tkinter.Label(win, text="save successfully")
        attention.pack()
        win.mainloop()

        print("save successfullly")


