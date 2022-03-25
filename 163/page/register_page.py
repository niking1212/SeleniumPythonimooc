# coding=utf-8
from base.find_element import FindElemnt


class RegisterPage(object):

    def __init__(self, driver):
        self.fd = FindElemnt(driver)

    # 获取用户名元素
    def get_username_element(self):
        return self.fd.get_elemnet("username")

    # 获取密码元素
    def get_password_element(self):
        return self.fd.get_elemnet("password")

    # 获取电话号码元素
    def get_phone_element(self):
        return self.fd.get_elemnet("phone")

    # 获取注册按钮元素
    def get_register_button_element(self):
        return self.fd.get_elemnet("register")

    # 获取用户名长度错误元素
    def get_username_long_error_element(self):
        return self.fd.get_elemnet("username_long_error")

    # 获取密码长度错误元素
    def get_password_long_error_element(self):
        return self.fd.get_elemnet("password_long_error")

    # 获取手机号码错误元素
    def get_phone_error_element(self):
        return self.fd.get_elemnet("phone_error")
