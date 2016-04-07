#-*- coding: utf8 -*-
import sys
import os
import time
import mail_crawler

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
            with open("d:/spycmds.txt","a",encoding= 'gbk') as f:
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
               
    def main(self):
        for i in range(50000):
            print('-'*30)
            print("cycle is :{0}".format(i+1))
            os.chdir(os.getcwd())
            # get cmd
            print("self.run_time :%d" % (self.run_time))
            if self.run_time == 8:
                os.system(r"C:\Python27\python.exe D:\office\message\mail_crawler.py")
                print("geting 163 cmd every 8 minutes... ")
                time.sleep(5)
            # force checking
            self.force()
            # remove cmd
            filename = "163cmd.txt"
            if os.path.exists(filename):
                os.remove(filename)
            else:
                print("no 163cmd.txt found,no deletion ")            
            print('-'*30)
            print("cycle done,start another cycle:{0}".format(i+1))
            self.run_time = i%9
            time.sleep(60)
        a = input

if __name__ == '__main__':

    myRegister = DailyRegisterMain()
    myRegister.main()

