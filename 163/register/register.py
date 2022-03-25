# coding=utf-8
from selenium import webdriver
import random
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)


# 浏览器初始化
def driver_init():
    driver.get("https://mail.163.com/register/index.htm?from=163mail")
    driver.maximize_window()


# 获取element的信息
def get_element(value):
    if value == 'username' or value == 'password' or value == 'phone':
        element = driver.find_element_by_id(value)
        return element
    elif value == "j-register":
        element = driver.find_element_by_class_name(value)
        return element
    elif value == "//div[@class='custom-checkbox service']/span":
        element = driver.find_element_by_xpath(value)
        return element


# 获取随机数
def get_range_user():
    user = ''.join(random.sample('1234567890', 8))
    return user


# 运行主程序
def run_main():
    um = '130' + get_range_user()
    driver_init()
    get_element("username").send_keys('q' + um)
    get_element("password").send_keys("hanyushi0703.")
    get_element("phone").send_keys(um)
    get_element("j-register").click()
    sleep(1)
    get_element("//div[@class='custom-checkbox service']/span").click()
    get_element("j-register").click()


run_main()
