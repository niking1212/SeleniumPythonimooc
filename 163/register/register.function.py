# coding=utf-8
from selenium import webdriver
import random
from time import sleep
from base.find_element import FindElemnt


class RegisterFunction(object):

    def __init__(self, url):
        self.driver = self.get_driver(url)

    # 获取driver并且打开url
    def get_driver(self, url):
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        return driver

    # 输入用户信息
    def send_user_info(self, key, data):
        self.get_user_elemnet(key).send_keys(data)

    # 定位用户信息，获取element
    def get_user_elemnet(self, key):
        find_element = FindElemnt(self.driver)
        user_element = find_element.get_elemnet(key)
        return user_element

    # 获取随机数
    def get_range_user(self):
        user_info = ''.join(random.sample('1234567890', 8))
        return user_info

    # 运行函数
    def main(self):
        um = '130' + self.get_range_user()
        self.send_user_info('username', 'q' + um)
        self.send_user_info('password', 'hanyushi0703.')
        self.send_user_info('phone', um)
        self.get_user_elemnet('register').click()
        sleep(1)
        self.get_user_elemnet('clause').click()
        self.get_user_elemnet('register').click()
        sleep(5)
        self.driver.close()


if __name__ == '__main__':
    ma = RegisterFunction('https://mail.163.com/register/index.htm?from=163mail&utm_source=163mail')
    ma.main()
