from tkinter import *
import subprocess
import os

root = Tk()
root.title('Rafsan jani made convater')

def convert():

  try:
    input = a.get()
    if input == '':
       error = Label(root,text='must give a drive letter').pack()
    elif input in ':':
         error2 = Label(root,text='Invalid input').pack()
    else:

      lable = Label(root,text='[+]Convert_successfully_compleate',fg='powder blue',bg='black').pack()
      process = subprocess.call(['convert',input,'/fs:ntfs'])
      return process
  except:
       Lable = Lable(root,text='[-]Some Thing Went Wrong ... Operation not compleate')











lable1 = Label(root,text='Md Rafsan jani made fat32 to ntfs converter',fg='Blue').pack()
line1 = Label(root,text='---------------------------------------------').pack()
label2 = Label(root,text='Enter Drive letter Which drive wanto convert').pack()
a = StringVar()
Txtbox1 = Entry(root,textvariable=a).pack()
button = Button(root,text='Convert!!!!', command=convert).pack()




root.mainloop()