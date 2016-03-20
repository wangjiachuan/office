# -*- coding: utf-8 -*-
import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import traceback
import os,time
import random


class DailyRegister(object):
    browser = None


    def __init__(self):
        self.internet_is_ok = True
        print ("self.internet_is_ok:{}".format(self.internet_is_ok))

        
    def is_working_day(self,work_time):
        print("week:Today is {}".format(work_time))
        #spring holiday
        #spring_holiday = [7,8,9,10,11,12,13,14,15]
        #spring_holiday = [0]
        #if time.localtime().tm_mday in spring_holiday:
        #    print("spring holiday")
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



    def internet_does_not_forbid_register(self):
        return True
    
        browser1 = webdriver.Firefox()
        browser1.get("http://email.163.com/")

        #assert "网易免费邮箱 - 中国第一大电子邮件服务商" in browser1.title
      
        browser1.find_element_by_id("userNameIpt").send_keys("mailaddress@163.com")
        time.sleep(2)
        browser1.find_element_by_id("pwdPlaceholder").send_keys("passwd")
        time.sleep(2)
        browser1.find_element_by_id("btnSubmit").send_keys(Keys.RETURN)
        print ("---"*10)
        time.sleep(5) # Let the page load

        try:   
            browser1.find_element_by_xpath("//span[contains(.,'写 信')]")
            browser1.close()
            print ("---"*10)
            return True

        except NoSuchElementException as e:
            print (e)
            print ("login fail,stop register")
            browser1.close()
            return False

    

    def wait_random_time(self):     
        value1 = random.randint(1, 1000)
        value2 = random.randint(1, 800)
        result = (value1+value2)%5
        time.sleep(result*60)


    def should_perform_register(self):
        if self.internet_is_ok == False:
            return self.time_to_register()

        else:
            if self.internet_does_not_forbid_register():
                return self.time_to_register()


    def should_perform_leave(self):
        if self.internet_is_ok == False:
            return self.time_to_leave()

        else:
            if self.internet_does_not_forbid_register():
                return self.time_to_register()



    def should_feedback_internet_status(self):
        if self.internet_is_ok == False:
            print ("internet is shut down,stop notificaiton")
            return False
        else:
            print("we think internet is ok ,keep notificaiton" )
            return self.time_to_feedback_internet_status()



    def perform_register_or_leave(self,option): 
        #self.wait_random_time()  
     
        self.browser = webdriver.Firefox() # Get local session of firefox

        self.browser.get("http://172.30.13.8/index.action") # Load page
        time.sleep(9) # Let the page load
        
        #assert "OA" in self.browser.title 
        if "OA" not in self.browser.title:
            print("Register System not accessable !!")
            self.browser.close()
            return
        else:
            print("Find the register page")

        

        elem = self.browser.find_element_by_id("email").send_keys("mailaddress")
        time.sleep(3)
        elem = self.browser.find_element_by_id("password").send_keys("passwd")
        time.sleep(3)

        self.browser.find_element_by_xpath("//input[contains(@class,'btn-sub')]").send_keys(Keys.RETURN)
        time.sleep(9) # Let the page load

        try:
             
            frame = self.browser.find_element_by_xpath("/html/frameset/frameset/frame[2]")
            self.browser.switch_to_frame(frame)

            print("Log in sucessfully")
            
            if option == "register":
                print("command is : register ")
                elem = self.browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/div[2]/ul/li[1]/input").send_keys(Keys.RETURN) #working

                time.sleep(5)
                
                #self.browser.save_screenshot("shot.png")
                
                self.browser.close()
                text = "Register  successfully at "+str(time.localtime().tm_hour)+":"+str(time.localtime().tm_min)
                print(text)
                self.send_message_by_mail(text)



            if option == "leave":
                print("command is : leave")
                elem = self.browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/div[2]/ul/li[2]/input").send_keys(Keys.RETURN) #leave

                time.sleep(5)
                self.browser.close()
                text = "Leave  successfully at "+str(time.localtime().tm_hour)+":"+str(time.localtime().tm_min)
                print(text)
                self.send_message_by_mail(text)

        except NoSuchElementException as e:
            print (e)
            self.browser.close()

        
        print ("---"*10)
        print ("---1 cycle done----")






    def send_message_by_mail(self,message):
        if self.internet_is_ok == False:
            return
        
        browser1 = webdriver.Firefox()
        browser1.get("http://email.163.com/")
      
        browser1.find_element_by_id("userNameIpt").send_keys("mailaddress@163.com")
        time.sleep(5)
        browser1.find_element_by_id("pwdPlaceholder").send_keys("passwd")
        time.sleep(5)
        browser1.find_element_by_id("btnSubmit").send_keys(Keys.RETURN)
        print ("---"*10)

        time.sleep(5) # Let the page load

        try:
  
            #click button to trigger a new letter
            browser1.find_element_by_xpath("/html/body/div[1]/nav/div[1]/ul/li[2]/span[2]").click()

            
            time.sleep(10)


            #print ("input the QQ mail address")
            browser1.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/section/header/div[1]/div[1]/div/div[2]/div/input").send_keys("93126721@qq.com")# receiver 's name
            
            time.sleep(5)
            print ("input the message content :{0} ,as title".format(message))
            browser1.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/section/header/div[2]/div[1]/div/div/input").send_keys(message)# title

            time.sleep(5)
            #print ("click send button to send out the mail")
            browser1.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/header/div/div[1]/div/span[2]").click()# send button

            time.sleep(5)
            browser1.close()
            print ("---"*10)
            print ("---"*10)

        except NoSuchElementException as e:
            print (e)
            print ("login fail,stop register")
            browser1.close()

    

    def run_timer(self):
        print("current time is :{0}:{1}".format(time.localtime().tm_hour,time.localtime().tm_min))

        if self.is_working_day(time.localtime().tm_wday)==True:
            if self.should_feedback_internet_status() == True:
                print ("time to feedback the internet status")
                time.sleep(3)
                text = "Internet is ok at "+str(time.localtime().tm_hour)+":"+str(time.localtime().tm_min)
                self.send_message_by_mail(text)
                return
            
            elif self.should_perform_register() == True:
                print ("time to register ")
                time.sleep(3)
                self.perform_register_or_leave("register")
                return
                

            elif self.should_perform_leave() == True:
                print ("time to leave ")
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
                    print("find it in table")
                    return find_it
                else:
                    print("not find it in table")

        return find_it



    # time to feedback the internet status. 
    def time_to_feedback_internet_status(self):

        feedback_list =[{'hour':6,'min_start':51,'min_end':58},
                        {'hour':7,'min_start':31,'min_end':38},
                        {'hour':8,'min_start':1,'min_end':8},
                        {'hour':14,'min_start':1,'min_end':8},
                        {'hour':15,'min_start':1,'min_end':8},
                        {'hour':16,'min_start':1,'min_end':8},
                        {'hour':17,'min_start':1,'min_end':8},
                        {'hour':20,'min_start':1,'min_end':8},
            ]
        return self.time_verify(feedback_list)


    # time to leave OA
    def time_to_leave(self):
        leave_list =[{'hour':18,'min_start':2,'min_end':16},
                     {'hour':11,'min_start':52,'min_end':59},
            ]

        return self.time_verify(leave_list)

            

    # time to register OA
    def time_to_register(self):
        register_list =[{'hour':8,'min_start':40,'min_end':59},
                        {'hour':12,'min_start':20,'min_end':29},
            ]

        return self.time_verify(register_list)
            

        

    def run_main(self):
        for i in range(50000):
            print('-'*30)
            print("cycle is :{0}".format(i))
            self.run_timer()
            print('-'*30)
            time.sleep(60)
        a = input



if __name__ == '__main__':

    myRegister = DailyRegister()
    myRegister.run_main()
