import smtplib#发送邮件模块
from email.mime.text import MIMEText#定义邮件内容
from email.header import Header#定义邮件标题

smtpserver='smtp.163.com'#发送邮件服务器
user='15058321650@163.com'#发送邮箱用户名和密码
password='jbw15058321650'
sender='15058321650@163.com'
receiver='295655698@qq.com'

#邮件正文
msg=MIMEText('你好,明天','html','utf-8')
msg['Subject']=Header('Web Selenium 自动化测试报告','utf-8')
msg['From']='15058321650@163.com'
msg['To']='295655698@qq.com'
smtp=smtplib.SMTP_SSL(smtpserver,465)#
#向服务器标志用户身份
smtp.helo(smtpserver)
smtp.ehlo(smtpserver)
smtp.login(user,password)
print('Start send Email...')
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()
print('send email end!')