import codecs
import tkinter
import search.listshowdata
import search.tableshowdata
import search.textshowdata
import search.savedatafind
import search.datamailsend
import search.inputview2

class datafind:
    def __init__(self,filepath,howtoshow,usage):
        self.savelist = []
        self.file=codecs.open(filepath,"rb","utf-8","ignore")
        self.howtoshow=howtoshow
        self.showdata=None
        if usage==0:
            if self.howtoshow=="listshowdata":
                self.showdata = search.listshowdata.showdata()
            elif self.howtoshow=="textshowdata":
                self.showdata = search.textshowdata.showdata2()
            else:
                self.showdata = search.tableshowdata.showdata3()
        else:
            pass
    def find(self,searchstr,usage):
        while True:
            line=self.file.readline()
            if usage==0:
                if line.find(searchstr)!=-1:
                    print(line,end="")
                    self.showdata.adddata(line)
                if not line:
                    break
            else:
                if line.find(searchstr)!=-1:
                    print(line,end="")
                    self.savelist.append(line)
                if not line:
                    break

    def show(self):
        self.showdata.show()

    def save(self,loadpath):
        Save = search.savedatafind.savedata(loadpath)
        Save.save(self.savelist)

    def send(self):
        sendstr=''
        for line in self.savelist:
            sendstr+=line
        Send=search.inputview2.view2(sendstr)




