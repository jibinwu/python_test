from selenium import webdriver
# from time import sleep
import time
driver=webdriver.Firefox()
driver.get('http://localhost:81/')
driver.find_element_by_name('username').clear()
driver.find_element_by_name('username').send_keys('51zxw')
driver.find_element_by_name('password').clear()
driver.find_element_by_name('password').send_keys('123456')
driver.find_element_by_css_selector('[value="登陆"]').click()
time.sleep(5)
driver.find_element_by_link_text('退出').click()
driver.switch_to_alert().accept()
time.sleep(3)
driver.quit()
