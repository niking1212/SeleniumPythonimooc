# coding=utf-8
import sys
import os

curPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(curPath)
from business.register_business import RegisterBusiness
from log.user_log import UserLog
from selenium import webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner


class FirstCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.log = UserLog()
        cls.logger = cls.log.get_log()

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://mail.163.com/register/index.htm?from=163mail&utm_source=163mail")
        self.logger.info("this is chrom")
        self.register_b = RegisterBusiness(self.driver)

    def tearDown(self):
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.abspath(os.path.dirname(os.getcwd())) + '\\report\\' + case_name + '.png'
                self.driver.save_screenshot(file_path)
        self.driver.close()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.log.close_handle()

    def test_register_username_error(self):
        username_error = self.register_b.register_username_error('130', 'hanyushi0703.', '13088353964')
        self.assertFalse(username_error, "测试失败")
        # if username_error:
        #     print("case执行失败")

    def test_register_password_error(self):
        password_error = self.register_b.register_password_error('q2325634', '1234', '13088353964')
        self.assertFalse(password_error)
        # if password_error:
        #     print("case执行失败")

    def test_register_phone_error(self):
        phone_error = self.register_b.register_phone_error('q2325634', 'hanyushi0703.', '123')
        self.assertFalse(phone_error)

    def test_login_success(self):
        self.register_b.user_base('q13060863776', 'hanyushi0703.', '13088353964')
        print("success")


if __name__ == '__main__':
    # f = FirstCase()
    # f.test_register_username_error()
    # f.test_register_password_error()
    # f.test_register_phone_error()
    # f.test_login_success()
    suite = unittest.TestSuite()
    suite.addTest(FirstCase('test_register_username_error'))
    suite.addTest(FirstCase('test_register_password_error'))
    suite.addTest(FirstCase('test_register_phone_error'))
    suite.addTest(FirstCase('test_login_success'))
    file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\report\\' + 'first_case.html'
    with open(file_path, 'wb') as f:
        runner = HTMLTestRunner(stream=f, title="百度搜索测试报告", description="运行环境: Windows 10, Chrome 浏览器")
        runner.run(suite)

    # unittest.main()
