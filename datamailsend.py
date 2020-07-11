import smtplib
import tkinter
from email.mime.text import MIMEText
class sendmail:
    def __init__(self,sender,password):
        self.SMTPsever="smtp.163.com"
        self.Sender=sender
        self.password=password     #"OHGXLDKBLCUUIJIJ"

    def send(self,Message,subject,aimaddr):
        msg = MIMEText(Message)
        msg["subject"] = subject
        msg["From"] = self.Sender
        msg["To"] = aimaddr

        mailsever = smtplib.SMTP(self.SMTPsever, 25)
        mailsever.login(self.Sender, self.password)
        mailsever.sendmail(self.Sender,
                           aimaddr,
                           msg.as_string())
        mailsever.quit()

        win=tkinter.Tk()
        win.geometry("150x50+800+400")
        attention=tkinter.Label(win,text="send successfully")
        attention.pack()
        win.mainloop()

        print("send successfullly")



'''sendtest=sendmail("smtp.163.com","nimendafeige@163.com","OHGXLDKBLCUUIJIJ")
sendtest.send("你好帅哥","测试","nimendafeige@163.com")'''
