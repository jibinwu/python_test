import time
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.3'
desired_caps['deviceName'] = '9889d539424d324a4d'
desired_caps['appPackage'] = 'com.qingzu.waterproof_work'
desired_caps['appActivity'] = '.WelcomeActivity'
desired_caps['appWaitActivity'] = '.LoginActivity'
desired_caps["unicodeKeyboard"] = "True"
desired_caps["resetKeyboard"] = "True"
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element_by_id("login_et_phone_number").send_keys("15058321650")
driver.find_element_by_id("login_et_password").send_keys("123456")
driver.find_element_by_id("login_bt_commit").click()

try:
    if driver.find_element_by_id("login_bt_commit").is_displayed():
        print('失败')
except Exception as e:
        print(e)
        print('成功')

driver.quit()

time.sleep(5)
