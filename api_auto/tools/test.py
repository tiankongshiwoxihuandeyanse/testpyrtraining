import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from HTMLTestRunner import HTMLTestRunner
from email.header import Header
import unittest
import time, os

# ==============定义发送邮件 ===============
def send_mail(file_new):
    f = open(file_new, 'rb')
    # 读取测试报告正文
    mail_body = f.read()
    f.close()
    # 发送邮箱服务器
    smtpserver = "smtp.126.com"
    # 发件人邮箱
    sender = 'wangqun@dealsports.cn'
    # 发件人邮箱密码
    password = 'Wangqun123'
    # 接收人邮箱
    receiver = ['1164843195@qq.com', 'buyer_1291455767_per@wondershare.cn']

    # 通过  模块构造的带附件的邮件如图
    msg = MIMEMultipart()
    # 编写html类型的邮件正文，MIMEtext()用于定义邮件正文
    # 发送正文
    text = MIMEText(mail_body, 'html', 'utf-8')
    text['Subject'] = Header('自动化测试报告', 'utf-8')
    msg.attach(text)
    # 发送附件
    # Header()用于定义邮件标题
    msg['Subject'] = Header('自动化测试报告', 'utf-8')
    msg_file = MIMEText(mail_body, 'html', 'utf-8')
    msg_file['Content-Type'] = 'application/octet-stream'
    msg_file["Content-Disposition"] = 'attachment; filename="TestReport.html"'
    msg.attach(msg_file)

    # 如果只发正文的话，上面的代码 从receiver下面到这段注释上面
    # 全部替换为下面的两行代码即可，上面的代码是增加了发送附件的功能。
    #     text = MIMEText(mail_body, 'html', 'utf-8')
    #     text['Subject'] = Header('自动化测试报告', 'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(sender, password)  # 登录的用户名和密码
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print('sendmail success')

# ======================查找最新的测试报告==========================

def new_report(testreport):
    dirs = os.listdir(testreport)
    dirs.sort()
    newreportname = dirs[-1]
    print('The new report name: {0}'.format(newreportname))
    file_new = os.path.join(testreport, newreportname)
    return file_new


if __name__ == '__main__':
    test_dir = r'../case'  # 测试用例所在目录
    test_report = r'../report'  # 测试报告所在目录

    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

    now = time.strftime('%Y%m%d %H%M%S')  # 获取当前时间
    filename = test_report + '\\' + now + 'result.html'  # 拼接出测试报告名
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况：')
    runner.run(discover)
    fp.close()  # 这边曾错写成fp.close，导致发送邮件时正文怎么都发不出来

    new_report = new_report(test_report)  # 获取最新报告文件
    # send_mail(new_report)  # 发送最新的测试报告

