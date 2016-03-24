#-*- coding: utf8 -*-
import sys
import os
import time
import mail_crawler

class DailyRegisterMain(object):
    def should_run(self):
        result = mail_crawler.get_mails()
        for i in result:
            print ('主题：%s'%(i['subject'].encode('utf8')))
            if i['subject'].encode('utf8') == "1":
                return False
    
        return True
    
    def main(self):
        for i in range(50000):
            print('-'*30)
            print("cycle is :{0}".format(i+1))
            os.chdir(os.getcwd())
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

