from tkinter import *
import threading
import MySQLdb
import time
root = Tk()

def main_work():
    global dead
    global stu_name
    global stu_father_name
    global stu_mother_name
    global stu_class
    global stu_batch
    global stu_roll
    global stu_section
    dead =True
    student_name = stu_name.get()
    student_father_name = stu_father_name.get()
    student_mother_name = stu_mother_name.get()
    student_class = stu_class.get()
    student_batch = stu_batch.get()
    student_roll = stu_roll.get()
    student_section  = stu_section.get()
    con = MySQLdb.Connect('localhost','root','','testDB')
    data = con.cursor()
    print (data)
    sql = 'insert into student (name, mother_name, father_name, roll, class,section_name,batch_name) values (%s,%s,%s,%s,%s,%s,%s)'
    val = (student_name,student_mother_name,student_father_name,student_roll,student_class,student_section,student_batch)
    data.execute(sql,val)
    con.commit()


def fetch():
    global dead2
    dead2= True
    con =  MySQLdb.Connect('localhost','root','','testDB')
    data = con.cursor()
    sql = 'select * from student'
    data.execute(sql)
    a = data.fetchall()
    for x in a:
       print ('--------------------------------------')
       print ('[+] Id is ===>{}'.format(x[0]))
       print ('[+] Name is ==>{}'.format(x[1]))
       print ('[+] Father name is==>{}'.format(x[2]))
       print ('[+] Mother Name is ===>{}'.format(x[3]))
       print ('[+] Roll is===>{}'.format(x[4]))
       print ('[+] Calss is ==>{}'.format(x[5]))
       print ('[+] Section Name is ==>{}'.format(x[6]))
       print ('[+] Batch Name is ===>{}'.format(x[7]))
       print ('\n\n')
    print '[+]Data Count in  From Database in ===>{}'.format(len(a))

def gui_show():
    global dead
    dead = True
    root2 = Tk()
    con = MySQLdb.Connect('localhost','root','','testDB')
    data  = con.cursor()
    sql  = 'select * from  student'
    data.execute(sql)
    d = data.fetchall()
    for x in d:
       deta1 = '--------------------------------------'
       deta2 =('[+] Id is ===>{}'.format(x[0]))
       deta3 =('[+] Name is ==>{}'.format(x[1]))
       deta4 = ('[+] Father name is==>{}'.format(x[2]))
       deta5 = ('[+] Mother Name is ===>{}'.format(x[3]))
       deta6 = ('[+] Roll is===>{}'.format(x[4]))
       deta7 =  ('[+] Calss is ==>{}'.format(x[5]))
       deta8 =  ('[+] Section Name is ==>{}'.format(x[6]))
       deta9 = ('[+] Batch Name is ===>{}'.format(x[7]))
       Label(root2,text=deta1).grid(column=2,row=1)
       Label(root2,text=deta2).grid(column=2,row=2)
       Label(root2,text=deta3).grid(column=2,row=3)
       Label(root2,text=deta4).grid(column=2,row=4)
       Label(root2,text=deta5).grid(column=2,row=5)
       Label(root2,text=deta6).grid(column=2,row=6)
       Label(root2,text=deta7).grid(column=2,row=7)
       Label(root2,text=deta8).grid(column=2,row=8)
       Label(root2,text=deta9).grid(column=2,row=9)
       Label(root2,text='\n\n').pack()




def temp():
    global t1
    global dead
    dead = threading.Thread(target=main_work).start()
    if dead == True:
       t1.start()

def temp2():
    global t2
    global dead2
    dead  = threading.Thread(target=fetch).start()
    if dead == True:
       t2.start()


def temp3():
    global t3
    global dead
    dead = threading.Thread(target=gui_show).start()
    if dead==True:
       t3.start()

def gui():
    global t2
    global t1
    global stu_name
    global stu_father_name
    global stu_mother_name
    global stu_class
    global stu_batch
    global stu_roll
    global stu_section
    Label(root,text='   School Management System').grid(column=3,row=0)
    Label(root,text='-------------------------------').grid(column=3,row=2)
    Label(root,text='Name:').grid(column=1,row=3)
    stu_name = StringVar()
    Entry(root,textvariable=stu_name).grid(column=2,row=3)
    Label(root,text='Mother Name:').grid(column=1,row=4)
    stu_mother_name = StringVar()
    Entry(root,textvariable=stu_mother_name).grid(column=2,row=4)
    Label(root,text='Father Name:').grid(column=1,row=5)
    stu_father_name = StringVar()
    Entry(root,textvariable=stu_father_name).grid(column=2,row=5)
    Label(root,text='Roll').grid(column=1,row=6)
    stu_roll = StringVar()
    Entry(root,textvariable=stu_roll).grid(column=2,row=6)
    Label(root,text='Class').grid(column=1,row=7)
    stu_class = StringVar()
    Entry(root,textvariable=stu_class).grid(column=2,row=7)
    Label(root,text='Section name:').grid(column=3,row=3)
    stu_section = StringVar()
    Entry(root,textvariable=stu_section).grid(column=4,row=3)
    Label(root,text='Batch name:').grid(column=3,row=4)
    stu_batch = StringVar()
    Entry(root,textvariable=stu_batch).grid(column=4,row=4)
    t1 = threading.Thread(target=main_work)
    t2 = threading.Thread(target=fetch)
    t3 = threading.Thread(target=gui_show)
    Button(root,text='Submit',command=temp).grid(column=3,row=8)
    Button(root,text='Fetch_All',command=temp2).grid(column=3,row=9)
    Button(root,text='Fetch_in_gui',command=temp3).grid(column=3,row=10)

    root.mainloop()

if __name__ == '__main__':
   gui()