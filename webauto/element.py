from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.implicitly_wait(3)
# driver.minimize_window()
# driver.set_window_size(480,800)
driver.maximize_window()
driver.get("https://www.baidu.com")
print(driver.name)
driver.get_screenshot_as_file(r"C:\drivers\baidu.png")
#driver.find_element_by_id("kw").send_keys("网易云课堂")
#driver.find_element_by_name("wd").send_keys("网易云课堂")
#driver.find_element_by_class_name("s_ipt").send_keys("网易云课堂")
#driver.find_element_by_tag_name("input").send_keys("网易云课堂")
#driver.find_element_by_link_text("新闻").click()
#driver.find_element_by_partial_link_text("hao").click()
#driver.find_element_by_xpath('//*[@id="kw"]').send_keys("网易云课堂")
# driver.find_element_by_xpath('//input[@id="kw"]').send_keys("网易云课堂")
# driver.find_element_by_xpath('//input[@name="wd"]').send_keys("网易云课堂")
# driver.find_element_by_xpath('//input[@class="s_ipt"]').send_keys("网易云课堂")
# driver.find_element_by_css_selector(".s_ipt").send_keys("网易云课堂")
# driver.find_element_by_css_selector("#kw").send_keys("网易云课堂")
driver.find_element_by_css_selector("#kw").send_keys("网易云课堂")
sleep(2)
driver.get_screenshot_as_file(r"C:\drivers\wangyi.png")
driver.find_element_by_xpath("//*[@id='2']/h3/a/em").click()
# sleep(3)
driver.get_screenshot_as_file(r"C:\drivers\baike.png")
# driver.find_element_by_partial_link_text("网易云课堂").click()
# driver.find_element_by_xpath("//*[@id='1']/h3/a[1]").click()

sleep(5)
# driver.back()
# driver.refresh()
# driver.forward()
driver.quit()