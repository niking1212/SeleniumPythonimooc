# coding=utf-8
from selenium import webdriver
from time import sleep
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC   # 将expected_conditions重命名为EC

driver = webdriver.Chrome()
driver.get("https://mail.163.com/register/index.htm?from=163mail")

username = driver.find_element_by_id("username")
um = ''.join(random.sample('1234567890123',11))
username.send_keys('q'+um)

# username = driver.find_element_by_id("username")
# username.send_keys("q13060863776")
# print(username.get_attribute("value"))
driver.find_element_by_id("password").send_keys("hanyushi0703.")
driver.find_element_by_id("phone").send_keys("13060863776")
driver.find_element_by_class_name("j-register").click()
sleep(1)
driver.find_element_by_xpath("//div[@class='custom-checkbox service']/span").click()

driver.find_element_by_class_name("j-register").click()
