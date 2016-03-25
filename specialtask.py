#-*- coding: utf8 -*-
import sys
import os
import time

class SpecialTask(object):
    
    def main(self):
        print("hello,i am special task")
        os.system("git pull git@github.com:wangjiachuan/office.git")
        cmd = "copy C:"+os.sep+"Users"+os.sep+"nfs"+os.sep+"*.py"+"  "+"D:"+os.sep+"office"+os.sep+"message"+os.sep+"."
        print(cmd)
        os.system(cmd)
        

if __name__ == '__main__':
    mySpecialTask = SpecialTask()
    mySpecialTask.main()

