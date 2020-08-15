from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
driver=webdriver.Firefox()
# driver.get('http://www.qq.com/')
# sleep(3)
# js='var action=document.documentElement.scrollTop=10000'
# driver.execute_script(js)
# sleep(3)
# js2='var action=document.documentElement.scrollTop=0'
# driver.execute_script(js2)
# driver.refresh()
# driver.maximize_window()
# driver.find_element_by_css_selector('#sougouTxt').send_keys('科比')
# driver.find_element_by_css_selector('#searchBtn').click()
# sleep(10)
driver.get('https://www.sogou.com/')
sleep(10)
driver.find_element_by_css_selector('#query').send_keys('科比')
driver.find_element_by_css_selector('#query').send_keys(Keys.CONTROL,'a')
driver.find_element_by_css_selector('#query').send_keys(Keys.CONTROL,'c')
driver.get('https://www.baidu.com')
driver.find_element_by_css_selector('#kw').send_keys(Keys.CONTROL,'v')
driver.find_element_by_css_selector('#su').click()


