# coding=utf-8
import sys
import os
curPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(curPath)
import ddt
import unittest
from business.register_business import RegisterBusiness
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
from util.excel_util import ExcelUitl

ex = ExcelUitl()
data = ex.get_data()

# 用户名、密码、手机号，错误信息定位元素、错误提示信息
@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://mail.163.com/register/index.htm?from=163mail&utm_source=163mail")
        self.register_b = RegisterBusiness(self.driver)

    def tearDown(self):
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.abspath(os.path.dirname(os.getcwd())) + '\\report\\' + case_name + '.png'
                self.driver.save_screenshot(file_path)
        self.driver.close()

    # @ddt.data(
    #     ['q13060863776', 'hanyushi0703.', '13088353964', 'username_long_error', '长度应为6～18个字符'],
    #     ['q13060863776', '1234', '13088353964', 'password_long_error', '密码长度应为8-16个字符'],
    #     ['q13060863776', 'hanyushi0703.', '1308', 'phone_error', '请填写正确的中国大陆地区手机号，其他地区请到网易帐号中心注册']
    # )
    # @ddt.unpack
    @ddt.data(*data)
    def test_register_case(self,data):
        username, password, phone, assertCode, assertText = data
        username_error = self.register_b.register_function(username,password,phone,assertCode,assertText)
        self.assertFalse(username_error, "测试失败")

if __name__ == '__main__':
    file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\report\\' + 'first_case.html'
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    with open(file_path, 'wb') as f:
        runner = HTMLTestRunner(stream=f, title="百度搜索测试报告", description="运行环境: Windows 10, Chrome 浏览器")
        runner.run(suite)