# coding=utf-8
from util.read_ini import RaedIni


class FindElemnt(object):

    def __init__(self, driver):
        self.driver = driver

    def get_elemnet(self, key):
        read_int = RaedIni()
        data = read_int.get_value(key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by == 'class_name':
                return self.driver.find_element_by_class_name(value)
            else:
                return self.driver.find_element_by_xpath(value)
        except:
            return None
