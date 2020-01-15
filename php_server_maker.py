##import BaseHTTPServer, SimpleHTTPServer
##import ssl
import threading
from Tkinter import *
from win10toast import ToastNotifier
import subprocess
import pyttsx
root = Tk()
toaster = ToastNotifier()
engin = pyttsx.init()

def start_server():
  global dead
##  global httpd
  dead = True
##  httpd = BaseHTTPServer.HTTPServer(('127.0.0.1', 4443), SimpleHTTPServer.SimpleHTTPRequestHandler)
  toaster.show_toast("Server Started","Server Started on 127.0.0.1 and port is 4443")
  print threading.current_thread()
  subprocess.call(['php','-S','127.0.0.1:1234'],shell=True)
  Label(root,text='Server Started on 127.0.0.1 and port is 12345').grid(column=0,row=2)
  engin.runAndWait()
  engin.say('Server Started on 127.0.0.1 and port is 4443')

##  httpd.serve_forever()
  dead = False


def stop_server():
##    global httpd
    global dead1
    dead1 = True
##    httpd.shutdown()
    subprocess.call(['taskkill','/f','/im','php.exe'],shell=True)
    toaster.show_toast("Server info","server Stop")
    Label(root,text='serverStop').grid(column=0,row=2)
    print threading.current_thread()
    dead1 = False

def browser():
    subprocess.call(['explorer','.'])

def temp2():
    global dead1
    global t2
    dead1 = threading.Thread(target=stop_server).start()
    if dead1 == True:
        t2.start()

def temp():
    global dead
    global t1
    dead = threading.Thread(target=start_server).start()
    if dead == True:
        t1.start()


def gui():
    Label(root,text='Code By Rafsan').grid(column=0,row=0)
    Label(root,text='------LocalServer----').grid(column=0,row=0)
    t1 = threading.Thread(target=start_server)
    Button(root,text='ClickForStartingserver',command=temp).grid(column=0,row=1)
    t2  = threading.Thread(target=stop_server)
    Button(root,text='StopServer',command=temp2).grid(column=0,row=3)
    Button(root,text='Browser_folder',command=browser).grid(column=0,row=4)
    root.mainloop()



if __name__ == '__main__':
    threading.Thread(target=gui).start()
    print threading.current_thread()