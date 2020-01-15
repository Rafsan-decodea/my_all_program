import subprocess
from tkinter import *


def finding_file():
   global Inp
   global root
   try:

    inp = Inp.get()
    File  = subprocess.check_output(['dir',inp,'/s','/p','|','findstr','Directory of'],shell=True)#dir secret.doc /s /p
    output = File.split("\n")
    for x in output:
        y = x.split(' ')
        for z in y:
            if len(z) >10:
                subprocess.call(['explorer',z],shell=True)
                find_file = '[+]find File on =={0}'.format(z)
                lev = Label(root,text=find_file).pack()
   except:
       lev = Label(root,text='[+]File not found').pack()


def gui():
    global Inp
    global root
    root = Tk()
    root.title('File Finder')
    root.geometry('250x150')
    root.configure(background='black')
    lev = Label(root,text='---------------File Finder----------------',fg='red',bg='black').pack()
    lev1 = Label(root,text='[+]input File name What Are you Want', fg='green',bg='black').pack()
    Inp = StringVar()
    box1 = Entry(root,textvariable=Inp).pack()
    button = Button(root,text='Find',command=finding_file,fg='black',bg='green').pack()
    def about():
        root1 = Tk()
        root1.title('About')
        ght = '''

                       [+]File Finder
                        [+] Code By Md Rafsan Jani shazid
                         [+] Gmail: shazidno123@gmail.com

                                     ------ uses-------
                     This filefinder.exe file Place That Drive where you wanted to
                                         Scerch File



              '''
        lev = Label(root1,text=ght).pack()
    button = Button(root,text='about',command=about).pack()
    root.mainloop()





if __name__ == '__main__':
   try:
    gui()
   except:
    lev = Label(root,text='[+]Some Thing Went Wrong').pack()

