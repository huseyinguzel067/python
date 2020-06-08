import threading
import smtplib
from subprocess import  run,PIPE
import subprocess
import os
import time

exitFlag = 0
class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        print_time(self.name, 500, self.counter)
        print("Exiting " + self.name)


def dede():
    #os.system('cls')
    #subprocess.call("cls", shel=True)

    while True:
        try:
            time.sleep(30)
            os.system('cls')
            hostname = "10.0.0.11"
            #batcmd = "ping -n 1 " + hostname
            batcmd = "ping " + hostname
            ada = run(batcmd, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
            if 'TTL' in ada.__str__():
                print("up")

            else:
                print("down")
                # email = '*'
                # password = '**'
                # send_to_email = '*'
                email = '**'
                password = '***'
                send_to_email = '****'
                message = 'ulasilamiyor : ' + hostname + " \n" + ada.__str__()
                subject = "Ip Test "
                m = "From: %s\r\nTo: %s\r\nSubject: %s\r\nX-Mailer: My-Mail\r\n\r\n" % (email, send_to_email, subject)
                # server = smtplib.SMTP('eposta.sdu.edu.tr', 587)
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                server.sendmail(email, send_to_email, m + message)
                server.quit()
                time.sleep(300)
        except:
            print("hata")

    return dede()

def print_time(threadName,counter,delay):
    try:
        while counter:
            if exitFlag:
                threadName.exit()
            print("%s: %s" % (threadName, time.ctime(time.time())))
            dede()
            #counter -= 1
    except:
        print("hata")
        return runi()

def runi():
    # Create new threads
    thread1 = myThread(1, "Thread-1", 1)
    # thread2 = myThread(2, "Thread-2", 2)
    # Start new Threads
    while True:
        os.system('cls')
        if thread1.is_alive():
            # print(thread1.is_alive())
            time.sleep(10)
        else:
            thread1.start()

    # thread2.start()
    print("Exiting Main Thread")
    return runi()

runi()







