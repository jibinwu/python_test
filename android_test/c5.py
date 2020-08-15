import pytest
import unittest
from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from ddt import ddt,unpack,data
@ddt
class TestCms(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get('https://cms.mamaqunaer.com/#/login')
        cls.driver.implicitly_wait(5)
    @unpack
    @data(('测试-季彬武','123456a'),('测试-季彬武','123456'))
    def test_login(self,username,password):
        sleep(3)
        usr=self.driver.find_element_by_xpath("//*[@id='app']/div/div/div/div[1]/input")
        # app > div > div > div > div:nth-child(1) > input
        usr.send_keys(username)
        pwd=self.driver.find_element_by_xpath("//*[@id='app']/div/div/div/div[2]/input")
        pwd.send_keys(password)
        confirmbt=self.driver.find_element_by_xpath("//*[@id='app']/div/div/div/button/span")
        confirmbt.click()
        sleep(3)
        if self.driver.find_element_by_xpath('//*[@id="main_container"]/aside/div/div[6]/div/span').is_displayed():
            self.driver.back()
        # else:
        #     usr.clear()
        #     pwd.clear()

    # @unittest.skip(reason='错误的密码')
    # def test_faiure(self):
    #     sleep(3)
    #     self.driver.find_element_by_xpath("//*[@id='app']/div/div/div/div[1]/input").send_keys('测试-季彬武')
    #     self.driver.find_element_by_xpath("//*[@id='app']/div/div/div/div[2]/input").send_keys('123456')
    #     confirmbt=self.driver.find_element_by_xpath("//*[@id='app']/div/div/div/button/span")
    #     confirmbt.click()
    #     sleep(3)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

#     assert add(2)==3
# def add(x):
#     return x+1
# def test_01():
#     add(2)
# @pytest.mark.skip(reason='过期')
# def test_02():
#     add(3)
#     assert add(3)==4
