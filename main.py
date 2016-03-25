#-*- coding: utf8 -*-
import sys
import os
import time
import mail_crawler

class DailyRegisterMain(object):

    def force(self):
        result = self.get_mail_cmd()
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
        elif result == "stop register please,i will not come":
            print("forbid register")
            return
        else:
            print("no 163 cmd,useing default dealer")
            os.system(r"C:\Python34\python.exe D:\office\message\sendmessage.py")

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
            pass
 

        
    
    def main(self):
        for i in range(50000):
            print('-'*30)
            print("cycle is :{0}".format(i+1))
            os.chdir(os.getcwd())
            # get cmd
            os.system(r"C:\Python27\python.exe D:\office\message\mail_crawler.py")
            print("geting 163 cmd ... ")
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
            time.sleep(60)
        a = input

if __name__ == '__main__':

    myRegister = DailyRegisterMain()
    myRegister.main()

