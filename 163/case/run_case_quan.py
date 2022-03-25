import unittest
from HTMLTestRunner import HTMLTestRunner
import time
import yagmail
import os


# 把测试报告座位附件发送到指定邮箱
def send_mail(report):
    yag = yagmail.SMTP(user='wqhuangg@isoftstone.com', password='Amway@123456', host='smtp.isoftstone.com')
    subject = "主题：自动化测试报告"
    contents = "正文，请查看附件"
    yag.send('13060863776@163.com', subject, contents, report)
    print("email has send out!")


if __name__ == '__main__':
    # 定义测试用例的目录为当前目录下的test_case目录
    test_dir = os.path.join(os.getcwd())  #
    suit = unittest.defaultTestLoader.discover(test_dir, pattern='first*.py')

    # 取当前日期时间，自动生成测试报告文件名
    now_time = time.strftime("%Y-%m-%d %H_%M_%S")  # 通过strftime()方法以指定格式获取当前日期时间，并赋值给now_time变量。
    html_report = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\report\\' + now_time + 'result.html'
    fp = open(html_report, 'wb')
    runner = HTMLTestRunner(stream=fp, title="163测试报告", description="运行环境: Windows 10, Chrome 浏览器")
    runner.run(suit)
    fp.close()
    send_mail(html_report)  # 发送报告
