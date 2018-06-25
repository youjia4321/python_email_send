# -*- coding:utf-8 -*-
__author__ = 'youjia'
__date__ = '2018/6/25 11:42'
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"
mail_user = "329345791@qq.com"  # 登录的邮箱
mail_password = '***********'  # 打开qq的smtp服务后的授权码
sender = '329345791@qq.com'
receivers = input('输入对方的邮箱：')  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# mail_host = "smtp.163.com"
# mail_user = "youjia4321@163.com"  # 登录的邮箱
# mail_password = '*********'  # 授权码
# sender = "youjia4321@163.com"
# receivers = input('输入对方的邮箱：')

msgRoot = MIMEMultipart('related')  # 设置邮件为多文格式
msgRoot['From'] = Header("一位不愿透露姓名的某某", 'utf-8')
msgRoot['To'] = receivers
subject = '一位不愿透露姓名的某某'
msgRoot['Subject'] = Header(subject, 'utf-8')

mail_msg = """
罗罗诺亚·索隆：<br>
<p><img src="cid:image1"></p>
"""
msgtext = MIMEText(mail_msg, 'html', 'utf-8')
msgRoot.attach(msgtext)

# 指定图片为当前目录
path = r'E:\PyCharmp\PycharmProjects\爬虫\爬虫及算法\小程序\picture\3.jpg'
fp = open(path, 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# 定义图片 ID，在 HTML 文本中引用
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

try:
    smtp = smtplib.SMTP(mail_host, 25)
    smtp.login(mail_user, mail_password)
    smtp.sendmail(sender, receivers, msgRoot.as_string())
    print("邮件发送成功")
    smtp.quit()
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
