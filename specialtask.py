#-*- coding: utf8 -*-
import sys
import os
import time



class SpecialTask(object):
    
    def main(self):
        print("hello,i am special task")
        os.chdir("D:\office\message")
        os.system("git pull git@github.com:wangjiachuan/office.git")

        


if __name__ == '__main__':

    mySpecialTask = SpecialTask()
    mySpecialTask.main()

