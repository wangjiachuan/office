#-*- coding: utf8 -*-
import sys
import os
import time
import mail_crawler

class DailyRegisterMain(object):
    def should_run(self):
        result = self.get_mail_cmd()
        if result == "stop register please,i will not come":
            return False
        else:
            pass
        return True

    def force(self):
        result = self.get_mail_cmd()
        if result == "force register please,i will not be there":
            os.system(r"C:\Python34\python.exe D:\office\message\sendmessage.py -r")
        elif result == "force leave please,i will not be there":
            os.system(r"C:\Python34\python.exe D:\office\message\sendmessage.py -l")
        elif result == "force feedback please,i will not be there":
            os.system(r"C:\Python34\python.exe D:\office\message\sendmessage.py -f")

    def get_mail_cmd(self):
        path = os.getcwd()
        filename = "163cmd.txt"
        if True == os.path.exists(path+os.sep+filename):
            with open(str(path+os.sep+filename),"rw") as f:
                f.seek(0,0)
                lines = f.readlines()
                if len(lines) == 1:
                    return lines
                else:
                    print("more than 1 command from 163")
                    return ""
 

        
    
    def main(self):
        for i in range(50000):
            print('-'*30)
            print("cycle is :{0}".format(i+1))
            os.chdir(os.getcwd())
            # get cmd
            os.system(r"C:\Python27\python.exe D:\office\message\mail_crawler.py")
            # force checking
            self.force()
            # forbid checking
            if True == self.should_run():
                os.system(r"C:\Python34\python.exe D:\office\message\sendmessage.py")
            else:
                print("find stop mail in 163 mail box,quit")
            # remove cmd
            os.system("rm 163cmd.txt")
            print('-'*30)
            print("cycle done,start another cycle:{0}".format(i+1))
            time.sleep(60)
        a = input

if __name__ == '__main__':

    myRegister = DailyRegisterMain()
    myRegister.main()

