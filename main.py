#-*- coding: utf8 -*-
import sys
import os
import time
import mail_crawler

class DailyRegisterMain(object):
    def should_run(self):
        result = mail_crawler.get_mails()
        for i in result:
            #print ('subject is：%s'%(i['subject'].encode('utf8')))
            if i['subject'].encode('utf8') == "stop register please,i will not come":
                return False
        return True

    def force(self):
        result = mail_crawler.get_mails()
        for i in result:
            if i['subject'].encode('utf8') == "force register please,i will not be there":
                os.system(r"C:\Python34\python.exe D:\office\message\sendmessage.py -r")
            elif i['subject'].encode('utf8') == "force leave please,i will not be there":
                os.system(r"C:\Python34\python.exe D:\office\message\sendmessage.py -l")
            elif i['subject'].encode('utf8') == "force feedback please,i will not be there":
                os.system(r"C:\Python34\python.exe D:\office\message\sendmessage.py -f")
        
    
    def main(self):
        for i in range(50000):
            print('-'*30)
            print("cycle is :{0}".format(i+1))
            os.chdir(os.getcwd())
            # force checking
            self.force()
            # forbid checking
            if self.should_run()== True:
                os.system(r"C:\Python34\python.exe D:\office\message\sendmessage.py")
            else:
                print("find stop mail in 163 mail box,quit")
            print('-'*30)
            print("cycle done,start another cycle:{0}".format(i+1))
            time.sleep(60)
        a = input

if __name__ == '__main__':

    myRegister = DailyRegisterMain()
    myRegister.main()

