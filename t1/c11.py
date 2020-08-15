from selenium import webdriver
chrome_driver="C:\drivers\chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_driver)
driver.get("https://www.baidu.com")