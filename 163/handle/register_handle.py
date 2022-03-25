# coding=utf-8
from page.register_page import RegisterPage


class RegisterHandle(object):

    def __init__(self, driver):
        self.register_p = RegisterPage(driver)

    # 输入用户名
    def send_user_username(self, username):
        self.register_p.get_username_element().send_keys(username)

    # 输入密码
    def send_user_password(self, password):
        self.register_p.get_password_element().send_keys(password)

    # 输入电话
    def send_user_phone(self, phone):
        self.register_p.get_phone_element().send_keys(phone)

    # 获取文字信息
    def get_user_text(self, info, user_info):
        if info == "username_long_error":
            text = self.register_p.get_username_long_error_element().text
            return text
        elif info == "password_long_error":
            text = self.register_p.get_password_long_error_element().text
            return text
        elif info == "phone_error":
            text = self.register_p.get_phone_error_element().text
            return text

    # 点击注册按钮
    def click_register_button(self):
        self.register_p.get_register_button_element().click()
