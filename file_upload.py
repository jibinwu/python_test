#上传文件
from selenium import webdriver
from time import sleep
driver=webdriver.Firefox()
driver.get('https://www.baidu.com')
sleep(2)
driver.find_element_by_css_selector('.soutu-btn').click()
sleep(2)
driver.find_element_by_css_selector('[value="上传图片"]').send_keys(r'C:\Users\Administrator\Desktop\11.jpg')
sleep(5)
driver.quit()
