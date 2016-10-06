#!/usr/bin/env python
#coding=utf-8
import time
import smtplib
from email.MIMEText import MIMEText
from email.Header import Header
#正文 
def sendmail():
	mail_body='hello, this is the mail content'
	#发信邮箱 
	mail_from='sender@163.com'
	#收信邮箱 
	mail_to=['tosomebody@qq.com'] 
	#定义正文 
	msg=MIMEText(mail_body) 
	#定义标题 
	msg['Subject']='this is the title'
	#定义发信人 
	msg['From']=mail_from 
	msg['To']=';'.join(mail_to) 
	smtp=smtplib.SMTP() 
	#连接SMTP服务器，此处用的163的SMTP服务器 
	smtp.connect('smtp.163.com') 
	#用户名密码 
	smtp.login('youremail','yourpassword') 
	smtp.sendmail(mail_from,mail_to,msg.as_string()) 
	smtp.quit()
	print 'ok'
	
sendmail()