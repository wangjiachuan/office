#-*- coding: utf8 -*-
import sys
import os
import time
import mail_crawler
from multiprocessing import Process

class DailyRegisterMain(object):
   

    def __init__(self):
        self.run_time = 0
        self.forbid = False

    def force(self):
        result = "".join((list(self.get_mail_cmd()))[:-1])
        print("force:cmd is :%s" % result)
        if result == "force register please,i will not be there":
            print("force register")
            os.system(r"C:\Python34\python.exe D:\office\message\sendmessage.py -r")
            return
        elif result == "force leave please,i will not be there":
            print("force leave")
            os.system(r"C:\Python34\python.exe D:\office\message\sendmessage.py -l")
            return
        elif result == "force feedback please,i will not be there":
            print("force feedback")
            os.system(r"C:\Python34\python.exe D:\office\message\sendmessage.py -f")
            return
        elif result == "stop register service please,i will not come":
            print("forbid register")
            self.forbid = True
            return
        elif result == "resume register service,please":
            print("resume register service")
            self.forbid = False
            os.system(r"C:\Python34\python.exe D:\office\message\sendmessage.py -f")
            return
        elif result == "special task assigned,please run it":
            print("special task")
            os.system(r"C:\Python34\python.exe D:\office\message\specialtask.py")
            return
        elif result == "give me the working directory files list":
            print("special task:get files list")
            os.system(r"C:\Python34\python.exe D:\office\message\spy.py")
            return
        elif "give me the file:" in result:
            print("special task:transfer file")
            with open("d:/spycmds.txt","a") as f:
                f.seek(0,0)
                f.write('%s\n'%(result))
            os.system(r"C:\Python34\python.exe D:\office\message\spy.py")
            time.sleep(6)
            if os.path.exists("d:/spycmds.txt"):
                os.remove("d:/spycmds.txt")
            return
        else:           
            if self.forbid != True:
                print("no 163 cmd,useing default dealer")
                os.system(r"C:\Python34\python.exe D:\office\message\sendmessage.py")
            else:
                print("service is stoped..")
                pass

    def get_mail_cmd(self):  
        path = os.getcwd()
        filename = "163cmd.txt"
        if True == os.path.exists(path+os.sep+filename):
            print("find 163cmd.txt")
            with open(str(path+os.sep+filename),"r") as f:
                f.seek(0,0)
                lines = f.readlines()
                if len(lines) == 1:
                    print("find 1 command from 163")
                    for item in lines:
                        print("cmd is :%s" % item)
                        return item
                else:
                    print("more than 1 command from 163")
                    return ""
        else:
            print("does not find 163cmd.txt")
            return ""

    def access_email_inbox(self):
        print("access email functions call begin...")
        p = Process(target=self.my_sub_process)
        p.start()
        print ("I am parent %d" % (os.getpid()))
        print("access email functions call end...")
        time.sleep(6)
        if p.is_alive():
            p.terminate()
        else:
            pass
        print ('child process status: %s' % (p.is_alive()))
        

    def my_sub_process(self):
        time.sleep(1)
        print("geting 163 cmd every 8 minutes... ")
        print ("child:my pid is :%d" % os.getpid())
        #print ("child :my parent pid is :%d\n" % os.getppid())
        os.system(r"C:\Python27\python.exe D:\office\message\mail_crawler.py")

        
    def main(self):
        for i in range(50000):
            print('='*80)
            print("Cycle is :{0}".format(i+1))
            print('='*40)
            print("Current time is :{0}:{1}".format(time.localtime().tm_hour,time.localtime().tm_min))
            print('='*40)
            os.chdir(os.getcwd())
            # get cmd
            print("self.run_time :%d" % (self.run_time))
            if self.run_time == 8:   
                self.access_email_inbox()                    
                time.sleep(6)
            # force checking
            self.force()
            # remove cmd
            filename = "163cmd.txt"
            if os.path.exists(filename):
                os.remove(filename)
            else:
                print("no 163cmd.txt found,no deletion ")            
            print('='*80)
            print("cycle done,start another cycle:{0}".format(i+1))
            self.run_time = i%9
            time.sleep(60)
        a = input

if __name__ == '__main__':

    myRegister = DailyRegisterMain()
    myRegister.main()

