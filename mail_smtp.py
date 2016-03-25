# -*- coding: utf-8 -*-
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import os.path
import mimetypes
from email import encoders

def send_smtp_message(mytitle,mycontent):

        From = "w93126721@163.com"
        To = "93126721@qq.com"
        file_name = "d:/1.txt"#附件名

        server = smtplib.SMTP("smtp.163.com")
        server.login("w93126721","201103") #仅smtp服务器需要验证时

        # 构造MIMEMultipart对象做为根容器
        main_msg = MIMEMultipart()

        # 构造MIMEText对象做为邮件显示内容并附加到根容器
        text_msg = MIMEText(mycontent,_charset="utf-8")
        main_msg.attach(text_msg)

        # 构造MIMEBase对象做为文件附件内容并附加到根容器

        ## 读入文件内容并格式化 [方式1]－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
        data = open(file_name, 'rb')
        ctype,encoding = mimetypes.guess_type(file_name)
        if ctype is None or encoding is not None:
                ctype = 'application/octet-stream'
        maintype,subtype = ctype.split('/',1)
        file_msg = MIMEBase(maintype, subtype)
        file_msg.set_payload(data.read())
        data.close( )
        encoders.encode_base64(file_msg)#把附件编码
        '''
         测试识别文件类型：mimetypes.guess_type(file_name)
         rar 文件             ctype,encoding值：None None（ini文件、csv文件、apk文件）
         txt text/plain None
         py  text/x-python None
         gif image/gif None
         png image/x-png None
         jpg image/pjpeg None
         pdf application/pdf None
         doc application/msword None
         zip application/x-zip-compressed None

        encoding值在什么情况下不是None呢？以后有结果补充。
        '''
        #－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－

        ## 设置附件头
        basename = os.path.basename(file_name)
        file_msg.add_header('Content-Disposition','attachment', filename = basename)#修改邮件头
        main_msg.attach(file_msg)

        # 设置根容器属性
        main_msg['From'] = From
        main_msg['To'] = To
        main_msg['Subject'] = mytitle
        #main_msg['Date'] = email.Utils.formatdate( )


        # 得到格式化后的完整文本
        fullText = main_msg.as_string( )

        # 用smtp发送邮件
        try:
            server.sendmail(From, To, fullText)
        finally:
            server.quit()


if __name__ == '__main__':
        send_smtp_message("leave at 11:00","leave ok")
