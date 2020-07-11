import tkinter
from tkinter import ttk
import search.datamailsend
class view2:
    def __init__(self,sendstr):
        self.sendstr=sendstr
        self.win=tkinter.Tk()
        self.win.geometry("450x300+550+250")

        self.label1=tkinter.Label(self.win,text="Subject")
        self.label1.place(x=0,y=0)
        #self.stringvar1 = tkinter.StringVar()
        #self.stringvar1.set("test")
        #self.entry1=tkinter.Entry(self.win,width=50,textvariable=self.stringvar1)
        self.entry1 = tkinter.Entry(self.win, width=50)
        self.entry1.place(x=50,y=0)

        self.label2 = tkinter.Label(self.win,text="Address")
        self.label2.place(x=0,y=50)
        #self.stringvar2=tkinter.StringVar()
        #self.stringvar2.set("nimendafeige@163.com")
        #self.entry2=tkinter.Entry(self.win,width=50,textvariable=self.stringvar2)
        self.entry2 = tkinter.Entry(self.win, width=50)
        self.entry2.place(x=50,y=50)

        self.label3 = tkinter.Label(self.win,text="Content")

        self.label3.place(x=0,y=100)
        #self.stringvar3=tkinter.StringVar()
        #self.stringvar3.set("It's a latest data needed to take care")
        #self.entry3=tkinter.Entry(self.win,width=50,textvariable=self.stringvar3)
        self.entry3 = tkinter.Entry(self.win, width=50)
        self.entry3.place(x=50,y=100)

        self.label4 = tkinter.Label(self.win, text="Sender")
        self.label4.place(x=0, y=150)
        #self.stringvar4 = tkinter.StringVar()
        #self.stringvar4.set("nimendafeige@163.com")
        #self.entry4 = tkinter.Entry(self.win, width=50, textvariable=self.stringvar4)
        self.entry4 = tkinter.Entry(self.win, width=50)
        self.entry4.place(x=50, y=150)

        self.label5 = tkinter.Label(self.win, text="SMTPpassword")
        self.label5.place(x=0, y=200)
        #self.stringvar5 = tkinter.StringVar()
        #self.stringvar5.set("OHGXLDKBLCUUIJIJ")
        #self.entry5 = tkinter.Entry(self.win, width=44, textvariable=self.stringvar5)
        self.entry5 = tkinter.Entry(self.win, width=44)
        self.entry5.place(x=95, y=200)

        self.label6 = tkinter.Label(self.win, text="(SMTPpassword:OHGXLDKBLCUUIJIJ)")
        self.label6.place(x=95, y=220)

        self.button=tkinter.Button(self.win,text="send",command=self.go,width=10)
        self.button.place(x=175,y=250)

        self.win.mainloop()

    def go(self):
        newsendstr=self.entry3.get()+"\n"+self.sendstr
        Send=search.datamailsend.sendmail(self.entry4.get(),self.entry5.get())
        Send.send(newsendstr,self.entry1.get(),self.entry2.get())
        #Send = search.datamailsend.sendmail("nimendafeige@163.com","OHGXLDKBLCUUIJIJ")
        #Send.send(newsendstr,"test","nimendafeige@163.com")

#go=view2("good")



