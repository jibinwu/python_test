#多窗口切换
from selenium import webdriver
from time import sleep
driver=webdriver.Firefox()
driver.get('http://www.51zxw.net/list.aspx?cid=615')
first=driver.current_window_handle
sleep(2)
driver.find_element_by_partial_link_text('2-1').click()
sleep(4)
driver.switch_to.window(first)
driver.find_element_by_partial_link_text('3-1').click()
sleep(3)
driver.quit()

