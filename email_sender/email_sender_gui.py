import smtplib
from Tkinter import *
import subprocess
root = Tk()
root.resizable(width=False, height=False)
root.title('Rafsan made  Email Sender')
def send_mail():
  User = username.get()
  Password = password.get()
  sender = Sending_Email_address.get()
  massage = body.get()
  try:
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(User,Password)
    lev = Label(root,text='Success Login',fg='green',bg='black').grid(row=3,column=1)
    server.sendmail(User,sender,massage)
    Label(root, text='Sending Mail SuccessFull',fg='green',bg='black').grid(row=10,column=1)
    server.quit()
  except smtplib.SMTPException as msg:
    plev = Label(root,text='Incurrect Username Or Password',fg='red',bg='black').grid(row=3,column=1)

def about():
    root1 = Tk()
    root1.title('about')
    level = Label(root1, text='''                                   ----------------------------------
                                -------------------------------------MD rafsan Jani made Email Sender -----------------------------------
                                                                    -----------------------------------
                                                                    Uses: 1)1st Trun on Your Email for Less secure App accessing
                                                                          2)That Use Only Testing Perpose
                                     ''').pack()


lebel1 = Label(root, text='Enter Mail Adress===>').grid(column=1,row=1)
username = StringVar()
entry1 = Entry(root,textvariable=username).grid(column=2,row=1)
level2 = Label(root,text='Enter Password===>').grid(column=1,row=2)
password = StringVar()
entry2 = Entry(root, textvariable=password,show="x").grid(column=2,row=2)
Sender_adress = StringVar()
entry3 = Entry(root,textvariable=Sender_adress)
leve = Label(root, text='Enter Sending Email Adress==>').grid(row=6,column=1)
Sending_Email_address = StringVar()
entry6 = Entry(root,textvariable=Sending_Email_address).grid(row=6,column=2)
Level10 = Label(root,text='Massage Body').grid(row=7,column=1)
body = StringVar()
massage_Body = Entry(root,textvariable=body).grid(row=8,column=1)
button = Button(root,text='Send Mail', command=send_mail).grid(column=2,row=9)
button = Button(root,text='About',command=about).grid(column=2,row=10)




root.mainloop()
