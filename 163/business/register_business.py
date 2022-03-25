# coding=utf-8
from handle.register_handle import RegisterHandle


class RegisterBusiness(object):

    def __init__(self, driver):
        self.register_h = RegisterHandle(driver)

    # 输入信息
    def user_base(self, username, password, phone):
        self.register_h.send_user_username(username)
        self.register_h.send_user_password(password)
        self.register_h.send_user_phone(phone)
        self.register_h.click_register_button()

    # 用户名错误
    def register_username_error(self, username, password, phone):
        self.user_base(username, password, phone)
        if self.register_h.get_user_text("username_long_error", "长度应为6～18个字符") != "长度应为6～18个字符":
            print("用户名检验不成功")
            return True
        else:
            return False

    def register_function(self,username,password,phone,assertCode,assertText):
        self.user_base(username, password, phone)
        if self.register_h.get_user_text(assertCode, assertText) != assertText:
            print("用户名检验不成功")
            return True
        else:
            return False

    # 密码错误
    def register_password_error(self, username, password, phone):
        self.user_base(username, password, phone)
        if self.register_h.get_user_text("password_long_error", "密码长度应为8-16个字符") != "密码长度应为8-16个字符":
            print("密码检验不成功")
            return True
        else:
            return False

    # 手机号码错误
    def register_phone_error(self, username, password, phone):
        self.user_base(username, password, phone)
        if self.register_h.get_user_text("phone_error", "请填写正确的中国大陆地区手机号，其他地区请到网易帐号中心注册") \
                != "请填写正确的中国大陆地区手机号，其他地区请到网易帐号中心注册":
            print("电话号码检验不成功")
            return True
        else:
            return False
