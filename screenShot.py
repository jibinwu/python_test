from selenium import webdriver
driver=webdriver.Firefox()
driver.get('https://www.baidu.com')
driver.get_screenshot_as_file(r'D:\baidu.jpg')
driver.get('http://www.51zxw.net')
driver.get_screenshot_as_file(r'D:\51zxw.jpg')