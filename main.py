#-*- coding: utf8 -*-
import sys
import os
import time

class DailyRegisterMain(object):           
    def main(self):
        for i in range(50000):
            print('-'*30)
            print("cycle is :{0}".format(i+1))
            os.chdir(os.getcwd())
            os.system(r"C:\Python34\python.exe D:\office\register\sendmessage.py")
            print('-'*30)
            print("cycle done,start another cycle:{0}".format(i+1))
            time.sleep(60)
        a = input

if __name__ == '__main__':

    myRegister = DailyRegisterMain()
    myRegister.main()
