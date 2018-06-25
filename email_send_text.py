# -*- coding:utf-8 -*-
__author__ = 'youjia'
__date__ = '2018/6/25 11:02'
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"
mail_user = "329345791@qq.com"  # 登录的邮箱
mail_password = '************'  # 打开qq的smtp服务后的授权码


# 网易邮箱
# mail_host = "smtp.163.com"
# mail_user = "youjia4321@163.com"  # 登录的邮箱
# mail_password = '*********'  # 授权码


sender = "329345791@qq.com"
receiver = input('输入对方的邮箱：')

'''
使用Python发送HTML格式的邮件
mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.runoob.com">这是一个链接</a></p>
"""
message = MIMEText(mail_msg, 'html', 'utf-8')
'''
content = 'python test'
message = MIMEText(content, 'utf-8')
message['From'] = Header('不愿透露姓名的某某', 'utf-8')
message['To'] = receiver

subject = '一位不愿透露姓名暗恋者'
message['Subject'] = Header(subject, 'utf-8')


try:
    smtp = smtplib.SMTP(mail_host, 25)  # smtp默认端口为25
    smtp.login(mail_user, mail_password)
    smtp.sendmail(sender, receiver, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")

