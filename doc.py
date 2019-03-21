"""命令行火车票查看器
Usage:
    send_email.py --from==<from> --to==<to> --content==<content>

Options:
    -h, --help               显示帮助菜
    -f, --from==<from>          发件人
    -t, --to==<to>              收件人
    -c, --content==<content>    邮件内容

Example:
    send_email.py 10407123@qq.com 3293451291@qq.com 'hello,send by python'
"""
from docopt import docopt
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

arguments = docopt(__doc__)
print(arguments)



#输出参数
print ('发件人>',arguments['--from'])
print ('收件人>',arguments['--to'])
print ('内容>',arguments['--content'])


# 第三方 SMTP 服务
mail_host = "smtp.qq.com"
mail_user = arguments['--from']  # 登录的邮箱
mail_password = 'xxxxxxxxxxx'  # 打开qq的smtp服务后的授权码

#处理选项 转换成list的格式(我上面没定义选项)
options=[]
for key in arguments:
    if arguments[key]==True:
        options.append(key)

sender = formataddr(["nagashi", arguments['--from']])

content = arguments['--content']
message = MIMEText(content, 'plain', 'utf-8')
message['From'] = sender
message['To'] = arguments['--to']

subject = 'python email'
message['Subject'] = Header(subject, 'utf-8')


smtp = smtplib.SMTP()  # smtp默认端口为25
smtp.connect(mail_host)
smtp.login(mail_user, mail_password)
smtp.sendmail(sender, arguments['--to'], message.as_string())
print("邮件发送成功")

