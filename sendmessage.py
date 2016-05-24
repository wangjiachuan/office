#-*- coding: utf8 -*-
import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import traceback
import os,time
import random
import mail_smtp
import getopt

class DailyRegister(object):
    '''this class is used to register or leave'''
    browser = None
    mail_pass = "201103"
    oa_pass = "jhl1981"

    def __init__(self):
        self.internet_is_ok = True
        self.selenium_or_smtp = "selenium"
        print ("self.internet_is_ok:{}".format(self.internet_is_ok))
        
    def is_working_day(self,work_time):
        print("week:Today is {}".format(work_time))
        #spring holiday
        #spring_holiday = [7,8,9,10,11,12,13,14,15]
        #if time.localtime().tm_mday in spring_holiday:
        #    print("spring holiay:Today is {}".format(time.localtime().tm_mday))
        #    return False
        #spring holiday
        
        work_day=[0,1,2,3,4]
        if work_time in work_day:
            print ("working day")
            return True
        else:
            print("weekend,do nothing.quit")
            return False
        
    def wait_random_time(self):     
        value1 = random.randint(1, 1000)
        value2 = random.randint(1, 800)
        # wait 0,1,2,3 seconds
        result = (value1+value2)%4
        print("wait random minutes ,{0} minutes".format(result))
        time.sleep(result*60)

    def perform_register_or_leave(self,option): 
        self.wait_random_time()  
        try:
            self.browser = webdriver.Firefox() # Get local session of firefox
            self.browser.get("http://172.30.13.8/index.action") # Load page
            time.sleep(9) # Let the page load
        
            #assert "OA" in self.browser.title 
            if "OA" not in self.browser.title:
                print("Register System not accessable !!")
                self.browser.quit()
                return
            else:
                print("Find the register page")
  
            elem = self.browser.find_element_by_id("email").send_keys("wangjc_os@sari.ac.cn")
            time.sleep(3) 
            elem = self.browser.find_element_by_id("password").send_keys(self.oa_pass)
            time.sleep(3)

            self.browser.find_element_by_xpath("//input[contains(@class,'btn-sub')]").send_keys(Keys.RETURN)
            time.sleep(9) # Let the page load
            
            frame = self.browser.find_element_by_xpath("/html/frameset/frameset/frame[2]")
            self.browser.switch_to_frame(frame)
            print("Log in sucessfully")            
            if option == "register":
                print("command is : register ")
                elem = self.browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/div[2]/ul/li[1]/input").send_keys(Keys.RETURN) #working
                time.sleep(5)                
                #self.browser.save_screenshot("shot.png")                
                self.browser.quit()
                text = "Register  successfully at "+str(time.localtime().tm_hour)+":"+str(time.localtime().tm_min)
                print(text)
                self.send_message_by_mail(text)
            if option == "leave":
                print("command is : leave")
                elem = self.browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/div[2]/ul/li[2]/input").send_keys(Keys.RETURN) #leave
                time.sleep(5)
                self.browser.quit()
                text = "Leave  successfully at "+str(time.localtime().tm_hour)+":"+str(time.localtime().tm_min)
                print(text)
                self.send_message_by_mail(text)
        except NoSuchElementException:
            print ("cann't find the element!!!")
            self.browser.quit()
            return None
        except WebDriverException:
            print("webdriver crushed!!!")
            self.browser.quit()
            return None
        except TimeoutException:
            self.browser.quit()
            print("time out with webdriver!!!")
            return None
        
        print ("---"*10)
        print ("---1 cycle done----")

    def send_message_by_mail(self,message):
        if self.internet_is_ok == False:
            return
        if self.selenium_or_smtp == "selenium":
            try:
                browser1 = webdriver.Firefox()
                browser1.get("http://email.163.com/")
          
                browser1.find_element_by_id("userNameIpt").send_keys("W93126721@163.com")
                time.sleep(5)
                browser1.find_element_by_id("pwdPlaceholder").send_keys(self.mail_pass)
                time.sleep(5)
                browser1.find_element_by_id("btnSubmit").send_keys(Keys.RETURN)
                time.sleep(5) # Let the page load
                #click button to trigger a new letter
                browser1.find_element_by_xpath("/html/body/div[1]/nav/div[1]/ul/li[2]/span[2]").click()       
                time.sleep(10)
                browser1.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/section/header/div[1]/div[1]/div/div[2]/div/input").send_keys("93126721@qq.com")# receiver 's name            
                time.sleep(5)
                print ("input the message content :{0} ,as title".format(message))
                browser1.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/section/header/div[2]/div[1]/div/div/input").send_keys(message)# title
                time.sleep(5)
                browser1.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/header/div/div[1]/div/span[2]").click()# send button
                time.sleep(5)
                browser1.quit()
                print ("---"*10)
            except NoSuchElementException:
                print ("cann't find the element!!!")
                browser1.quit()
                return None
            except WebDriverException:
                print("webdriver crushed!!!")
                browser1.quit()
                return None
            except TimeoutException:
                browser1.quit()
                print("time out with webdriver!!!")
                return None
        elif self.selenium_or_smtp == "smtp":
            mail_smtp.send_smtp_message(message,message)

        mail_smtp.send_smtp_message(message,message)

    def run_timer(self):
        print("current time is :{0}:{1}".format(time.localtime().tm_hour,time.localtime().tm_min))
        if self.is_working_day(time.localtime().tm_wday)==True:
            if self.time_to_feedback_internet_status() == True:
                print ("time to feedback the internet status")
                time.sleep(3)
                text = "Internet is ok at "+str(time.localtime().tm_hour)+":"+str(time.localtime().tm_min)
                self.send_message_by_mail(text)
                return            
            elif self.time_to_register() == True:
                print ("time to register ")
                time.sleep(3)
                self.perform_register_or_leave("register")
                return
            elif self.time_to_leave() == True:
                print ("time to leave ")
                time.sleep(3)
                self.perform_register_or_leave("leave")
                return
            else:
                print("current time is :{0}:{1}, do nothing ,quit".format(time.localtime().tm_hour,time.localtime().tm_min))
        else:
            print("weekend ,do nothing,quit")

    def time_verify(self,time_list):
        find_it=False       
        for item in time_list:
            print("hour,start,end is {}:{}:{}".format(item['hour'],item['min_start'],item['min_end']))
            if time.localtime().tm_hour == item['hour']:
                if time.localtime().tm_min > item['min_start'] and time.localtime().tm_min < item['min_end']:
                    find_it = True                    
                    print("find task in table!")                    
                    return find_it
                else:
                    print("not find it in table")
        return find_it

    # time to feedback the internet status. 
    def time_to_feedback_internet_status(self):
        feedback_list =[{'hour':5,'min_start':51,'min_end':58},
                        {'hour':6,'min_start':51,'min_end':58},
                        {'hour':7,'min_start':5,'min_end':8},
                        {'hour':7,'min_start':15,'min_end':18},
                        {'hour':7,'min_start':25,'min_end':28},
                        {'hour':7,'min_start':35,'min_end':38},
                        {'hour':7,'min_start':45,'min_end':48},
                        {'hour':7,'min_start':55,'min_end':58},
                        {'hour':8,'min_start':5,'min_end':8},
                        {'hour':8,'min_start':15,'min_end':18},
                        {'hour':8,'min_start':25,'min_end':28},
                        {'hour':15,'min_start':1,'min_end':8},
                        {'hour':16,'min_start':1,'min_end':8},
                        {'hour':17,'min_start':1,'min_end':8},
                        {'hour':20,'min_start':1,'min_end':8},
                        {'hour':21,'min_start':1,'min_end':8},
                        {'hour':22,'min_start':1,'min_end':8},]
        return self.time_verify(feedback_list)

    # time to leave OA
    def time_to_leave(self):
        leave_list =[{'hour':18,'min_start':2,'min_end':18},
                     {'hour':11,'min_start':48,'min_end':58},]
        return self.time_verify(leave_list)

    # time to register OA
    def time_to_register(self):
        register_list =[{'hour':8,'min_start':36,'min_end':58},
                        {'hour':12,'min_start':26,'min_end':38},]
        return self.time_verify(register_list)
            
    def main(self):
        try:
            options,args = getopt.getopt(sys.argv[1:],"rlf",["register","leave=","feedback="])
        except getopt.GetoptError:
            sys.exit()

        for name,value in options:
            print(name,value)
            if name in ["-r","--register"]:
                print("receive force register cmd,force register...")
                self.perform_register_or_leave("register")
                return 
            if name in ["-l","--leave"]:
                print("receive force leave cmd,force leave...")
                self.perform_register_or_leave("leave")
                return 
            if name in ["-f","--feedback"]:
                print("receive force feedback cmd,force feedback...")
                text = "Internet is ok at "+str(time.localtime().tm_hour)+":"+str(time.localtime().tm_min)
                self.send_message_by_mail(text)
                return
            else:
                pass
        
        self.run_timer()
        


if __name__ == '__main__':

    myRegister = DailyRegister()
    myRegister.main()
